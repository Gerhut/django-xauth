from django.http import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from django.contrib.auth import authenticate

def login(request):
    try:
        username = request.META['HTTP_X_AUTH_USERNAME']
        password = request.META['HTTP_X_AUTH_PASSWORD']
    except KeyError:
        return HttpResponseBadRequest()

    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponseNotFound()

    return JsonResponse({
        'email': user.email
    })