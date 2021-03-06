'''
This is the envs folder of ALPHAbot v3.0 package
'''

from collections import defaultdict
from telegram.ext import Defaults
from telegram import ParseMode

# LGinfo03bot (currently used bot)
live_token = '832661637:AAFVs-8z6xE7S-hyqSWiR07_oSSoqSN1vxg'
live_username = 'LGinfo03bot'
# ABbot (testing bot)
testing_token = '1081436727:AAEDUCJ_kV9Uy2utZN_HWQ7QuSGeU4L6Uo0'
testing_username = 'ABLGbot'

ALPHA_CHAT_ID = -1001479454631
BOT_TEST_ID = -1001200591015

coders = [333647246]
# admins = {'Hosea': 333647246, 'Ivan': 299385070, 'Yi Han': 447584594, 'Zames': 113200946}
# members = {'Hosea': 333647246, 'vernjoshua': 553175669, 'Ivan': 299385070,\
# 'Yu Fei': 678686611, 'Gbalo': 326819149, 'Zames Tan :sunglasses:': 113200946,\
# 'Ryan': 851265766}
admins = {'ollayf':333647246}
members = {'ollayff':678686611, 'ollayf':333647246}

# parse mode for bolding,
defaults_updater = Defaults(quote=True, parse_mode=ParseMode.HTML)

# only this bot_data attribute needs to be a dict object
# the rest must be defaultdict object
default_bot_data = {
'chat_id': BOT_TEST_ID,
"members": members if type(members)==dict else {},
'admins': admins if type(members)==dict else {},
'coders': coders,
'permissions_changed': [], # platform, url
'events': {},
'library': {
    'limit': 3, # for testing usually put 6 
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

usage_timeout_msg = '15 minutes is up, I will automatically be going to \
sleep. Next time please remember to end me when not in use.\nYou can also use \
/eventlist or /teaching list without starting me up.'   

first_use = 'Permissions and data set for you'

start_msg = 'Eh sup {}! yeboi ALPHAbot here. /help to display the list of commands you can use.'
alr_started_msg = 'Eh sup {}! yeboi ALPHAbot he-- wait aren\'t we alr in a conversation??!'

first_start_msg = 'Welcome {}! Is this your first time? Hi my name is ALPHAbot. I store important \
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

cfmation_msg=\
"""Confirmation for LG & SVC:balloon:


SERVICE(time):wedding::heart_eyes:
Coming:grinning::






CMI:cry::




LG(time/post svc):raising_hand:🏼♂

Coming:grinning::




CMI:cry::"""

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

already_admin_msg = 'this person is already and admin lol'
add_admin_fin = 'New admin {} added!'
permission_fail_msg = 'You have no power here!'
bruh_message = 'BRUHHHHHHHHHHH........... You are literally alr in admin menu'
function_fail_msg = 'This function is not allowed in the mode you have activated. E.G. admin_menu'
backend_init_fail = 'This function is only allowed in the backend... If you are even allowed\
in the first place...'
remove_user_fail = 'Pls la you give me wrong format. Should be:/remove_function <member username>'
remove_not_exist = '{}: {} does not exist'
quit_fail_msg = 'bruh there\'s nothing to quit lol'
call_format_error = 'Wrong format inputted. It should be /start_call <url>'
invalid_call_url = 'Invalid url input'
call_not_started_msg = 'There is ongoing calls currently... Wake up your idea pls'
not_reg_platform_error = 'This is an unregistered call platform, please contact yu fei to update the code'

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

#################
# BACKEND TINGZ #
#################

remov_user_fin = '{} has been succesfully removed from {}'

possible_commands = {
    'sleep' : { # the default mode
        'events': 'shows the list of upcoming events',
        'library': 'opens up a library of recent good teachings and articles',
        'start': 'start a conversation with me :)',
        'start_call': '/start_call <url> to start a call. \
Sends a message to the group that the call is on, don\'t say bojio.(only available for admins)',
        'end_call': 'Informs me that the call is ended, aka stopping the spam (only available for admins)',
        'base_menu': ''
        },

    'started' : { # the mode activated after /start
        'events': 'shows the list of upcoming events',
        'library': 'opens up a library of recent good teachings and articles',
        'start_call': '/start_call <url> to start a call.\
Sends a message to the group that the call is on, don\'t say bojio.',
        'end_call': 'Informs me that the call is ended, aka stopping the spam',
        'feedback': 'opens up the floor for a good ol\' one sided roasting session. Come at me bro',
        'end': 'ends the conversation with me :(',
        'admin_menu': 'Opens the menu of functions you can use as an admin',
        'base_menu': ''
        },

    'admin_menu' : { # the mode activated after /admin_menu
        'events': 'shows the list of upcoming events',
        'library': 'opens up a library of recent good teachings and articles',
        'broadcast_msg': '/broadcast <msg> and the <msg> will be sent to all members',
        # for events handling
        'add_event': 'create a new event. Input data step by step with me. The event will \
be created when done',
        'add_whole_event': 'add a whole event with the correct. If the format is wrong, the event will\
be rejected.',
        'del_event': 'delete a currently existing event',
        #'clear_events': 'delete all events that are currently stored',
        # for library handling
        'add_teaching': 'create a new teaching step by step. I will help you with the formatting',
        'add_whole_teaching': 'add a whole teaching with the correct formatting',
        'del_teaching': 'delete a currently existing teaching',
        #'clear_library': 'delete all teachings that are currently stored',
        'quit': 'exits the admin menu',
        'end': 'ends the conversation with me :(',
        'base_menu': ''
        },
    'backend': { # the mode activated after /backend
        'events_dict': 'shows the events in the dictionary form read by python',
        'lib_dict': 'shows the teachings in the dictionary form read by python',
        'admins_dict': 'shows the list of members with admins permissions',
        'members_dict': 'shows the list of members',
        'coders_list': 'shows the list of members with coders permissions',
        'make_admin': 'makes a currently registered member into an admin by passing in the \
member\'s chat_id',
        'remove_member': 'removes member from the list of members. I.E removing from broadcast\
list',
        'remove_admin': 'remove admin permissions on a member',
        'quit': 'leaves the backend',
        'end': 'ends the conversation with me',
        'base_menu': 'Welcome Master {}'
        }
    }


# special messages
# <b>bold</b> <i>italic</i> <a href="http://google.com">link</a>
# parse_mode = telegram.ParseMode.HTML
