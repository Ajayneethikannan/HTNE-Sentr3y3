from rest_framework import routers
from details.views import UserViewSet, AppViewSet


router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'apps', AppViewSet)

urls = router.urls