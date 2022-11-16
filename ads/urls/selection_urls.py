from django.urls import path

from ads.views import SelectionListView, SelectionDetailView, SelectionCreateView, SelectionUpdateView, \
    SelectionDeleteView

urlpatterns = [
    path('', SelectionListView.as_view(), name='all_selection'),
    path('<int:pk>/', SelectionDetailView.as_view()),
    path('create/', SelectionCreateView.as_view(), name='create_selection'),
    path('update/<int:pk>/', SelectionUpdateView.as_view()),
    path('<int:pk>/delete/', SelectionDeleteView.as_view()),
]
