from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from .serializers import CategoryListSerializer, ProductListSerializer, ReviewListSerializer

#___Category__

@api_view(['GET'])
def category_deteil_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(
        {'error': 'product does not exist!'},
        status=status.HTTP_404_NOT_FOUND
        )

    data = CategoryListSerializer(category).data
    return Response(data=data)


@api_view(['GET'])
def category_list_api_view(request):
    category = Category.objects.all()
    data = CategoryListSerializer(category, many=True).data
    return Response(data=data)


#__Product__

@api_view(['GET'])
def product_deteil_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(
        {'error': 'product does not exist!'},
        status=status.HTTP_404_NOT_FOUND
        )

    data = ProductListSerializer(product).data
    return Response(data=data)


@api_view(['GET'])
def product_list_api_view(request):
    product = Product.objects.all()
    data = ProductListSerializer(product, many=True).data
    return Response(data=data)



#Review

@api_view(['GET'])
def review_deteil_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(
        {'error': 'review does not exist!'},
        status=status.HTTP_404_NOT_FOUND
        )

    data = ReviewListSerializer(review).data
    return Response(data=data)


@api_view(['GET'])
def review_list_api_view(request):
    review = Review.objects.all()
    data = ReviewListSerializer(review, many=True).data
    return Response(data=data)



