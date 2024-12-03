from .views import StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'student', StudentViewSet, basename='student')
urlpatterns = router.urls