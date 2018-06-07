from django.conf.urls import url
from .views import MembershipDetailView, MembershipListView

urlpatterns = [
    url(r'^$', MembershipListView.as_view(), name='list'),
    url(r'^1/$', MembershipDetailView.as_view(), name='detail'),
]