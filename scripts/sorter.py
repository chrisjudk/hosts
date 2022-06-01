try:
	import os
except ImportError as e:
	print("\n\n".join("Import Error(s)".center(80,'=')))
	print(f"Package {e.name} is required for this tool!")

############################################################
# Path(s)

path = os.getcwd() + "/../"
catdir = path + "whitelist-categories/"

############################################################
# List files

files = os.listdir(catdir)

############################################################
# methods
def sorter(rootDir, filesList):
	for fn in filesList:
		lines = []
		with open(rootDir.join(fn), 'r') as file:
			for line in file:
				lines.append(line)
		lines.sort()
		with open(rootDir.join(fn), 'w') as file:
			for line in lines:
				file.writelines(line)

############################################################
# sort files
sorter(rootDir=catdir, filesList = files)
