from django.conf.urls import url
from .views import MembershipDetailView, MembershipListView, MembershipCreateView

urlpatterns = [
    url(r'^$', MembershipListView.as_view(), name='list'),
    url(r'^1/$', MembershipDetailView.as_view(), name='detail'),
    url(r'create/$', MembershipCreateView.as_view(), name='create'),
]