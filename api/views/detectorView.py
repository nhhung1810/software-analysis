from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ..producer import producer
import json


@csrf_exempt
def detect(request):
    if request.method != 'POST':
        return HttpResponse(json.dumps({"error": "Invalid Method, only POST method is supported"}))

    plate_number = request.POST['plate_number']
    lat = request.POST['lat'] if 'lat' in request.POST else ''
    lon = request.POST['lon'] if 'lon' in request.POST else ''
    detected_time = request.POST['detected_time'] if 'detected_time' in request.POST else ''

    data = {
        'plate_number': plate_number,
        'lat': lat,
        'lon': lon,
        'detected_time': detected_time
    }
    producer.Producer.send('my_topic', data)
    return HttpResponse(json.dumps({'message': 'Received report for plate number {}'.format(plate_number)}))
