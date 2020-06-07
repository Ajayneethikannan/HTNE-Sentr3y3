import time, cv2, pickle, requests, json, os
from utils.detect_face import detect_face
from utils.open_windows import get_win_info
from utils.notifs import notif
from utils.profanity import check_profanity
from utils.patches import increment, set_warning
from utils.toggle_process import  toggle_process
from utils.userDetailsText import currentUserDetails

user_cache = None
count = 0
def monitor(refreshTime):
    global count
    #1. Recognise the person using the computer, implement for multiple people later
    user_id, seconds = detect_face()

    if user_id ==  None: # No one in front of the computer --> lock or standby
        count = count+1
        if count > 3:
            os.popen('gnome-screensaver-command --lock')
            count = 0

        displayText = "No user found"

    elif user_id ==  -1: # An anonymous user is sitting in front of the computer --> Prevent keyboard, mouse input
        displayText = "Anonymous user"

    else: # The face detector has detected a person properly --> Regain mouse  keyboard input, increment screen time for applications    
        count = 0
        # get open apps
        open_apps = get_win_info()

        displayText, user, apps, isUnderAge, responseStatus = currentUserDetails(user_id)
        
        # verify open apps
        if (responseStatus == 200):

            print("Detected " + user)

            for app in apps:
                for open_app in open_apps:

                    pid, process_name, title = open_app

                    if (app['title'].lower() == process_name):
                        print("Observing " + title)
                        print("Time spent on " + app['title'] + " is " + str(app['time_today']) + ' seconds')
                        print("****************************************************************************")
                        increment(app, seconds + refreshTime)
                        

                        profanity = check_profanity(title)
                        if (profanity != False and isUnderAge == True): # If age restricted applications used by underage children at home
                            notif('AGE RESTRICTED CONTENT!!!', f'{profanity}. Your action will be reported!')
                            set_warning(app, profanity)
                            toggle_process(pid, 2)
                            break
                        
                        # time limit warning
                        remaining_time = app['time_limit'] - app['time_today']
                        print(remaining_time)
                        if (remaining_time > 2*refreshTime and remaining_time < 3*refreshTime ):
                            message = 'The time limit of ' + app['title'] + ' will be reached after ' + str(remaining_time) + ' seconds.'
                            notif('Session limit warning', message)

                        # time limit ended
                        if (remaining_time <= 0):
                            message = 'The time limit of ' + app['title'] + ' has been reached.'
                            notif('Time limit ended', message)
                            toggle_process(pid, 1)
                        else:
                            toggle_process(pid, 0)

    return displayText
    

