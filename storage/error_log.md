2020-06-07 19:49:39,836 - root -                     INFO - members
2020-06-07 19:49:39,836 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 166, in typing_func
    return func(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 370, in cfm_settings
    if not check_permission(permissions, 'cfm_IC'):
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 624, in check_permission
    assert tuple(power_level.keys()).__contains__(auth), 'User Perms not exist'
AssertionError: User Perms not exist
2020-06-07 19:50:32,039 - root -                     INFO - members
2020-06-07 19:50:54,563 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 166, in typing_func
    return func(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 932, in make_cfm
    chat_id = int(args[0])
ValueError: invalid literal for int() with base 10: 'ollayff'
2020-06-07 20:08:00,272 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 166, in typing_func
    return func(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 936, in make_cfm
    if not is_chat_id(args[0]):
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 653, in is_chat_id
    if len(id_str) == 14 and id_str[0] == '-':
UnboundLocalError: local variable 'id_str' referenced before assignment
2020-06-07 20:09:33,235 - root -                     INFO - members
2020-06-07 20:09:50,036 - root -                     INFO - cfm_IC
2020-06-07 20:11:37,591 - root -                     INFO - members
2020-06-07 20:11:52,950 - root -                     INFO - cfm_IC
2020-06-07 20:12:29,779 - root -                     INFO - members
2020-06-07 20:13:25,280 - root -                     INFO - members
2020-06-07 20:13:56,572 - root -                     INFO - bday_IC
2020-06-11 23:15:31,405 - root -                     INFO - cfm sent to group
2020-06-11 23:20:34,447 - root -                     INFO - cfm sent to group
2020-06-11 23:28:34,590 - root -                     INFO - cfm sent to group
2020-06-12 17:44:48,646 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 198, in typing_func
    return func(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 149, in help
    update.message.reply_text(text=menu, parse_mode= ParseMode.HTML)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\message.py", line 510, in reply_text
    return self.bot.send_message(self.chat_id, *args, **kwargs)
  File "<decorator-gen-2>", line 2, in send_message
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\bot.py", line 351, in send_message
    timeout=timeout, **kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\bot.py", line 178, in _message
    result = self._request.post(url, data, timeout=timeout)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\utils\request.py", line 334, in post
    **urlopen_kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\utils\request.py", line 245, in _request_wrapper
    raise BadRequest(message)
telegram.error.BadRequest: Can't parse entities: unsupported start tag "url" at byte offset 225
2020-06-12 17:50:49,036 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 198, in typing_func
    return func(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 149, in help
    update.message.reply_text(text=menu, parse_mode= ParseMode.HTML)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\message.py", line 510, in reply_text
    return self.bot.send_message(self.chat_id, *args, **kwargs)
  File "<decorator-gen-2>", line 2, in send_message
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\bot.py", line 351, in send_message
    timeout=timeout, **kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\bot.py", line 178, in _message
    result = self._request.post(url, data, timeout=timeout)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\utils\request.py", line 334, in post
    **urlopen_kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\utils\request.py", line 245, in _request_wrapper
    raise BadRequest(message)
telegram.error.BadRequest: Can't parse entities: unsupported start tag "url" at byte offset 225
2020-06-12 17:51:38,433 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 198, in typing_func
    return func(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 149, in help
    update.message.reply_text(text=menu, parse_mode= ParseMode.HTML)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\message.py", line 510, in reply_text
    return self.bot.send_message(self.chat_id, *args, **kwargs)
  File "<decorator-gen-2>", line 2, in send_message
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\bot.py", line 351, in send_message
    timeout=timeout, **kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\bot.py", line 178, in _message
    result = self._request.post(url, data, timeout=timeout)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\utils\request.py", line 334, in post
    **urlopen_kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\utils\request.py", line 245, in _request_wrapper
    raise BadRequest(message)
telegram.error.BadRequest: Can't parse entities: unsupported start tag "url" at byte offset 218
2020-06-12 17:53:19,656 - root -                     INFO - 

/events -- shows the list of upcoming events
/library -- opens up a library of recent good teachings and articles
/start -- start a conversation with me :)
<u><b>ONLY AVAILABLE FOR ADMINS</b></u>
/start_call -- /start_call <url> to start a call. Sends a message to the group that the call is on, don't say bojio.
/end_call -- Informs me that the call is ended, aka stopping the spam

2020-06-12 17:53:20,332 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 198, in typing_func
    return func(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 153, in help
    update.message.reply_text(text=menu, parse_mode=ParseMode.HTML)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\message.py", line 510, in reply_text
    return self.bot.send_message(self.chat_id, *args, **kwargs)
  File "<decorator-gen-2>", line 2, in send_message
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\bot.py", line 351, in send_message
    timeout=timeout, **kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\bot.py", line 178, in _message
    result = self._request.post(url, data, timeout=timeout)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\utils\request.py", line 334, in post
    **urlopen_kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\utils\request.py", line 245, in _request_wrapper
    raise BadRequest(message)
telegram.error.BadRequest: Can't parse entities: unsupported start tag "url" at byte offset 225
2020-06-12 17:59:32,378 - root -                     INFO - coders
2020-06-12 18:02:21,093 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 99, in process_members
    bot_print(update, context['status']['initiated'])
TypeError: 'CallbackContext' object is not subscriptable
2020-06-12 18:02:59,888 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 99, in process_members
    bot_print(update, context.bot_data['status']['initiated'])
KeyError: 'status'
2020-06-12 18:04:26,086 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 99, in process_members
    bot_print(update, context.bot_data['status']['initiated'])
KeyError: 'status'
2020-06-12 18:04:26,089 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 1228, in process_msg
    permissions = context.user_data['permissions'] # find permissions of this user
KeyError: 'permissions'
2020-06-12 18:10:52,192 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 99, in process_members
    bot_print(update, context.user_data['status']['initiated'])
KeyError: 'status'
2020-06-12 18:10:52,193 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\ALPHAbot\lib\site-packages\telegram\ext\handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 1228, in process_msg
    permissions = context.user_data['permissions'] # find permissions of this user
KeyError: 'permissions'
2021-07-26 13:59:52,205 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "main.py", line 107, in process_members
    initiate_user(user_id, update, context) # in utils
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/utils.py", line 298, in initiate_user
    permissions {context.user_data["permissions"]}.')
KeyError: 'permissions'
2021-07-26 13:59:52,218 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "main.py", line 1246, in process_msg
    permissions = context.user_data['permissions'] # find permissions of this user
KeyError: 'permissions'
2021-07-26 14:00:51,733 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "main.py", line 107, in process_members
    initiate_user(user_id, update, context) # in utils
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/utils.py", line 298, in initiate_user
    permissions {context.user_data["permissions"]}.')
KeyError: 'permissions'
2021-07-26 14:00:51,734 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "main.py", line 1246, in process_msg
    permissions = context.user_data['permissions'] # find permissions of this user
KeyError: 'permissions'
2021-07-26 14:01:36,589 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "main.py", line 107, in process_members
    initiate_user(user_id, update, context) # in utils
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/utils.py", line 298, in initiate_user
    permissions {context.user_data["permissions"]}.')
KeyError: 'permissions'
2021-07-26 14:01:36,591 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "main.py", line 1246, in process_msg
    permissions = context.user_data['permissions'] # find permissions of this user
KeyError: 'permissions'
2021-07-26 14:01:42,444 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "main.py", line 107, in process_members
    initiate_user(user_id, update, context) # in utils
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/utils.py", line 308, in initiate_user
    text=first_use)
  File "<decorator-gen-2>", line 2, in send_message
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 351, in send_message
    timeout=timeout, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 178, in _message
    result = self._request.post(url, data, timeout=timeout)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 243, in _request_wrapper
    raise Unauthorized(message)
telegram.error.Unauthorized: Forbidden: bot can't initiate conversation with a user
2021-07-26 14:04:15,423 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "main.py", line 107, in process_members
    initiate_user(user_id, update, context) # in utils
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/utils.py", line 308, in initiate_user
    text=first_use)
  File "<decorator-gen-2>", line 2, in send_message
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 351, in send_message
    timeout=timeout, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 178, in _message
    result = self._request.post(url, data, timeout=timeout)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 243, in _request_wrapper
    raise Unauthorized(message)
telegram.error.Unauthorized: Forbidden: bot can't send messages to bots
2021-07-26 14:06:03,241 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:06:03,241 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:06:08,861 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:06:08,862 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:06:38,669 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:06:38,670 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:06:44,200 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:06:44,200 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:06:50,201 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:06:50,202 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:06:57,414 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:06:57,414 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:07:06,544 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:07:06,544 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:07:16,054 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:07:16,054 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:07:28,094 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:07:28,094 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:07:44,011 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:07:44,012 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:08:10,628 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:08:10,628 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:08:16,025 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:08:16,026 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:08:22,833 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:08:22,834 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:08:30,736 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:08:30,737 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:08:37,972 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:08:37,973 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:08:47,496 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:08:47,496 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:09:00,005 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:09:00,005 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:09:15,866 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:09:15,866 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:09:37,398 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:09:37,400 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:10:07,603 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:10:07,604 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:11:21,817 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:11:21,817 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:11:57,249 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:11:57,250 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:12:32,628 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:12:32,629 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:13:07,190 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:13:07,190 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:13:12,722 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:13:12,722 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:13:18,658 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:13:18,658 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:13:25,931 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:13:25,932 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:13:35,145 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:13:35,145 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:13:40,063 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:13:40,063 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:13:45,490 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:13:45,490 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:13:50,901 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:13:51,529 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:13:56,957 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:13:56,958 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:14:04,234 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:14:04,234 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:14:13,294 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:14:13,294 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:14:22,149 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:14:22,149 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:14:35,259 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:14:35,260 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:14:54,712 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:14:54,712 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:15:42,331 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:15:42,331 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:15:55,511 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:15:55,512 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:15:56,462 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "main.py", line 107, in process_members
    initiate_user(user_id, update, context) # in utils
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/utils.py", line 298, in initiate_user
    permissions {context.user_data["permissions"]}.')
KeyError: 'permissions'
2021-07-26 14:15:57,383 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/handler.py", line 119, in handle_update
    return self.callback(update, context)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/utils.py", line 199, in typing_func
    return func(update, context)
  File "main.py", line 281, in start
    status_dict = context.user_data['status']
KeyError: 'status'
2021-07-26 14:15:59,738 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:15:59,738 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:00,968 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:00,969 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:05,780 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:05,780 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:07,521 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:07,521 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:13,053 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:13,053 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:14,279 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:14,279 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:17,864 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:17,864 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:22,049 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:22,049 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:27,389 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:27,390 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:31,573 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:31,574 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:39,368 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:39,369 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:43,771 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:43,772 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:55,447 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:55,448 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:59,637 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:16:59,637 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:17:16,953 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:17:16,953 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:17:21,561 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:17:21,562 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:17:47,405 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:17:47,405 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:17:51,666 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2021-07-26 14:17:51,666 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/ext/updater.py", line 341, in polling_action_cb
    allowed_updates=allowed_updates)
  File "<decorator-gen-31>", line 2, in get_updates
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 334, in post
    **urlopen_kwargs)
  File "/media/hosea/ARCHIVE/Telegram_Projects/new_ALPHAbot/venv/lib/python3.7/site-packages/telegram/utils/request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
