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

router.register('test/nuts1', views.Bruttoinlandsproduktnuts1ViewSet)
# router.register('bruttoinlandsprodukt/nuts3', views.Bruttoinlandsproduktnuts3ViewSet)



app_name = 'statistik'

urlpatterns = [
    path('', include(router.urls)),
    path('<str:indicator_type>/', views.BaseIndikatorViewSet.as_view({'get': 'list'}), name='base-indikator-list'),
    # path('bruttoinlandsprodukt', views.BaseIndikatorViewSet.as_view({'get': 'list'}), name='bruttoinlandsprodukt'),
    # path('erwerbtaetige', views.BaseIndikatorViewSet.as_view({'get': 'list'}), name='erwerbtaetige'),
]
# urlpatterns = [
#     path('', include(router.urls)),
# ]