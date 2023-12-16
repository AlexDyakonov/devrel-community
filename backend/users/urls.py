from django.urls import path
from .views import UserList, UserDetail, SpecializationList, SkillList, UserLoginView

urlpatterns = [
    path('specializations/', SpecializationList.as_view(), name='specialization-list'),
    path('skills/', SkillList.as_view(), name='skill-list'),
    path('', UserList.as_view(), name='user-list'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]