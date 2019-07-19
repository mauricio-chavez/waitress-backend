"""Project Schema"""

import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required

from waitress.bills.schema import Mutation as BillsMutation
from waitress.food_sessions.schema import (
    Query as FoodSessionsQuery,
    Mutation as FoodSessionsMutation
)
from waitress.items.schema import Mutation as ItemsMutation
from waitress.users.schema import Query as UsersQuery, Mutation as UserMutation


class Query(UsersQuery, FoodSessionsQuery, graphene.ObjectType):
    """Query Object for project Schema"""
    hello = graphene.String()
    hello_authenticated = graphene.String()

    def resolve_hello(self, info, **kwargs):
        return 'Hello, stranger'

    @login_required
    def resolve_hello_authenticated(self, info, **kwargs):
        return f'Hello, { info.context.user.first_name }'


class Mutation(
    BillsMutation, FoodSessionsMutation, ItemsMutation, UserMutation,
    graphene.ObjectType
):
    """Mutation Object for project Schema"""
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
