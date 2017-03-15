from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import smtplib

sender_email = "enter Email id"
sender_passwd = "password of that"
reciever_email = "reciever email id"
# Create your views here.
def showBase(request):
    Name = 'Django'
    return render(request, 'feedback/form.html', locals())

def formProcess(request):
    if request.method == 'POST':
        print(request.POST.keys())
        Name = request.POST.get('name')
        sender = request.POST.get('email')
        message = request.POST.get('des')
        msg = "Sent by "+ sender + " " + message
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_passwd)
        server.sendmail(sender_email, reciever_email, msg)
        server.quit()

    return render(request, 'feedback/base.html', {'Name': 'Submission DOne'})
