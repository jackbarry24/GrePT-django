import os
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

#create a json rep of the file system 
def create_fs_tree(path):
    if os.path.isfile(path):
        return {'id': path, 'text': os.path.basename(path), 'type': 'file'}
    elif os.path.isdir(path):
        children = []
        for fname in os.listdir(path):
            child_path = os.path.join(path, fname)
            children.append(create_fs_tree(child_path))
        return {'id': path, 'text': os.path.basename(path), 'type': 'folder', 'children': children}

def index(request):
    tree = []
    #iterate over the directory "." and call create_fs_tree on ech file and folder within the directory
    for fname in os.listdir('.'):
        tree.append(create_fs_tree(fname))
    files_json = json.dumps(tree)

    return render(request, 'index.html', {'files': files_json})

@csrf_exempt
def add_selected_file(request):
    if request.method == 'POST':
        selected_paths = json.loads(request.body)
        print(selected_paths)
        return HttpResponse("success")
    else:
        return HttpResponse("error")
        #return JsonResponse({'selected_paths': selected_paths, "status": "success"})

def new_message(request):
    if request.method == 'POST':
        message = json.loads(request.body)
        print(message)
        return HttpResponse("success")
    else:
        return HttpResponse("error")
    


    
    
