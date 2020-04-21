from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    """Allow user to update their own status"""

    def has_object_permission(self,request,view,obj):
        """checks if the user is tying to update their own status"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id