"""the permission class

    to add permissions to the user attitude (behavior)
    in this case we adding basic permission
    in case of updating a profile or deletin it
    we make sure that the user is changing his pwn profile
    not someone elses
"""

#import the permission calss
from rest_framework import permissions
#creating the class that's gonna handle the update permission
class UpdateOwnProfile(permissions.BasePermission):
    #this is a call back that get called every time
    #the user try to modify an object
    def has_object_permission(self,request,view,object):
        #if the req method is a safe method such as GET
        # we return true bacause the user is just reading the database
        # in this case
        if request.method == permissions.SAFE_METHODS:
            return True

        #otherwise we make sure that the user is updating
        #his own profile and return the value (True,False)
        return object.id == request.user.id
