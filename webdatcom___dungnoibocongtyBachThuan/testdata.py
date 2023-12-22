import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webdatcom___dungnoibocongtyBachThuan.settings");
django.setup()
 
from cuahang.models import Cuahang
 
Cuahang.objects.create(tencuahang='Better Call Saul', mota='Kim Welex')
Cuahang.objects.create(tencuahang='Better Call Saul_', mota='Saul Goodman')
Cuahang.objects.create(tencuahang='Breaking Bad', mota='Walter White')
Cuahang.objects.create(tencuahang='Breaking Bad', mota='Pink Jsdfgksfj')
