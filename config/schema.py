"""Project Schema"""

import graphene


class Query(graphene.ObjectType):
    """Query Object for project Schema"""
    hello = graphene.String()

    def resolve_hello(self, info, **kwargs):
        return 'Hello, stranger'


schema = graphene.Schema(query=Query)
