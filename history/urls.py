from django.urls import path
from .views import TadaListView, CreateTadaView, approve_paid, tada_pdf_view

urlpatterns = [
    path('', TadaListView.as_view(), name='tada-list'),
    path('create/', CreateTadaView.as_view(), name='tada-create'),
    path('update/<int:pk>/', approve_paid, name='tada-update'),
    path('report-pdf/<pk>/', tada_pdf_view, name='tada-pdf'),
    
]