from django.http import JsonResponse
from .models import Department,Student
from .serializers import DepartmentSerializer, StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def department_list(request):
    if request.method == 'GET':
        department = Department.objects.all()
        ser = DepartmentSerializer(department, many=True)
        return Response({'department':ser.data})
    elif request.method == 'POST':
        ser = DepartmentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)    

@api_view(['GET','PUT','DELETE'])
def department_details(request,id):
    try:
        print(id)
        department = Department.objects.get(pk=id)
        print(department)
    except Department.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        ser = DepartmentSerializer(department)
        return Response(ser.data)
    elif request.method == 'PUT':
        ser = DepartmentSerializer(department, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
    elif request.method =='DELETE':
        department.delete()
        return Response({'message':f'{department.name} department deleted'},status=status.HTTP_204_NO_CONTENT)
    


@api_view(['GET','POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        ser = StudentSerializer(students, many=True)
        return Response({'students':ser.data})
    elif request.method == 'POST':
        ser = StudentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)    
        
@api_view(['GET','PUT','DELETE'])
def student_details(request,id):
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        ser = StudentSerializer(student)
        return Response(ser.data)
    elif request.method == 'PUT':
        ser = StudentSerializer(student, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
    elif request.method =='DELETE':
        student.delete()
        return Response({'message':f'{student.first_name} {student.last_name} has been deleted'},status=status.HTTP_204_NO_CONTENT)
