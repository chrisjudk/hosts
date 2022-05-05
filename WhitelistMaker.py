try:
    import os
    import sys
    from pprint import pprint
    from simple_term_menu import TerminalMenu
except ImportError as e:
    print("There was an error while importing required modules!",
    end="\n================================================================\n")
    print(f"{e.name} is a required package!")
    sys.exit(os.EX_UNAVAILABLE)

##################################################################################
# Main menu builder
path = os.getcwd()
catPath = path + "/whitelist-categories/"
categories = os.listdir(catPath)

options = []
for cat in categories:
    options.append(cat)
options.append("[a] All")
options.append("[q] Quit")

quit = False
selections = []
while quit == False:
    index = TerminalMenu(options).show()
    option = options[index]
    
    if(option == "[q] Quit"):
        quit = True
    elif(option =="[a] All"):
        for o in options:
            if(o != "[a] All" and o != "[q] Quit"):
                selections.append(o)
                options.remove(o)
        print(selections)
        quit = True
    else:
        selections.append(option)
        options.remove(option)
        print(selections)

##################################################################################
# Build the list
with open(path + "/customWhitelist", "w") as out:
    for file in selections:
        with open(catPath + file,"r") as f:
            lines = f.readlines()
            for line in lines:
                out.write(line)
