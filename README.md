# hosts
This is a list of hosts I have found to be used for ads, malware, etc.
## Installation
### Pihole
Add this as a blocklist:
``` https://raw.githubusercontent.com/chrisjudk/hosts/master/hosts ```
Then to use the whitelist file run this command (note: can be insecure to pipe to bash. You may want to verify the file before you run it):
``` bash
curl -sSL https://raw.githubusercontent.com/chrisjudk/hosts/master/pihole/whitelist.sh | bash
```
