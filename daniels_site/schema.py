from django.core.checks.messages import Error
import graphene
from graphene.types import schema
from graphene_django import DjangoObjectType
from django.core.validators import RegexValidator
from ArtShop.models import ArtPiece, Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ArtPieceType(DjangoObjectType):
    class Meta:
        model = ArtPiece
        #Not sure I'm going to use the image field but I'm keeping it here for now
        fields = ('id', 'name', 'description', 'price', 'category')


class Query(graphene.ObjectType):
    category_by_name = graphene.Field(CategoryType, name=graphene.String())
    art_pieces = graphene.List(ArtPieceType)
    art_pieces_by_name = graphene.List(ArtPieceType, name=graphene.String())
    art_pieces_by_category = graphene.List(ArtPieceType,
                                           name=graphene.String())

    def resolve_category_by_name(self, info, name, **kwargs):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

    def resolve_art_pieces(self, info, **kwargs):
        return ArtPiece.objects.select_related('category').all()

    def resolve_art_pieces_by_name(self, info, name, **kwargs):
        return ArtPiece.objects.filter(name__icontains=name)

    def resolve_art_pieces_by_category(self, info, name, **kwargs):
        valid_category = r'^[a-zA-Z0-9_]'
        validator = RegexValidator(regex=valid_category,
                                   message='Invalid category name',
                                   code='invalid_category')
        validator(name)

        ##TODO: This is a hack to get the name of the category to work might implement something better later
        ##TODO: Need to find a way to neglect the case of the name ex: Peaches -> peaches -> PEACHES ...
        if Category.objects.filter(name=name).exists():
            return ArtPiece.objects.filter(category__name=name)
        else:
            return []


schema = graphene.Schema(query=Query)