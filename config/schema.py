"""Project Schema"""

import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required


class Query(graphene.ObjectType):
    """Query Object for project Schema"""
    hello = graphene.String()
    hello_authenticated = graphene.String()

    def resolve_hello(self, info, **kwargs):
        return 'Hello, stranger'

    @login_required
    def resolve_hello_authenticated(self, info, **kwargs):
        return f'Hello, { info.context.user.email }'


class Mutation(graphene.ObjectType):
    """Mutation Object for project Schema"""
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
