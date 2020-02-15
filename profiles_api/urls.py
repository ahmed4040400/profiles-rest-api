from django.urls import path,include
from profiles_api import views
#router is a way to define a urlpattern for a ViewSet
from rest_framework.routers import DefaultRouter
#an other url pathes under the parent url urlpattern wich is api/

#making instance of the router
router = DefaultRouter()
#adding the urlpattern and the view and the basename (just the name)
#and register it to the router
router.register("helloViewSet",views.helloViewSet,base_name = "helloViewSet")
# in this router we don't need to add the basename
#bacause a already added a queryset in this class
#wich leads the rest_framework to get the basename
#from this queryset
router.register('profile',views.UserProfileViewSet)
urlpatterns = [
    #as_view() is a method from the APIView class
    #that we inherited in our helloWorld class
    # that allow django to know that this is ment to be
    # an api view
    path('hello/', views.helloWorld.as_view()),
    #including all the urls inside the router
    #in this case its just one viewset inside the router
    path('',include(router.urls)),

]
