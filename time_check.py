'''
This is v2.3 of time_check class file
It is used to check for most processes having to do with dates including storing
of dates and info events.
'''
class Time_Checker():

    def __init__(self, telebot):
        self.remindlist = []
        self.reminddict = {}
        self.deletelist = []
        self.event_count = 1
        self.cur_add_event = ''
        self.eventlist = ''
        self.today = None
        self.telebot = telebot

    # sort the remind dict by order of index
    def sort_reminddict(self):
        l = list(self.reminddict.values())
        l.sort()
        l = tuple(l)
        i = 1
        for value in l:
            self.reminddict[i] = value
            i += 1

    # make changes according to the day (to be called at the beginning of the day)
    def update_day(self, today):
        for key in tuple(self.reminddict.keys()):
            if (self.reminddict[key][0]-today).days == 3:
                for member in self.telebot.members.values():
                    self.telebot.send_msg(member, 'Reminder:\n{}'.format(self.reminddict[key][2]))
            elif (self.reminddict[key][0]-today).days == 1:
                for member in self.telebot.members.values():
                    self.telebot.send_msg(member, 'Reminder: {} is tomorrow!'.format(self.reminddict[key][1]))
            elif (self.reminddict[key][0]-today).days < 0:
                # informs me which ones its gonna delete
                self.deletelist.append(key)
                self.telebot.send_coders('This event:\n{}\n\nis over and will be deleted.'.format(self.reminddict[key][1]))
        if self.deletelist != []:
            for key in tuple(self.deletelist):
                self.reminddict.pop(key, None)
            self.deletelist = []
            self.update_reminddict_txt()

    # sends the event list to the chat_id
    def send_eventlist(self, chat_id):
        if self.reminddict == {}:
            self.telebot.send_msg(chat_id, 'event list is empty (sadly)')
        else:
            self.sort_reminddict()
            for event in self.reminddict.values():
                self.eventlist += event[2]
            self.telebot.send_msg(chat_id, '{}'.format(self.eventlist))
            self.eventlist = ''

    # update the remind dict txt file
    def update_reminddict_txt(self):
        with open('/home/ollayf/ALPHAbot_beta/reminddict.txt', 'w') as t:
            t.write(str(self.reminddict))
            t.close()
