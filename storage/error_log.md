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
