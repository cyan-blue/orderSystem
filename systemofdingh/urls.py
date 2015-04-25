from django.conf.urls import include, url
from systemofdingh import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'flashsale.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home/', views.home, name="home"),
    url(r'^add/',  views.add, name="addorder"),
    url(r'^delorder/(?P<del_id>\d+)',  views.delorder, name="delorder"),
    url(r'^update/(?P<modify_id>\d+)', views.update, name="updateorder"),
    url(r'^login/', views.login, name="login"),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^register/$', views.regist, name='register'),
    url(r'^detail/(?P<detail_id>\d+)', views.detail, name='orderdetail'),
    url(r'^addorderitem/(?P<order_id>\d+)$', views.addorderitem, name='addorderitem'),
    url(r'^ajax_deal/$', views.ajax_index, name="test-ajax"),
    url(r'^ajax_list/$', views.ajax_list, name='ajax-list'),
    url(r'^checkorderexist/$', views.CheckOrderExist, name='CheckOrderExist'),
    url(r'^test/$', views.test, name='test'),


]
