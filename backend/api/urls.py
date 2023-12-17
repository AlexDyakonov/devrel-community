from django.urls import include, path, re_path
from .views import EventList, EventDetail, FormFieldsListCreateView, FormFieldsDetailView, UserByTokenAPIView, \
    AskGPTView, ParticipateView

urlpatterns = [
    path('events/', EventList.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
    path('events/<int:pk>/participate', ParticipateView.as_view(), name='event-participate'),
    path('formfields/', FormFieldsListCreateView.as_view(), name='formfields-list-create'),
    path('formfields/<int:pk>/', FormFieldsDetailView.as_view(), name='formfields-detail'),
    path('user-by-token/', UserByTokenAPIView.as_view(), name='user-by-token'),
    path('ask-gpt/', AskGPTView.as_view(), name='ask-gpt')
]
]
