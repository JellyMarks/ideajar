import random
import json
import os


energy_jars = {
    "low": [],
    "medium": [],
    "high": [],
}

def pull_idea(energy_jars: dict, energy_level):
    if energy_level in energy_jars:
        content = energy_jars[energy_level]
        if content:
            return (random.choice(content))
        else:
            print ("\nError, please add an idea\n")
    else:
        print ("\nError, invalid energy level\n")

def add_idea(energy_jars: dict, energy_level, task_description):
    if energy_level in energy_jars:
        content = energy_jars[energy_level]
        content.append(task_description)
        print (f"\nAdd successful! Current tasks:\n{energy_jars[energy_level]}\n")
    else:
        print ("\nError, invalid energy level\n")

def save_jars(energy_jars, filename):
    with open(filename, 'w') as f:
        json.dump(energy_jars, f)
        print ("\nSave successful!\n")

def load_jars(filename):
    if os.path.exists(filename):
        with open (filename, 'r') as f:
            loaded_jars = json.load(f)
            print (f"Current Jars:\n{loaded_jars}\n")
            return loaded_jars
    else:
        with open(filename, 'w') as f:
                json.dump(energy_jars, f)
        load_jars(filename)
        



def main():
    filename = input("Please enter the jar(s) filename:\n")
    loaded_jars = load_jars(filename)
            
    while True:
        x = input("What would you like to do today?\n[1] Pull idea\n[2] Add idea\n[3] Save\n[4] Exit\n")
        match x:
            case "1":
                energy_level = input("\nWhat is your energy level?\n")
                idea = pull_idea(loaded_jars, energy_level)
                print (f"\nLet's try: [{idea}]\n")
            case "2":
                energy_level = input("\nWhat energy level do you want to add to?\n")
                task_description = input("\nWhat is your idea?\n")
                add_idea(energy_jars, energy_level, task_description)
            case "3":
                save_jars(energy_jars, filename)
            case "4":
                print ("\nBye, see you soon!")
                return

main()