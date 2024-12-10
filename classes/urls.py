from .views import ClassViewSet, MaterialViewSet, AttendanceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'classes', ClassViewSet, basename='classes')
router.register(r'material', MaterialViewSet, basename='material')
router.register(r'attendance', AttendanceViewSet, basename='attendance')

urlpatterns = router.urls