"""
:project: telegram-onedrive
:author: L-ING
:copyright: (C) 2023 L-ING <hlf01@icloud.com>
:license: MIT, see LICENSE for more details.
"""

PART_SIZE = 2 * 1024 * 1024

file_param_name_list = ['name', 'filename', 'file_name', 'title', 'file']

logs_lines_per_page = 50

tg_bot_session_path = 'session/bot.session'
tg_client_session_path = 'session/user.session'
od_session_path = 'session/onedrive.session'


cmd_helper = '''
- /auth to authorize for Telegram and OneDrive.
- /clear to clear all history except status message.
- /autoDelete to toggle whether bot should auto delete message.
- /clearLogs to clear logs.
- /logs to show all logs.

- ```/links message_link range```: Transfer sequential restricted content.
- ```/url file_url```: Upload file through url.
- ```/logs range```: Show the most recent logs for the specified page number.
'''


start_res = '''
Transfer files to Onedrive.

Forward or upload files to me, or pass message link to transfer restricted content from group or channel.
%s
- /help: Ask for help.
'''%cmd_helper


help_res = '''
%s
- To transfer files, forward or upload to me.
- To transfer restricted content, right click the content, copy the message link, and send to me.
- Tap Status on replied status message to locate current job.
- Uploading through url will call Onedrive's API, which means Onedrive's server will visit the url and download the file for you. If the url is invalid to OneDrive, the bot will try using bot's uploader to transfer.
- Each log page contains 50 lines of logs.
'''%cmd_helper


check_in_group_res = '''
This bot must be used in a Group!

Add this bot to a Group as Admin, and give it ability to Delete Messages.
'''


not_login_res = '''
You haven't logined to Telegram.
'''


links_res = '''
Command ```/links``` format wrong.

Usage: ```/links message_link range```
'''


url_res = '''
Command ```/url``` format wrong.

Usage: ```/url file_url```
'''


logs_res = '''
Command ```/logs``` format wrong.

Usage: ```/logs range```
'''


analysis_not_http_or_forbidden = 'Url protocol is not HTTP, or the url has been forbidden because of too many failed requests.'

analysis_content_not_found = 'Content not found.'

analysis_work_canncelled = 'The work was canncelled for unknown reason.'