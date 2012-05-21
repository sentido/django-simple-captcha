from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('captcha.views',
    url(r'image/(?P<key>\w+)/$', 'captcha_image', name='captcha-image'),
    url(r'audio/(?P<key>\w+)/$', 'captcha_audio', name='captcha-audio'),
    url(r'captcha_reload/$', 'captcha_reload_ajax', name='captcha-reload-ajax'),
)
