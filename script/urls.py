from django.urls import path
from .import views

app_name = 'script'

urlpatterns=[
    path('large1js',views.script_large1js,name="large1js"),
    path('large2js',views.script_large2js, name="large2js"),
    path('palindrome',views.script_palindrome, name="palindrome"),
    path('element1',views.script_element1, name="element1"),
    path('element2',views.script_element2, name="element2")

]