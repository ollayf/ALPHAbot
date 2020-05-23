'''
This is v2.3 of the misc class.
It's main function is to store data and attribute functions of the misc capabilities of the bot (to be expanded on as the bot develops
'''
from datetime import date, timedelta, datetime

class Misc():

    def __init__(self, telebot):
        self.added_teaching = ''
        self.alpha_library = {}
        self.del_teachingmode = False
        self.clear_teachingmode = False
        self.telebot = telebot
        self.ongoing_call_app = ''
        self.ongoing_call_reminder = None


    def del_teaching(self, key, chat_id):
        teachings_number = len(self.alpha_library.keys())
        count = key
        while count < teachings_number:
            self.alpha_library[count] = self.alpha_library[count+1]
            count += 1
        self.alpha_library.pop(teachings_number, None)
        self.telebot.send_msg(chat_id, 'Teaching no. {} was successfully removed.'.format(key))

    def add_teaching(self, chat_id):
        # if more than 5 teachings currently
        if len(self.alpha_library.keys()) >= 5:
            self.telebot.send_msg(chat_id, 'Since there is currently more than 5, the oldest teaching will be removed from the library')
            self.del_teaching(1, chat_id)

        self.alpha_library[len(self.alpha_library.keys()) + 1] = self.added_teaching + '\n\n'
        self.added_teaching = ''
        # from telegram_chatbot
        self.telebot.send_msg(chat_id, 'New teaching added to library')

    def alpha_lib(self, chat_id):
        for key in tuple(self.alpha_library.keys()):
            self.added_teaching += '{}. {}'.format(key, self.alpha_library[key])
        self.telebot.send_msg(chat_id, '{}'.format(self.added_teaching))
        self.added_teaching = ''

    def clear_lib(self, chat_id):
        self.added_teaching = ''
        self.alpha_library = {}
        self.telebot.send_msg(chat_id, 'Alpha library cleared')

    # update the txt file
    def update_teachings_txt(self):
        with open('/home/ollayf/ALPHAbot_beta/alpha_library.txt', 'w') as t:
            t.write(str(self.alpha_library))
            t.close()

    # check if there is a call started
    def check_if_call_started(self, msg, chat_id):
        if msg.__contains__('us04web.zoom.us'):
            self.ongoing_call_app = 'Zoom'
            self.ongoing_call_last_reported = (datetime.now() + timedelta(minutes = 10)).minute
            self.telebot.send_msg(chat_id, 'A new call has been started on {}. accept the call\
            using this link:\n{}'.format(self.ongoing_call_app, msg))

    # alert of an ongoing call every 10 mins
    def alert_ongoing_call(self, msg, chat_id):
        if datetime.datetime.now().minute == self.ongoing_call_reminder:
            if self.ongoing_call_app != '':
                self.telebot.broadcast(chat_id, 'A call is currently ongoing on {}. accept the call\
                using this link:\n{}\n\nIf the call has ended, ask a CT member to type /end_call\
                '.format(self.ongoing_call_app, msg))
