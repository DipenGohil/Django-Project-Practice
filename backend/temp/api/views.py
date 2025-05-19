from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    data = {}
    body = request.body
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    return JsonResponse({"message": "hi, this is django api response"})


