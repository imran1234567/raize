from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Membership
# Create your views here.


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