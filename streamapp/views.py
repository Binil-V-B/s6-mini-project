from django.shortcuts import render,redirect
import datetime
from django.http.response import StreamingHttpResponse
# from django.http import HttpResponse
from streamapp.camera import VideoCamera #, LiveWebCam
from .models import user
# Create your views here.

def index(request):
	if request.method=='POST':
		user_name=request.POST.get('u_name')
		phone_number=request.POST.get('ph_no')
		vehicle_reg_no=request.POST.get('veh_no')
		time=datetime.datetime.now()
		user_new=user.objects.create(name=user_name,phone_no=phone_number,vehicle_reg_no=vehicle_reg_no,login_time=time)
		user_new.save()
		return redirect('video')
	else:
		return render(request,'login/main.html')


def vid(request):
	return render(request, 'streamapp/video.html')


def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')






