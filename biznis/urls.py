from rest_framework import routers
from .views import BusinessViewSet

router = routers.DefaultRouter()
router.register(r'', BusinessViewSet)

urlpatterns = router.urls