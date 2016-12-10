from django.shortcuts import render
from django.http import HttpResponse
from panel.models import Account

def about(request):
	return render(request, "about.html", {})

def contact(request):
	return render(request, "contact.html", {})

from bokeh.plotting import figure
from bokeh.charts import Bar
from bokeh.embed import components
import httplib2

def dashboard(request):
	all_accounts = Account.objects.all()
	accounts = []
	tags = []
	for a in all_accounts:
		if a.user == request.user:
			tag = str(a.tag)
			tags.append(tag)
			account = str(a.user_name) 
			accounts.append(account)
	print(accounts)
	plot = figure(plot_width=700,plot_height=500, responsive = True)
	plot.circle([1,2], [3,4])
	plot.toolbar.logo=None
	script, div = components(plot)
	h = httplib2.Http()
	try:
		response, content = h.request("http://www.reddit.com")

	except httplib2.ServerNotFoundError:
		reddit_status = "Offline"

	if response.status==200:
		reddit_status = "Online"
	return render(request, "dashboard.html", {"the_script": script,"the_div": div, "status": reddit_status, "accounts": accounts})