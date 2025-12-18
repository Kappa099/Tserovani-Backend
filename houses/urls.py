from rest_framework import routers
from .views import HouseViewSet

router = routers.DefaultRouter()
router.register(r'', HouseViewSet)

urlpatterns = router.urls