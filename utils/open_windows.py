import subprocess

def window_ids():
    numbers =  subprocess.check_output('xprop -root | \
                            grep \'_NET_CLIENT_LIST_STACKING(WINDOW)\' | \
                            grep -o "0x[0-9a-z]*"',
                            shell=True)
    numbers = str(numbers)[2:-1].replace('\\n', ' ').split()
    return numbers

def get_win_info():
    ids = window_ids()
    info = []
    for win_id in ids:

        title = subprocess.check_output(f'xprop -id {win_id}  | grep \"^WM_NAME\" | grep -o  "\\\".*\\\""', shell=True)
        title = str(title)[3:-4]
        process_id = subprocess.check_output(f'xprop -id {win_id} | grep "_NET_WM_PID" | grep -o "[0-9]*"', shell=True)
        process_id = int(process_id)
        process_name = subprocess.check_output(f'cat /proc/{process_id}/comm', shell=True)
        process_name = str(process_name)[2:-3]
        info.append((process_id, process_name, title))
    return info
