from .models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

@permission_classes([IsAuthenticated])
class student_Views(APIView):
    
    def get(self, request, pk=-1):  # axios.get
        if pk > -1:
            my_model = Student.objects.get(id=pk)
            serializer = StudentSerializer(my_model, many=False)
        else:
            my_model = Student.objects.all()
            serializer = StudentSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):  # axios.post
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):  # axios.put
        my_model = Student.objects.get(pk=pk)
        serializer = StudentSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):  # axios.delete
        my_model = Student.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)