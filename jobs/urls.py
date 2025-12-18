from rest_framework import routers
from .views import JobViewSet

router = routers.DefaultRouter()
router.register(r'', JobViewSet)

urlpatterns = router.urls