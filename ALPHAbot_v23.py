''' This is the ALPHAbot v2.3, created for NS-Alpha LG to assist in administration for the entire lifegroup
This is mainly done so by:
    1. Storing upcoming events
    2. Giving timely reminders as these events are approaching
    3. Storing recent sermons that LG members may have missed
    4. Sending broadcasts to all members via pm
    5. Staying cool while doing all these
'''


import time
from datetime import date, timedelta, datetime
from messages import *

# importing the classes
from bot import Telegram_Chatbot
from time_check import Time_Checker
from misc import Misc

# select bot token to be used
token = testing_token

# create instances of the classes
bot = Telegram_Chatbot(token)
timer = Time_Checker(bot)
misc = Misc(bot)

def override():
    bot.autosleep_min = None
    bot.cur_convo_id = None
    bot.cur_chat_id = None
    bot.adminmenu = False
    bot.debug = False
    bot.var = None
    timer.cur_add_event = ''
    bot.delevent_mode = False
    bot.feedback = False
    bot.confirm_message = False
    bot.broadc_mode = False
    misc.del_teachingmode = False
    misc.clear_teachingmode = False
    

# The infinite loop which the server must run 24/7

def check():
    while True:
        # while in sleep mode
        if bot.cur_convo_id == None:
            time.sleep(3)
            today = date.today()
            if today != timer.today:
                timer.today = today
                timer.update_day(timer.today)

        # when bot has been activated
        else:
            time.sleep(0.5)

        # bot goes to sleep automatically after 15 mins of being started up, person is logged out
        if bot.autosleep_min != None:
            if datetime.now().minute == bot.autosleep_min:
                bot.send_msg(bot.cur_convo_id, '15 minutes is up, I will automatically be going to \
                sleep. Next time please remember to end me when not in use.\nYou can also use /eventlist\
                or /teaching list without starting me up.')
                override()

        # in the case there are no updates on the api or the api is erased at certain intervals
        try :
            update = bot.last_update()
            last_msg_id = update['message']['message_id']
        except:
            continue

        #only proceed if the newest message is distinct
        if last_msg_id != bot.last_msg:
            bot.last_msg = last_msg_id

            # getting the important information
            chat_id = update['message']['chat']['id']
            person_id = update['message']['from']['id']
            name = update['message']['from']['first_name']

            #automatically add members in the chat when they say something in chat
            if person_id not in bot.members.values():
                bot.update_members(name, person_id)
            offset = update['update_id'] - 10
            bot.get_updates(offset)

            # in case of recordings or videos
            try:
                text = update['message']['text']
            except:
                if person_id == bot.cur_convo_id:
                    bot.send_msg(chat_id, 'can\'t read dat shit fool')
                return check()

            '''--------------------------------------------------------
               Special cases that do not require bot to be activated
            --------------------------------------------------------'''

            # in case there is an ongoing call, otherwise this will be ignored
            misc.check_if_call_started(text, chat_id)
            misc.alert_ongoing_call(text, chat_id)

            # coder override
            if text == '/override':
                if person_id in bot.coders and bot.cur_convo_id != \
                    chat_id:
                    override()
                    bot.send_msg(chat_id, 'rekt that n00b')
                else:
                    bot.send_msg(chat_id, 'you have no power here!')
                return check()

            # coder check current convo
            elif text == '/curconvo' and bot.cur_convo_id != chat_id:
                if bot.coders.__contains__(person_id):
                    if bool(bot.cur_convo_id) == False:
                        bot.send_msg(chat_id, 'talking to no one rn lol')
                        return check()
                    else:
                        bot.send_msg(chat_id, str(bot.cur_convo_id))
                        return check()
                else:
                    bot.send_msg(chat_id, 'you have no power here!')
                    return check()

            # teaching quick check
            elif text == '/ALPHA_library' or text == '/ALPHA_library@LGinfo03bot':
                if misc.alpha_library != {}:
                    misc.alpha_lib(chat_id)
                else:
                    bot.send_msg(chat_id, 'Sorry, the library is currently empty, please come back again next time.')
                return check()

            # events quick check
            elif text == '/eventlist@LGinfo03bot' or text == '/eventlist':
                timer.send_eventlist(chat_id)
                return check()

            elif text == '/startALPHAbot':
                if bot.cur_convo_id == None:
                    bot.autosleep_min = (datetime.now() + timedelta(minutes = 15)).minute
                    bot.cur_convo_id = person_id
                    bot.cur_chat_id = chat_id
                    bot.send_msg(chat_id, 'Hello {}!\nStart inputting a command or /help for more.'.format(name))
                    return check()
                else:
                    if person_id != bot.cur_convo_id:
                        bot.send_msg(chat_id, 'HAHA loser! I\'m currently having a convo with {}.\nYou can still use /eventlist and /ALPHA_library tho.')
                    else:
                        bot.send_msg(chat_id, 'Bruh im alr currently in a convo with you?!?!??!??!')
                    return check()


            # only proceed to main fn if the user alr started a convo with the bot
            elif person_id == bot.cur_convo_id:
                return main(chat_id, text, name, person_id)

            else:
                return check()

def main(chat_id, text, name, person_id):

    #access debug function
    if bot.debug == True:
        return debug(chat_id, text, name, person_id)

    #access confirm clear message
    elif bot.confirm_message == True or misc.clear_teachingmode == True:
        return confirm_clear(chat_id, text, name, person_id)

    #access adminmenu function
    elif bot.adminmenu == True:
        return admin(chat_id, text, name, person_id, timer.today)

    #access feedback function
    elif bot.feedback == True:
        bot.send_coders(text)
        bot.send_msg(chat_id, 'lol k thanks yu fei will read and consider your feedback')
        bot.feedback = False
        bot.send_msg(chat_id, help_msg)
        return check()

    # only entertain if it is in the same chat
    elif bot.cur_chat_id == chat_id:

        # activate debug mode
        if text == '/troubleshoot':
            if person_id in bot.coders:
                bot.send_msg(chat_id, 'time to find some bugs')
                bot.debug = True
                return check()
            else:
                bot.send_msg(chat_id, 'you have no power here!')
                return check()

        # activate adminmenu
        elif text == '/adminmenu@LGinfo03bot' or text == '/adminmenu':
            if person_id in bot.admins.values():
                bot.adminmenu = True
                bot.send_msg(chat_id, 'admin menu activated')
                bot.send_msg(chat_id, admin_msg.format(name))
                return check()
            else:
                bot.send_msg(chat_id, 'you have no power here!')
                return check()

        # normal access commands
        elif text == '/help@LGinfo03bot' or text == '/help':
            bot.send_msg(chat_id, help_msg)
            return check()

        elif text == '/end@LGinfo03bot' or text == '/end':
            bot.cur_convo_id = None
            bot.autosleep_min = None
            bot.send_msg(chat_id, 'Going to sleep')
            return check()

        elif text == '/feedback@LGinfo03bot' or text == '/feedback':
            bot.feedback = True
            bot.send_msg(chat_id, 'what is your problem with me?')
            return check()
        
        elif text == '/end_call@LGinfo03bot' or text == '/end_call':
            if bot.admins.values().__contains__(person_id):
                if misc.ongoing_call_app != '':
                    misc.ongoing_call_app = ''
                    misc.ongoing_call_reminder = None
                    bot.send_msg(chat_id, 'Call has been ended. Reminders cancelled')
                else:
                    bot.send_msg(chat_id, 'There is no call currently ongoing. Wake up\
                        your idea pls.')
            else:
                bot.send_msg(chat_id, 'Access denied.')

        # to simulate an error
        elif text == '/error':
            crash = 1 // 0

        # to be safe in case of any random unexpected cases
        else:
            return check()

    else:
        return check()

def debug(chat_id, text, name, person_id):
    if text == '/reminddict@LGinfo03bot' or text == '/reminddict':
        bot.send_msg(chat_id, '{}'.format(timer.reminddict))
        return check()
    elif text == '/admins@LGinfo03bot' or text == '/admins':
        bot.send_msg(chat_id, '{}'.format(bot.admins))
        return check()
    elif text == '/members@LGinfo03bot' or text == '/members':
        bot.send_msg(chat_id, '{}'.format(bot.members))
        return check()
    elif text == '/coders@LGinfo03bot' or text == '/coders':
        bot.send_msg(chat_id, '{}'.format(bot.coders))
        return check()
    elif text == '/alphalib@LGinfo03bot' or text == '/alphalib':
        bot.send_msg(chat_id, '{}'.format(misc.alpha_library))
        return check()
    elif text == '/stop@LGinfo03bot' or text == '/stop':
        bot.send_msg(chat_id, 'stopping')
        bot.debug = False
        return check()
    elif text == '/today@LGinfo03bot' or text == '/today':
        bot.send_msg(chat_id, '{}'.format(str(timer.today)))
        return check()

    elif '/removemember' in text:
        member = text.split(':')[1]
        if member in bot.members.keys():
            bot.members.pop(member, None)
            bot.send_msg(chat_id, 'member: {} removed from the list.'.format(member))
        else:
            bot.send_msg(chat_id, 'member {} does not exist'.format(member))
        return check()
    else:
        bot.send_msg(chat_id, coder_msg.format(name))
        return check()

def admin(chat_id, text, name, person_id, today):
    # to broadcast messages
    if bot.broadc_mode == True:
        bot.broadcast_msg(chat_id, text)
        bot.broadc_mode = False
        bot.send_msg(chat_id, admin_msg.format(name))
        return check()
    elif misc.del_teachingmode == True:
        if '/' in text:
            bot.send_msg(chat_id, 'Finish giving me all the info first can?')
            return check()

        # to cancel deleting teaching
        elif text == 'Nah':
            misc.del_teachingmode = False
            bot.send_msg(chat_id, 'k thx bai')
            bot.send_msg(chat_id, admin_msg.format(name))
            return check()

        # to delete a teaching
        else:
            try:
                deleted_index = int(text)
                if deleted_index not in misc.alpha_library.keys():
                    bot.send_msg(chat_id, "uhm... this index isn't in the library?")
                else:
                    misc.del_teaching(deleted_index,chat_id)
                bot.send_msg(chat_id, "Any other teaching to delete? type 'Nah' if otherwise")
            # text is not an integer
            except:
                bot.send_msg(chat_id, 'hello bro pls send a SINGLE number')
            return check()

    elif type(bot.var) == int:

        # to cancel any action when bot.var == True
        if text == 'Nah':
            if bot.var % 10 < 2 or (bot.var == 22 and misc.added_teaching == ''):
                bot.var = None
                bot.send_msg(chat_id, 'k thx bye')
                bot.send_msg(chat_id, admin_msg.format(name))
            else:
                bot.send_msg(chat_id, 'Too late no going back now')
            return check()

        # adding event
        elif 1 <= bot.var < 10 and '/' in text and not '2' in text:
            bot.send_msg(chat_id, 'Finish giving me all the info first can?')
            return check()
        elif bot.var == 1:
            print(timer.remindlist)
            print(type(timer.remindlist))
            timer.remindlist = [text]
            timer.remindlist.append(text)
            timer.cur_add_event += '{}. {}\n'.format(timer.event_count, text)
            bot.send_msg(chat_id, 'Short description of what it is about?')
            bot.var = 2
            return check()
        elif bot.var == 2:
            timer.cur_add_event += 'Description: {}\n'.format(text)
            bot.send_msg(chat_id, 'Where will it be held?')
            bot.var = 3
            return check()
        elif bot.var == 3:
            timer.cur_add_event += 'Location: {}\n'.format(text)
            bot.send_msg(chat_id, 'When will it be held? format: DD-MM-YYYY, TIME (dont put anyth before the date ah)')
            bot.var = 4
            return check()
        elif bot.var == 4:
        #try to get the date from the text
            # format of eventlist is [event_date, event_name, event_details]
            try:
                dateTime = text.split(',')[0].split('-')
                day, month, year = int(dateTime[0]), int(dateTime[1]), int(dateTime[2])
                event_date = date(year, month, day)
                timer.remindlist[0] = event_date
                days_left = (event_date - today).days
                if days_left < 3:
                    bot.send_msg(chat_id, 'Event is less than 3 days away, reminder will be sent out 1 day before the event!')
                else:
                    bot.send_msg(chat_id, 'Reminders for this event will be sent out 3 days before the event')
            except:
                bot.send_msg(chat_id, 'bruh cant u give the correct format? adding event cancelled')
                bot.var = None
                bot.send_msg(chat_id, admin_msg.format(name))
                return check()

            timer.cur_add_event += 'Datetime: {}\n\n'.format(text)
            timer.remindlist.append(timer.cur_add_event)
            timer.reminddict[timer.event_count] = timer.remindlist
            timer.remindlist = []
            timer.cur_add_event = ''
            bot.send_msg(chat_id, 'New event saved. Thanks for serving!')
            bot.send_msg(chat_id, admin_msg.format(name))
            bot.var = None
            timer.update_reminddict_txt()
            return check()

        #adding whole event
        elif bot.var == 11:
            timer.event_count = 1
            while timer.event_count in timer.reminddict.keys():
                timer.event_count += 1
            event_name = text.split('\n')[0]

        #try to get date from whole text
            try:
                dateTime = text.split('\n')[3].split()[1].split(',')[0].split('-')
                day, month, year = int(dateTime[0]), int(dateTime[1]), int(dateTime[2])
                event_date = date(year, month, day)
                days_left = (event_date - today).days
                if days_left < 3:
                    bot.send_msg(chat_id, 'Event is less than 3 days away, reminder will be sent out 1 day before the event!')
                else:
                    bot.send_msg(chat_id, 'Reminders for this event will be sent out 3 days before the event')
            except:
                bot.send_msg(chat_id, 'adding whole event cancelled cos of wrong format. Check /eventlist out or just use /addevent if you dk')
                bot.var = None
                bot.send_msg(chat_id, admin_msg.format(name))
                return check()

        #add to reminddict
            event = '{}. {}\n\n'.format(timer.event_count, text)
            timer.reminddict[timer.event_count] = [event_date, event_name, event]
            timer.event_count = 1
            bot.send_msg(chat_id, 'anymore whole events to add? type Nah to stop adding')
            timer.update_reminddict_txt()
            return check()

        elif bot.var == 21:
            misc.added_teaching = text + '\n'
            bot.send_msg(chat_id, 'URL for the resources?')
            bot.var = 22
            return check()

        elif bot.var == 22:
            misc.added_teaching += text
            misc.add_teaching(chat_id)
            bot.send_msg(chat_id, admin_msg.format(name))
            bot.var = None
            misc.update_teachings_txt()
            return check()

        else:
            return check()

    # delete event mode
    elif bot.delevent_mode == True:

        # to check if the text is a valid integer

        if text in str(timer.reminddict.keys()):
            try:
                key = int(text)
                timer.reminddict.pop(key, None)
                bot.send_msg(chat_id, 'event no.{} deleted, any other event to delete? Otherwise, type "Nah"'.format(text))
                timer.update_reminddict_txt()
            except:
                bot.send_msg(chat_id, 'hello bro pls send a SINGLE number')
            return check()

        elif text == 'Nah':
            bot.delevent_mode = False
            bot.send_msg(chat_id, 'going back to adminmenu')
            bot.send_msg(chat_id, admin_msg.format(name))
            return check()

        else:
            bot.send_msg(chat_id, 'pls give a valid response lol. type "Nah" to cancel deletion')
            return check()

    # normal admin commands
    else:

        if text == '/newevent@LGinfo03bot' or text == '/newevent':
            bot.var = 1
            timer.event_count = 1
            while timer.event_count in timer.reminddict.keys():
                timer.event_count += 1
            bot.send_msg(chat_id, 'what is the name of this event?')
            return check()

        elif text == '/clear_events@LGinfo03bot' or text == '/clear_events':
            bot.confirm_message = True
            bot.send_msg(chat_id, 'Are you sure you want to clear all events? To double confirm, type exactly:\n\nI am sure.\n\nOtherwise tell me if your jk(to cancel just type jk)')
            return check()

        elif text == '/endsession@LGinfo03bot' or text == '/endsession':
            bot.send_msg(chat_id, 'Session ended')
            bot.adminmenu = False
            bot.send_msg(chat_id, help_msg)
            return check()

        elif text == '/delevent@LGinfo03bot' or text == '/delevent':
            if timer.reminddict != {}:
                bot.delevent_mode = True
                bot.send_msg(chat_id, 'Which event do you want to delete? (input a single number) type "Nah" to cancel')
            else:
                bot.send_msg(chat_id, 'There are currently no events... Sending you back to adminmenu')
                bot.send_msg(chat_id, admin_msg.format(name))
            return check()

        elif text == '/addwholeevent' or text == '/addwholeevent@LGinfo03bot':
            bot.var = 11
            bot.send_msg(chat_id, 'Chop chop kali pok. Gimme that event! Type "Nah" to cancel')
            return check()


        elif text == '/addteaching' or text == '/addteaching@LGinfo03bot':
            bot.var = 21
            bot.send_msg(chat_id, 'Tell me the summary of this teaching my child. Type "Nah" to cancel.')
            return check()

        elif text == '/addwholeteaching' or text == '/addwholeteaching@LGinfo03bot':
            bot.var = 22
            bot.send_msg(chat_id, 'Gimme that teaching!')
            return check()

        elif text == '/del_teaching' or text == '/del_teaching@LGinfo03bot':
            misc.del_teachingmode = True
            bot.send_msg(chat_id, 'Which teaching (number) do you want to delete? type "Nah" to cancel')
            return check()

        elif text == '/clear_library' or text == '/clear_library@LGinfo03bot':
            misc.clear_teachingmode = True
            bot.send_msg(chat_id, 'Are you sure you want to clear all events? To double confirm, type exactly:\n\nI am sure.\n\nOtherwise tell me if your jk(to cancel just type jk)')
            return check()

        elif text == '/broadcast_msg' or text == '/broadcast_msg@LGinfo03bot':
            bot.send_msg(chat_id, 'What do you want to broadcast?')
            bot.broadc_mode = True
            return check()

        else:
            bot.send_msg(chat_id, admin_msg.format(name))
            return check()

def confirm_clear(chat_id, text, name, person_id):
    if text == 'I am sure.':
        if misc.clear_teachingmode == True:
            misc.clear_lib(chat_id)
            misc.clear_teachingmode = False
            misc.update_teachings_txt()
        else:
            timer.reminddict = {}
            bot.confirm_message = False
            bot.send_msg(chat_id, 'Cleared the eventlist')
            timer.update_reminddict_txt()

        bot.send_msg(chat_id, admin_msg.format(name))
        return check()

    elif 'jk' in text or 'Jk' in text:
        bot.send_msg(chat_id, 'whew almost made a big mistake huh?')
        bot.confirm_message = False
        misc.clear_teachingmode = False
        bot.send_msg(chat_id, admin_msg.format(name))
        return check()
    else:
        bot.send_msg(chat_id, 'Are you sure you want to clear all events? To double confirm, type exactly:\n\nI am sure.\n\nOtherwise tell me if your jk(to cancel just type jk)')
        return check()

# ALPHAbot startup
if __name__ == '__main__':
    
    # sets up the telegram bot to be used
    last_error = None

    # load the important information and store into memory
    with open('reminddict.txt', 'r') as t:
        timer.reminddict = eval(t.read())
        print(timer.reminddict)

    with open('alpha_library.txt', 'r') as t:
        misc.alpha_library = eval(t.read())

    with open('members.txt', 'r') as t:
        bot.members = eval(t.read())
        print(bot.members)

    # start the loop
    while True:
        try:
            bot.send_coders('Booting up')
            timer.today = date.today()
            check()
            # in case it exits the infinite loop
            bot.send_coders('Exiting the loop. ALPHAbot restarting')
        except Exception as e:
            bot.send_coders('{}'.format(type(e)))
            bot.send_coders('{}'.format(e))
            if last_error == e: # if the same error happens twice, exit and send a report
                bot.send_coders('same error has been made twice, the bot will now kill itself')
                break
            else:
                last_error = e
                continue

    print(last_error)

