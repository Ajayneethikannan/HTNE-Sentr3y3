import psutil
import os

def get_all_ids(id):
    all_ids = []
    def get_children_ids(id):
        try:
            process = psutil.Process(id)
        except psutil.NoSuchProcess:
            return
        else:
            all_ids.append(id)
            for child in process.children():
                get_children_ids(child.pid)
    get_children_ids(id)
    return all_ids

def toggle_process(id, option):
    if option == 1:
        option = '-STOP'
    elif option == 0:
        option = '-CONT'
    else:
        option=''
    children = get_all_ids(id)
    for child in children:
        os.system(f'kill {option} {child}')
