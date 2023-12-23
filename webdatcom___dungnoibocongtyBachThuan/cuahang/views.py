##from django.http import HttpResponse
##from django.template import loader
import json
from django.shortcuts import render
from .models import Cuahang as Member


##def home(request):
##  mymembers = Member.objects.all().values()
##  template = loader.get_template('myfirst.html')
##  context = {
##    'mymembers': mymembers,
##  }
##  return HttpResponse(template.render(context, request))


def home(request):
##  mymembers = Member.objects.all().values()
##  context = {
##    'mymembers': mymembers,
##  }
####  allUsers = User.objects.all() # QuerySet: allUsers
####  serializedData = [ json.dumps({'usrname': user.username, 
####                  'mail': user.email}) for user in allUsers]
####  https://stackoverflow.com/questions/63745167/how-to-convert-django-object-into-json
##  context = {}
##  context["items_json"] = json.dumps(items)  # items: list = [...]
##  https://vsupalov.com/vue-js-in-django-template/
  mymembers = Member.objects.all()
  mymembers = [{
      'tencuahang': member.tencuahang,
      'mota': member.mota
      } for member in mymembers]
  context = {
    'mymembers': json.dumps(mymembers),
  }
  return render(request, 'vue_list.html', context)

