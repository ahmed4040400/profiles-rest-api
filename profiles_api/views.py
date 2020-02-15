#APIView is a view to api calling
#any api serving class should inherit it
from rest_framework.views import APIView

#viewsets is view to also api calling but in much simpler way
#ant basic api serving class should inherit it
from rest_framework import viewsets
#what this does is Generating a authtoken to add to the
#url to know which user is making the requist
#or if its authed user or not
# auth token is just a hash of string
from rest_framework.authentication import TokenAuthentication
#this import serves the responsing
#it return json format as default
from rest_framework.response import Response
#importing the serializer (validator) that we've created
from profiles_api import serializer

#importing the models
from profiles_api import models

from profiles_api import permissions




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
    # in case the request method is put
    # we just return dummy data with the method name
    # put is for updating the whole view
    def put (self , request , pk = None):
        return Response({"method" : "put"})
    # in case the request method is patch
    # we just return dummy data with the method name
    #patch is for updating a specifice object of the views module
    def patch (self , request , pk = None):
        return Response({"method" : "patch"})
    # in case the request method is delete
    # we just return dummy data with the method name
    #delete is for deleting a specifice object of the views module
    def delete (self , request , pk = None):
        return Response({"method" : "delete"})


#creating the view and inherit the viewsets
#cause its a basic api serving class
class helloViewSet(viewsets.ViewSet):

    serializer_class = serializer.helloSerializer


    #in case the request mthod is get
    def list (self,req):
        return Response({"viewsets":True})

    def create (self,req):
        # pass the data to the serializer to validate it
        serializer = self.serializer_class(data = req.data)
        #making decision depending on the validity
        if serializer.is_valid():
            # getting the valid data from the serializer
            name = serializer.validated_data.get('name')
            #return the hello message with status code 200 ok ,
            return Response ({"message" : f"hello {name}"})
        else:
            #return the serializer eroor message with a status code  400 bad requist
            return Response(serializer.errors , status = 400)


    # in viewsets if the function require pk
    # it won't be visible til we put the desired pk in the url


    # retreive is for getting an specific object by its pk (primary key) (id)
    def retrieve(self , req , pk = None):
        return Response({"dummy data" : "retrieve"})

    #in case the request method is put
    def update(self , req , pk = None):
        return Response({"dummy data" : "update"})


    #in case the request method is put
    def partial_update(self , req , pk = None):
        return Response({"dummy data" : "partial_update"})



    #in case the request method is patch
    def destroy(self , req , pk = None):
        return Response({"dummy data" : "destroy"})







class UserProfileViewSet(viewsets.ModelViewSet):
    #defineing the serializer_class to  manage adding the data
    #with a validation
    serializer_class = serializer.userProfileSerializer
    # the queryset is to refiere to a place to read the data from
    queryset = models.UserProfile.objects.all()

    #the authentication_classes to add a auth token to the
    #requist url to know which user is making the requist
    authentication_classes = (TokenAuthentication,)
    #permission_classes to add permissions to the user behavior
    #so he dosen't ruin the data base

    # so any requist gonna be made on this view will go
    # first to check if its legit and allow it
    # if its not legit it will block the requist 
    permission_classes = (permissions.UpdateOwnProfile,)
