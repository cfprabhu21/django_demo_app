from django.urls import path
from .views import CategoryList

urlpatterns = [
    path('category_list/', CategoryList.as_view(), name='category_list'),
]