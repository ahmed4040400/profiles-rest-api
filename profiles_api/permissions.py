"""the permission class

    to add permissions to the user attitude (behavior)
    in this case we adding basic permission
    in case of updating a profile or deletin it
    we make sure that the user is changing his pwn profile
    not someone elses
"""

# import the permission calss
from rest_framework import permissions


# creating the class that's gonna handle the update permission
class UpdateOwnProfile(permissions.BasePermission):
    # this is a call back that get called every time
    # the user try to modify an object
    def has_object_permission(self, request, view, obj):
        # if the req method is a safe method such as GET
        # we return true because the user is just reading the database
        # in this case
        if request.method in permissions.SAFE_METHODS:
            return True

        # otherwise we make sure that the user is updating
        # his own profile and return the value (True,False)
        return obj.id == request.user.id


# just like UpdateOwnProfile but this time checking the
# the user_profile field and getting that user id and then
# make sure it matches the id of the user that made the request
class UpdateOwnStatus(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
