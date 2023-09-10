from rest_framework import permissions
from rest_framework.request import Request


class IsChatID(permissions.BasePermission):
    """
    Custom permission to check if a user has a chat_id.

    Users with a chat_id are granted access, while others are denied access.

    Attributes:
        message (str): The error message to display when access is denied.
    """
    message = 'User does not have a chat_id.'

    def has_permission(self, request: Request, view) -> bool:
        """
        Check if the user has a chat_id.

        Args:
            request (Request): The request object.
            view: The view that is being accessed.

        Returns:
            bool: True if the user has a chat_id, False otherwise.
        """
        return bool(request.user.chat_id)
