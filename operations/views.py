from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class AdditionView(APIView):
    def get(self,request,*args,**kwargs):
        return Response(data="inside addition get method")
    def post(self,request,*args,**kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=int(n1)+int(n2)
        return Response(data=res)

class SubstractionView(APIView):
    def get(self,request,*args,**kwargs):
        return  Response(data="inside substraction get method")
    def post(self,request,*args,**kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=int(n1)-int(n2)
        return Response(data=res)

class FactorialView(APIView):
    def get(self,request,*args,**kwargs):
        return  Response(data="inside factorial get method")
    def post(self,request,*args,**kwargs):
        n=request.data.get("num")
        fact=1
        for i in range(1,int(n)+1):
            fact=fact*i
        return Response(data=fact)

