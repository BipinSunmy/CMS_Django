from rest_framework.routers import DefaultRouter
from .views import staffView,signupView
from django.urls import path


router = DefaultRouter()
router.register(r"staff",staffView)


urlpatterns = [
    path("signup/",signupView.as_view(),name="sigup")
]

urlpatterns += router.urls
# urlspatterns += router.urls
