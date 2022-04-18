from django.shortcuts import render
from django.views import View
from .models import Institution, Donation


class LandingPage(View):
    def get(self, request):
        sum_donation = Donation.objects.all().count()
        sum_institution = Institution.objects.all().count()
        data = {'sum_donation': sum_donation, 'sum_institution': sum_institution}
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



