checkout.html                           x
cart/home.html                          x
orders/model.                           x
cart/views.py                           x
addresses.views. (authenticated(),)     X
templates/base/navbar cart_items        X
carts/urls  -  gettingstarted/urls.py   x

jquery:
fasttrack to jquery


10. Products & Async
products/templates.update-cart.html     x
base.html                               x
carts/template/checkout.html            x
carts/template/home.html                x
gettingstarted/forms.py
base/urls.py                            x
static/js/
hello.views contact_page( )             x
templates/contact/views.html            x


11. Custom User Model
accounts/models.py
accounts/admin.py
accounts/forms.py
settings.py "AUTH_USER_MODEL"
gettingstarted/urls.py - added imports


12. Custom Analytics
analytics/models.py
gettingstarted/settings
products/views.py productdetailsslug
accounts/views.py
accounts/signal.py

13. Stripe integration
pipenv install stripe
billings/models.py added test apikey, changed to from django.urls import

billing/view.py  authenticated()
billing/templates/payment-method.html
billing/admin.py
gettingstarted/urls added url
gettingstarted/settings
static/base/js.html
static/js/....
static/css/stripe-custom-css.css
carts/checkout.html
carts/views
gettingstarted/settings

14. Mail chimp
pipenv install requests
marketing/models
marketing/utils.py
marketing/admin.py
marketing/views.py
marketing/mixins.py

templates/base/forms.html
gettingstarted/settings
gettingstarted/urls.py

go to mailchimp webhook
ex: eeltest8.com/webhooks/mailchimp

15. Deployment

How to find a file path
Python manage.py shell
From django.conf import settings
settings.BASE_DIR
import os
manage_path = os.path.join(settings.BASE_DIR, "manage.py")

create .gitignore  change settings

setting up staticfiles aws
create account
go to aim- create a user get secret key and download .csv
            -add aws access keys to base.py
add policy to user - copy  from guide
AKIAIVLVI4AWMHAGKGBA
7V0bfz8YYqnBuFw73hJ/qVmGBCp+p/eFrSGzOHxg
https://www.codingforentrepreneurs.com/blog/s3-static-media-files-for-django/

    pipenv install boto3 django - storages boto
    gettingstarted/aws/utils.py
    gettingstarted/aws/conf.py  add settings