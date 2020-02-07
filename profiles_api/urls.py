from django.urls import path
from profiles_api import views

#an other url pathes under the parent url urlpattern wich is api/


urlpatterns = [
    #as_view() is a method from the APIView class
    #that we inherited in our helloWorld class
    # that allow django to know that this is ment to be
    # an api view 
    path('hello/', views.helloWorld.as_view()),
]
