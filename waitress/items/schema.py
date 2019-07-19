"""Items app schema"""

import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from graphql import GraphQLError

from .models import Item


class ItemType(DjangoObjectType):
    """Item object for GraphQL"""
    class Meta:
        model = Item


class CreateItem(graphene.Mutation):
    """Mutation that creates an item"""
    item = graphene.Field(ItemType)

    class Arguments:
        """Args that are allowed in mutation"""
        name = graphene.String(required=True)
        amount = graphene.Float(required=True)

    @login_required
    def mutate(self, info, **kwargs):
        """Creates an item"""
        item = Item.objects.create(**kwargs)
        return CreateItem(item=item)


class Mutation:
    """Mutation object for items app"""
    create_item = CreateItem.Field()
