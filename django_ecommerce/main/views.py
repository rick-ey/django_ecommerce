# main/views.py

from django.shortcuts import render_to_response, RequestContext
from payments.models import User
from main.models import MarketingItem, StatusReport, Announcement
from datetime import date, timedelta


def index(request):
    uid = request.session.get('user')
    if uid is None:
        # main landing page
        market_items = MarketingItem.objects.all()
        return render_to_response(
            'main/index.html',
            {'marketing_items': market_items}
        )
    else:
        # membership page
        status = StatusReport.objects.all().order_by('-when')[:20]

        announce_date = date.today() - timedelta(days=30)
        announce = (Announcement.objects.filter(
            when__gt=announce_date).order_by('-when')
        )

        usr = User.get_by_id(uid)
        badges = usr.badges.all()

        return render_to_response(
            'main/user.html',
            {
                'user': usr,
                'badges': badges,
                'reports': status,
                'announce': announce
            },
            context_instance=RequestContext(request),
        )


def report(request):
    if request.method == "POST":
        status = request.POST.get("status", "")

        # update the database with the status
        if status:
            uid = request.session.get('user')
            user = User.get_by_id(uid)
            StatusReport(user=user, status=status).save()

        # always return something
        return index(request)
