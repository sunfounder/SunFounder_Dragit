from django.shortcuts import render_to_response
from django.http import HttpResponse

def home(request):
    return render_to_response("snap.html")

def SnapCloud(request):
    if 'SESSIONGLUE' in request.GET:
        session_glue = request.GET['SESSIONGLUE']
        print("Get SESSIONGLUE: %s"%session_glue)
    else:
        if 'Username' in request.GET:
            username = request.GET['Username']
            print("Get Username: %s"%username)
        if 'Email' in request.GET:
            email = request.GET['Email']
            print("Get Email: %s"%email)
	if request.POST:
		print request.POST

    return HttpResponse('OK')