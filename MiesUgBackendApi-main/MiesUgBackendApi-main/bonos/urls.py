
from django.urls import path, re_path
from bonos import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    
   path('bonos/', views.Crudbonos.list_bono_view),
   path('bonos/<int:pk>/', views.Crudbonos.user_detail_view),
   
  #path('bonos/',views.listBons.as_view())
  # path('^bonos/(?P<entrepreneur>.+)/$', bonosListView.as_view()),
]
