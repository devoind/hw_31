from django.urls import path
from ads.views import AdListView, AdDetailView, AdCreateView, AdDeleteView, AdUpdateView

urlpatterns = [
    path('', AdListView.as_view(), name='list_ad'),
    path('<int:pk>/', AdDetailView.as_view(), name='detail_ad'),
    path('create/', AdCreateView.as_view(), name='ad_create'),
    path('<int:pk>/upload_image/', AdUpdateView.as_view()),
    path('<int:pk>/delete/', AdDeleteView.as_view()),
]
