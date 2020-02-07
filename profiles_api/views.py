#APIView is a view to api callin
#any api serving class should inherit it
from rest_framework.views import APIView
#this import serves the responsing
#it return json format as default
from rest_framework.response import Response
#importing the serializer (validator) that we've created
from profiles_api import serializer


#creating the view and inherit the APIView
#cause its an api serving class
class helloWorld(APIView):
    #this creating instance of the serializer (validator)
    # that we've created
    serializer_class = serializer.helloSerializer
    #in case the request method is get
    #we return a dummy data with status code 200 ok
    def get(self , request , format = None):
        return Response({"name":"ahmed" , "future": " drawen :)"})
    # in case the request method is post
    # we validate the input first using serializer
    # and if its valid we return the hello message with
    #status code 200 ok ,
    # but if it's not valid we return the error statment
    #from the serializer with status code 400 bad request
    def post(self , request):
        # pass the data to the serializer to validate it
        serializer = self.serializer_class(data = request.data)
        #making decision depending on the validity
        if serializer.is_valid():
            # getting the valid data from the serializer
            name = serializer.validated_data.get('name')
            #return the hello message with status code 200 ok ,
            return Response ({"message" : f"hello {name}"})

        else :
            # return the error statment
            #from the serializer with status code 400 bad request
            return Response (serializer.errors, status = 400)

    def put (self , request , pk = None):
        return Response({"method" : "put"})

    def patch (self , request , pk = None):
        return Response({"method" : "patch"})

    def delete (self , request , pk = None):
        return Response({"method" : "delete"})
