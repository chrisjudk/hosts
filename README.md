# hosts

[![Github file size](https://img.shields.io/github/size/chrisjudk/hosts/hosts.svg?label=hosts+file+size)](github.com/chrisjudk/hosts/blob/master/hosts)
[![License](https://img.shields.io/github/license/chrisjudk/hosts.svg)](https://github.com/chrisjudk/hosts/blob/master/LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/chrisjudk/hosts.svg)](https://github.com/chrisjudk/hosts/commits/master)
[![GitHub commit activity the past year](https://img.shields.io/github/commit-activity/y/chrisjudk/hosts.svg)](https://github.com/chrisjudk/hosts/graphs/commit-activity)

This is a list of hosts I have found to be used for ads, malware, etc.
## Installation
### HOSTS file
``` https://raw.githubusercontent.com/chrisjudk/hosts/master/hosts ```

### Pihole Whitelist (Automatic)
To use the whitelist file run this command (note: can be insecure to ioe to bash. You may want to verify the file before you run it):
``` bash
curl -sSL https://raw.githubusercontent.com/chrisjudk/hosts/master/pihole/whitelist.sh | bash
```

### Normal whitelist (manual)
``` https://raw.githubusercontent.com/chrisjudk/hosts/master/whitelist ```
