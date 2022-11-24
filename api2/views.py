from django.shortcuts import render,HttpResponse
from .serializer import StudentSerializer
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from api2.models import Student
@api_view(['GET','POST'])
def get_data(request):
    if request.method == 'GET':
        student = Student.objects.all()
        print(student)
        try:
            serializer = StudentSerializer(student,many = True)
            return Response({"message":[serializer.data[len(serializer.data)-1]]})
        except Exception as e:
            return Response({"error":e})
    elif request.method == 'POST':
        data = request.data
        # #Validating data------
        try:
            data = request.data
            print(data)
            serializer = StudentSerializer(data = data)
            if serializer.is_valid() == True:
                serializer.save()    
                print(serializer.data)
                return Response({"message": "Your data is saved successfully",
                          "status":"Success"
                          })
            
            else:
                return Response({"message": serializer.errors,
                          "status":"Failed"
                          })
            
        except Exception as e:
            return Response({"message":e})
            
            
            
            
            
            
            
            
            
            
            
            
            