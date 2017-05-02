from payments.models import User, UnpaidUsers
from payments.forms import UserForm
from payments.views import Customer
from payments.serializers import PasswordSerializer
from rest_framework.response import Response
from django.db import transaction
from django.db import IntegrityError
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework import generics, status, permissions


@api_view(['POST'])
def post_user(request):
    form = UserForm(request.data)

    if form.is_valid():
        try:
            # update based on your billing method (subscription vs one time)
            customer = Customer.create(
                "subscription",
                email=form.cleaned_data['email'],
                description=form.cleaned_data['name'],
                card=form.cleaned_data['stripe_token'],
                plan="gold",
            )
        except Exception as exp:
            form.addError(exp)

        cd = form.cleaned_data
        try:
            with transaction.atomic():
                user = User.create(
                    cd['name'], cd['email'],
                    cd['password'], cd['last_4_digits'], stripe_id='')

                if customer:
                    user.stripe_id = customer.id
                    user.save()
                else:
                    UnpaidUsers(email=cd['email']).save()

        except IntegrityError:
            form.addError(cd['email'] + ' is already a member')
        else:
            request.session['user'] = user.pk
            resp = {"status": "ok", "url": '/'}
            return Response(resp, content_type="application/json")

        resp = {"status": "fail", "errors": form.non_field_errors()}
        return Response(resp)
    else:  # for not valid
        resp = {"status": "form-invalid", "errors": form.errors}
        return Response(resp)


class ChangePassword(generics.GenericAPIView):
    """
    Change password of any user if super admin.
    * pwd
    * pwd2
    """
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = PasswordSerializer

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        print("<put> Got the user.")
        serializer = PasswordSerializer(user, data=request.data)
        print("<put> PasswordSerializer with user.")
        if serializer.is_valid():
            print("<put> Serializer is valid.")
            serializer.save()  # my guess is this is failing on update
            print("<put> Serializer saved.")
            return Response("Password Changed.")
        print("<put> Serializer invalid!")
        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)
