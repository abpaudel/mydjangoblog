from django.http import JsonResponse

def page_not_found(request):
   	return JsonResponse(status=404, data={'status':'404','message':'Not found'})

def server_error(request):
   	return JsonResponse(status=500, data={'status':'500','message':'Internal Server Error'})
