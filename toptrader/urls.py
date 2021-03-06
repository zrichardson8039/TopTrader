from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers
import apps.contests.views as contests
import apps.stockmarket.views as stockmarket


router = routers.DefaultRouter()

# Contests
router.register('portfolios', contests.PortfolioViewSet)

# Stock Market
router.register('stocks', stockmarket.StockViewSet)
router.register('prices', stockmarket.PriceViewSet)


# General URLs
urlpatterns = [
    url(r'^$', 'apps.common.views.home', name='home'),
    url(r'^play/$', 'apps.contests.views.play', name='play'),
    url(r'^profile/$', 'apps.contests.views.profile', name='profile'),
    url(r'^registration/$', 'apps.common.views.registration', name='registration'),
    url(r'^login/$', 'apps.common.views.login_request', name='login_request'),
    url(r'^logout/', 'apps.common.views.logout_request', name='logout_request'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
]
