from django.urls import path,include
from profiles_api import views

from rest_framework.routers import DefaultRouter
#an other url pathes under the parent url urlpattern wich is api/


router = DefaultRouter()
router.register("helloViewSet",views.helloViewSet,base_name = "helloViewSet")

urlpatterns = [
    #as_view() is a method from the APIView class
    #that we inherited in our helloWorld class
    # that allow django to know that this is ment to be
    # an api view
    path('hello/', views.helloWorld.as_view()),

    path('',include(router.urls)),

]
