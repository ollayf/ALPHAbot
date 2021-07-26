import datetime
from pytz import timezone
from functools import wraps
import telegram
import os
import threading
import time
from telegram import ParseMode
from envs import *
import logging
import requests
import re

# deprecated
# def get_input(question, success_msg=False, fail_msg=False, cancel_msg=False, boolean=True):
#     '''
#     Ask the user the question
#     :param question: The question to ask the user
#     :param boolean: Whether the options are bolean, i.e. y/n
#     :param success_msg: Optional message to print if there is a success
#     :param fail_msg: Optional message to print if answer is no
#     :param cancel_msg: Optional message to send if the question is cancelled
#     '''
#     confirmed = False
#     question += '\n'
#     while not confirmed:
#         answer = input(question)
        
#         if answer == 'y':
#             confirmed = True
#             answer = True
#             if bool(success_msg):
#                 print(success_msg)
        
#         elif answer == 'n':
#             confirmed = True
#             answer = False
#             if bool(fail_msg):
#                 print(fail_msg)
        
#         else:
#             print('invalid input. Please just input y or n')
#     return answer

            
def menu_is_open(user_data):
    '''
    If a new menu is added, change this function and the next only
    Returns True if a menu is open otherwise, return False
    '''
    if user_data['status']['admin_menu'] or user_data['status']['backend'] \
        or user_data['status']['cfm_settings']:
        return True
    else:
        return False

def close_all_menus(user_data):
    '''
    Closes all menus in the conversation
    If a new menu is added, change this function and the next only
    '''
    user_data['status']['admin_menu'] = False
    user_data['status']['backend'] = False
    user_data['status']['cfm_settings'] = False
    user_data['status']['bday_settings'] = False


def clear_user_memory(user_data, end=False, quit=False):
    '''
    in an event such as ending the bot, reset all the attributes of the user to default
    '''
    status = user_data['status']
    status['feedback'] = False
    status['action'] = False
    status['add_event'] = 0
    status['add_teaching'] = 0

    user_data['temp_list'] = []
    user_data['temp_string'] = ''

    # if end, clear everything includes quit
    if end:
        status['started'] = False
        status['admin_menu'] = False
        status['backend'] = False
        close_all_menus(user_data)
    
    # quits without ending
    elif quit:
        close_all_menus(user_data)

def manual_convert_SGT(dateTime):
    '''
    Manually converts datetime objects to UTC timing to be taken in by ptb
    '''
    assert isinstance(dateTime, (datetime.datetime, datetime.time)), \
        'Must be datetime.time or datetime.datetime obj'
    assert dateTime.tzinfo == None, 'Must be a naive datetime.time or datetime.datetime object!'
    # if it is a datetime.datetime obj
    if isinstance(dateTime, datetime.datetime):
        diff = datetime.timedelta(hours=8)
        dateTime -= diff
    # else if it is a datetime.time obj
    else:
        hour = dateTime.hour - 8
        # account for if the hour is a value less than 8
        if hour < 0:
            hour = 24 - hour
        dateTime = dateTime.replace(hour=hour)
    # returns the converted times
    return dateTime

def getDatetimeOfNextXDay(isoweekday, hour):
    '''
    Returns a datetime.datetime object with time zone of Singapore, at 0000 hours
    of the date of the iso weekday
    timezone is the timezone we are at as recorded by pytz package
    hour is the hour of the day the time will be set on
    isoweekday value is an integer value corresponding to the day of the week
    e.g. Monday = 1, Sunday = 7
    '''
    assert isinstance(isoweekday, int), 'isoweekday must be an integer!'
    assert 1 <= isoweekday <= 7, 'isoweekday must be between 1 and 7!'

    today = datetime.datetime.now()
    days_ahead = isoweekday - today.isoweekday()
    if days_ahead < 0: # Target day already happened this week
        days_ahead += 7
    date = today + datetime.timedelta(days=days_ahead)
    dateTime = datetime.datetime(date.year, date.month, date.day, hour, 0, 0)
    dateTime = manual_convert_SGT(dateTime)
    return dateTime
    
def get_next_day(hour):
    '''
    gets the format of the next day to be passed into the script in local SG timezone
    :param hour: the hour of the next day that is required
    :return: the datetime.datetime object corresponding to the given time of tomorrow
    '''

    today_isoweekday = datetime.datetime.now().isoweekday()
    # normally, just add one to get the next day
    if today_isoweekday < 7:
        tmr_isoweekday = today_isoweekday + 1
    # if the value is 7, convert the next day to be 0
    else:
        tmr_isoweekday = 1
    
    tmr_dateTime = getDatetimeOfNextXDay(tmr_isoweekday, hour)
    return tmr_dateTime
    
def get_key_from_value(value, dictionary):
    '''
    Gets the key that has a value value in the dictionary
    returns None if such values doesn't exist
    '''
    for key in tuple(dictionary.keys()):
        if dictionary[key] == value:
            return key

    return None

def parseMD(file, dict=False):
    '''
    This function parses the information out of md/ textfiles
    Returns the content of the file
    '''
    path = os.path.join('storage', file)
    with open(path, 'r') as f:
        result = f.read()
    if dict:
        result = eval(result)
    return result

def updateMD(file, data):
    '''
    This functions updates the md/ textfile whenever a change is made in case the server 
    is shut down for maintenance
    '''
    path = os.path.join('storage', file)
    if type(data) != str:
        data = str(data)
    with open(path, 'w+') as f:
        f.write(data)


def send_typing_action(func):
    '''Sends typing action while func command.
    Just: 
    @send_typing_action
    def my_handler(update, context):
        pass
    '''
    
    @wraps(func)
    def typing_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id, \
            action=telegram.ChatAction.TYPING)
        return func(update, context)

    return typing_func

def check_for_personal_changes(update, context):
    '''
    Checks for and make changes for the person for their:
    - permissions changes
    '''
    # only carries on if there are changes in permissions
    if not context.bot_data['permissions_changed'] == []:
        user_id = update.message.from_user.id # gets the user_id
        # checks through the list of permission changes to see if user is one
        for id in context.bot_data['permissions_changed']:
            # changes permissions to the important users
            if int(id) == int(user_id):
                context.bot_data['permissions_changed'].remove(id)
                new_perms = get_user_permissions(user_id, context)
                context.user_data['permissions'] = new_perms
                update.message.reply_text(text='You have been changed to permissions level: {}'.format(new_perms))


def sort_events_dict(events_dict):
    '''
    This function sorts the dictionary taken as an argument according the the its keys
    It works only if the values are lists AND
    the keys are integers
    '''
    l = list(events_dict.values())
    l.sort()
    sorted_dict = dict()
    key = 1
    for value in l:
        sorted_dict[key] = value
        key += 1
    return sorted_dict

def get_user_permissions(user_id, context):
    '''
    Given the context and user_id, get the permissions level of the user
    '''
    bot_data = context.bot_data
    if bot_data['coders'].__contains__(user_id):
        permissions = 'coders'
    elif tuple(bot_data['admins'].values()).__contains__(user_id):
        permissions = 'admins'
    elif tuple(bot_data['bday_ICs'].values()).__contains__(user_id):
        permissions = 'bday_IC'
    elif tuple(bot_data['cfm_ICs'].values()).__contains__(user_id):
        permissions = 'cfm_IC'
    else:
        permissions = 'members'
    return permissions
        
def time_function(fn):
    '''
    This function is meant to be a decorator to time any function that is happening
    Prints the time taken to complete function in second(s)
    '''
    def timer(*args, **kwargs):
        start = time.time()
        # run the function
        fn(*args, **kwargs)
        end = time.time()
        time_taken = end - start
        print(time_taken)
    return timer
    
def set_user_data_to_default(update, context, default_user_data):
    '''
    Recursively sets user_data of this user to default user_data
    '''
    assert isinstance(default_user_data, (dict, defaultdict)), \
        'default user data must be a defaultdict or dict'
    # recursively add the attributes of the dictionary
    for key in default_user_data.keys():
        # make the list or dictionary immutable
        if isinstance(default_user_data[key], (dict, list)):
            context.user_data[key] = default_user_data[key].copy()
        else:
            context.user_data[key] = default_user_data[key]


def initiate_user(user_id, update, context):
    '''
    Set ups the important information for each user that hasn't been initiated yet
    '''
    username = update.message.from_user.username
    # use first name if the user doesn't have a username
    if username == None:
        username = update.message.from_user.first_name

    # for people that are not yet members in bot_data
    if not tuple(context.bot_data['members'].values()).__contains__(user_id):
        context.bot_data['members'][username] = user_id

        # sends a message to the coders when someone is initiated nbv   
        for coder in context.bot_data['coders']:
            context.bot.send_message(chat_id=coder, text=f'{user_id} added to list of members as {username} with \
permissions {context.user_data["permissions"]}.')
    
    # initiate user
    if context.user_data == {}:
        # create default user_data for this user
        set_user_data_to_default(update, context, default_user_data.copy())
        # give permissions
        context.user_data['permissions'] = get_user_permissions(user_id, context)
        # pms the person briefly about the role of alphabot
        context.bot.send_message(chat_id=update.effective_message.from_user.id, \
                        text=first_use)
        
        # initiates the username, user_id, group_id
        context.user_data['username'] = username
        context.user_data['user_id'] = user_id
        context.user_data['group_id'] = context.bot_data['chat_id']


# in the future for multiple groups
# def get_users_group_id(update, context):
#     member_ids = context.bot_data['members'].values()
#     if member_ids.__contains__()

def process_add_event(update, context, user_data):
    '''
    Processes the whole adding and deleting of events
    '''
    # gets the title
    if user_data['status']['add_event'] == 1:
        # bolds the title
        title = f'<b>{update.message.text}</b>\n'
        # resets the temp list in case
        user_data['temp_list'] = ['date', title, title]
        update.message.reply_text(text=add_event_1)
        user_data['status']['add_event'] = 2
    # gets the description
    elif user_data['status']['add_event'] == 2:
        description = f'<b>Description:</b> {update.message.text}\n'
        user_data['temp_list'][2] += description
        update.message.reply_text(text=add_event_2)
        user_data['status']['add_event'] = 3
    # gets the location
    elif user_data['status']['add_event'] == 3:
        location = f'<b>Location:</b> {update.message.text}\n'
        user_data['temp_list'][2] += (location)
        update.message.reply_text(text=add_event_3)
        user_data['status']['add_event'] = 4
    # gets the date and time 
    elif user_data['status']['add_event'] == 4:
        try:
            # try to convert the info into the correct format
            date = update.message.text.split(',')[0].split('-')
            day, month, year = int(date[0]), int(date[1]), int(date[2])
            event_date = datetime.date(year, month, day)
            days_left = (event_date - datetime.date.today()).days
            if days_left <= 3:
                update.message.reply_text(text='Event is less than 3 days away, reminder will be \
sent out 1 day before the event!')
            else:
                update.message.reply_text(text='Reminders for this event will be sent out 3 days \
before the event')
        except:
            # if wrong format let them try again
            update.message.reply_text(text=add_event_fail)
            return

        
        user_data['temp_list'][0] = event_date
        date_time = f'<b>Datetime:</b> {update.message.text}'
        user_data['temp_list'][2] += date_time
        user_data['status']['add_event'] = 0
        # add into the events dictionary
        key = 1
        while context.bot_data['events'].keys().__contains__(key):
            key += 1
        context.bot_data['events'][key] = user_data['temp_list']
        # reset temp list
        clear_user_memory(user_data)
        update.message.reply_text(text=add_event_fin)
    
    # for adding whole event
    elif user_data['status']['add_event'] == 5:
        event_name = update.message.text.split('\n')[0] # passed in as index [1]
        event_name = f'<b>{event_name}</b>' # add the bolding to the event name
        # try to get date from whole event
        try:
            # try to get the date out of the 
            date = update.message.text.split('\n')[3].split()[1].split(',')[0].split('-')
            day, month, year = int(date[0]), int(date[1]), int(date[2])
            event_date = datetime.date(year, month, day) # passed in as index [0]
            days_left = (event_date - datetime.date.today()).days
            if days_left < 3:
                update.message.reply_text(text='Event is less than 3 days away, reminder \
                will be sent out 1 day before the event!')
            else:
                update.message.reply_text(text='Reminders for this event will be sent out \
                3 days before the event')
            # try converting the event into the bolded HTML parse format
            event = convert_to_bold(update.message.text, True, event_name) # passed in as index [2]

        except Exception as e:
            bot_print(update, e)
            bot_print(update, type(e))
            update.message.reply_text(text='adding whole event cancelled cos of wrong format. Check /eventlist out or just use /addevent if you dk')
            user_data['status']['add_event'] = 0
            raise

        else: # if the try block doesn't run into error

            # add into the events dictionary
            key = 1
            while tuple(context.bot_data['events'].keys()).__contains__(key):
                key += 1
            context.bot_data['events'][key] = [event_date, event_name, event]
            # reset settings
            clear_user_memory(user_data)
            update.message.reply_text(text=add_teaching_fin)

    # for deleting events
    elif user_data['status']['add_event'] == -1:
        # check if the input is an integer
        try:
            key = int(update.message.text)
        except Exception:
            update.message.reply_text(text=not_integer_error)
            return
        
        # if the key is part of this dictionary
        if not tuple(context.bot_data['events'].keys()).__contains__(key):
            update.message.reply_text(text=out_of_range_error)
            return
        
        # if the key is part of the dictionary
        else:
            event_name = context.bot_data['events'][key][1]
            context.bot_data['events'].pop(key)
            clear_user_memory(user_data)
            update.message.reply_text(text=del_event_fin.format(event_name), \
            parse_mode= ParseMode.HTML)
    
def convert_to_bold(text: str, event=False, event_name=None):
    '''
    converts a text in a string to bold in HTML format
    '''
    assert isinstance(text, str), 'text must be a str'

    if event:
        full_event = []
        assert event_name != None, 'if event is True, name must not be None!'
        lines = text.split('\n')[1:]
        # split up the lines into strings
        for line in lines:
            # split the lines up into lists 
            words = line.split()
            tag = words[0]
            tag = f'<b>{tag}</b>'
            words[0] = tag
            line = ' '.join(words)
            full_event.append(line)
        # put everything back together
        full_event = '\n'.join(full_event)
        full_event = f'{event_name}\n{full_event}' # add the event name back in
        return full_event
            


def process_add_teaching(update, context, user_data):
    '''
    Processes the whole adding and deleting of teachings in the library
    '''

    if user_data['status']['add_teaching'] == 1:
        # resets the string in case it is being used
        user_data['temp_string'] = f'{update.message.text}\n'
        user_data['status']['add_teaching'] = 2
        update.message.reply_text(text= add_teaching_1)
    
    elif user_data['status']['add_teaching'] == 2:
        teaching_str = user_data['temp_string'] + update.message.text
        # if the limit is reached delete the oldest teaching
        limit = context.bot_data['library']['limit']
        if len(tuple(context.bot_data['library']['teachings'].keys())) >= limit:
            remove_teaching(update, context, 1)
            update.message.reply_text(text= add_teaching_limit.format(limit))
        
        # process to add the teaching into bot_data
        new_teaching_index = len(context.bot_data['library']['teachings']) + 1
        context.bot_data['library']['teachings'][new_teaching_index] = teaching_str

        # reset temp string
        clear_user_memory(user_data)
        update.message.reply_text(text= add_teaching_fin)
    
    elif user_data['status']['add_teaching'] == -1:
        # check if the message is a single integer
        try:
            delete_index = int(update.message.text)
        except:
            update.message.reply_text(text= add_teaching_fin)
        
        # removes the teaching and sorts the library
        completed = remove_teaching(update, context, delete_index)
        clear_user_memory(user_data)
        if completed:
            update.message.reply_text(text=del_teaching_fin.format(delete_index))

def remove_teaching(update, context, teaching_index):
    '''
    Deals with the clean removal and resorting of the library when a teaching is removed
    '''
    highest_index = len(context.bot_data['library']['teachings'])
    # check if the chosen teaching is within the limit of the dictionary
    if not 1 <= teaching_index <= highest_index:
        update.message.reply_text(text=out_of_range_error)
        return False
    
    else:
        # pushes everything after the teaching to be deleted down
        highest_index = len(context.bot_data['library']['teachings'].keys())
        key = teaching_index
        while key < highest_index:
            context.bot_data['library']['teachings'][key] = \
                context.bot_data['library']['teachings'][key + 1]
            key += 1
        context.bot_data['library']['teachings'].pop(highest_index, None)
        return True

def bot_print(update, text):
    '''
    replies a certain msg to the sender
    '''
    if type(text) != str:
        text = str(text)
    update.message.reply_text(text=text)

def convert_dict_to_str(relevant_dict, teaching= False):
    '''
    Converts the events in the bot_data into a string to be displayed
    '''
    displayed = '' 
    if teaching:
        for key in relevant_dict.keys():
            displayed += f'<b>{key}.</b> {relevant_dict[key]}\n\n'
    else:
        for key in tuple(relevant_dict.keys()):
            event = relevant_dict[key]
            event_displayed = f'{key}. {event[2]}\n\n'
            displayed += event_displayed
    return displayed

def create_menu(commands_dict, menu):
    '''
    Converts the commands dict into a menu (str) to be sent to the user
    '''
    assert tuple(commands_dict.keys()).__contains__(menu), 'Input menu is not valid'
    base_menu = commands_dict[menu]['base_menu']
    commands_dict = commands_dict[menu]
    displayed_menu = f'{base_menu}\n\n'
    for key in commands_dict:
        # ignore the base_menu
        if key == 'base_menu':
            continue
        # add partitions in the menu for easier viewing
        elif key.__contains__('part'):
            displayed_menu += f'<u><b>{commands_dict[key]}</b></u>\n'
        else:
            # create a menu based on the keys and values
            displayed_menu += f'/{key} -- {commands_dict[key]}\n'
    
    return displayed_menu

def daily_events_update(context):
    '''
    The update that is run daily at 8am to send out reminders or remove events where necessary
    '''
    # get a tuple of members
    member_ids = tuple(context.bot_data['members'].values())
    # easier access to events dict
    events_dict = context.bot_data['events']
    # get the datetime.datetime object for today
    today = datetime.date.today()
    for key in tuple(events_dict.keys()):
        # send a detailed reminder to all members 3 days prior to the event
        if (events_dict[key][0] - today).days == 3:
            for member_id in member_ids:
                context.bot.send_message(chat_id=member_id,\
                    text='<b>Reminder:</b>\n\n{}'.format(events_dict[key][2]), parse_mode=ParseMode.HTML)
        # send a summarised reminder to all members 1 day prior to the event
        elif (events_dict[key][0] - today).days == 1:
            for member_id in member_ids:
                context.bot.send_message(chat_id=member_id,\
                    text= '<b>Reminder:</b> {} is tomorrow!'.format(events_dict[key][1]),\
                        parse_mode = ParseMode.HTML)
        # deletes the event if it is over
        elif (events_dict[key][0] - today).days < 0:
            # informs me which ones its gonna delete
            coders_msg = 'This event: {} is over and will be deleted.'.format(events_dict[key][1])
            events_dict.pop(key)
            for coder_id in tuple(context.bot_data['coders']):
                context.bot.send_message(chat_id= coder_id, text=coders_msg, parse_mode=ParseMode.HTML)
    
    # after every day

def process_url(update, url):
    '''
    Gets the relevant platform from the url
    '''
    try:
        requests.get(url)
    # fails if the request cannot be sent
    except Exception:
        update.effective_message.reply_text(text=invalid_call_url)
        raise

    else:
        if url.__contains__('zoom.us'):
            platform = 'Zoom'
        
        elif url.__contains__('discord.gg'):
            platform = 'Discord'
        
        elif url.__contains__('join.skype.com'):
            platform = 'Skype'
        
        else:
            platform = None
        
        return platform

# if __name__ == '__main__':
#     event = convert_to_bold('Ytd\nDes: des pa cito que\nLoc: loc\nDT: dt', True, '<b>title</b>')
#     print(event)

def menu_activated(user_data):
    '''
    Checks if any menu is currently activated
    Returns True if it is and False if it isn't
    '''
    menus = ['admin_menu', 'backend', 'confirmation', 'birthday']
    status_dict = user_data['status']
    result = False
    # checks if any of the menus are accessed currently
    for menu in menus:
        # if this condition is never invoked, result will return False
        if status_dict[menu]:
            result = True

    return result

def check_permission(auth, requirement):
    '''
    Checks if the permission level of the user is sufficient for the action
    Returns True if allowed, False if not
    '''
    power_level = {
        'coders': 20,
        'admins': 10,
        'bday_IC': 2,
        'cfm_IC': 2,
        'members': 1
    }
    logging.info(f'{auth}')
    assert tuple(power_level.keys()).__contains__(auth), 'User Perms not exist'
    assert tuple(power_level.keys()).__contains__(requirement), 'Reqm Perms not exist'

    # to be returned
    result = False
    if auth == requirement:
        result = True
    
    elif power_level[auth] > power_level[requirement]:
        result = True

    else:
        result = False

    return result

def is_chat_id(chat_id, return_type=False):
    '''
    Checks if a string, int entered is a chat_id
    :param return_type: True or False value Whether you want to get the type of chat id this is
    Returns False if it isnt and True if it is
    '''
    result = False
    
    # converts it into str if it is not alr a str
    if not isinstance(chat_id, str):
        id_str = str(chat_id)
    else:
        id_str = chat_id
    
    # checks
    if len(id_str) == 14 and id_str[0] == '-':
        result = True
        id_type = 'chat'
    
    elif len(id_str) == 9:
        result = True
        id_type = 'user'

    else:
        id_type = None

    # check if it can be an integer
    try:
        int(chat_id)
    except ValueError:
        result = False
    
    if return_type:
        return result, id_type
    else: 
        return result

# Deprecated
# # Initiating bot functions
# def reset_bot(password=False):
#     '''
#     Checks if the user wants to reset the bot
#     Returns True if the bot is reset else False
#     '''
#     result = False
#     # only asks the user if there is a saved state
#     if os.path.isfile(PICKLE_FILE):
#         if get_input('Do you want to reset the bot? y/n', False, 'Ok carrying on last saved version'):
#             if get_input('Are you sure you want to reset it?', 'Bot is being reset', 'Phew close one ay?'):
#                 os.remove(PICKLE_FILE)
#                 result = True
#     return result

    
def update_bot_data(bot_data):
    '''
    Used to update variables in the bot other than the persistent variables
    - cfm
    - library
    - events
    - birthday
    '''

    for key in tuple(default_bot_data.keys()):
        if key in PERSISTENT_VARS:
            continue
        else:
            # ensure protection for mutable objects
            if isinstance(default_bot_data[key], (list, dict)):
                bot_data[key] = default_bot_data[key].copy() 
            else: 
                bot_data[key] = default_bot_data[key]
        
    print(f'Bot successfully updated excluding {PERSISTENT_VARS}')

def get_bot_info(version_updates):
    '''
    Used to parse the version updates file to get the current version of ALPHAbot and its patch notes
    returns the bot version as a string
    '''
    section = 0
    patch_notes = ''
    with open(version_updates, 'r') as updates:
        lines = updates.readlines()
        for line in lines:
            # stops after it reaches the end of this version section
            if section == 2:
                break
            elif '=' in line:
                section += 1
                # gets the version number from this line
                if section == 1:
                    version_number = re.findall('\d.\d.\d', line)[0]
                    patch_notes = f'<u>ALPHAbot Version {version_number} Patch Notes:</u>\n'
                continue
            # skip lines that are empty
            elif line.split() == []:
                continue
            elif line.split()[0] == '-':
                info = '<b>' + ' '.join(line.split()[1:]) + '</b>\n'
                patch_notes += info

    print('Version number: ', version_number)
    print('Patch notes: ', patch_notes)

    return version_number, patch_notes