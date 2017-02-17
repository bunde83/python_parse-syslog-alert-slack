# python_parse-syslog-alert-slack
Parses syslog (or any flat log file) for user defined matches and sends matching lines to slack webhook

To use:

1. Modify parse.py with your slack webhook URL, log location, and match conditions.

2. If using matches.txt for matches, comment out the basic matching in parse.py (lines 32-33) and uncomment the matching file option (lines 36-38), modify with one match condition per line with no trailing spaces, match conditions are case sensitive but can contain spaces. 

TO DO:

1. Additional parsing to format syslog message.

2. Additional alert options (XMPP, Email, etc)
