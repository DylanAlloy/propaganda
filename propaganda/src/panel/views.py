from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import AddRedditForm
from .models import Account
import pdb


# Create your views here.
def panel(request):
    user = request.user
    all_accounts = Account.objects.all()
    tags = []
    for a in all_accounts:
        if a.user == user:
            tag = a.tag
            tags.append(tag)


    title = 'Add Reddit Account'

    # Add form
    form = AddRedditForm(request.POST)

    selected_account = None

    context = {
        "title": title,
        "user": user,
        "form": form,
        "accounts": all_accounts,
        "tags": tags,
        "account": selected_account
    }
    return render(request, 'redditpanel/panel.html', context)


@require_http_methods(["POST"])
def add_account(request):
    form = AddRedditForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect('/dashboard/panel/?success')
    else:
        form = AddRedditForm(request.POST)
        return HttpResponseRedirect('/dashboard/panel/?fail')


@require_http_methods(["POST"])
def make_active(request):
    try:
        user = request.POST['account']
        account_exists = Account.objects.filter(user_name=user).count() == 1
    except Exception as e:
        print(e)
        account_exists = False

    if account_exists:
        selected_account = Account.objects.filter(user_name=user)[0]
        selected_account.is_active = True
        selected_account.save()
    else:
        selected_account = None
        print("Account doesn't exist or wasn't found")

    return HttpResponseRedirect('/dashboard/panel/')
