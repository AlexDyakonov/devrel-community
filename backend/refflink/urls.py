from django.urls import path
from .views import ReffLinkListView, ReffLinkDetailView, ReffLinkRedirectView

urlpatterns = [
    path('manage/', ReffLinkListView.as_view(), name='refflink-list'),
    path('manage/<int:pk>/', ReffLinkDetailView.as_view(), name='refflink-detail'),
    path('go/<str:pk>', ReffLinkRedirectView.as_view(), name='redirect-ref')
]
