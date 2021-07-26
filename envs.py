'''
This is the envs folder of ALPHAbot v3.0 package
'''

from collections import defaultdict
from telegram.ext import Defaults
from telegram import ParseMode

# LGinfo03bot (currently used bot)
live_token = '1929924574:AAEEzVSHRRHTJmqslsA0chEl1mzkpfOUjZg'
live_username = 'E2InfoBot'
# ABbot (testing bot)
testing_token = '1081436727:AAEDUCJ_kV9Uy2utZN_HWQ7QuSGeU4L6Uo0'
testing_username = 'ABLGbot'

ALPHA_CHAT_ID = -530924757
BOT_TEST_ID = -1001200591015

coders = [333647246]
bday_ICs = {'andykohby': 323323}
cfm_ICs = {'Ryan': 851265766, 'ollayff':678686611}
# admins = {'Hosea': 333647246, 'Ivan': 299385070, 'Yi Han': 447584594, 'Zames': 113200946}
# members = {'Hosea': 333647246, 'vernjoshua': 553175669, 'Ivan': 299385070,\
# 'Yu Fei': 678686611, 'Gbalo': 326819149, 'Zames Tan :sunglasses:': 113200946,\
# 'Ryan': 851265766}
admins = {'ollayf':333647246, 'zamestan': 113200946, 'Yi Han': 447584594, 'Ivan_Ang':299385070}
members = {'ollayff':678686611, 'ollayf':333647246, 'zamestan': 113200946, 'Yi Han': 447584594, 'Ivan_Ang':299385070, \
    'Ryan': 851265766}

# parse mode for bolding,
defaults_updater = Defaults(quote=True, parse_mode=ParseMode.HTML)

# default msg to be sent out for confirmation
cfmation_msg=\
"""Confirmation for LG & SVC:balloon:


SERVICE(2pm):wedding::heart_eyes:
Coming:grinning::






CMI:cry::




LG(time/post svc):raising_hand::🏼♂

Coming:grinning::




CMI :cry: :"""

PERSISTENT_VARS = ['cfm', 'events', 'library', 'birthdays']
VERSION_UPDATES = './version_updates.md'
PICKLE_FILE = 'storage/bot_memory.pickle'

BOT_DESCRIPTION = '''\
Hello! My name is R2-E2! My job is to assist in the administrative efforts of NUS E2. Please cooperate with me as much \
as you can :)!!

What can you do with me?
As a normal member the simple commands you can do are:
/events
/library
/feedback (Though you would need to start a convo with me to use this)
At any time, use /help to check the list of possible commands for you. I hope we would get to know each other more
as we interact with each other!

P.S. ALL COMMANDS work SEAMLESSLY on pm and in group as long as you have started me before. So feel free to use me whenever and
whereever you want to! :)
'''

# only this bot_data attribute needs to be a dict object
# the rest must be defaultdict object
default_bot_data = {
'bot_info': {
    'version_number': None, # There is a script to parse the version updates textfile to get this
    'patch_notes': None,
    'description': BOT_DESCRIPTION,
    'creator': 'Yu Fei',
    'coders': 'ollayf'
},
'chat_id': ALPHA_CHAT_ID,
'cfm_ICs': cfm_ICs,
'bday_ICs': bday_ICs,
"members": members if type(members)==dict else {},
'admins': admins if type(members)==dict else {},
'coders': coders,
'permissions_changed': [], # platform, url
'cfm': {
    'active': True,
    'cfm_msg': cfmation_msg,
    'temp_msg': ''
    },
'events': {},
'library': {
    'limit': 10, # for testing usually put 6 
    'teachings': {}
    },
'current_call': [],
'birthdays': {}
}

default_user_data = {
'username': None,
'user_id': None,
'group_id': None,
'permissions': None,
'status': {
    # for members
    'initiated': False, 'started': False, 'feedback': False, 'action': False,
    # for cfm IC
    'cfm_settings': False, 'change_msg': 0,
    # for admins
    'admin_menu': False, 'add_event': 0, 'add_teaching': 0,
    # for coders
    'backend': False
    },
'temp_list': [],
'temp_string' : ''
}


# COMMANDS = {
#     'start'
#     'help'
# }

#####################
# Repeated Messages #
#####################

initialised_msg = 'Energize!'

fail_end_msgs = ['Wait bruh we aren\'t even in a conversation...',\
    'Uhm ok... It\'s not like i wanted to talk to you anyway',\
    'Wait whats there to end? Wait end me?!! Why do you want to end me?!'
    ]
end_msgs = ['Going so soon...._Alright..._Bye then...',\
    'Alright come back soon ok? :D',\
    'Don\'t go, I\'m lonely...',\
    'Have nice day',\
    'Thank you for waiting._We\'ve restored your Pokémon to full health._We hope to see you again!',\
    'k thx bai'
    ]

cancel_msg = 'Alrighty! Action cancelled!'

usage_timeout_msg = '15 minutes is up, I will automatically be going to \
sleep. Next time please remember to end me when not in use.\nYou can also use \
/eventlist or /teaching list without starting me up.'   

first_use = 'Permissions and data set for you'

start_msg = 'Eh sup {}! yeboi R2-E2 here. /help to display the list of commands you can use.'
alr_started_msg = 'Eh sup {}! yeboi ALPHAbot he-- wait aren\'t we alr in a conversation??!'

first_start_msg = 'Welcome {}! Is this your first time? Hi my name is R2-E2. I store important \
information and do particular administrative tasks to aide the running of LG. However just \
like you I am not perfect, so please do not hesitate to give me feedback on how I can serve you \
and the LG better. You can use \n/feedback to give me your feedback\n\n\
\
Commands you can use without doing /start (for quick use):\n\
/events -- shows the list of upcoming events including their dates, timings and locations.\n\
/library -- shows the list of good articles/ sermons to read in you own time.\n\
/start_call -- to be called when you start a call on any platform (only available for admins)\n\
/end_call -- ends the call that is currently on (only available for admins)\n\
/birthdays -- shows the full list of birthdays as well as the closest birthday.\n\
/help -- can be used at any time to give the list of possible functions'

broadcasted_fin_msg = 'Message broadcasted! Thanks for serving'
middle_of_action_msg = 'Command failed as you are currently in an action!'

lib_empty_msg = 'Sorry, the library is currently empty, please come back again next time.'
events_empty_msg = 'There are no upcoming evens sadly...*sadness doggo noises*'

feedback_msg = 'What is your problem with me?'
feedback_repeated_msg = 'Stop beating about the bush and tell me what your problem is.'
feedback_given_msg = 'Your feedback has been taken into consideration. Thanks for your help to \
improve the bot :D! Type /end to end this conversation with me!'
quit_fin_msg = 'Thanks bro. Goodbye!'
call_ended_msg = 'Call has ended'

##################
# error messages #
##################

not_started_error = 'Hello... Please start a conversation with me first with /start'
not_admined_error = 'You must be in the admin menu to access this command.'
not_integer_error = 'Value is not an integer. Try inputting index again'
out_of_range_error = 'Index out of range'
one_arg_error = 'Only 1 argument allowed to be input'
not_exist_error = 'this person does not exist'
not_in_action_error = 'You are not currently in an action!'
other_menu_error = 'You are currently in another menu. /quit first before accessing this menu'

already_admin_msg = 'this person is already and admin lol'
perms_present = 'This user already has such privileges'
add_perms_fin = '{} permissions added for {}!'
add_admin_fin = 'New admin {} added!'
permission_fail_msg = 'You have no power here!'
bruh_message = 'BRUHHHHHHHHHHH........... You are literally alr in admin menu'
function_fail_msg = 'This function is not allowed in the mode you have activated. E.G. admin_menu'
backend_init_fail = 'This function is only allowed in the backend... If you are even allowed\
in the first place...'
remove_user_fail = 'Pls la you give me wrong format. Should be:/remove_function <member username>'
remove_not_exist = '{}: {} does not exist'
quit_fail_msg = 'bruh there\'s nothing to quit lol'
call_format_error = 'Wrong format inputted. It should be /start_call [url]'
invalid_call_url = 'Invalid url input'
call_not_started_msg = 'There are no ongoing calls currently... Wake up your idea pls'
not_reg_platform_error = 'This is an unregistered call platform, please contact yu fei to update the code'
only_cfm_settings= 'This function is only allowed in cfm settings'
not_chat_id_error = 'This is not a chat id'

user_timeout_msg = '15 minutes is up, I will automatically be going to sleep. Please remember \
to end the conversation when not in use.\nYou can also use /events, /library, /start_call \
/end_call without starting me up.'

###############################
# For adding/ deleting events #
###############################

add_event_0 = 'What is the name of this event?'
add_event_1 = 'Short description of what it is about?'
add_event_2 = 'Where will it be held?'
add_event_3 = 'When will it be held? format: DD-MM-YYYY, TIME (dont put anyth before the date ah)'
add_event_fail = 'bruh cant u give the correct format? try inputting datetime again\n\n\
\
DD-MM-YYYY, TIME (dont put anyth before the date ah)'
add_event_fin = 'New event saved. Thanks for serving!'
whole_event_msg = 'Chop chop kali pok. Gimme that event! Type "Nah" to cancel'
del_event_fin = 'Event {} deleted. Thanks for serving!'
del_event_init = 'Which event do you want to delete? (single integer value)'

###################################
# For adding / deleting teachings #
###################################

add_teaching_0 = 'Tell me the summary of this teaching my child. Type "Nah" to cancel.'
add_teaching_1 = 'URL for the resources?'
whole_teaching_msg = 'Gimme that teaching!'
del_teaching_init = 'Which teaching do you want to delete? (single integer value)'
del_teaching_fin = 'Teaching no.{} deleted, any other event to delete? Otherwise, type "Nah"'
add_teaching_fin = 'New teaching saved. Thanks for serving'
add_teaching_limit = 'Since there is currently more than {}, the oldest teaching will be removed \
from the library'

###########
# FOR CFM #
###########

cfm_access_msg = 'Welcome Confirmation IC {}! What would you like to do today?'
cfm_restarted = 'Confirmation will be sent out starting from next Friday!'
cfm_stopped = 'Confirmation message will no longer be sent out automatically :('
cfm_change_init = 'What is the new confirmation message?'
cfm_change_fin = 'Confirmation message changed. Thanks for serving.'
cfm_once_fin = 'Confirmation message changed temporarily. Thanks for serving.'

#################
# BACKEND TINGZ #
#################

remov_user_fin = '{} has been succesfully removed from {}'
limit_change_msg = 'New teaching limit is: {}.'

possible_commands = {
    'sleep' : { # the default mode
        'events': 'shows the list of upcoming events',
        'library': 'opens up a library of recent good teachings and articles',
        'patch_notes': 'Shows the patch notes of the last update',
        'info': 'Find out more about me and what I do!',
        'start': 'start a conversation with me :)',
        'part1': 'ONLY AVAILABLE FOR ADMINS',
        'start_call': '/start_call [url] to start a call. \
Sends a message to the group that the call is on, don\'t say bojio.',
        'end_call': 'Informs me that the call is ended, aka stopping the spam',
        'base_menu': ''
        },

    'started' : { # the mode activated after /start
        'events': 'shows the list of upcoming events',
        'library': 'opens up a library of recent good teachings and articles',
        'patch_notes': 'Shows the patch notes of the last update',
        'info': 'Find out more about me and what I do!',
        'feedback': 'opens up the floor for a good ol\' one sided roasting session. Come at me bro',
        'part1': 'FOR ADMINS ONLY',
        'start_call': '/start_call [url] to start a call.\
Sends a message to the group that the call is on, don\'t say bojio.',
        'end_call': 'Informs me that the call is ended, aka stopping the spam',
        'admin_menu': 'Opens the menu of functions for admins',
        'cfm_settings': 'Opens the menu of functions for the confirmation IC',
        'bday_settings': 'Opens the menu of functions for the birthday IC',
        'end': 'ends the conversation with me :(',
        'base_menu': ''
        },

    'cfm_settings':{ # /cfm_settings
        'view_msg': 'Views the next message to be sent to the chat',
        'change_msg': 'changes the confirmation message that is sent out every week',
        'change_once': 'changes the confirmation just for one time',
        'stop_cfm': 'stops automatically sending the confirmation message',
        'start_cfm': 'restarts the weekly automatic confirmation message',
        'quit': 'exits the admin menu',
        'end': 'ends the conversation with me :(',
        'base_menu': ''
        },
    
    'bday_settings':{ # /bday_settings
        'add_bday': 'adds a birthday into the memory',
        'remove_bday': 'removes a birthday stored',
        'default_bdays': 'sets the default list of bdays',
        'clear_bdays': 'clear all bdays that are currently saved in system',
        'quit': 'exits the admin menu',
        'end': 'ends the conversation with me :(',
        'base_menu': ''
        },

    'admin_menu' : { # the mode activated after /admin_menu
        'events': 'shows the list of upcoming events',
        'library': 'opens up a library of recent good teachings and articles',
        'patch_notes': 'Shows the patch notes of the last update',
        'info': 'Find out more about me and what I do!',
        'broadcast_msg': '/broadcast [msg] and the [msg] will be sent to all members',
        # for events handling
        'part1': 'FOR EVENTS HANDLING',
        'add_event': 'create a new event. Input data step by step with me. The event will \
be created when done',
        'add_whole_event': 'add a whole event with the correct. If the format is wrong, the event will\
be rejected.',
        'del_event': 'delete a currently existing event',
        #'clear_events': 'delete all events that are currently stored',
        # for library handling
        'part2': 'FOR LIBRARY HANDLING',
        'add_teaching': 'create a new teaching step by step. I will help you with the formatting',
        'add_whole_teaching': 'add a whole teaching with the correct formatting',
        'del_teaching': 'delete a currently existing teaching',
        #'clear_library': 'delete all teachings that are currently stored',
        'quit': 'exits the admin menu',
        'end': 'ends the conversation with me :(',
        'base_menu': ''
        },
    'backend': { # the mode activated after /backend
        'part1': 'FOR VIEWING STATUS',
        'events_dict': 'shows the events in the dictionary form read by python',
        'lib_dict': 'shows the teachings in the dictionary form read by python',
        'bday_dict': 'shows the birthdays in the dictionary form read by python', # new
        'perm_events_dict': 'shows the permanent events in the dictionary form read by python', # new
        'lib_limit': 'shows the limit on the library', 
        'change_lib_limit': 'changes the library limit', 
        'part2': 'USERS DICTS',
        'admins_dict': 'shows the list of members with admins permissions',
        'cfm_ICs_dict': 'shows the dict of members with cfm_IC permissions', 
        'bday_ICs_dict': 'shows the dict of members with bday_IC permissions', 
        'members_dict': 'shows the list of members', 
        'coders_list': 'shows the list of members with coders permissions',
        'part3': 'FOR CHANGING PERMISSIONS',
        'make_admin': 'makes a currently registered member into an admin by passing in the \
member\'s chat_id',
        'remove_member': 'removes member from the list of members. I.E removing from broadcast\
list',
        'remove_admin': 'remove admin permissions on a member',
        'make_cfm': 'gives the user cfm_IC permissions', 
        'remove_cfm': 'removes cfm_IC permissions from the user',
        'make_bday': 'makes a currently registered member into a bday_IC', 
        'remove_bday': 'removed bday_IC permissions on the member',  
        'quit': 'leaves the backend',
        'end': 'ends the conversation with me',
        'base_menu': 'Welcome Master {}'
        }
    }


# special messages
# <b>bold</b> <i>italic</i> <a href="http://google.com">link</a>
# parse_mode = telegram.ParseMode.HTML
