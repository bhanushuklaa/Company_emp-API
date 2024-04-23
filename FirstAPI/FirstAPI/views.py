from django.http import HttpResponse, JsonResponse


def home(request):
    print("These is new page...")
    x = ["bhanu", "shreya", "alisha", "harsh"]
    return JsonResponse(x, safe=False)
