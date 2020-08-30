
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('app.urls'))
]


# celery -A mydiplom worker --pool=solo -l info
# celery -A mydiplom worker -l info -P eventlet