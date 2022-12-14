"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path

from izoor.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'goods', GoodAPIModelView, basename='goods')
router.register(r'organizations', OrganizationAPIModelView)
router.register(r'pos_user', POSUserAPIModelView)
router.register(r'wristband', WristbandView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/women/', WomenCLView.as_view()),
    path('api/v1/woman/<str:pk>/', WomanRUView.as_view()),
    path('api/v1/woman_delete/<str:pk>/', WomanRDView.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/wristbands/', WristbandListView.as_view()),
    path('api/v1/wristband_balance_history/', WristbandBalanceHistoryView.as_view()),
    #path('api/v1/wristband/<str:pk>/', WristbandView.as_view()),
    # path('api/v1/goods_list/', GoodAPIModelView.as_view({'get': 'list'})),
    # path('api/v1/org_list/', OrganizationAPIModelView.as_view({'get': 'list'})),
    # path('api/v1/org_list/<str:pk>/', OrganizationAPIModelView.as_view({'get': 'retrieve'})),
    # path('api/v1/pos_user/', POSUserAPIModelView.as_view({'get': 'list'})),
    # path('api/v1/pos_user/<str:pk>/', POSUserAPIModelView.as_view({'get': 'retrieve'})),

]
