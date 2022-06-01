try:
	import os
except ImportError as e:
	print("\n\n".join("Import Error(s)".center(80,'=')))
	print(f"Package {e.name} is required for this tool!")

############################################################
# Path(s)

path = os.getcwd() + "/../"

############################################################
# Methods
def makeScript(rootDir, whitelist):
	script = "#!/bin/bash\n/usr/local/bin/pihole -w "
	with open(os.path.join(rootDir, whitelist),'r') as f:
		for line in f:
			line = line.replace("\n"," ")
			script = script + line
	with open(os.path.join(rootDir,"pihole/{}.sh".format(whitelist)), 'w') as f:
		f.write(script)

# Generate the script(s)
if os.path.exists(os.path.join(path,"whitelist")):
	makeScript(rootDir=path,whitelist="whitelist")
if os.path.exists(os.path.join(path,"customWhitelist")):
	makeScript(rootDir=path,whitelist="customWhitelist")
