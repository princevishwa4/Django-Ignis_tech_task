from django.urls import path
from events.views import (
    home,
    user_login,
    user_register,
    user_logout,
    create_event,
    event_detail,
    like_event,
    like_view,
)

urlpatterns = [
    path('', home, name="home"),

    #Authentication
	path('login/', user_login, name="login"),
	path('register/', user_register, name="register"),
	path('logout/', user_logout, name="logout"),

    #Events
    path('create_event/', create_event, name="create_event"),
    path('event_detail/<int:pk>', event_detail, name="event_detail"),
    path('like_event/', like_event, name="like_event"),
    path('like_view/', like_view, name="like_view")
]