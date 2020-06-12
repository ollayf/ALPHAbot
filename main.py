'''
This is the main.py file of ALPHAbot v3.0
to be run to start the bot and keep it running indefinitely

'''

import telegram
import datetime
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, PicklePersistence
from envs import *
from utils import *
import logging
import random
from pytz import timezone
import emojis

####################
# INITIALISING BOT #
####################

# asks user if they want to reset the bot
reset_bot()

# Setting up persistence based on when it was last reset
persistence = PicklePersistence(PICKLE_FILE, store_user_data=False)
# setting up patch notes and bot version
default_bot_data['bot_info']['version_number'], default_bot_data['bot_info']['patch_notes'] = get_bot_info(VERSION_UPDATES)

print('initialising')
# initialises the updater object
updater = Updater(token=live_token, use_context=True, persistence=persistence)
dispatcher = updater.dispatcher # for quicker access to the dispatcher object
jobqueuer = updater.job_queue # for quicker access to JobQueue object

# set bot_data to default if it does not already exist
if dispatcher.bot_data == {}:
    dispatcher.bot_data = default_bot_data
    print('bot_data set to default')
# if there is a saved version of alphabot
else:
    print('there is a saved version of bot_data already')
    update_bot_data(dispatcher.bot_data)

# logs the problems in log.md file with level INFO
logging.basicConfig(filename='storage/error_log.md', format='%(asctime)s - %(name)s - \
                    %(levelname)s - %(message)s', level=logging.INFO)

# inform coders that it is initialised
for coder in coders:
    updater.bot.send_message(coder, initialised_msg)

######################
# CALLBACK FUNCTIONS #
######################
# You can create a context for the job to be accessed via context.job.context: object obj

def call_spammer(context):
    '''
    To be called when a call is started every 10 minutes after starting the call
    '''
    j_context = context.job.context
    current_call_list = j_context.bot_data['current_call']
    chat_id = j_context.bot_data['chat_id']
    # if the call has been ended remove without any messages
    if current_call_list == []:
        context.job.schedule_removal
        # message to be spammed
    else:
        context.bot.send_message(chat_id=chat_id,\
            text=f'Currently ongoing call on {current_call_list[0]} at {current_call_list[1]}!')


def user_timeout(context):
    '''
    Callback function to be called after 15 mins of the starting the bot. It:
    - ends the conversation
    - clears user_data
    '''
    # for easier access to context
    j_context = context.job.context
    # for easier access to user_data
    user_data = j_context.user_data
    if user_data['status']['started']:
        user_id = user_data['user_id']
        # resets user session
        clear_user_memory(user_data, True)
        # informs the user
        j_context.bot.send_message(chat_id=user_id, text = user_timeout_msg)
        return

############
# COMMANDS #
############

# to make sure all members are initiated
def process_members(update, context):
    # for easier access to user_id
    user_id = update.message.from_user.id

    # initiates the user if it is his first time
    initiate_user(user_id, update, context) # in utils

    # updates the permission according to quits by the coder
    check_for_personal_changes(update, context)

dispatcher.add_handler(MessageHandler(Filters.text, process_members), group=0) # gives most prirority


#######################
# CAN RUN IN ANY MODE #
#######################

# /patch_notes
@send_typing_action
def patch_notes(update, context):
    # for easier access to bot_data
    patch_notes = context.bot_data['bot_info']['patch_notes']
    # if events has stuff
    if patch_notes != {}:
        update.message.reply_text(text=patch_notes, parse_mode=ParseMode.HTML)

    # if patch notes is empty
    else:
        update.message.reply_text(text='Patch notes currently unavailable')

dispatcher.add_handler(CommandHandler('patch_notes', patch_notes), group=1)

# /info
@send_typing_action
def info(update, context):
    # for easier access to bot_data
    _info = context.bot_data['bot_info']['description']
    # if events has stuff
    if _info != {}:
        update.message.reply_text(text=_info, parse_mode=ParseMode.HTML)

    # if patch notes is empty
    else:
        update.message.reply_text(text='Bot info currently unavailable')

dispatcher.add_handler(CommandHandler('info', info), group=1)

# /help
@send_typing_action
def help(update, context):
    # returns fail msg if the user is currently in an action
    if context.user_data['status']['action']:
        update.message.reply_text(text=function_fail_msg)
        return
    # creates the different menus
    elif context.user_data['status']['backend']: # backend mode
        menu = create_menu(possible_commands, 'backend')
    elif context.user_data['status']['admin_menu']: # adminmenu mode
        menu = create_menu(possible_commands, 'admin_menu')
    elif context.user_data['status']['cfm_settings']: # cfm_settings
        menu = create_menu(possible_commands, 'cfm_settings')
    elif context.user_data['status']['started']: # start mode
        menu = create_menu(possible_commands, 'started')
    else: # in sleep mode
        menu = create_menu(possible_commands, 'sleep')

    # send the menu out
    update.message.reply_text(text=menu, parse_mode=ParseMode.HTML)

dispatcher.add_handler(CommandHandler('help', help), group=1)

# /start_call <url>
@send_typing_action
def start_call(update, context): 
    # returns fail msg if the user is currently in an action
    if context.user_data['status']['action']:
        update.message.reply_text(text=function_fail_msg)
        return
    # check the user permissions
    elif context.user_data['permissions'] != 'coders' and context.user_data['permissions'] != 'admins':
        update.message.reply_text(text=permission_fail_msg)
    # there must only be one argument which is the url
    elif not len(context.args) == 1:
        update.message.reply_text(text=call_format_error)
        return
    
    else:
        if context.bot_data['current_call'] == []:
            bot_print(update, 'Creating spammer')
            # spams the chat every 10 minutes
            jobqueuer.run_repeating(callback=call_spammer, interval=datetime.timedelta(minutes=10),\
                first=datetime.timedelta(minutes=15), context=context)
        url = context.args[0]
        # gets the name of the platform of the ongoing call
        platform = process_url(update, url)
        chat_id = context.bot_data['chat_id']
        # In case the process_url function doesnt support this platform
        if platform == None:
            context.bot.send_message(chat_id = chat_id, text=not_reg_platform_error)
        else:
            context.bot_data['current_call'] = [platform, url]
            context.bot.send_message(chat_id = chat_id, text=f'New call started on {platform}')
        
dispatcher.add_handler(CommandHandler('start_call', start_call), group=1)

# /end_call
@send_typing_action
def end_call(update, context): 
    # returns fail msg if the user is currently in an action
    if context.user_data['status']['action']:
        update.message.reply_text(text=function_fail_msg)
        return
    # only continues if there is an going call
    elif context.bot_data['current_call'] == []:
        update.message.reply_text(text=call_not_started_msg)
        return
    # if there is an ongoing call and user wants to end it
    else:
        context.bot_data['current_call'] = []
        chat_id = context.bot_data['chat_id']
        context.bot.send_message(chat_id = chat_id, text=call_ended_msg)
    
dispatcher.add_handler(CommandHandler('end_call', end_call), group=1)

# sends the content of alpha events into the chat
@send_typing_action
def display_events(update, context):
    # get the events dictionary and sort it 
    events_dict = context.bot_data['events']
    
    # if events has stuff
    if events_dict != {}:
        context.bot_data['events'] = sort_events_dict(events_dict)
        displayed_events = convert_dict_to_str(context.bot_data['events'])
        update.message.reply_text(text=displayed_events, parse_mode = telegram.ParseMode.HTML)

    # if library is empty
    else:
        update.message.reply_text(text=events_empty_msg)

dispatcher.add_handler(CommandHandler('events', display_events), group=1)

# sends the contents of alpha library into the chat
@send_typing_action
def display_lib(update, context):
    # get the library dictionary
    lib_dict = context.bot_data['library']['teachings']

    # if library has stuff
    if lib_dict != {}:
        displayed_library = convert_dict_to_str(lib_dict, True)
        update.message.reply_text(text=displayed_library, parse_mode= ParseMode.HTML)

    # if library is empty
    else:
        update.message.reply_text(text=lib_empty_msg)

dispatcher.add_handler(CommandHandler('library', display_lib), group=1)

# /cancel
@send_typing_action
def cancel(update, context):
    # dont run command if the user is currently doing an action
    if not context.user_data['status']['action']:
        update.effective_message.reply_text(text= not_in_action_error)

    # if no other issue
    else:
        user_data = context.user_data
        user_data['status']['action'] = False
        clear_user_memory(user_data)
        update.message.reply_text(text=cancel_msg)

dispatcher.add_handler(CommandHandler('cancel', cancel), group=1)

# msg sent when /start
@send_typing_action
def start(update, context):
    # for easier acces to user's status dict
    status_dict = context.user_data['status']

    # if the user is supposed to be in admin menu, in action or in backend, fail this action
    if status_dict['admin_menu'] or status_dict['action'] or status_dict['backend']:
        update.message.reply_text(text=function_fail_msg)
        return

    # gets the persons username
    username = update.message.from_user.username

    if context.user_data['status']['started']:
        update.message.reply_text(text=alr_started_msg.format(username))
        return

    # if they havent been initiated, pm them the first start msg
    elif not context.user_data['status']['initiated']:
        context.user_data['status']['initiated'] = True
        context.user_data['status']['started'] = True
        # set timeout in 15 mins
        jobqueuer.run_once(user_timeout, datetime.timedelta(minutes=15), context=context)
        context.bot.send_message(chat_id=update.message.from_user.id, \
            text=first_start_msg.format(username))

    # for normal users
    else:
        context.user_data['status']['started'] = True
        # set timeout in 15 mins
        jobqueuer.run_once(user_timeout, datetime.timedelta(minutes=15), context=context)
        update.message.reply_text(text=start_msg.format(username))

dispatcher.add_handler(CommandHandler('start', start), group=1)

# /broadcast <msg>
@send_typing_action
def broadcast(update, context): 
    # returns fail msg if the user is currently in an action
    if context.user_data['status']['action']:
        update.message.reply_text(text=function_fail_msg)
        return
    # check the user permissions
    elif context.user_data['permissions'] != 'coders' and context.user_data['permissions'] != 'admins':
        update.message.reply_text(text=permission_fail_msg)

    # if theres no other issue
    else:
        # converts message into a string
        message = context.args
        message = ' '.join(message)
        # makes sure sender is not a recipient
        sender_id = update.message.from_user.id
        for member_id in tuple(context.bot_data['members'].values()):
            if sender_id == member_id:
                continue
            context.bot.send_message(chat_id=member_id, text= f'{message}')
        
        # informs the sender the message is sent
        update.message.reply_text(text=broadcasted_fin_msg)

dispatcher.add_handler(CommandHandler('broadcast', broadcast), group=1)

###################
# MUST BE STARTED #
###################

# /end
def end(update, context):
    # quick access to user_data
    user_data = context.user_data
    # if not alr ready in a conversation
    if not user_data['status']['started']:
        # generates a random fail end message
        no_of_end_msgs = len(fail_end_msgs)
        end_msg_index = random.randint(0, no_of_end_msgs-1)
        end_msg = fail_end_msgs[end_msg_index]
        splitted_end_msg = end_msg.split('_')
        for msg in splitted_end_msg:
            update.message.reply_text(text=msg)
    
    # in normal circumstances
    else:
        # resets everything
        clear_user_memory(user_data, True)
        # generates a random end message
        no_of_end_msgs = len(end_msgs)
        end_msg_index = random.randint(0, no_of_end_msgs-1)
        end_msg = end_msgs[end_msg_index]
        splitted_end_msg = end_msg.split('_')
        for msg in splitted_end_msg:
            update.message.reply_text(text=msg)
    
dispatcher.add_handler(CommandHandler('end', end), group=1)

# to collect feedback from anybody
@send_typing_action
def give_feedback(update, context):
    # makes sure user has started the conversation
    if not context.user_data['status']['started']:
        update.message.reply_text(text=not_started_error)
    # dont run command if the user is currently doing an action
    elif context.user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
    elif not context.user_data['status']['feedback']:
        # events_dict feedback status to True
        context.user_data['status']['feedback'] = True
        context.user_data['status']['action'] = True
        update.message.reply_text(text=feedback_msg)
    else: 
        update.message.reply_text(text=feedback_given_msg)

dispatcher.add_handler(CommandHandler('feedback', give_feedback), group=1)

# /cfm_settings
@send_typing_action
def cfm_settings(update, context):
    # makes sure user has started the conversation
    if not context.user_data['status']['started']:
        update.message.reply_text(text=not_started_error)
    # dont run command if the user is currently doing an action
    elif context.user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
    # dont allow accessing this if the user is in another menu
    elif menu_is_open(context.user_data):
        update.message.reply_text(text= other_menu_error)
        return
    else:
        # gets user permissions
        permissions = context.user_data['permissions']
        # in case the permission does not have permissions
        if not check_permission(permissions, 'cfm_IC'):
            update.message.reply_text(text=permission_fail_msg)
        # if no other issue
        else:
            username = update.message.from_user.username
            context.user_data['status']['cfm_settings'] = True
            update.message.reply_text(text=cfm_access_msg.format(username))
        
dispatcher.add_handler(CommandHandler('cfm_settings', cfm_settings), group=1)

################################
# COMMANDS FOR CONFIRMATION IC #
################################

# /view_msg
@send_typing_action
def view_msg(update, context):
    # makes sure user has started the conversation
    if not context.user_data['status']['started']:
        update.message.reply_text(text=not_started_error)
    # dont run command if the user is currently doing an action
    elif context.user_data['status']['action']:
        update.effective_message.reply_text(text=middle_of_action_msg)
    # dont continue if user is not in cfm_settings:
    elif not context.user_data['status']['cfm_settings']:
        update.message.reply_text(text=only_cfm_settings)
    # if no other issue
    else:
        if context.bot_data['cfm']['temp_msg'] != '':
            msg = context.bot_data['cfm']['temp_msg']
        else:
            msg = context.bot_data['cfm']['cfm_msg']
        update.message.reply_text(text=emojis.encode(msg))

dispatcher.add_handler(CommandHandler('view_msg', view_msg), group=1)

# /change_msg
@send_typing_action
def change_msg(update, context):
    # makes sure user has started the conversation
    if not context.user_data['status']['started']:
        update.message.reply_text(text=not_started_error)

    # dont run command if the user is currently doing an action
    elif context.user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        
    # dont continue if user is not in cfm_settings:
    elif not context.user_data['status']['cfm_settings']:
        update.message.reply_text(text=only_cfm_settings)

    # if no other issue
    else:
        context.user_data['status']['change_msg'] = 2
        update.message.reply_text(text=cfm_change_init)

dispatcher.add_handler(CommandHandler('change_msg', change_msg), group=1)

# /change_once
@send_typing_action
def change_once(update, context):
    # makes sure user has started the conversation
    if not context.user_data['status']['started']:
        update.message.reply_text(text=not_started_error)
    # dont run command if the user is currently doing an action
    elif context.user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)

    # dont continue if user is not in cfm_settings:
    elif not context.user_data['status']['cfm_settings']:
        update.message.reply_text(text=only_cfm_settings)

    # if no other issue
    else:
        context.user_data['status']['change_msg'] = 1
        update.message.reply_text(text=cfm_change_init)

dispatcher.add_handler(CommandHandler('change_once', change_once), group=1)

# /start_cfm
@send_typing_action
def start_cfm(update, context):
    # makes sure user has started the conversation
    if not context.user_data['status']['started']:
        update.message.reply_text(text=not_started_error)
    # dont run command if the user is currently doing an action
    elif context.user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)

    # dont continue if user is not in cfm_settings:
    elif not context.user_data['status']['cfm_settings']:
        update.message.reply_text(text=only_cfm_settings)

    # if no other issue
    else:
        context.bot_data['cfm']['active'] = True
        update.message.reply_text(text=cfm_restarted)

dispatcher.add_handler(CommandHandler('start_cfm', start_cfm), group=1)

# /stop_cfm
@send_typing_action
def stop_cfm(update, context):
    # makes sure user has started the conversation
    if not context.user_data['status']['started']:
        update.message.reply_text(text=not_started_error)
    # dont run command if the user is currently doing an action
    elif context.user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)

    # dont continue if user is not in cfm_settings:
    elif not context.user_data['status']['cfm_settings']:
        update.message.reply_text(text=only_cfm_settings)

    # if no other issue
    else:
        context.bot_data['cfm']['active'] = False
        update.message.reply_text(text=cfm_stopped)

dispatcher.add_handler(CommandHandler('stop_cfm', stop_cfm), group=1)

#######################
# COMMANDS FOR ADMINS #
#######################

# access the admin menu /admin_menu
@send_typing_action
def admin_session(update, context):
    # dont run command if the user is currently doing an action
    if context.user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        return
    # if the person doesn't have permissions
    elif (context.user_data['permissions'] != 'coders') and \
        (context.user_data['permissions'] != 'admins'):
        update.message.reply_text(text=permission_fail_msg)
    # if the person is supposed to be in the admin menu already
    elif context.user_data['status']['admin_menu']:
        update.message.reply_text(text=bruh_message)
    
    # dont allow this to be run in admin menu or backend
    elif menu_is_open(context.user_data):
        update.message.reply_text(text= other_menu_error)
        return

    # starts the admin session
    else:
        context.user_data['status']['admin_menu'] = True
        menu = create_menu(possible_commands, 'admin_menu')
        update.message.reply_text(text=menu.format(context.user_data['username']), parse_mode=ParseMode.HTML)

dispatcher.add_handler(CommandHandler('admin_menu', admin_session), group=1)

# /add_event
@send_typing_action
def add_event(update, context):
    # makes sure user has accessed admin menu
    if not context.user_data['status']['admin_menu']:
        update.message.reply_text(text=not_admined_error)
        return
    # dont run command if the user is currently doing an action
    elif context.user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        return
    else:
        context.user_data['status']['action'] = True
        context.user_data['status']['add_event'] = 1
        update.message.reply_text(text=add_event_0)

dispatcher.add_handler(CommandHandler('add_event', add_event), group=1)

# /add_whole_event
@send_typing_action
def add_whole_event(update, context):
    # makes sure user has accessed admin menu
    if not context.user_data['status']['admin_menu']:
        update.message.reply_text(text=not_admined_error)
        return
    # dont run command if the user is currently doing an action
    elif context.user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)  
        return
    
    else:
        context.user_data['status']['action'] = True
        context.user_data['status']['add_event'] = 5
        update.message.reply_text(text=whole_event_msg)

dispatcher.add_handler(CommandHandler('add_whole_event', add_whole_event), group=1)

# /del_event
@send_typing_action
def del_event(update, context):
    # makes sure user has accessed admin menu
    if not context.user_data['status']['admin_menu']:
        update.message.reply_text(text=not_admined_error)
        return
    # dont run command if the user is currently doing an action
    elif context.user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)  
        return
    
    events_dict = context.bot_data['events']
    # if events has stuff
    if events_dict != {}:
        context.user_data['status']['action'] = True
        # sort the events_dict
        events_dict = sort_events_dict(events_dict)
        displayed_events = del_event_init + '\n\n'
        displayed_events += convert_dict_to_str(events_dict)
        update.message.reply_text(text=displayed_events, parse_mode = telegram.ParseMode.HTML)
        context.user_data['status']['add_event'] = -1

    # if library is empty
    else:
        update.message.reply_text(text=events_empty_msg)

dispatcher.add_handler(CommandHandler('del_event', del_event), group=1)

# /add_teaching
@send_typing_action
def add_teaching(update, context):
    # makes sure user has accessed admin menu
    if not context.user_data['status']['admin_menu']:
        update.message.reply_text(text=not_admined_error)
        return
    # dont run command if the user is currently doing an action
    elif context.user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        return
    else:
        context.user_data['status']['action'] = True
        context.user_data['status']['add_teaching'] = 1
        update.message.reply_text(text=add_teaching_0)

dispatcher.add_handler(CommandHandler('add_teaching', add_teaching), group=1)

# /add_whole_teaching
@send_typing_action
def add_whole_teaching(update, context):
    # makes sure user has accessed admin menu
    if not context.user_data['status']['admin_menu']:
        update.message.reply_text(text=not_admined_error)
        return
    # dont run command if the user is currently doing an action
    elif context.user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        return
    else:
        context.user_data['status']['action'] = True
        context.user_data['status']['add_teaching'] = 2
        update.message.reply_text(text=whole_teaching_msg)

dispatcher.add_handler(CommandHandler('add_whole_teaching', add_whole_teaching), group=1)

# /del_teaching
@send_typing_action
def del_teaching(update, context):
    # makes sure user has accessed admin menu
    if not context.user_data['status']['admin_menu']:
        update.message.reply_text(text=not_admined_error)
        return
    # dont run command if the user is currently doing an action
    elif context.user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        return

    # for easier access to lib_dict
    lib_dict = context.bot_data['library']['teachings']
    # if the library is empty
    if lib_dict == {}:
        update.message.reply_text(text=lib_empty_msg)
        # otherwise normallys
    else:
        context.user_data['status']['action'] = True
        context.user_data['status']['add_teaching'] = -1
        displayed_lib = del_teaching_init + '\n\n' + convert_dict_to_str(lib_dict, True)
        update.message.reply_text(text=displayed_lib)

dispatcher.add_handler(CommandHandler('del_teaching', del_teaching), group=1)

##############
# FOR CODERS #
##############

# def reset_bot(update, context):
#     for member in tuple(context.bot_data['members'].values()):
# /backend
@send_typing_action
def backend(update, context):
    # for easier access to user data
    user_data = context.user_data
    # requirement for it to go through
    if not user_data['permissions'] == 'coders':
        update.message.reply_text(text= permission_fail_msg)
        return

    # dont allow this to be run in admin menu or backend
    elif menu_is_open(user_data):
        update.message.reply_text(text= other_menu_error)
        return

    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        return

    # else if all goes well
    else:
        username = update.message.from_user.username
        user_data['status']['backend'] = True
        menu = create_menu(possible_commands, 'backend')
        update.message.reply_text(text=menu.format(username))

dispatcher.add_handler(CommandHandler('backend', backend), group=1)

# /events_dict
@send_typing_action
def events_dict(update, context):
    # for easier access to user data
    user_data = context.user_data
    # user must access backend first
    if not user_data['status']['backend']:
        update.message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        return
    # if theres no other issue
    else:
        eventsdict = context.bot_data['events']
        update.message.reply_text(text= str(eventsdict))

dispatcher.add_handler(CommandHandler('events_dict', events_dict), group=1)

# /lib_dict
@send_typing_action
def lib_dict(update, context):
    # for easier access to user data
    user_data = context.user_data
    # user must access backend first
    if not user_data['status']['backend']:
        update.message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        return
    # if theres no other issue
    else:
        libdict = context.bot_data['library']['teachings']
        update.message.reply_text(text= str(libdict))

dispatcher.add_handler(CommandHandler('lib_dict', lib_dict), group=1)

# /admins_dict
@send_typing_action
def admins_dict(update, context):
    # for easier access to user data
    user_data = context.user_data
    # user must access backend first
    if not user_data['status']['backend']:
        update.message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        return
    # if theres no other issue
    else:
        admins_dict = context.bot_data['admins']
        update.message.reply_text(text= str(admins_dict))

dispatcher.add_handler(CommandHandler('admins_dict', admins_dict), group=1)

# /members_dict
@send_typing_action
def members_dict(update, context):
    # for easier access to user data
    user_data = context.user_data
    # user must access backend first
    if not user_data['status']['backend']:
        update.message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        return
    # if theres no other issue
    else:
        membersdict = context.bot_data['members']
        update.message.reply_text(text= str(membersdict))

dispatcher.add_handler(CommandHandler('members_dict', members_dict), group=1)

# /cfm_ICs_dict
@send_typing_action
def cfm_ICs_dict(update, context):
    # for easier access to user data
    user_data = context.user_data
    # user must access backend first
    if not user_data['status']['backend']:
        update.effective_message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.effective_message.reply_text(text=middle_of_action_msg)
        return
    # if theres no other issue
    else:
        _cfm_ICs_dict = context.bot_data['cfm_ICs']
        update.message.reply_text(text= str(_cfm_ICs_dict))

dispatcher.add_handler(CommandHandler('cfm_ICs_dict', cfm_ICs_dict), group=1)

# /bday_ICs_dict
@send_typing_action
def bday_ICs_dict(update, context):
    # for easier access to user data
    user_data = context.user_data
    # user must access backend first
    if not user_data['status']['backend']:
        update.effective_message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.effective_message.reply_text(text=middle_of_action_msg)
        return
    # if theres no other issue
    else:
        _bday_ICs_dict = context.bot_data['bday_ICs']
        update.message.reply_text(text= str(_bday_ICs_dict))

dispatcher.add_handler(CommandHandler('bday_ICs_dict', bday_ICs_dict), group=1)

# /lib_limit
@send_typing_action
def lib_limit(update, context):
    # for easier access to user data
    user_data = context.user_data
    # user must access backend first
    if not user_data['status']['backend']:
        update.effective_message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.effective_message.reply_text(text=middle_of_action_msg)
        return
    # if theres no other issue
    else:
        limit = context.bot_data['library']['limit']
        update.message.reply_text(text= str(limit))

dispatcher.add_handler(CommandHandler('lib_limit', lib_limit), group=1)

# /change_lib_limit
@send_typing_action
def change_lib_limit(update, context):
    # for easier access to user data
    user_data = context.user_data
    # user must access backend first
    if not user_data['status']['backend']:
        update.effective_message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.effective_message.reply_text(text=middle_of_action_msg)
        return
    # if theres no other issue
    else:
        try:
            new_limit = int(context.args[0])
        except ValueError:
            update.message.reply_text(text= str(not_integer_error))
            pass
        context.bot_data['library']['limit'] = new_limit
        update.message.reply_text(text= limit_change_msg.format(new_limit))

dispatcher.add_handler(CommandHandler('change_lib_limit', change_lib_limit), group=1)

# /coders_list
@send_typing_action
def coders_list(update, context):
    # for easier access to user data
    user_data = context.user_data
    # user must access backend first
    if not user_data['status']['backend']:
        update.message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        return
    # if theres no other issue
    else:
        coderslist = context.bot_data['coders']
        update.message.reply_text(text= str(coderslist))

dispatcher.add_handler(CommandHandler('coders_list', coders_list), group=1)

# /make_admin
@send_typing_action
def make_admin(update, context):
    # for easier access to user data
    user_data = context.user_data
    # user must access backend first
    if not user_data['status']['backend']:
        update.message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        return
    # check the content of the args passed in
    else:
        args = context.args
        if not len(args) == 1:
            update.message.reply_text(text=one_arg_error)
            return

        else:
            if not is_chat_id(args[0]):
                update.message.reply_text(text=not_chat_id_error)
                return
            else:
                chat_id = int(args[0])
            current_perm = get_user_permissions(chat_id, context)
            # checks if the person is a registered member
            if not tuple(context.bot_data['members'].values()).__contains__(chat_id):
                update.message.reply_text(text=not_exist_error)
                return
            # checks if the person is already an admin
            elif check_permission(current_perm, 'cfm_IC'):
                update.message.reply_text(text=perms_present)
                return
            # if no other issues
            else:
                username = get_key_from_value(chat_id, context.bot_data['members'])
                context.bot_data['admins'][username] = chat_id
                if not context.bot_data['permissions_changed'].__contains__(chat_id):
                    context.bot_data['permissions_changed'].append(chat_id)
                update.message.reply_text(text= add_admin_fin.format(username))

dispatcher.add_handler(CommandHandler('make_admin', make_admin), group=1)

# /make_cfm
@send_typing_action
def make_cfm(update, context):
    # for easier access to user data
    user_data = context.user_data
    # user must access backend first
    if not user_data['status']['backend']:
        update.message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        return
    # check the content of the args passed in
    else:
        args = context.args
        if not len(args) == 1:
            update.message.reply_text(text=one_arg_error)
            return

        else:
            if not is_chat_id(args[0]):
                update.message.reply_text(text=not_chat_id_error)
                return
            else:
                chat_id = int(args[0])
            current_perm = get_user_permissions(chat_id, context)
            # checks if the person is a registered member
            if not tuple(context.bot_data['members'].values()).__contains__(chat_id):
                update.message.reply_text(text=not_exist_error)
                return
            # checks if the person is already an admin
            elif check_permission(current_perm, 'cfm_IC'):
                update.message.reply_text(text=perms_present)
                return
            # if no other issues
            else:
                username = get_key_from_value(chat_id, context.bot_data['members'])
                context.bot_data['cfm_ICs'][username] = chat_id
                if not context.bot_data['permissions_changed'].__contains__(chat_id):
                    context.bot_data['permissions_changed'].append(chat_id)
                update.message.reply_text(text= add_perms_fin.format('cfm_IC', username))

dispatcher.add_handler(CommandHandler('make_cfm', make_cfm), group=1)

# /make_bday
@send_typing_action
def make_bday(update, context):
    # for easier access to user data
    user_data = context.user_data
    # user must access backend first
    if not user_data['status']['backend']:
        update.message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        return
    # check the content of the args passed in
    else:
        args = context.args
        if not len(args) == 1:
            update.message.reply_text(text=one_arg_error)
            return

        else:
            if not is_chat_id(args[0]):
                update.message.reply_text(text=not_chat_id_error)
                return
            else:
                chat_id = int(args[0])
            current_perm = get_user_permissions(chat_id, context)
            # checks if the person is a registered member
            if not tuple(context.bot_data['members'].values()).__contains__(chat_id):
                update.message.reply_text(text=not_exist_error)
                return
            # checks if the person is already an admin
            elif check_permission(current_perm, 'bday_IC'):
                update.message.reply_text(text=perms_present)
                return
            # if no other issues
            else:
                username = get_key_from_value(chat_id, context.bot_data['members'])
                context.bot_data['bday_ICs'][username] = chat_id
                if not context.bot_data['permissions_changed'].__contains__(chat_id):
                    context.bot_data['permissions_changed'].append(chat_id)
                update.message.reply_text(text= add_perms_fin.format('bday_IC', username))

dispatcher.add_handler(CommandHandler('make_bday', make_bday), group=1)

# /remove_member
@send_typing_action
def remove_member(update, context):
    # for easier access to user data
    user_data = context.user_data
    # user must access backend first
    if not user_data['status']['backend']:
        update.message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        return
    # if authentication goes through, check validity
    else:
        args = context.args # returns a list of strings
        # check if it is a single word(name) passed in
        if not len(args) == 1:
            update.message.reply_text(text= remove_user_fail)
            return
        # must make sure that the args is not empty
        else:            
            username = args[0]
            # check if such member exists
            if not tuple(context.bot_data['members'].keys()).__contains__(username):
                update.message.reply_text(text=remove_not_exist.format('Member', username))
                return
            # if the input is correct
            else:
                context.bot_data['members'].pop(username)
                update.message.reply_text(text= remov_user_fin.format(username, 'members'))

dispatcher.add_handler(CommandHandler('remove_member', remove_member), group=1)

# /remove_admin
@send_typing_action
def remove_admin(update, context):
    # for easier access to user data
    user_data = context.user_data
    # user must access backend first
    if not user_data['status']['backend']:
        update.message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        return
    # if authentication goes through, check validity
    else:
        args = context.args # returns a list of strings        
        # check if it is a single word passed in
        if not len(args) == 1:
            update.message.reply_text(text= remove_user_fail)
            return
        # make sure that there is at least one arg passed in 
        else:
            username = args[0]
            # check if such member exists
            if not tuple(context.bot_data['admins'].keys()).__contains__(username):
                update.message.reply_text(text=remove_not_exist.format('Admin', username))
                return
            # if the input is correct
            else:
                context.bot_data['permissions_changed'].append(context.bot_data['admins'][username])
                context.bot_data['admins'].pop(username)
                update.message.reply_text(text= remov_user_fin.format(username, 'Admins'))

dispatcher.add_handler(CommandHandler('remove_admin', remove_admin), group=1)

# /remove_cfm
@send_typing_action
def remove_cfm(update, context):
    # for easier access to user data
    user_data = context.user_data
    # user must access backend first
    if not user_data['status']['backend']:
        update.message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        return
    # if authentication goes through, check validity
    else:
        args = context.args # returns a list of strings        
        # check if it is a single word passed in
        if not len(args) == 1:
            update.message.reply_text(text= remove_user_fail)
            return
        # make sure that there is at least one arg passed in 
        else:
            username = args[0]
            # check if such member exists
            if not tuple(context.bot_data['cfm_ICs'].keys()).__contains__(username):
                update.message.reply_text(text=remove_not_exist.format('cfm_IC', username))
                return
            # if the input is correct
            else:
                context.bot_data['permissions_changed'].append(context.bot_data['cfm_ICs'][username])
                context.bot_data['cfm_ICs'].pop(username)
                update.message.reply_text(text= remov_user_fin.format(username, 'cfm_IC'))

dispatcher.add_handler(CommandHandler('remove_cfm', remove_cfm), group=1)

# /remove_bday
@send_typing_action
def remove_bday(update, context):
    # for easier access to user data
    user_data = context.user_data
    # user must access backend first
    if not user_data['status']['backend']:
        update.message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        return
    # if authentication goes through, check validity
    else:
        args = context.args # returns a list of strings        
        # check if it is a single word passed in
        if not len(args) == 1:
            update.message.reply_text(text= remove_user_fail)
            return
        # make sure that there is at least one arg passed in 
        else:
            username = args[0]
            # check if such member exists
            if not tuple(context.bot_data['bday_ICs'].keys()).__contains__(username):
                update.message.reply_text(text=remove_not_exist.format('bday_IC', username))
                return
            # if the input is correct
            else:
                context.bot_data['permissions_changed'].append(context.bot_data['bday_ICs'][username])
                context.bot_data['bday_ICs'].pop(username)
                update.message.reply_text(text= remov_user_fin.format(username, 'bday_IC'))

dispatcher.add_handler(CommandHandler('remove_bday', remove_bday), group=1)

# /quit
@send_typing_action
def quit(update, context):
    # for easier access to user data
    user_data = context.user_data
    # user must access backend first
    if not menu_is_open(user_data):
        update.message.reply_text(text=quit_fail_msg)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.message.reply_text(text=middle_of_action_msg)
        return
    # if theres no other issue
    else:
        close_all_menus(user_data)
        update.message.reply_text(text= quit_fin_msg)

dispatcher.add_handler(CommandHandler('quit', quit), group=1)

## for testing the daily updates
# @send_typing_action
# def update(update, context):
#     daily_events_update(dispatcher)
#     bot_print(update, 'Daily Update Done!')

# dispatcher.add_handler(CommandHandler('update', update), group=1)

## for testing confirmation sender
# @send_typing_action
# def confirm(update, context):
#     bot_print(update, 'Attempted send confirmation')
#     # collect confirmation
#     chat_id = dispatcher.bot_data['chat_id']
#     # # doesn't continue if cfm is not started
#     # if not dispatcher.bot_data['cfm']['active']:
#     #     return
#     # if there is a temp msg, use it
#     if dispatcher.bot_data['cfm']['temp_msg'] != '':
#         cfm_msg = dispatcher.bot_data['cfm']['temp_msg']
#         # erase temp_msg after use
#         dispatcher.bot_data['cfm']['temp_msg'] = ''
#     # take the permanent msg if there is no temp msg
#     else:
#         cfm_msg = dispatcher.bot_data['cfm']['cfm_msg']
#     dispatcher.bot.send_message(chat_id=chat_id, text=emojize(cfm_msg), parse_mode=ParseMode.HTML)

# # for testing the daily updates
# dispatcher.add_handler(CommandHandler('confirm', confirm), group=1)

# send a message to people that inputted an invalid command (lowest priority)
@send_typing_action
def unknown(update, context):
    update.message.reply_text(text='That\'s not a real command fool!')
dispatcher.add_handler(MessageHandler(Filters.command, unknown), group=1)

# process every message depending on what the user is doing (needs to be of lowest priority possible)
def process_msg(update, context):
    # for easier access to user_id
    user_id = update.message.from_user.id

    user_data = context.user_data # for easier access to user_data
    permissions = context.user_data['permissions'] # find permissions of this user

    # if the user is trying to give feedback
    if user_data['status']['feedback']:
        for coder in coders:
            context.bot.send_message(chat_id=coder, text=update.message.text)
        update.message.reply_text(text=feedback_given_msg)
        user_data['status']['feedback'] = False
        user_data['status']['action'] = False
    
    # if user is trying to add or delete events
    elif bool(user_data['status']['add_event']):
        process_add_event(update, context, user_data)
    
    # if user is trying to add or delete teachings
    elif bool(user_data['status']['add_teaching']):
        process_add_teaching(update, context, user_data)

    # if user is trying to change cfm msg
    elif bool(context.user_data['status']['change_msg']):
        new_msg = update.message.text
        # changes temporarily
        if context.user_data['status']['change_msg'] == 1:
            context.bot_data['cfm']['temp_msg'] = new_msg
            context.user_data['status']['change_msg'] = 0
            update.message.reply_text(text=emojis.decode(cfm_once_fin))

        # changes permanently
        elif context.user_data['status']['change_msg'] == 2:
            context.bot_data['cfm']['cfm_msg'] = new_msg
            context.user_data['status']['change_msg'] = 0
            update.message.reply_text(text=emojis.decode(cfm_change_fin))


dispatcher.add_handler(MessageHandler(Filters.text, process_msg), group=1)

##############
# FIXED JOBS #
##############

# collect confirmation every week on Thursday 1800hrs
def collect_cfmation(context: telegram.ext.CallbackContext):
    # collect confirmation
    logging.info('cfm sent to group')
    print('cfm sent to group')
    chat_id = dispatcher.bot_data['chat_id']
    # doesn't continue if cfm is not started
    if not dispatcher.bot_data['cfm']['active']:
        pass
    # if there is a temp msg, use it
    elif dispatcher.bot_data['cfm']['temp_msg'] != '':
        cfm_msg = dispatcher.bot_data['cfm']['temp_msg']
        # erase temp_msg after use
        dispatcher.bot_data['cfm']['temp_msg'] = ''
    # take the permanent msg if there is no temp msg
    else:
        cfm_msg = dispatcher.bot_data['cfm']['cfm_msg']
    dispatcher.bot.send_message(chat_id=chat_id, text=emojis.encode(cfm_msg), parse_mode=ParseMode.HTML)

cfmation_collector = jobqueuer.run_repeating(callback=collect_cfmation, \
    interval=datetime.timedelta(days=7), first=getDatetimeOfNextXDay(isoweekday=4, hour=18))


# daily send msg for daily events
def remind_events(context: telegram.ext.CallbackContext):
    dispatcher.bot.send_message(chat_id = 333647246, text='UPDATE ATTEMPED') # NEW ADDED
    # send reminders or remove events accordingly to every user registered as a member
    daily_events_update(dispatcher)

event_reminder = jobqueuer.run_daily(callback=remind_events,\
    time=manual_convert_SGT(datetime.time(8, 0, 0, 0)))

print('polling')
# to start the bot
updater.start_polling()
