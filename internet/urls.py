from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home-internet/', views.home_internet, name='home-internet'),
    path('corporate-internet/', views.corporate_internet, name='corporate-internet'),
    path('sme-internet/', views.sme_internet, name='sme-internet'),
    path('cloud-pabx/', views.cloud_pabx, name='cloud-pabx'),
    path('cloud-pabx/audio-video-calling-group-chat-sms/', views.audio_video_calling_group_chat_sms, name='audio-video-calling-group-chat-sms'),
    path('cloud-pabx/employee-attendance/', views.employee_attendance, name='employee-attendance'),
    path('support/', views.support, name='support'),
    path('bill-pay/', views.bill_pay, name='bill-pay'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

