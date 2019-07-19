"""Items app schema"""

import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from .models import Item


class ItemType(DjangoObjectType):
    class Meta:
        model = Item


# TODO protect it!
class CreateItem(graphene.Mutation):
    """Mutation that creates an item"""
    item = graphene.Field(ItemType)

    class Arguments:
        """Args that are allowed in mutation"""
        name = graphene.String(required=True)
        amount = graphene.Float(required=True)

    def mutate(self, info, **kwargs):
        """Creates an item"""
        item = Item.objects.create(**kwargs)

        return CreateItem(item=item)


class Mutation:
    create_item = CreateItem.Field()
