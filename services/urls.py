from rest_framework import routers
from .views import ServiceViewSet

router = routers.DefaultRouter()
router.register(r'', ServiceViewSet)

urlpatterns = router.urls