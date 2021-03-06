# APIView is a view to api calling
# any api serving class should inherit it
from rest_framework.views import APIView

# viewsets is view to also api calling but in much simpler way
# ant basic api serving class should inherit it
from rest_framework import viewsets

from rest_framework import filters
# what this does is asking for authtoken to add to the
# url to know which user is making the request
# or if its authed user or not
# auth token is just a hash of string
from rest_framework.authentication import TokenAuthentication
# this is a pre made login view that comes with a rest_framework
# that we can use to generate an authtoken
from rest_framework.authtoken.views import ObtainAuthToken

# allow us to access some setting in the rest api testing console
from rest_framework.settings import api_settings
# a pre made permission that make sure the user is authenticated
# if not it blocks his ability's so he cant read or write data
from rest_framework.permissions import IsAuthenticated

# this import serves the responding
# it return json format as default
from rest_framework.response import Response
# importing the serializer (validator) that we've created
from profiles_api import serializer

# importing the models
from profiles_api import models
# the file that contains all the permissions
from profiles_api import permissions


# creating the view and inherit the APIView
# cause its an api serving class
class helloWorld(APIView):
    # this creating instance of the serializer (validator)
    # that we've created
    serializer_class = serializer.HelloSerializer

    # in case the request method is get
    # we return a dummy data with status code 200 ok
    def get(self, request, format=None):
        return Response({"name": "ahmed", "future": " drawen :)"})

    # in case the request method is post
    # we validate the input first using serializer
    # and if its valid we return the hello message with
    # status code 200 ok ,
    # but if it's not valid we return the error statment
    # from the serializer with status code 400 bad request
    def post(self, request):
        # pass the data to the serializer to validate it
        serializer = self.serializer_class(data=request.data)
        # making decision depending on the validity
        if serializer.is_valid():
            # getting the valid data from the serializer
            name = serializer.validated_data.get('name')
            # return the hello message with status code 200 ok ,
            return Response({"message": f"hello {name}"})

        else:
            # return the error statment
            # from the serializer with status code 400 bad request
            return Response(serializer.errors, status=400)

    # in case the request method is put
    # we just return dummy data with the method name
    # put is for updating the whole view
    def put(self, request, pk=None):
        return Response({"method": "put"})

    # in case the request method is patch
    # we just return dummy data with the method name
    # patch is for updating a specifice object of the views module
    def patch(self, request, pk=None):
        return Response({"method": "patch"})

    # in case the request method is delete
    # we just return dummy data with the method name
    # delete is for deleting a specifice object of the views module
    def delete(self, request, pk=None):
        return Response({"method": "delete"})


# creating the view and inherit the viewsets
# cause its a basic api serving class
class helloViewSet(viewsets.ViewSet):
    serializer_class = serializer.HelloSerializer

    # in case the request mthod is get
    def list(self, req):
        return Response({"viewsets": True})

    def create(self, req):
        # pass the data to the serializer to validate it
        serializer = self.serializer_class(data=req.data)
        # making decision depending on the validity
        if serializer.is_valid():
            # getting the valid data from the serializer
            name = serializer.validated_data.get('name')
            # return the hello message with status code 200 ok ,
            return Response({"message": f"hello {name}"})
        else:
            # return the serializer eroor message with a status code  400 bad requist
            return Response(serializer.errors, status=400)

    # in viewsets if the function require pk
    # it won't be visible til we put the desired pk in the url

    # retreive is for getting an specific object by its pk (primary key) (id)
    def retrieve(self, req, pk=None):
        return Response({"dummy data": "retrieve"})

    # in case the request method is put
    def update(self, req, pk=None):
        return Response({"dummy data": "update"})

    # in case the request method is put
    def partial_update(self, req, pk=None):
        return Response({"dummy data": "partial_update"})

    # in case the request method is patch
    def destroy(self, req, pk=None):
        return Response({"dummy data": "destroy"})


# this view for showing all the  profiles that created
# and allow adding more and delete own individual profiles
# with a really handy class (viewsets.ModelViewSet)
# that allow us dealing with models and serializers a lot easier
class UserProfileViewSet(viewsets.ModelViewSet):
    # defining the serializer_class to manage adding the data
    # with a validation
    serializer_class = serializer.UserProfileSerializer
    # the queryset is to referee to a place to read the data from
    queryset = models.UserProfile.objects.all()

    # the authentication_classes is a class variable
    # to add a authentication method that we are using with the api
    # in this case we're using TokenAuthentication
    # which is requires an authToken
    # the authToken well be generated by the ObtainAuthToken later
    # in other class
    authentication_classes = (TokenAuthentication,)
    # permission_classes to add permissions to the user behavior
    # so he doesn't ruin the data base

    # so any request gonna be made on this view will go
    # first to check if its legit and allow it
    # if its not legit it will block the request
    permission_classes = (permissions.UpdateOwnProfile,)

    # adding a searching functionality using the class search filter from rest_framework
    filter_backends = (filters.SearchFilter,)
    # adding the fields that the user can use to lok
    search_fields = ('name', 'email',)


# like i said ObtainAuthToken is a view
# that allow us to generate a auth token in order to
# make an authenticated request to have advantage of
# the services that requires authentication
# it's a login view and we're overriding it
class UserLoginApiView(ObtainAuthToken):
    # in order to have the ObtainAuthToken
    # in the rest_framework testing console
    # we have to overrider this class variable
    # and add the default renderer from the api_settings

    # renderer functionality : it just take the view and
    #                         allow interacting with it
    #                         in the rest_framework testing console
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("status_text", "user_profile", "create_on")

    # it's a callback that get called when the view is ready to
    # create an other object using the serializer
    # and we override it to add the user_profile parameter
    # using the _serializer.save() method
    def perform_create(self, _serializer):
        _serializer.save(user_profile=self.request.user)
