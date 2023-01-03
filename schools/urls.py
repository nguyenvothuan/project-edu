
from django.urls import path
from schools.views import SchoolViewSet
from rest_framework.routers import SimpleRouter
app_name = 'schools'

router = SimpleRouter()
router.register("", SchoolViewSet, basename="School")
urlpatterns = router.urls
