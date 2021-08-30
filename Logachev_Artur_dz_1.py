import os
structure = {'my_project': {'settings', 'mainapp', 'adminapp', 'authapp'}}
for root, folders in structure.items():
    if os.path.exists(root):
        print('данные папки уже существуют на диске')
    else:
        for folder in folders:
            cur_dir = os.path.join(root, folder)
            os.makedirs(cur_dir)

blockchain = os.makedirs()

