from rest_framework.views import APIView
from rest_framework.response import Response



class helloWorld(APIView):
    def get(self , request , format = None):
        return Response({"name":"ahmed" , "future": " drawen :)"})
