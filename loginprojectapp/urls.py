from unicodedata import name
from django import views
from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.Home,name='Home'),

    path('signup/',views.signup,name='signup'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('about/',views.about,name='about'),

    path('usercreate/',views.usercreate,name="usercreate"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),




    path('Student',views.Student,name='Student'),
    path('student_details',views.student_details,name='student_details'),
    path('student_showpage',views.student_showpage,name='student_showpage'),
    path('student_editpage/<int:pk>',views.student_editpage,name='student_editpage'),
    path('edit_student_details/<int:pk>',views.edit_student_details,name='edit_student_details'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage')
]