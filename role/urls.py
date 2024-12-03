from .views import RoleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'role', RoleViewSet, basename='role')
urlpatterns = router.urls