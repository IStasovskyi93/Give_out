from django.shortcuts import render
from django.views import View
from .models import Institution, Donation, Category


class LandingPage(View):
    def get(self, request):
        sum_donation = Donation.objects.all().count()
        sum_institution = Institution.objects.all().count()
        foundation = Institution.objects.filter(type="fundacja")
        organ_non_govern = Institution.objects.filter(type="organ. pozarządowa")
        local_coll = Institution.objects.filter(type="zbiórka lokalna")
        data = {'sum_donation': sum_donation, 'sum_institution': sum_institution, 'foundation': foundation,
                'organ_non_govern': organ_non_govern, 'local_coll': local_coll}
        return render(request, "charity/index.html", context=data)


class AddDonation(View):
    def get(self, request):
        return render(request, "charity/form.html")


class Login(View):
    def get(self, request):
        return render(request, "charity/login.html")


class Register(View):
    def get(self, request):
        return render(request, "charity/register.html")


