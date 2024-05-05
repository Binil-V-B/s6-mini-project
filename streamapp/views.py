from django.shortcuts import render
from django.http.response import StreamingHttpResponse
# from django.http import HttpResponse
from streamapp.camera import VideoCamera #, LiveWebCam
# Create your views here.

def index(request):
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






