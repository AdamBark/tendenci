from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',                  
    url(r'^payonline/(?P<invoice_id>\d+)/(?P<guid>[\d\w-]+)?$', 'payments.views.pay_online', name="payments.pay_online"),
    #url(r'^payonline/(?P<invoice_id>\d+)/$', 'payments.views.pay_online', name="payments.pay_online"),
    (r'^authorizenet/', include('payments.authorizenet.urls')),
)