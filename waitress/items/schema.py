"""Items app schema"""

import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from graphql import GraphQLError

from .models import PersonalItem, SharedItem
from waitress.users.decorators import check_user_in_session


class PersonalItemType(DjangoObjectType):
    """PersonalItem object for GraphQL"""
    class Meta:
        model = PersonalItem


class SharedItemType(DjangoObjectType):
    """SharedItem object for GraphQL"""
    class Meta:
        model = SharedItem


class AddPersonalItem(graphene.Mutation):
    """Mutation that creates a personal item"""
    personal_item = graphene.Field(PersonalItemType)

    class Arguments:
        """Args that are allowed in mutation"""
        name = graphene.String(required=True)
        amount = graphene.Float(required=True)

    @login_required
    @check_user_in_session
    def mutate(self, info, session_user, **kwargs):
        """Creates an item"""
        item = PersonalItem.objects.create(owner=session_user, **kwargs)
        return AddPersonalItem(personal_item=item)


class AddSharedItem(graphene.Mutation):
    """Mutation that creates a shared item"""
    shared_item = graphene.Field(SharedItemType)

    class Arguments:
        """Args that are allowed in mutation"""
        name = graphene.String(required=True)
        amount = graphene.Float(required=True)

    @login_required
    @check_user_in_session
    def mutate(self, info, session_user, **kwargs):
        """Creates an item"""
        food_session = session_user.food_session
        item = SharedItem.objects.create(food_session=food_session, **kwargs)
        return AddSharedItem(shared_item=item)


class DeletePersonalItem(graphene.Mutation):
    """Mutation that deletes a personal item"""
    personal_item = graphene.Field(PersonalItemType)

    class Arguments:
        """Args that are allowed in mutation"""
        item_id = graphene.Int(required=True)

    @login_required
    @check_user_in_session
    def mutate(self, info, item_id, **kwargs):
        """Deletes a personal item"""
        item_queryset = PersonalItem.objects.filter(id=item_id)
        if not item_queryset.exists():
            raise GraphQLError(
                f"The personal item with the id {item_id} doesn't exists."
            )
        item = item_queryset.get()
        item.delete()
        return DeletePersonalItem(personal_item=item)


class DeleteSharedItem(graphene.Mutation):
    """Mutation that deletes a shared item"""
    shared_item = graphene.Field(SharedItemType)

    class Arguments:
        """Args that are allowed in mutation"""
        item_id = graphene.Int(required=True)

    @login_required
    @check_user_in_session
    def mutate(self, info, item_id, **kwargs):
        """Deletes a shared item"""
        item_queryset = SharedItem.objects.filter(id=item_id)
        if not item_queryset.exists():
            raise GraphQLError(
                f"The shared item with the id {item_id} doesn't exists."
            )
        item = item_queryset.get()
        item.delete()
        return DeleteSharedItem(shared_item=item)


class Mutation:
    """Mutation object for items app"""
    add_personal_item = AddPersonalItem.Field()
    add_shared_item = AddSharedItem.Field()
    delete_personal_item = DeletePersonalItem.Field()
    delete_shared_item = DeleteSharedItem.Field()
