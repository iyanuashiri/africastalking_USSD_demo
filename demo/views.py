from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.


@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""

        if text == "":
            response = "CON What would you want to check \n"
            # response .= "1. My Account \n"
            response += "1. My Phone Number"


        elif text == "1":
            response = "END My Phone number is {0} Tolu".format(phone_number)

        return HttpResponse(response)
