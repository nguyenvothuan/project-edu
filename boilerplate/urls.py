"""boilerplate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from boilerplate.swagger import schema_view
urlpatterns = [
    path('admin/', admin.site.urls),

    path('docs/', schema_view.with_ui("swagger",
         cache_timeout=0), name="schema_view"),

    path('api/v1.0/accounts/',
         include("accounts.urls", namespace="accounts-api")),

    path('api/v1.0/companies/',
         include("companies.urls", namespace="companies-api")),

    path('api/v1.0/schools/',
         include("schools.urls", namespace="schools-api")),

    path("graphql/", GraphQLView.as_view(graphiql=True)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
