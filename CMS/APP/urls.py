from rest_framework.routers import DefaultRouter
from .views import staffView,signupView,medicineView,doctorView,patientView,PaymentView,PrescribleView,BillingView,appointmentView,timeView,labView,specializationView,qualificationView,GroupView,bloodView,loginView
from django.urls import path


router = DefaultRouter()
router.register(r"staff",staffView)
router.register(r"medicine",medicineView)
router.register(r"doctor",doctorView)
router.register(r"patient",patientView)
router.register(r"payment",PaymentView)
router.register(r"prescribe",PrescribleView)
router.register(r"billing",BillingView)
router.register(r"appointment",appointmentView)
router.register(r"time",timeView)
router.register(r"lab",labView)
router.register(r"group",GroupView)
router.register(r"specialization",specializationView)
router.register(r"qualification",qualificationView)
router.register(r"bg",bloodView)

urlpatterns = [
    path("signup/",signupView.as_view(),name="sigup"),
    path("login/",loginView.as_view(),name="login")
]

urlpatterns += router.urls
# urlspatterns += router.urls
