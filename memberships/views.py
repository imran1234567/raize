from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .forms import MembershipModelForm
from .models import Membership
from .mixins import FormUserNeededMixin, UserOwnerMixin
# Create your views here.


class MembershipCreateView(CreateView):
    # queryset = Membership.object.all()
    form_class = MembershipModelForm
    template_name = 'memberships/create_view.html'
    success_url = "/login/#login"


class MembershipDetailView(DetailView):
    # template_name = "memberships/detail_view.html"
    queryset = Membership.objects.all()

    def get_object(self):
        return Membership.objects.get(id=1)


class MembershipListView(ListView):
    # template_name = "memberships/list_view.html"
    queryset = Membership.objects.all()

# def member_detail_view(request, id=1):
#     return render(request, "memberships/detail_view.html",{})
#
# def member_list_view(request):
#         return render(request, "memberships/list_view.html", {})