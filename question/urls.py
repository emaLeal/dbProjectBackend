from .views import QuestionViewSet, OptionViewSet, StudentQuestionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'question', QuestionViewSet, basename='question')
router.register(r'options', OptionViewSet, basename='option')
router.register(r'student_question', StudentQuestionViewSet, basename='student_question')

urlpatterns = router.urls