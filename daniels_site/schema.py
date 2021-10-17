import graphene
from graphene import Decimal
from ArtShop.models import ArtPiece, Category
from django.core.checks.messages import Error
from django.core.validators import RegexValidator
from graphene.types import schema
from graphene_django import DjangoObjectType


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


class ArtPieceMutations(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String()
        price = graphene.Decimal()
        category = graphene.String()

    art_piece = graphene.Field(ArtPieceType)

    @classmethod
    def mutate(cls, root, info, name, description, price, category):
        mutation_category = Category(name=category)
        art_piece = ArtPiece(name=name,
                             description=description,
                             price=price,
                             category=mutation_category)
        mutation_category.save()
        art_piece.save()
        return ArtPieceMutations(art_piece=art_piece)


# class ArtPieceUpdateMutation(graphene.Mutation):
#     class Arguments:
#         name = graphene.String()
#         description = graphene.String()
#         price = graphene.Decimal()
#         category = graphene.String()

#     art_piece = graphene.Field(ArtPieceType)

#     @classmethod
#     def mutate(cls, root, info, name, description, price, category):
#         art_piece = ArtPiece.objects.get(name=name)
#         art_piece.name = name
#         art_piece.description = description
#         art_piece.price = price
#         art_piece.category = Category(name=category)
#         art_piece.save()
#         category.save()
#         return ArtPieceUpdateMutation(art_piece=art_piece)


class ArtPieceDeleteMutation(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.Int()

    art_piece = graphene.Field(ArtPieceType)

    @classmethod
    def mutate(cls, root, info, id):
        art_piece = ArtPiece.objects.get(id=id)
        art_piece.delete()
        return cls(ok=True)


class Mutation(graphene.ObjectType):
    create_art_piece = ArtPieceMutations.Field()
    # update_art_piece = ArtPieceUpdateMutation.Field()
    delete_art_piece = ArtPieceDeleteMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
