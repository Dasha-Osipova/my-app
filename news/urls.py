from django.conf.urls import url
from news import views

urlpatterns = [
    url(r'^$', views.articles_list, name='articles_list'),
    url(r'^feeds/new', views.new_feed, name='feed_new'),
    url(r'^feeds/', views.feeds_list, name='feeds_list'),
	url(r'^posts/post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^posts/', views.posts_list, name='posts_list'),]