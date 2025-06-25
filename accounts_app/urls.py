from django.urls import path

from accounts_app.views import ProfileViewSet

profile_list = ProfileViewSet.as_view({'get':'list','post':'create'})
profile_detail = ProfileViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'})

urlpatterns = [
    path('', profile_list, name='profile-list'),
    path('<int:pk>', profile_detail, name='profile-detail'),
]