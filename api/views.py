from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

from django.core import serializers
# Create your views here.

#for one object
# def student_details(request,pk):
#     stu = Student.objects.get(id = pk)
#     print("stu is",stu)
#     serializer = StudentSerializers(stu)
#     print("serializer is",serializer)
#     json_data = JSONRenderer().render(serializer.data)
#     print("josn data is",json_data)
#     print('data',serializer.data)
#     return HttpResponse(json_data,content_type = 'application/json')


# try another
def student_details(request,pk):
    # stu = Student.objects.get(id = pk)
    stu = Student.objects.all()
    print("stu is.......................................",stu)

    # json_data = serializers.serialize('json', [stu])
    json_data = serializers.serialize('json', stu)

    print("+++++++++++++++++++",json_data)
    return HttpResponse(json_data,content_type = 'application/json')




#for all student(query_set)
def student_list(request):
    stu = Student.objects.all()
    # print("stu is",stu)
    serializer = StudentSerializers(stu,many = True)
    # print("serializer is",serializer)
    # json_data = JSONRenderer().render(serializer.data)
    # print("josn data is",json_data)
    # print('data',serializer.data)
    # return HttpResponse(json_data,content_type = 'application/json')

    # also we can write, comment line 26,29
    return JsonResponse(serializer.data,safe=False)