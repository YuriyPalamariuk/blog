from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # url('^', include('django.contrib.auth.urls')),
    url(r'^login/$', auth_views.login, {'template_name': 'blog/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^password_change/$', auth_views.password_change, name='password_change'),
    url(r'^password_change/done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    # url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.PostList.as_view(), name='post_list'),

    # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post_detail'),

    # url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/new/$', views.PostCreate.as_view(), name='post_new'),

    # url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.PostUpdate.as_view(), name='post_edit'),

    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name='post_delete'),
]
