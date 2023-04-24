from django.shortcuts import render
import os
import json

#create a json rep of the file system 
def create_fs_tree(path):
    if os.path.isfile(path):
        return {'id': path, 'text': os.path.basename(path)}
    elif os.path.isdir(path):
        children = []
        for fname in os.listdir(path):
            child_path = os.path.join(path, fname)
            children.append(create_fs_tree(child_path))
        return {'id': path, 'text': os.path.basename(path), 'children': children}

# Create your views here.
#create index view which displays the index.html template
def index(request):
    # tree = []
    # for root, dirnames, filenames in os.walk('.'):
    #     for fname in filenames:
    #         tree.append(create_fs_tree(os.path.join(root, fname)))
    #     for dirname in dirnames:
    #         tree.append(create_fs_tree(os.path.join(root, dirname)))
    tree = create_fs_tree('.')
    files_json = json.dumps([tree])

    return render(request, 'index.html', {'files': files_json})


    
    
