from django.urls import path
from . import views

urlpatterns = [
    path('ftp_home', views.home, name='ftp_home'),
    path('ftp_data', views.mac_list, name='ftp_data'),
    path('ftp_register', views.registration, name='ftp_register'),
    path('ftp_records', views.records, name='ftp_records'),
    path('delete_record/<int:mobid>', views.delete_record, name='delete_record'),
    path('companyDetails/', views.getCompanyName, name='companydetail'),
    path('ftp_records_api', views.recordsapi, name='ftp_records_api'),

]