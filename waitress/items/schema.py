"""Items app schema"""

import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from .decorators import check_user_in_session
from .models import Item, PersonalItem, SharedItem
from waitress.users.models import SessionUser


class ItemType(DjangoObjectType):
    """Item object for GraphQL"""
    class Meta:
        model = Item


class AddPersonalItem(graphene.Mutation):
    """Mutation that creates a personal item"""
    item = graphene.Field(ItemType)

    class Arguments:
        """Args that are allowed in mutation"""
        name = graphene.String(required=True)
        amount = graphene.Float(required=True)

    @login_required
    @check_user_in_session
    def mutate(self, info, session_user_queryset, **kwargs):
        """Creates an item"""
        session_user = session_user_queryset.get()
        item = Item.objects.create(**kwargs)
        PersonalItem.objects.create(item=item, owner=session_user)
        return AddPersonalItem(item=item)


class AddSharedItem(graphene.Mutation):
    """Mutation that creates a shared item"""
    item = graphene.Field(ItemType)

    class Arguments:
        """Args that are allowed in mutation"""
        name = graphene.String(required=True)
        amount = graphene.Float(required=True)

    @login_required
    @check_user_in_session
    def mutate(self, info, session_user_queryset, **kwargs):
        """Creates an item"""
        food_session = session_user_queryset.get().food_session
        item = Item.objects.create(**kwargs)
        SharedItem.objects.create(item=item, food_session=food_session)
        return AddSharedItem(item=item)


class DeleteSharedItem(graphene.Mutation):
    """Mutation that deletes a shared item"""
    item = graphene.Field(ItemType)

    class Arguments:
        """Args that are allowed in mutation"""
        item_id = graphene.Int(required=True)

    @login_required
    @check_user_in_session
    def mutate(self, info, session_user_queryset, **kwargs):
        """Creates an item"""
        food_session = session_user_queryset.get().food_session
        item = Item.objects.create(**kwargs)
        SharedItem.objects.create(item=item, food_session=food_session)
        return DeleteSharedItem(item=item)


class Mutation:
    """Mutation object for items app"""
    add_personal_item = AddPersonalItem.Field()
    add_shared_item = AddSharedItem.Field()
    delete_shared_item = DeleteSharedItem.Field()
