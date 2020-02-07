from rest_framework import serializers


"""serializer is a validation class uses a service called ..
   well 'serializer' this allow you to validate the
   post request input like this exaple there
   i'me validating the name to not have more than
   15 chars 
"""

class helloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 15);
