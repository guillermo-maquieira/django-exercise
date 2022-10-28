from django.contrib import admin
from django.urls import path
from valerdat import prodsApiView, coordsprodsApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('valerdat/prods/', prodsApiView.as_view()),
    path('valerdat/coordsprods/', coordsprodsApiView.as_view()),
]