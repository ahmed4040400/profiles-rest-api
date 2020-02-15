from rest_framework import serializers
from profiles_api import models


"""serializer is a validation class uses a service called ..
   well 'serializer' this allow you to validate the
   post request input like this exaple there
   i'me validating the name to not have more than
   15 chars
"""

class helloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 15);



#another serializer for user profile models
#in this statuation we use another parent class calles ModelSerializer
#instade of Serializer because this add some functionality to the
class userProfileSerializer(serializers.ModelSerializer):
    # a meta calss is a upper levle class in python
    # in this it's required to define the field of the user profile model
    class Meta:
        #refiering to the desired model
        model = models.UserProfile
        #refiering to the desired fields
        fields = ('id','email','name','password')
        #adding some extra key words atguments
        extra_kwargs = {
            # refiering to the field that we want to add the atteripute to
            'password': {
                #making the password field read only
                #to prevent retreiving  (getting it's value) it in any case
                'write_only':True,
                #styling the field in this case we just set the
                #input_type into password incase of a browsable api
                'style':{'input_type':'password'}
            }
        }

    # the creat function the serializer call it automaticly
    # when we use the the UserProfileserializer()

    #that means the creat function is a callback
    def create(self ,validated_data):
        #creating the user profile object in the model

        # validated_data is the valid data that we got from the serializer
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name= validated_data['name'],
            password = validated_data['password']
        )
        #returning the data
        return user
