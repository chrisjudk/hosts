try:
	import os
	from convertHostsFileToDomainsList import hostsToDomainList
except ImportError as e:
	print("\n\n".join("Import Error(s)".center(80,'=')))
	print(f"Package {e.name} is required for this tool!")
	
########################################################################################################################
# Config

# Path(s)
outputDir = os.getcwd() + "/../pihole/"
outputFileName = "StevenBlack_hosts"

# This is generic, so I'm using the very popular hosts file by StevenBlack for personal use
# Check out his repo here: (https://github.com/StevenBlack/hosts)
urlOfRawHosts = "https://raw.githubusercontent.com/StevenBlack/hosts/refs/heads/master/hosts"

############################################################
# Run
outputLocation = os.path.join(outputDir,"{}".format(outputFileName))
with open(outputLocation, 'w') as outputFile:
		outputFile.write(hostsToDomainList(urlOfRawHosts))