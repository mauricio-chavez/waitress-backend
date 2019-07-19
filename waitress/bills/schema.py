"""Bills app schema"""

from django.db.models import Sum

import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from graphql import GraphQLError

from .models import PersonalBill, FoodSessionBill, SharedBill
from waitress.food_sessions.models import FoodSession
from waitress.items.models import SharedItem, PersonalItem
from waitress.users.decorators import check_admin_in_session
from waitress.users.models import SessionUser


class PersonalBillType(DjangoObjectType):
    """PersonalBill object for GraphQL"""
    class Meta:
        model = PersonalBill


class SharedBillType(DjangoObjectType):
    """SharedBill object for GraphQL"""
    class Meta:
        model = SharedBill


class FoodSessionBillType(DjangoObjectType):
    """FoodSessionBill object for GraphQL"""
    class Meta:
        model = FoodSessionBill


class EndUpSession(graphene.Mutation):
    """Mutation that ends up a session and get total amounts"""
    personal_bills = graphene.List(PersonalBillType, required=True)
    shared_bill = graphene.Field(SharedBillType, required=True)
    food_session_bill = graphene.Field(FoodSessionBillType, required=True)

    @login_required
    @check_admin_in_session
    def mutate(self, info, food_session, **kwargs):
        """Ends up session and get bills"""
        food_session.is_active = False
        food_session.save()
        users_in_session = SessionUser.objects.filter(
            food_session=food_session
        )
        users_in_session.update(is_active=False)

        total_shared = SharedItem.objects.filter(
            food_session=food_session
        ).aggregate(Sum('amount'))['amount__sum']

        total_per_person = total_shared / len(users_in_session)

        shared_bill = SharedBill.objects.create(
            food_session=food_session,
            total_per_person=total_per_person,
            total_amount=total_shared
        )

        total_amount = total_shared

        personal_bills = []
        for user in users_in_session:
            total_personal = PersonalItem.objects.filter(
                owner=user
            ).aggregate(Sum('amount'))['amount__sum']
            personal_bills.append(
                PersonalBill.objects.create(
                    user=user,
                    total_amount=total_personal
                )
            )
            total_amount += total_personal
        food_session_bill = FoodSessionBill.objects.create(
            food_session=food_session,
            total_amount=total_amount
        )
        return EndUpSession(
            personal_bills=personal_bills,
            shared_bill=shared_bill,
            food_session_bill=food_session_bill
        )


class Mutation:
    """Mutation object for bills app"""
    end_up_session = EndUpSession.Field(required=True)
