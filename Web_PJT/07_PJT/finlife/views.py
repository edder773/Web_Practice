from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import DepositOptions, DepositProducts
from django.conf import settings
import requests, json
from .serializers import DepositOptionsSerializer, DepositProductsSerializer

API_KEY = settings.API_KEY

@api_view(['GET'])
def save_deposit_products(request):
    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': '1'
    }
    response = requests.get(url, params=params)
    products_data = response.json()['result']['baseList']
    
    for product_data in products_data:
        product_serializer = DepositProductsSerializer(data=product_data)
        if product_serializer.is_valid():
            product = product_serializer.save()
            options_data = response.json()['result']['optionList']
            for option_data in options_data:
                if option_data['fin_prdt_cd'] == product_data['fin_prdt_cd']:
                    option_data['fin_prdt_cd'] = product.id
                    if option_data['intr_rate'] == None:
                        option_data['intr_rate'] = -1
                    option_serializer = DepositOptionsSerializer(data=option_data)
                    if option_serializer.is_valid():
                        option_serializer.save()
            
    return Response(status=status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def deposit_products(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializers = DepositProductsSerializer(products, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = DepositProductsSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    product = DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).first()
    options = product.depositoptions_set.all()
    serializers = DepositOptionsSerializer(options, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def top_rate(request):
    products = DepositOptions.objects.all()
    max_rate_product = None
    max_rate = 0.0
    for product in products:
        if product.intr_rate > max_rate:
            max_rate = product.intr_rate
            max_rate_product = product
            
    product_serializer = DepositProductsSerializer(max_rate_product.fin_prdt_cd)
    option_serializer = DepositOptionsSerializer(max_rate_product.fin_prdt_cd.depositoptions_set.filter(intr_rate=max_rate), many=True)
    response_data = {
        'product': product_serializer.data,
        'options': option_serializer.data
    }
    
    return Response(response_data, status=status.HTTP_200_OK)