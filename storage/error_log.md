2020-05-23 13:05:34,586 - root -                     INFO - cfm sent to group
2020-05-23 13:18:12,511 - telegram.ext.updater -                     ERROR - Error while getting Updates: urllib3 HTTPError ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))
2020-05-23 13:18:12,512 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\connectionpool.py", line 614, in urlopen
    httplib_response = self._make_request(conn, method, url,
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\connectionpool.py", line 402, in _make_request
    six.raise_from(e, None)
  File "<string>", line 2, in raise_from
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\connectionpool.py", line 398, in _make_request
    httplib_response = conn.getresponse()
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\http\client.py", line 1322, in getresponse
    response.begin()
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\http\client.py", line 303, in begin
    version, status, reason = self._read_status()
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\http\client.py", line 264, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 669, in readinto
    return self._sock.recv_into(b)
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\ssl.py", line 1241, in recv_into
    return self.read(nbytes, buffer)
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\ssl.py", line 1099, in read
    return self._sslobj.read(len, buffer)
ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\utils\request.py", line 225, in _request_wrapper
    resp = self._con_pool.request(*args, **kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\request.py", line 68, in request
    return self.request_encode_body(method, url, fields=fields,
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\request.py", line 148, in request_encode_body
    return self.urlopen(method, url, **extra_kw)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\poolmanager.py", line 244, in urlopen
    response = conn.urlopen(method, u.request_uri, **kw)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\connectionpool.py", line 665, in urlopen
    retries = retries.increment(method, url, error=e, _pool=self,
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\util\retry.py", line 347, in increment
    raise six.reraise(type(error), error, _stacktrace)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\packages\six.py", line 685, in reraise
    raise value.with_traceback(tb)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\connectionpool.py", line 614, in urlopen
    httplib_response = self._make_request(conn, method, url,
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\connectionpool.py", line 402, in _make_request
    six.raise_from(e, None)
  File "<string>", line 2, in raise_from
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\connectionpool.py", line 398, in _make_request
    httplib_response = conn.getresponse()
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\http\client.py", line 1322, in getresponse
    response.begin()
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\http\client.py", line 303, in begin
    version, status, reason = self._read_status()
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\http\client.py", line 264, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 669, in readinto
    return self._sock.recv_into(b)
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\ssl.py", line 1241, in recv_into
    return self.read(nbytes, buffer)
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\ssl.py", line 1099, in read
    return self._sslobj.read(len, buffer)
telegram.vendor.ptb_urllib3.urllib3.exceptions.ProtocolError: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\updater.py", line 338, in polling_action_cb
    updates = self.bot.get_updates(self.last_update_id,
  File "<decorator-gen-31>", line 2, in get_updates
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\utils\request.py", line 331, in post
    result = self._request_wrapper('POST', url,
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\utils\request.py", line 231, in _request_wrapper
    raise NetworkError('urllib3 HTTPError {0}'.format(error))
telegram.error.NetworkError: urllib3 HTTPError ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))
2020-05-23 13:59:06,556 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\connectionpool.py", line 614, in urlopen
    httplib_response = self._make_request(conn, method, url,
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\connectionpool.py", line 402, in _make_request
    six.raise_from(e, None)
  File "<string>", line 2, in raise_from
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\connectionpool.py", line 398, in _make_request
    httplib_response = conn.getresponse()
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\http\client.py", line 1322, in getresponse
    response.begin()
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\http\client.py", line 303, in begin
    version, status, reason = self._read_status()
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\http\client.py", line 264, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 669, in readinto
    return self._sock.recv_into(b)
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\ssl.py", line 1241, in recv_into
    return self.read(nbytes, buffer)
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\ssl.py", line 1099, in read
    return self._sslobj.read(len, buffer)
ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\utils\request.py", line 225, in _request_wrapper
    resp = self._con_pool.request(*args, **kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\request.py", line 68, in request
    return self.request_encode_body(method, url, fields=fields,
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\request.py", line 148, in request_encode_body
    return self.urlopen(method, url, **extra_kw)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\poolmanager.py", line 244, in urlopen
    response = conn.urlopen(method, u.request_uri, **kw)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\connectionpool.py", line 665, in urlopen
    retries = retries.increment(method, url, error=e, _pool=self,
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\util\retry.py", line 347, in increment
    raise six.reraise(type(error), error, _stacktrace)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\packages\six.py", line 685, in reraise
    raise value.with_traceback(tb)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\connectionpool.py", line 614, in urlopen
    httplib_response = self._make_request(conn, method, url,
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\connectionpool.py", line 402, in _make_request
    six.raise_from(e, None)
  File "<string>", line 2, in raise_from
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\vendor\ptb_urllib3\urllib3\connectionpool.py", line 398, in _make_request
    httplib_response = conn.getresponse()
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\http\client.py", line 1322, in getresponse
    response.begin()
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\http\client.py", line 303, in begin
    version, status, reason = self._read_status()
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\http\client.py", line 264, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 669, in readinto
    return self._sock.recv_into(b)
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\ssl.py", line 1241, in recv_into
    return self.read(nbytes, buffer)
  File "C:\Users\Hosea\AppData\Local\Programs\Python\Python38-32\lib\ssl.py", line 1099, in read
    return self._sslobj.read(len, buffer)
telegram.vendor.ptb_urllib3.urllib3.exceptions.ProtocolError: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\handler.py", line 117, in handle_update
    return self.callback(update, context)
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 161, in typing_func
    context.bot.send_chat_action(chat_id=update.effective_message.chat_id, \
  File "<decorator-gen-20>", line 2, in send_chat_action
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\bot.py", line 1513, in send_chat_action
    result = self._request.post(url, data, timeout=timeout)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\utils\request.py", line 331, in post
    result = self._request_wrapper('POST', url,
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\utils\request.py", line 231, in _request_wrapper
    raise NetworkError('urllib3 HTTPError {0}'.format(error))
telegram.error.NetworkError: urllib3 HTTPError ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))
2020-05-23 13:59:07,598 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\handler.py", line 117, in handle_update
    return self.callback(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 96, in process_members
    initiate_user(user_id, update, context) # in utils
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 258, in initiate_user
    context.bot.send_message(chat_id=update.effective_message.from_user.id, \
  File "<decorator-gen-2>", line 2, in send_message
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\bot.py", line 349, in send_message
    return self._message(url, data, disable_notification=disable_notification,
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\bot.py", line 178, in _message
    result = self._request.post(url, data, timeout=timeout)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\utils\request.py", line 331, in post
    result = self._request_wrapper('POST', url,
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\utils\request.py", line 243, in _request_wrapper
    raise Unauthorized(message)
telegram.error.Unauthorized: Forbidden: bot can't initiate conversation with a user
2020-05-23 18:55:07,606 - root -                     INFO - Attempted send confirmation
2020-05-23 18:55:08,157 - root -                     INFO - ^^ cfm msg
2020-05-23 18:55:08,158 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\handler.py", line 117, in handle_update
    return self.callback(update, context)
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 163, in typing_func
    return func(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 939, in confirm
    update.bot.send_message(chat_id=chat_id, text=emojize(cfm_msg), parse_mode=ParseMode.HTML)
AttributeError: 'Update' object has no attribute 'bot'
2020-05-30 18:42:21,464 - telegram.ext.updater -                     ERROR - Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2020-05-30 18:42:21,465 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\updater.py", line 380, in _network_loop_retry
    if not action_cb():
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\updater.py", line 338, in polling_action_cb
    updates = self.bot.get_updates(self.last_update_id,
  File "<decorator-gen-31>", line 2, in get_updates
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\bot.py", line 2136, in get_updates
    result = self._request.post(url, data, timeout=float(read_latency) + float(timeout))
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\utils\request.py", line 331, in post
    result = self._request_wrapper('POST', url,
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\utils\request.py", line 249, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
2020-05-30 18:44:15,474 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\handler.py", line 117, in handle_update
    return self.callback(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 97, in process_members
    initiate_user(user_id, update, context) # in utils
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 258, in initiate_user
    context.bot.send_message(chat_id=update.effective_message.from_user.id, \
  File "<decorator-gen-2>", line 2, in send_message
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\bot.py", line 349, in send_message
    return self._message(url, data, disable_notification=disable_notification,
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\bot.py", line 178, in _message
    result = self._request.post(url, data, timeout=timeout)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\utils\request.py", line 331, in post
    result = self._request_wrapper('POST', url,
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\utils\request.py", line 243, in _request_wrapper
    raise Unauthorized(message)
telegram.error.Unauthorized: Forbidden: bot can't initiate conversation with a user
2020-05-30 18:44:16,321 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\handler.py", line 117, in handle_update
    return self.callback(update, context)
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 163, in typing_func
    return func(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 261, in start
    context.bot.send_message(chat_id=update.message.from_user.id, \
  File "<decorator-gen-2>", line 2, in send_message
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\bot.py", line 349, in send_message
    return self._message(url, data, disable_notification=disable_notification,
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\bot.py", line 178, in _message
    result = self._request.post(url, data, timeout=timeout)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\utils\request.py", line 331, in post
    result = self._request_wrapper('POST', url,
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\utils\request.py", line 243, in _request_wrapper
    raise Unauthorized(message)
telegram.error.Unauthorized: Forbidden: bot can't initiate conversation with a user
2020-05-30 21:40:38,862 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\handler.py", line 117, in handle_update
    return self.callback(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 97, in process_members
    initiate_user(user_id, update, context) # in utils
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 261, in initiate_user
    context.bot.send_message(chat_id=update.effective_message.from_user.id, \
  File "<decorator-gen-2>", line 2, in send_message
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\bot.py", line 70, in decorator
    result = func(*args, **kwargs)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\bot.py", line 349, in send_message
    return self._message(url, data, disable_notification=disable_notification,
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\bot.py", line 178, in _message
    result = self._request.post(url, data, timeout=timeout)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\utils\request.py", line 331, in post
    result = self._request_wrapper('POST', url,
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\utils\request.py", line 243, in _request_wrapper
    raise Unauthorized(message)
telegram.error.Unauthorized: Forbidden: bot can't initiate conversation with a user
2020-05-30 22:19:16,323 - root -                     INFO - 6
2020-05-30 22:19:16,323 - root -                     INFO - 0
2020-05-30 22:23:00,001 - root -                     INFO - cfm sent to group
2020-05-31 16:24:32,795 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\handler.py", line 117, in handle_update
    return self.callback(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 97, in process_members
    initiate_user(user_id, update, context) # in utils
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 268, in initiate_user
    context.user_data['permissions'] = get_user_permissions(user_id, context)
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 208, in get_user_permissions
    elif tuple(bot_data['bday_ICs'].values()).__contains__(user_id):
KeyError: 'bday_ICs'
2020-05-31 16:24:35,583 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\handler.py", line 117, in handle_update
    return self.callback(update, context)
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 163, in typing_func
    return func(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 369, in cfm_settings
    if not check_permission(permissions, 'cfm_IC'):
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 620, in check_permission
    assert tuple(power_level.keys()).__contains__(auth), 'User Perms not exist'
AssertionError: User Perms not exist
2020-05-31 16:28:17,279 - root -                     INFO - coders
2020-05-31 16:28:34,263 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\handler.py", line 117, in handle_update
    return self.callback(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 97, in process_members
    initiate_user(user_id, update, context) # in utils
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 268, in initiate_user
    context.user_data['permissions'] = get_user_permissions(user_id, context)
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 208, in get_user_permissions
    elif tuple(bot_data['bday_ICs'].values()).__contains__(user_id):
KeyError: 'bday_ICs'
2020-05-31 16:28:36,619 - root -                     INFO - None
2020-05-31 16:28:36,620 - telegram.ext.dispatcher -                     ERROR - No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\dispatcher.py", line 343, in process_update
    handler.handle_update(update, self, check, context)
  File "d:\Telegram_Projects\new_ALPHAbot\venv\lib\site-packages\telegram\ext\handler.py", line 117, in handle_update
    return self.callback(update, context)
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 163, in typing_func
    return func(update, context)
  File "d:/Telegram_Projects/new_ALPHAbot/main.py", line 369, in cfm_settings
    if not check_permission(permissions, 'cfm_IC'):
  File "d:\Telegram_Projects\new_ALPHAbot\utils.py", line 622, in check_permission
    assert tuple(power_level.keys()).__contains__(auth), 'User Perms not exist'
AssertionError: User Perms not exist
2020-05-31 16:30:00,830 - root -                     INFO - cfm_IC
