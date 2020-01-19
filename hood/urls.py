from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^hood/(?P<id>\d+)/',views.hood,name='hood'),
    url(r'^new/hood$', views.new_hood, name='new-hood'),
    url(r'^profile/$', views.profile, name='profile'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)