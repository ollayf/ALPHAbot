================ ALPHAbot v3.2.4 =====================
- Edited the start.sh and server_setup.sh to allow running on the pi in background
- Removed typing action processing msgs
- Changed the way emojis are added to the cfm_msg

================ ALPHAbot v3.2.3 =====================
- Changed the logging of users added to members dict
- Updated README.md to be able to host it on the pi

================ ALPHAbot v3.2.2 =====================
- Changed teaching limit
- Changed user_timeout to only activate if the user has not ended convo
- Updated start.sh file and .gitignore file
- use username if the bot cannot access the
- updated DockerFile
- fixed getDatetimeOfNextDay function

================ ALPHAbot v3.2.1 =====================
- Hotfix for server issues
- Added start.sh (separated from server_setup.sh)

================ ALPHAbot v3.2.0 =====================
- Added the main cfm_menu fns
- Need to stress test
- Added msgs for future bday IC part
- Removed all uses of effective message
- Allowed emojis for the confirmation message

================ ALPHAbot v3.1.1 =====================
- Hot fix for send_typing_action

================ ALPHAbot v3.1.1 =====================
- Hot fix for timezones

================ ALPHAbot v3.1.0 =====================
- Added conversation timeouts (15mins)
- Added spam chat with a call has started
- Added broadcast function
- Added hidden coders only update functions for immediate updates

================ ALPHAbot v3.0.1 =====================
- Dockerised ALPHAbot
- Version Updates separated from README.md which now only describes what ALPHAbot does in the latest update
- added requirements.txt

================ ALPHAbot v 3.0.0 ====================
- Now using python telegram bot which is a package to deal with the API to handle callbacks and queries.
- Moving forward, the bot should no longer manually check for updates and store data in mem