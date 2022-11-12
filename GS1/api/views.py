from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Model object -- Single student data 

# function based view example to get one object from student model
def student_detail(request,pk):
    # stu = Student.objects.get(id=2) # we created model object which was a comples data 
    # id =2 will default pull the seconf value 
    # we can use primary key to get id from user 
    stu = Student.objects.get(id=pk)
    print(stu)
    # output - Student object (2)
    serializer = StudentSerializer(stu) # converted to python data object 
    print(serializer)
    # Output -
    # StudentSerializer(<Student: Student object (2)>):
    # name = CharField(max_length=50)
    # roll = IntegerField()
    # city = CharField(max_length=40)
    print(serializer.data)
    # Output - 
    #{'name': 'shweta', 'roll': 201, 'city': 'pune'}
    
    ######### deserialized to seend the data to http reponse ##########
    # json_data  = JSONRenderer().render(serializer.data) # serialized data will be stored in data variable passed here . Python data  converted to json
    # print(json_data)
    # # Output -
    # #b'{"name":"shweta","roll":201,"city":"pune"}'
    # # we have to now send the json data as response to client
    # return HttpResponse(json_data, content_type='application/json')
    
    ######### using json response ##########
    return JsonResponse(serializer.data)

# function based on query set - All Student data 
# this will print all data from student model 
def student_list(request):
    stu = Student.objects.all()
    # output - Student object (2)
    serializer = StudentSerializer(stu,many=True) # converted to python data object 
    ########### using HttpReponse ##########
    # json_data  = JSONRenderer().render(serializer.data) # serialized data will be stored in data variable passed here . Python data  converted to json
    # return HttpResponse(json_data, content_type='application/json')

    ####### using JsonResponse ###########
    return JsonResponse(serializer.data,safe=False)
