'''
This is v2.3 of the main telegram_chatbot class that stores all the important class functions like sending messages and administrative information.
'''
import requests

class Telegram_Chatbot():

    def __init__(self, token):
        self.token = token
        self.base = 'https://api.telegram.org/bot{}'.format(self.token)
        self.last_msg = None
        self.cur_convo_id = None
        self.cur_chat_id = None
        self.admins = {'Hosea': 333647246, 'Ivan': 299385070, 'Yi Han': 447584594, 'Zames': 113200946}
        self.members = {}
        self.coders = [333647246]
        self.var = None
        self.debug = False
        self.adminmenu = False
        self.delevent_mode = False
        self.feedback = False
        self.confirm_message = False
        self.broadc_mode = False
        self.autosleep_min = None

    # sends a request to delete entries using inbuilt api offset function
    def get_updates(self, offset=None):
        url = self.base + '/getUpdates?timeout=100&offset={}'.format(offset)
        requests.get(url)

    # gets the data of the last update
    def last_update(self):
        url = self.base + '/getUpdates?timeout=100'
        response = requests.get(url).json()
        result = response['result']
        total_updates = len(result) - 1
        return result[total_updates]

    # send message to chat_id
    def send_msg(self, chat_id, msg):
        url = self.base + "/sendMessage?chat_id={}&text={}".format(chat_id, msg)
        if msg is not None:
            requests.get(url)

    # broadcasts message to everybody
    def broadcast_msg(self, chat_id, msg):
        for member_id in self.members.values():
            self.send_msg(member_id, msg)
        self.send_msg(chat_id, 'message broadcasted to all members. Going back to adminmenu.')

    # sending messagers to all coders
    def send_coders(self, msg):
        for coder in self.coders:
            self.send_msg(coder, msg)
    
    # updates the members dictionary
    def update_members(self, name, person_id):
        self.members[name] = person_id
        self.send_coders('Updated dict: {}'.format(self.members))
        with open('members.txt', 'w+') as t:
            t.write(self.members)