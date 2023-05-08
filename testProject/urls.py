from django.urls import path
from rest_framework.routers import DefaultRouter
from testProject import views

router = DefaultRouter()
router.register('role', views.RoleViews)

urlpatterns = []
urlpatterns += router.urls
