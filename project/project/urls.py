"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from stc.views import company_article_list, ChartData, dash, dash_ajax, close_price, StockClose

 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('companies/', company_article_list, name='companies'),
    path('api/chart/data/', ChartData.as_view(), name='api-chart-data'),
    path('close/', close_price, name='close'),
    path('api/chart/close/', StockClose.as_view(), name='api-chart-close'),
	path('dash', dash),
	path('dash', dash_ajax),
	]
