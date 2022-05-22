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
# Functions
def buildwl():
    with open(path + "/customWhitelist", "w") as out:
        for file in selections:
            with open(catPath + file,"r") as f:
                lines = f.readlines()
                for line in lines:
                    out.write(line)
        print(f"File saved to: {os.path.realpath(out.name)}")
##################################################################################
# Main menu builder
path = os.getcwd()
catPath = path + "/whitelist-categories/"
categories = os.listdir(catPath)
temp = []
options = []
for cat in categories:
    options.append(cat)
options.append("[a] All")
options.append("[q] Quit")
options.append("[b] Build")
quit = False
selections = []
while quit == False:
    exit = False
    index = TerminalMenu(options).show()
    option = options[index]

    if(option == "[q] Quit"):
        quit = True
    elif(option == "[b] Build"):
        quit = True
        buildwl()
    elif(option == "[a] All"):
        for o in options:
            if(o != "[b] Build" and o != "[a] All" and o != "[q] Quit"):
                selections.append(o)
                options.remove(o)

        print(selections)
    elif(os.path.isdir(catPath + option)):
        temp.clear()
        temp = os.listdir(catPath + option + "/")
        temp.append("[b] Back")
        while exit == False:
            file = temp[TerminalMenu(temp).show()]
            if file == "[b] Back":
                exit = True
            else:
                temp.remove(file)
                selections.append(option + "/" + file)
    else:
        selections.append(option)
        options.remove(option)
        print(selections)
