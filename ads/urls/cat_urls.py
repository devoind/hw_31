from django.urls import path
from ads.views import CategoryView, CategoryDetailView, CategoryUpdateView, CategoryCreateView, CategoryDeleteView

urlpatterns = [
    path('', CategoryView.as_view(), name='all_categories'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='cat_detail'),
    path('update/<int:pk>/', CategoryUpdateView.as_view()),
    path('create/', CategoryCreateView.as_view()),
    path('<int:pk>/delete/', CategoryDeleteView.as_view()),
]
