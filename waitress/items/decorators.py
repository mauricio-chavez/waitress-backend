"""Items app decorators"""

from graphql import GraphQLError

from waitress.users.models import SessionUser

def check_user_in_session(func):
    """Checks if user is in a session"""
    def wrapper(self, info, **kwargs):
        user = info.context.user
        session_user_queryset = SessionUser.objects.filter(
            user=user,
            is_active=True
        )
        if not session_user_queryset.exists():
            raise GraphQLError('Current user is not in an active session')
        return func(self, info, session_user_queryset, **kwargs)

    return wrapper
