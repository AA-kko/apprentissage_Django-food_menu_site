from django.urls import path
from . import views

urlpatterns = [
    #avant il y a toujours /food/
    path('',views.index,name='index'),
    path('item/',views.item,name='item'),
    path('<int:item_id>',views.detail,name='detail'),
 ]
