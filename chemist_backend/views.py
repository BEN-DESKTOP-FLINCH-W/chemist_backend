from .models import Products, Categories, Sales, Expenses
from django.db.models import Sum, IntegerField
from .serializers import ProductSerializer, CategorySerializer,SalesSerializer,SaleSerializer, ExpenseSerializer
from .serializers import CategoryTotalSerializer
from django.conf import settings



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .access_token import generate_access_token
from .utils import timestamp_conversion
from .encode_base64 import generate_password
import requests
import json


#Products Logic
@api_view(['GET','POST'])
def product_list(request, format=None):
    if request.method =='GET':
        products=Products.objects.all()
        serializer= ProductSerializer(products, many=True)
        return Response(serializer.data)
    if request.method =='POST':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        


@api_view(['GET','PUT','DELETE'])
def product_detail(request,id, format=None):

    try:
        product=Products.objects.get(pk=id)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer= ProductSerializer(product)
        return Response(serializer.data)
       
    elif request.method=='PUT':
        serializer=ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Categories Logic
@api_view(['GET','POST'])
def category_list(request, format=None):
    if request.method =='GET':
        categories=Categories.objects.all()
        serializer= CategorySerializer(categories, many=True)
        return Response(serializer.data)
    if request.method =='POST':
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def category_detail(request,id, format=None):

    try:
        category=Categories.objects.get(pk=id)
    except Categories.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer= CategorySerializer(category)
        return Response(serializer.data)
       
    elif request.method=='PUT':
        serializer=CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#sales Logic
@api_view(['GET','POST'])
def sales_list(request, format=None):
    if request.method =='GET':
        sales=Sales.objects.all()
        serializer= SalesSerializer(sales, many=True)
        return Response(serializer.data)
    if request.method =='POST':
        serializer=SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)     
        

#Expenses Logic
@api_view(['GET','POST'])
def expenses_list(request, format=None):
    if request.method =='GET':
        expenses=Expenses.objects.all()
        serializer= ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)
    if request.method =='POST':
        serializer=ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        
#Analysis
@api_view(['GET','POST'])
def category_analysis(request, format=None):
    if request.method =='GET':
        category_totals = Sales.objects.values('category').annotate(total_price=Sum('total', output_field=IntegerField()))
        serializer = CategoryTotalSerializer(category_totals, many=True)

        # Return the serialized data as JSON response
        return Response(serializer.data)
    
#mpesa daraja stk push
@api_view(['POST'])
def mpesa(request, format=None):
    data = json.loads(request.body)
    amount = data.get('amount')
    phone = data.get('phone_number')

    access_token=generate_access_token()
    formated_time= timestamp_conversion()
    decoded_password= generate_password(formated_time)

    headers={"Authorization":"Bearer %s" %access_token}
    request={
            "BusinessShortCode": settings.BUSINESS_SHORT_CODE,
            "Password": decoded_password,
            "Timestamp": formated_time,
            "TransactionType": settings.TRANSACTION_TYPE,
            "Amount": amount,
            "PartyA": phone,
            "PartyB": settings.BUSINESS_SHORT_CODE,
            "PhoneNumber": phone,
            "CallBackURL": settings.CALL_BACK_URL,
            "AccountReference": settings.ACCOUNT_REFERENCE,
            "TransactionDesc":settings.TRANSACTION_DESCRIPTION
            }
    response= requests.post(settings.API_RESOURCE_URL, json=request,headers=headers)
    mystr=response.text
    json_response= json.loads(mystr)
    



    return Response(json_response)
