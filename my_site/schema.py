import graphene
from graphene_django.types import DjangoObjectType
from .models import Crecimiento

class CrecimientoType(DjangoObjectType):
    class Meta:
        model = Crecimiento

class Query(graphene.ObjectType):
    crecimiento = graphene.List(CrecimientoType)

    def resolve_crecimiento(self, info):
        return Crecimiento.objects.all().order_by("año")

schema = graphene.Schema(query=Query)
