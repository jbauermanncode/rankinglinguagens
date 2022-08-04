
from django.contrib import admin
from django.urls import include, path
from linguagens_api.views import LinguagensViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('linguagens',LinguagensViewSet, basename = 'Linguagens')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
