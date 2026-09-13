try:
	import os
	import shutil
except ImportError as e:
	print("\n\n".join("Import Error(s)".center(80,'=')))
	print(f"Package {e.name} is required for this tool!")

############################################################
# Path(s)

path = os.getcwd() + "/../"
catdir = path + "whitelist-categories/"

##########################################################
# List files

files = os.listdir(catdir)

#########################################################
# Rename
for file in files:
	myfile = file.replace("-", "_")
	shutil.move(catdir+file, catdir+myfile)
