from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

#for rest_framework. using"GET" for api/chart/data
from rest_framework.response import Response
from rest_framework.views import APIView

from django.views.decorators.csrf import csrf_exempt

from .models import Company
from .as_dash import dispatcher

def company_article_list(request):
	return render(request, "stc/plotly.html", {})  
	#will not return anything. will use js


#for api/chart/data
class ChartData(APIView):
	#could do authenication and permission, but not doing
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, format=None):
        articles = dict()
        #information from .models
        for company in Company.objects.all():
        	#filters out companies with articles 
            if company.articles > 0:
            	#make key value pairs of company name and article
                articles[company.name] = company.articles
    	#artiles is a dictionary, use .items to iterate and sort in ascend order
        articles = sorted(articles.items(), key=lambda x: x[1])
        #items returned in dictionary
        articles = dict(articles)

        #used for x, y values for plotly.html
        #return in .json
        data = {
            "article_labels": articles.keys(),
            "article_data": articles.values(),
        }
    	#return data for GET f(), plotly.html
        return Response(data)



### dash ###

def dash(request, **kwargs):
    return HttpResponse(dispatcher(request))


@csrf_exempt
def dash_ajax(request):
    return HttpResponse(dispatcher(request), content_type='application/json')
