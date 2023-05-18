from django.urls import path, include
from rest_framework import routers
from taskApi import views

router = routers.DefaultRouter()
router.register(r'task',views.TaskView,'tasks')

#api version

urlpatterns = [
    path("api/v1/", include(router.urls))

]
