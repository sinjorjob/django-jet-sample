from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls')),  
    path('jet/dashboard/', include('jet.dashboard.urls',namespace='jet-dashboard')),#追加
]
