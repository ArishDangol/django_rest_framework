from django.http import HttpResponse, JsonResponse


def home_page(request):
    print("Home page requested")  #prints in console
    
    # friends =[
    #     'ankit',
    #     'ravi',
    # ]
    # return JsonResponse(friends, safe=False)
    return HttpResponse("<h1>This is home page</h1>")
    #return HttpResponse("This is home page")
    
    
    
    
    