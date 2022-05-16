try:
    import os
except ImportError as e:
    print("Error while importing modules:", end="\n=================================================================\n")
    print(f"{e.name} is a required module!")
################################################################################
# Paths
path = os.getcwd()
hostsFile = path + "/../hosts"

################################################################################
# get user to input the domains
domains = []
userInput = ""
while not (userInput == "q" or userInput == "Q"):
    userInput = input("Enter a domain ('q' to add new domains): ")
    if not (userInput == "q" or userInput == "Q" or userInput == ""):
        domains.append(userInput)


if os.path.exists(hostsFile):
    with open(hostsFile, "a") as f:
        for domain in domains:
            f.write("0.0.0.0 " + domain + "\n")
            print(f"Added {domain} to hosts")
