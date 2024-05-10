"""
URL mapping for the statistik app.
"""

from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from statistik import views




app_name = 'statistik'

urlpatterns = [
    path('bruttoinlandsprodukt/nuts1/', views.BruttoinlandsproduktNuts1ViewSet.as_view({'get': 'list'}), name='bruttoinlandsprodukt_nuts1'),
    path('bruttoinlandsprodukt/nuts3/', views.BruttoinlandsproduktNuts3ViewSet.as_view({'get': 'list'}), name='bruttoinlandsprodukt_nuts3'),
    path('erwerbtaetige/nuts1/', views.IndikatorErwerbstaetigeNuts1ViewSet.as_view({'get': 'list'}), name='erwerbtaetige_nuts1'),
    path('erwerbtaetige/nuts3/', views.IndikatorErwerbstaetigeNuts3ViewSet.as_view({'get': 'list'}), name='erwerbtaetige_nuts3'),
    path('metadaten/', views.MetaDatenViewSet.as_view({'get': 'list'}), name='metadaten'),
]

