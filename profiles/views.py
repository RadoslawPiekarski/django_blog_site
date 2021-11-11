from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from forms import ProfileForm
# Create your views here.


def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:  # wb+ -> pliki binarne
        for chunk in file.chunks():  # czyta plik partiami aby nie zajmować dużej ilości pamięci
            dest.write(chunk)  # zapisuje kawałek pliku


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {
            "form": form
        })

    def post(self, request):
        store_file(request.FILES["image"])
        return HttpResponseRedirect("/profiles")
