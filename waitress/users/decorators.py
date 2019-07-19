"""Users app decorators"""

from graphql import GraphQLError

from .models import SessionUser


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
        session_user = session_user_queryset.get()
        return func(self, info, session_user=session_user, **kwargs)

    return wrapper


def check_admin_in_session(func):
    """Checks if user is in a session"""

    def wrapper(self, info, **kwargs):
        user = info.context.user
        session_user_queryset = SessionUser.objects.filter(
            user=user,
            is_active=True
        )
        if not session_user_queryset.exists():
            raise GraphQLError('Current user is not in an active session')
        session_user = session_user_queryset.get()
        food_session = session_user.food_session
        if food_session.admin != user:
            raise GraphQLError('Current user is not session admin')
        return func(self, info, food_session=food_session, **kwargs)

    return wrapper
