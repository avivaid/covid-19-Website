
from django.urls import path
from myapp  import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('usaState', views.usState, name = 'usaState' ),
    path('restoftheworld', views.keycountryies , name = 'row'),
    path('usaDeath', views.usaDeath, name = 'usaDeath'),
 	path('login/', auth_views.LoginView.as_view() , name = 'login'),
	path('register/', views.register , name = 'register'),
 	path('logout/', views.logoutUserOut , name = 'logout'),
 	path('chat/<str:room_name>/', views.chatrooms, name='chatroom'),
]


