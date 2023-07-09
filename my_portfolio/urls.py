from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'home'),
    path('profile/',views.profile, name='profile'),
    path('register/',views.register, name = 'register'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name='skills'),
    path('profession/', views.profession, name='profession'),
    path('experience/',views.experience, name='experience')
]
