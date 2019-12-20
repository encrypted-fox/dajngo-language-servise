from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/v0/countries', CountryViewSet, 'countries')

urlpatterns = router.urls
