from django.urls import include, path, re_path
from .views import SourceListView, SourceUsersListView, SourceDetailView, SourceUsersDetailView, TopCitiesAPIView, SkillAPIView, SpecializationAPIView, EventStatisticsAPIView, UserEventsAPIView


urlpatterns = [
    path('sources/', SourceListView.as_view(), name='source-list'),
    path('source-users/', SourceUsersListView.as_view(), name='source-users-list'),
    path('sources/<int:pk>/', SourceDetailView.as_view(), name='source-detail'),
    path('source-users/<int:pk>/', SourceUsersDetailView.as_view(), name='source-users-detail'),
    path('top-cities/', TopCitiesAPIView.as_view(), name='top-cities'),
    path('skills/', SkillAPIView.as_view(), name='skills'),
    path('specializations/', SpecializationAPIView.as_view(), name='specializations'),
    path('event-statistics/', EventStatisticsAPIView.as_view(), name='event-statistics'),
    path('user-events/<int:user_id>/', UserEventsAPIView.as_view(), name='user-events'),
]
