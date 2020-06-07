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
