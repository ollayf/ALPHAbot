'''
This is the main.py file of ALPHAbot v3.0
to be run to start the bot and keep it running indefinitely

'''

import telegram
import datetime
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from envs import *
from utils import *
import logging
import random
from pytz import timezone

####################
# INITIALISING BOT #
####################

print('initialising')
# initialises the updater object
updater = Updater(token=testing_token, use_context=True, persistence=False)

dispatcher = updater.dispatcher # for quicker access to the dispatcher object
jobqueuer = updater.job_queue # for quicker access to JobQueue object

# alpha_lib = parseMD('alpha_lib.md', True)
# events = parseMD('events.md', True)
# members = parseMD('members.md', True)

# set bot_data to default if it does not already exist
if dispatcher.bot_data == {}:
    dispatcher.bot_data = default_bot_data
    print('bot_data set to default')
else:
    print('there is a saved version of bot_data already')

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

# /help
@send_typing_action
def help(update, context):
    # returns fail msg if the user is currently in an action
    if context.user_data['status']['action']:
        update.effective_message.reply_text(text=function_fail_msg)
        return
    # creates the different menus
    elif context.user_data['status']['backend']: # backend mode
        menu = create_menu(possible_commands, 'backend')
    elif context.user_data['status']['admin_menu']: # adminmenu mode
        menu = create_menu(possible_commands, 'admin_menu')
    elif context.user_data['status']['started']: # start mode
        menu = create_menu(possible_commands, 'started')
    else: # in sleep mode
        menu = create_menu(possible_commands, 'sleep')
    
    # send the menu out
    update.message.reply_text(text=menu)

dispatcher.add_handler(CommandHandler('help', help), group=1)

# /start_call <url>
@send_typing_action
def start_call(update, context): 
    # returns fail msg if the user is currently in an action
    if context.user_data['status']['action']:
        update.effective_message.reply_text(text=function_fail_msg)
        return
    # check the user permissions
    elif context.user_data['permissions'] != 'coders' and context.user_data['permissions'] != 'admins':
        update.effective_message.reply_text(text=permission_fail_msg)
    # there must only be one argument which is the url
    elif not len(context.args) == 1:
        update.effective_message.reply_text(text=call_format_error)
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
        update.effective_message.reply_text(text=function_fail_msg)
        return
    # only continues if there is an going call
    elif context.bot_data['current_call'] == []:
        update.effective_message.reply_text(text=call_not_started_msg)
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

# msg sent when /start
@send_typing_action
def start(update, context):
    # for easier acces to user's status dict
    status_dict = context.user_data['status']

    # if the user is supposed to be in admin menu, in action or in backend, fail this action
    if status_dict['admin_menu'] or status_dict['action'] or status_dict['backend']:
        update.effective_message.reply_text(text=function_fail_msg)
        return

    # gets the persons username
    username = update.effective_message.from_user.username

    if context.user_data['status']['started']:
        update.effective_message.reply_text(text=alr_started_msg.format(username))
        return

    # if they havent been initiated, pm them the first start msg
    elif not context.user_data['status']['initiated']:
        context.user_data['status']['initiated'] = True
        context.user_data['status']['started'] = True
        # set timeout in 15 mins
        jobqueuer.run_once(user_timeout, datetime.timedelta(minutes=15), context=context)
        context.bot.send_message(chat_id=update.effective_message.from_user.id, \
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
        update.effective_message.reply_text(text=function_fail_msg)
        return
    # check the user permissions
    elif context.user_data['permissions'] != 'coders' and context.user_data['permissions'] != 'admins':
        update.effective_message.reply_text(text=permission_fail_msg)

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
        update.effective_message.reply_text(text=middle_of_action_msg)
    elif not context.user_data['status']['feedback']:
        # events_dict feedback status to True
        context.user_data['status']['feedback'] = True
        context.user_data['status']['action'] = True
        update.effective_message.reply_text(text=feedback_msg)
    else: 
        update.effective_message.reply_text(text=feedback_given_msg)

dispatcher.add_handler(CommandHandler('feedback', give_feedback), group=1)

#######################
# COMMANDS FOR ADMINS #
#######################

# access the admin menu /admin_menu
@send_typing_action
def admin_session(update, context):
    # dont run command if the user is currently doing an action
    if context.user_data['status']['action']:
        update.effective_message.reply_text(text=middle_of_action_msg)
        return
    # if the person doesn't have permissions
    elif (context.user_data['permissions'] != 'coders') and \
        (context.user_data['permissions'] != 'admins'):
        update.effective_message.reply_text(text=permission_fail_msg)
    # if the person is supposed to be in the admin menu already
    elif context.user_data['status']['admin_menu']:
        update.effective_message.reply_text(text=bruh_message)
    
    # dont allow this to be run in admin menu or backend
    elif context.user_data['status']['admin_menu'] or context.user_data['status']['backend']:
        update.message.reply_text(text= function_fail_msg)
        return

    # starts the admin session
    else:
        context.user_data['status']['admin_menu'] = True
        menu = create_menu(possible_commands, 'admin_menu')
        update.message.reply_text(text=menu.format(context.user_data['username']))

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
        update.effective_message.reply_text(text=middle_of_action_msg)
        return
    else:
        context.user_data['status']['action'] = True
        context.user_data['status']['add_event'] = 1
        update.effective_message.reply_text(text=add_event_0)

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
        update.effective_message.reply_text(text=middle_of_action_msg)  
        return
    
    else:
        context.user_data['status']['action'] = True
        context.user_data['status']['add_event'] = 5
        update.effective_message.reply_text(text=whole_event_msg)

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
        update.effective_message.reply_text(text=middle_of_action_msg)  
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
        update.effective_message.reply_text(text=middle_of_action_msg)
        return
    else:
        context.user_data['status']['action'] = True
        context.user_data['status']['add_teaching'] = 1
        update.effective_message.reply_text(text=add_teaching_0)

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
        update.effective_message.reply_text(text=middle_of_action_msg)
        return
    else:
        context.user_data['status']['action'] = True
        context.user_data['status']['add_teaching'] = 2
        update.effective_message.reply_text(text=whole_teaching_msg)

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
        update.effective_message.reply_text(text=middle_of_action_msg)
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
        update.effective_message.reply_text(text=displayed_lib)

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
    elif user_data['status']['admin_menu'] or user_data['status']['backend']:
        update.message.reply_text(text= function_fail_msg)
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
        update.effective_message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.effective_message.reply_text(text=middle_of_action_msg)
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
        update.effective_message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.effective_message.reply_text(text=middle_of_action_msg)
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
        update.effective_message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.effective_message.reply_text(text=middle_of_action_msg)
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
        update.effective_message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.effective_message.reply_text(text=middle_of_action_msg)
        return
    # if theres no other issue
    else:
        membersdict = context.bot_data['members']
        update.message.reply_text(text= str(membersdict))

dispatcher.add_handler(CommandHandler('members_dict', members_dict), group=1)

# /coders_list
@send_typing_action
def coders_list(update, context):
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
            chat_id = int(args[0])
            # checks if the person is a registered member
            if not tuple(context.bot_data['members'].values()).__contains__(chat_id):
                update.message.reply_text(text=not_exist_error)
                return
            # checks if the person is alraedy an admin
            elif tuple(context.bot_data['admins'].values()).__contains__(chat_id):
                update.message.reply_text(text=already_admin_msg)
                return
            # if no other issues
            else:
                username = get_key_from_value(chat_id, context.bot_data['members'])
                context.bot_data['admins'][username] = chat_id
                context.bot_data['permissions_changed'].append(chat_id)
                update.message.reply_text(text= add_admin_fin.format(username))

dispatcher.add_handler(CommandHandler('make_admin', make_admin), group=1)

# /remove_member
@send_typing_action
def remove_member(update, context):
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
        update.effective_message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.effective_message.reply_text(text=middle_of_action_msg)
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

# /quit
@send_typing_action
def quit(update, context):
    # for easier access to user data
    user_data = context.user_data
    # user must access backend first
    if not user_data['status']['backend'] and not user_data['status']['admin_menu']:
        update.effective_message.reply_text(text=quit_fail_msg)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.effective_message.reply_text(text=middle_of_action_msg)
        return
    # if theres no other issue
    else:
        user_data['status']['admin_menu'] = False
        user_data['status']['backend'] = False
        update.message.reply_text(text= quit_fin_msg)

dispatcher.add_handler(CommandHandler('quit', quit), group=1)

# for testing the daily updates
@send_typing_action
def update(update, context):
    daily_events_update(dispatcher)
    bot_print(update, 'Daily Update Done!')

dispatcher.add_handler(CommandHandler('update', update), group=1)

# process every message depending on what the user is doing (needs to be of lowest priority possible)
def process_msg(update, context):
    # for easier access to user_id
    user_id = update.message.from_user.id

    user_data = context.user_data # for easier access to user_data
    permissions = context.user_data['permissions'] # find permissions of this user

    # if the user is trying to give feedback
    if user_data['status']['feedback']:
        for coder in coders:
            context.bot.send_message(chat_id=coder, text=update.effective_message.text)
        update.effective_message.reply_text(text=feedback_given_msg)
        user_data['status']['feedback'] = False
        user_data['status']['action'] = False
    
    elif bool(user_data['status']['add_event']):
        process_add_event(update, context, user_data)

    elif bool(user_data['status']['add_teaching']):
        process_add_teaching(update, context, user_data)

dispatcher.add_handler(MessageHandler(Filters.text, process_msg), group=1)

##############
# FIXED JOBS #
##############

# collect confirmation every week on Thursday 1800hrs
def collect_cfmation(context: telegram.ext.CallbackContext):
    # collect confirmation
    chat_id = dispatcher.bot_data['chat_id']
    dispatcher.bot.send_message(chat_id= chat_id, text=cfmation_msg)
cfmation_collector = jobqueuer.run_repeating(callback=collect_cfmation, interval=datetime.timedelta(days=7),\
first=getDatetimeOfNextXDay(isoweekday=4, hour=18))

# daily send msg for daily events
def remind_events(context: telegram.ext.CallbackContext):
    dispatcher.bot.send_message(chat_id = 333647246, text='UPDATE ATTEMPED') # NEW ADDED
    # send reminders or remove events accordingly to every user registered as a member
    daily_events_update(dispatcher)

event_reminder = jobqueuer.run_daily(callback=remind_events,\
    time=manual_convert_SGT(datetime.time(8, 0, 0, 0)))

# send a message to people that inputted an invalid command (lowest priority)
@send_typing_action
def unknown(update, context):
    update.message.reply_text(text='That\'s not a real command fool!')
dispatcher.add_handler(MessageHandler(Filters.command, unknown), group=1)



print('polling')
# to start the bot
updater.start_polling()