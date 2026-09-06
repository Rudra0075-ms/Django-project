from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('students/', views.student_list, name='student_list'),

    path('add/', views.add_student, name='add_student'),

    path('edit/<int:id>/', views.edit_student, name='edit_student'),

    path('delete/<int:id>/', views.delete_student, name='delete_student'),

    path('login/', views.login_view, name='login'),

    path('signup/', views.signup_view, name='signup'),

    path('logout/', views.logout_view, name='logout'),
]