from django.urls import path
from . import views


urlpatterns = [
    path('', views.InvoiceListView.as_view(), name='home'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('invoices/new/', views.InvoiceCreateView.as_view(), name='new-invoice'),
    path('invoices/<int:pk>/', views.InvoiceDetailView.as_view(), name='invoice-detail'),
    path('clients/', views.ClientListView.as_view(), name='client-list'),
    path('clients/new/', views.ClientCreateView.as_view(), name='new-client'),
    path('clients/<int:pk>/', views.ClientDetailView.as_view(), name='client-detail'),
]
