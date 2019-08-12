from django.urls import path

from . import views

urlpatterns = [
    path('index/',views.index, name='index'),
    path('hash/',views.hash, name='hash'),
    path('base_64/',views.base_64, name='base_64'),
    path('base_642/',views.base_642, name='base_642'),
    path('tizhong/',views.tizhong, name='tizhong'),
    path('yasuo/',views.yasuo, name='yasuo'),
    path('vue_encode/',views.vue_encode, name='vue_encode'),
    path('vue_decode/',views.vue_decode, name='vue_decode'),
    path('vue_json/',views.vue_json, name='vue_json'),
    path('vue_bmi/',views.vue_bmi, name='vue_bmi'),


]