try:
    import os
    import sys
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
options.append("Quit")

menu = TerminalMenu(options)
quit = False
while quit == false:
    index = menu.show()
    option = options[index]

    if(option == "Quit"):
        quit = True
    else:
        print(option)
