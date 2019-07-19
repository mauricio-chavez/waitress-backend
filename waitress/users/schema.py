"""Users schema"""

from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()

    def mutate(self, info, email, **kwargs):
        user_exists = get_user_model().objects.filter(email=email).exists()
        if user_exists:
            raise GraphQLError('User already exists!')
        user = get_user_model().objects.create_user(email=email, **kwargs)

        return CreateUser(user=user)


class Mutation:
    create_user = CreateUser.Field()
