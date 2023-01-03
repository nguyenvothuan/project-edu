
from django.urls import path
from companies.views import CompanyViewSet
from rest_framework.routers import SimpleRouter
app_name = 'companies'

router = SimpleRouter()
router.register("", CompanyViewSet, basename="posts")
urlpatterns = router.urls
