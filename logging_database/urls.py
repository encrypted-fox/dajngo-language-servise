from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/v0/logging', LoggingViewSet, 'logging')

urlpatterns = router.urls
