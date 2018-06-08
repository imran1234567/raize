from django import forms

from .models import Membership

class MembershipModelForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = [
            "name",
            "contact_no",
            "email",
            "address",
            "dob",
            "aniversary_date",
            "material_status",
            "food_pref",
        ]