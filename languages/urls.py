from rest_framework import routers
from .api import LanguageViewSet

router = routers.DefaultRouter()
router.register('api/v0/languages', LanguageViewSet, 'languages')

urlpatterns = router.urls
