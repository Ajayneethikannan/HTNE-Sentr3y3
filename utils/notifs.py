import os

def notif(title, message):
    command = (f'notify-send --urgency=critical '
            f'"{title}" '
            f'"{message}"')
    os.system(command)
