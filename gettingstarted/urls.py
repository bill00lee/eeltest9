from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path, reverse
from django.conf.urls import include, url
from django.views.generic import TemplateView

from django.contrib import admin
from django.contrib.auth.views import LogoutView
admin.autodiscover()

from carts.views import cart_detail_api_view
import hello.views
import carts.urls
import products.urls
import accounts.views
import towguideline.views
import addresses.views

from accounts.views import LoginView, RegisterView, guest_register_view

app_name = products

urlpatterns = [
    url(r'^$', hello.views.home_page, name='home_url'),
    url(r'^about_page/$', hello.views.about_page, name= 'about_page'),
    url(r'^contact/$', hello.views.contact_page, name='contact_url'),
    url(r'^logout/$', LoginView.as_view(), name='login'),
    url(r'^checkout/address/create/$', addresses.views.checkout_address_create_view, name='checkout_address_create'),
    url(r'^checkout/address/reuse/$', addresses.views.checkout_address_reuse_view, name='checkout_address_reuse'),
    url(r'^logout/$', LogoutView.as_view(), name= 'logout'),
    url(r'^register/guest/$', accounts.views.guest_register_view, name='guest_register'),
    url(r'^api/cart/$', cart_detail_api_view, name='api-cart'),
    url(r'^cart/', include(('carts.urls', 'cart'))),
    url(r'^products/', include(('products.urls', 'products'))),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^estimator/$', towguideline.views.TowEstimatorView, name= 'Tow_Estimator_View'),
    url(r'^search/', include(('search.urls', 'search'))),
    url(r'^admin/', admin.site.urls),
]



if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
