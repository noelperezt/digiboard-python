from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from pessoas.models import Pessoas
from pessoas.serializers import PessoasSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def pessoas_list(request):
    
    if request.method == 'GET':
        pessoas = Pessoas.objects.all()      
        pessoas_serializer = PessoasSerializer(pessoas, many=True)
        return JsonResponse(pessoas_serializer.data, safe=False)

    elif request.method == 'POST':
        pessoas_data = request.data
        pessoas_serializer = PessoasSerializer(data=pessoas_data)

        if pessoas_serializer.is_valid():
            pessoas_serializer.save()
            return JsonResponse(pessoas_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(pessoas_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def pessoas_detail(request, pk):
    pessoa = Pessoas.objects.get(pk=pk)
 
    if request.method == 'GET': 
        pessoas_serializer = PessoasSerializer(pessoa) 
        return JsonResponse(pessoas_serializer.data) 

    elif request.method == 'PUT': 
        pessoas_data = request.data
        print(request.data['foto'])
        if request.data['foto'] is None:
            request.data['foto'] = pessoa.foto

        pessoas_serializer = PessoasSerializer(pessoa, data=pessoas_data) 
        if pessoas_serializer.is_valid(): 
            pessoas_serializer.save() 
            return JsonResponse(pessoas_serializer.data) 
        return JsonResponse(pessoas_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE': 
        pessoa.delete() 
        return JsonResponse({'message': 'Cadastro apagado com sucesso!'}, status=status.HTTP_204_NO_CONTENT)
