from django.urls import include, path
from rest_framework import routers
from backend import views

router = routers.DefaultRouter()
router.register(r'troops', views.TroopViewSet)
router.register(r'patrols', views.PatrolViewSet)
router.register(r'scouts', views.ScoutViewSet)
router.register(r'scores', views.ScoreViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]