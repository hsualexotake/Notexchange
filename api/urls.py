
from django.urls import path
#from .views import main
from . import views


from .views import RoomView,CreateRoomView, GetRoom

urlpatterns = [
    
    #path("", main)

    #path('home',views.main)

    path('room', RoomView.as_view()),
    path('create-room', CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view())
   
 

]
#name='home