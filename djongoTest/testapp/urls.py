from rest_framework import routers
from django.urls import path
from testapp import views

router = routers.SimpleRouter()
router.register('user', views.UserViewSets)
router.register('manager', views.ManagerViewSets)
urlpatterns = [
    # path('some_functional_view_rul', views.functional_view)
]
urlpatterns += router.urls