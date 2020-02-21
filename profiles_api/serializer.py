from rest_framework import serializers
from profiles_api import models

"""serializer is a validation class uses a service called ..
   well 'serializer' this allow you to validate the
   post request input like this exaple there
   i'me validating the name to not have more than
   15 chars
"""


class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=15);


# another serializer for user profile models
# in this situation we use another parent class called ModelSerializer
# instate of Serializer because this add some functionality to the
# to the serializer that allow us to control the models a lot easier
class UserProfileSerializer(serializers.ModelSerializer):
    # a meta class is a upper level class in python
    # in this it's required to define the field of the user profile model
    class Meta:
        # referring to the desired model
        model = models.UserProfile
        # referring to the desired fields
        fields = ('id', 'email', 'name', 'password')
        # adding some extra key words arguments
        extra_kwargs = {
            # referring to the field that we want to add the attribute to
            'password': {
                # making the password field read only
                # to prevent retrieving  (getting it's value) it in any case
                'write_only': True,
                # styling the field in this case we just set the
                # input_type into password incas of a brows able api
                'style': {'input_type': 'password'}
            }
        }

    # the create function the serializer call it automatic
    # when we use the the UserProfileSerializer()

    # that means the create function is a callback (abstract method)
    def create(self, validated_data):
        # creating the user profile object in the model

        # validated_data is the valid data that we got from the serializer
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        # returning the data
        return user


# a validation for the ProfileFeedItem model
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        # referring to the model
        model = models.ProfileFeedItem
        # the field that's in the model
        fields = ("id", "user_profile", "status_text", "create_on")
        # we don't need the user to write anything but status_text
        # to the feed model and the id and create_on field
        # are read_only by default so we make the user_profile
        # read only as well
        extra_kwargs = ({"user_profile": {"read_only": True}})
