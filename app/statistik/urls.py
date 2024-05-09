"""
URL mapping for the statistik app.
"""

from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from statistik import views

router = DefaultRouter()

# router.register('bruttoinlandsprodukt/nuts1', views.Bruttoinlandsproduktnuts1ViewSet)
# router.register('bruttoinlandsprodukt/nuts3', views.Bruttoinlandsproduktnuts3ViewSet)



app_name = 'statistik'

urlpatterns = [
    path('bruttoinlandsprodukt/nuts1', views.Bruttoinlandsproduktnuts1ViewSet.as_view({'get': 'list'}), name='bip-statistik'),
    path('statistik/erwerbtaetige/', views.Bruttoinlandsproduktnuts1ViewSet.as_view({'get': 'list'}), name='erwerbtaetige-statistik'),
]
# urlpatterns = [
#     path('', include(router.urls)),
# ]