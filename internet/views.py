from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home_internet(request):
    return render(request, 'home-internet.html')

def corporate_internet(request):
    return render(request, 'corporate-internet.html')

def sme_internet(request):
    return render(request, 'sme-internet.html')

def cloud_pabx(request):
    return render(request, 'cloud-pabx.html')

def audio_video_calling_group_chat_sms(request):
    return render(request, 'audio-video-calling-group-chat-sms.html')

def employee_attendance(request):
    return render(request, 'employee-attendance.html')

def support(request):
    return render(request, 'support.html')

def bill_pay(request):
    return render(request, 'bill-pay.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')