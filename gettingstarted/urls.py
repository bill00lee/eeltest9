from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

from products.views import (
                            ProductListView,
                            product_list_view,
                            ProductDetailView,
                            product_detail_view,
                            ProductFeaturedListView,
                            ProductFeaturedDetailView)

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.home_page, name='home_page'),
    url(r'^about_page/$', hello.views.about_page, name= 'about_page'),
    url(r'^contact/$', hello.views.contact_page, name= 'contact_page'),
    url(r'^login/$', hello.views.login_page, name= 'login'),
    url(r'^register/$', hello.views.register_page, name= 'register_page'),
    url(r'^featured/$', ProductFeaturedListView.as_view()),
    url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
    url(r'^products/$', ProductListView.as_view()),
    url(r'^products/$', ProductListView.as_view()),
    url(r'^products-fbv/$', product_list_view),
    url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
    path('admin/', admin.site.urls),
]



if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
