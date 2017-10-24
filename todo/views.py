from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser, FileUploadParser, FormParser, MultiPartParser
from rest_framework.response import Response
from todo.serializers import ToDoSerializer
from django.core.files.storage import FileSystemStorage
from todo.models import ToDo
from todo.models import Uploads
from todo.serializers import UploadsSerializer

class ToDoListView(APIView):
    def get(self, request):
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        print(get_client_ip(request))
        return Response(serializer.data)

    def put(self, request):
        print(request.data)
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDoDetailView(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(ToDo, pk=pk)
        serializer = ToDoSerializer(todo)
        return Response(serializer.data)

    def delete(self, request, pk):
        todo = get_object_or_404(ToDo, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UploadsListView(APIView):
    parser_classes = (FormParser, MultiPartParser,FileUploadParser,)

    def get(self, request):
        uploads = Uploads.objects.all()
        #serializer = UpSerializer(todos, many=True)
        serializer = UploadsSerializer(uploads,many=True)
        return Response(serializer.data)

    def put(self,request):
        file_obj = request.FILES['upload']
        #print(file_obj)
        fs = FileSystemStorage()
        filename = fs.save(file_obj.name, file_obj)
        uploaded_file_url = fs.url(filename)
        print("i am upload ")
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
        #file_obj = request.data['file']
        #uploads = Uploads.objects.all()
        #serializer = ToDoSerializer(data=request.data)
        #serializer = UploadsSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       # return Response({"Name":"Samaid"});
    def post(self,request):
        print(request.data.get('name'))
        ip = get_client_ip(request)
        new_upload = Uploads.objects.create(file=request.FILES['abc'],ip= ip, name=request.data.get('name') )
        new_upload.save()
        my_upload = Uploads.objects.filter(name=request.data.get('name'))
        print(get_client_ip(request))
        #print(my_upload.file.path)
        #file_obj = request.FILES['abc']
        #print(file_obj)
        #import pdb; pdb.set_trace()

        # fs = FileSystemStorage()
        # filename = fs.save(file_obj.name, file_obj)
        # uploaded_file_url = fs.url(filename)

        # print("i am upload ")
        # return render(request, 'core/simple_upload.html', {
        #     'uploaded_file_url': uploaded_file_url
        # })
        #file_obj = request.data['file']
        #uploads = Uploads.objects.all()
        serializer = UploadsSerializer(my_upload , many=True)
        # serializer = UploadsSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



