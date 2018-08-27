# hosts
This is a list of hosts I have found to be used for ads, malware, etc.
## Installation
### HOSTS file
``` https://raw.githubusercontent.com/chrisjudk/hosts/master/hosts ```

### Pihole Whitelist (Automatic)
To use the whitelist file run this command (note: can be insecure to pipe to bash. You may want to verify the file before you run it):
``` bash
curl -sSL https://raw.githubusercontent.com/chrisjudk/hosts/master/pihole/whitelist.sh | bash
```

### Normal whitelist (manual)
``` https://raw.githubusercontent.com/chrisjudk/hosts/master/whitelist ```
