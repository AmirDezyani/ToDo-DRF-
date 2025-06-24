from django.urls import path

from public.views import TodosViewSet

todos_list=TodosViewSet.as_view({'get':'list', 'post':'create'})
todos_detail=TodosViewSet.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'})

urlpatterns = [
    path('', todos_list, name='todos-list'),
    path('<uuid:pk>', todos_detail, name='todos-detail'),
]