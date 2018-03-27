from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

#from products.views import ProductListView, product_list_view, ProductDetailView, product_detail_view
import carts.views
import hello.views
import products.urls
from django.urls import include, path, re_path, reverse
#from towguideline.views import TowEstimatorView #, TowEstimateView
import towguideline.views
# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
app_name = products

urlpatterns = [
    url(r'^$', hello.views.home_page, name='home_url'),
    url(r'^about_page/$', hello.views.about_page, name= 'about_page'),
    url(r'^contact/$', hello.views.contact_page, name='contact_url'),
    url(r'^login/$', hello.views.login_page, name= 'login'),
    url(r'^cart/', include(('carts.urls', 'cart'))),
    url(r'^search/', include(('search.urls', 'search'))),
    url(r'^products/', include(('products.urls', 'products'))),
    url(r'^register/$', hello.views.register_page, name='register'),
    url(r'^towestimator/$', towguideline.views.TowEstimatorView, name= 'TowEstimatorView'),
    url(r'^admin/', admin.site.urls),
]



if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
