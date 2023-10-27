from django.shortcuts import render
from rest_framework.decorators import api_view
from django.conf import settings
from rest_framework.response import Response
from django.http import JsonResponse
from .models import DepositOptions, DepositProducts
from .serializers import DepositProductsSerializer, DepositOptionsSerializer
from pprint import pprint
import requests
import json

# Create your views here.
# requests 모듈을 활용하여 정기예금 상품 목록 데이터를 가져와 정기예금 
# 상품 목록과 옵션 목록을 DB에 저장
@api_view(['GET'])
def save_deposit_products(request):
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1' 
    
    # 정기 예금 상품 목록 및 옵션 목록 받기
    deposit_json = requests.get(url).json()
    product_list = deposit_json.get('result').get('baseList')
    option_list = deposit_json.get('result').get('optionList')
    
    # 상품 목록 저장
    # 이 때 중복된 코드가 저장되지 않도록 try-except 사용
    for product in product_list:
        deposit_products = {
            'fin_prdt_cd': product.get('fin_prdt_cd'),
            'kor_co_nm': product.get('kor_co_nm'),
            'fin_prdt_nm': product.get('fin_prdt_nm'),
            'etc_note': product.get('etc_note'),
            'join_deny': product.get('join_deny'),
            'join_member': product.get('join_member'),
            'join_way': product.get('join_way'),
            'spcl_cnd': product.get('spcl_cnd'),
        }
        
        serializer = DepositProductsSerializer(data = deposit_products)
        
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        except:
            pass
    
    # 옵션 목록 저장    
    # 이 때 중복된 코드가 저장되지 않도록 try-except 사용
    for option in option_list:
        product = DepositProducts.objects.get(fin_prdt_cd=option.get('fin_prdt_cd')),
        deposit_options = {
            'fin_prdt_cd': option.get('fin_prdt_cd'),
            'intr_rate_type_nm': option.get('intr_rate_type_nm'),
            'intr_rate': option.get('intr_rate') or -1,
            'intr_rate2': option.get('intr_rate2') or -1,
            'save_trm': option.get('save_trm'),
        }
        
        serializer = DepositOptionsSerializer(data = deposit_options)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save(product=product)
        except:
            pass
    
    return JsonResponse({ 'message' : 'success' })

# GET: 전체 정기예금 상품 목록 반환
# POST: 상품 데이터 저장
@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse({ 'message' : 'success' })
        return JsonResponse({ 'message' : 'failed' })
    
    elif request.method == 'GET':
        deposit_products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(deposit_products, many=True)
        return Response(serializer.data)

# 특정 상품의 옵션 리스트 반환
@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd): 
    option_list = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(option_list, many=True)
    return Response(serializer.data)

# 가입 기간에 상관없이 금리가 가장 높은 상품과 해당 상품의 옵션 리스트 출력
@api_view(['GET'])
def top_rate(request):
    option_list = DepositOptions.objects.all()
    top_rate_products_code = ""
    max_intr = -1
    for option in option_list:
        if top_rate_products_code == "":
            top_rate_products_code = option.fin_prdt_cd
            max_intr = option.intr_rate2
        else:
            if option.intr_rate2 > max_intr:
                top_rate_products_code = option.fin_prdt_cd
                max_intr = option.intr_rate2
    
    top_rate_option_list = DepositOptions.objects.filter(fin_prdt_cd=top_rate_products_code)
    top_rate_product = DepositProducts.objects.get(fin_prdt_cd=top_rate_products_code)
    
    top_rate_option_dict_list = []
    top_rate_product_dict = top_rate_product.__dict__
    top_rate_product_dict.pop('_state', None)
    
    for option in top_rate_option_list:
        option_dict = option.__dict__
        option_dict.pop('_state', None)
        top_rate_option_dict_list.append(option_dict)
    
    print(top_rate_product_dict)
    print(top_rate_option_dict_list)
    
    ret = {
        'deposit_product': top_rate_product_dict,
        'option': top_rate_option_dict_list,
    }
    
    return Response(ret)
    