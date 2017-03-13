# main/permissions.py

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permisison(self, request, view, obj):

        # Allow all read type requests
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        # This leaves us with write requests (i.e. POST / PUT / DELETE)
        return obj.user == request.user
