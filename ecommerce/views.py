from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        "title": "Hello World!",
        "content": " Welcome to the homepage.",
    }
    if request.user.is_authenticated():
        context["premium_content"] = "YEAHHHHHH"
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About Page",
        "content": " Welcome to the about page."
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "content": " Welcome to the contact page.",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    # print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request=request, username=username, password=password)
        print(user)
        # print(request.user.is_authenticated())
        if user is not None:
            # print(request.user.is_authenticated())
            login(request, user)
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            print("Error")

    return render(request, "auth/login.html", context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        return redirect("/")
    return render(request, "auth/register.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")


def form_check(request):
    return render(request, "static_sites/form.html", {})


def table_view(request):
    return render(request, "static_sites/tables.html", {})


def form_controller_view(request):
    print(request.POST)
    print(request.POST.get('exampleFormControlSelect2', "==> Was not interacted with <=="))
    print(request.POST.getlist('exampleFormControlSelect2'))
    context = {
        "keko1": request.POST.get('exampleFormControlSelect1', "Not selected"),
        "keko2": request.POST.getlist('exampleFormControlSelect2'),
        "keko3": request.POST.get('exampleFormControlTextarea1', "Not selected"),
        "keko3_file": request.POST.get('exampleFormControlFile1', "Not selected"),
        "keko4": str(request.POST.get('exampleRadios1', "Not selected") != "Not selected"),
        "keko5": str(request.POST.get('exampleRadios2', "Not selected") != "Not selected"),
        "keko6": str(request.POST.get('inlineCheckbox1', "Not selected") != "Not selected"),
        "keko7": str(request.POST.get('inlineCheckbox2', "Not selected") != "Not selected"),
        "keko8": str(request.POST.get('inlineCheckbox3', "Not selected") != "Not selected"),
        "keko9": request.POST.get('inputEmail4', "Not selected"),
        "keko10": request.POST.get('inputPassword4', "Not selected"),
        "keko11": request.POST.get('inputAddress', "Not selected"),
        "keko12": request.POST.get('inputAddress2', "Not selected"),
        "keko13": request.POST.get('inputCity', "Not selected"),
        "keko14": request.POST.get('inputState', "Not selected"),
        "keko15": request.POST.get('inputZip', "Not selected"),
        "keko16": str(request.POST.get('gridCheck', "Not selected") != "Not selected"),
    }
    print(context)
    return render(request, "static_sites/form_check.html", context)
