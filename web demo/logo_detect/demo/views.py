from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import default_storage
import os
import mimetypes
# Create your views here.
class Index(View):
    def get(self, req):
        return render(req, 'demo/index.html', {'file_name': '817598.jpg'})

    def post(self, req):
        file = req.FILES.get('file')
        if file is None:
            return render(req, 'demo/index.html', {'file_name': '817598.jpg'})

        file_name = default_storage.save('files/upload/' + file.name, file)
        # 
         
        # 
        context = {
            'file_name':file.name
        }
        print(file.name)
        return render(req, 'demo/index.html', context)

class Download(View):
    def get(self, request, path):
        file_path = os.path.join(settings.MEDIA_ROOT, 'files/upload/' + path)
        content_type = mimetypes.guess_type(str(file_path))[0]
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type=content_type)
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        raise Http404()