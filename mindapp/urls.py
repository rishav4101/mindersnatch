from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('situation',views.answer, name="index"),
    path('leaderboard',views.leaderboard,name="leaderboard")
]