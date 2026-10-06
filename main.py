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

def add_idea(energy_jars: dict, energy_level, task_description, filename):
    if energy_level in energy_jars:
        content = energy_jars[energy_level]
        content.append(task_description)
        save_jars(energy_jars, filename)
        print (f"\nAdd successful! Current tasks:\n{energy_jars[energy_level]}\n")
    else:
        print ("\nError, invalid energy level\n")

def edit_jars(energy_jars: dict, choice, energy_level, filename):
    match choice:
        case "add":
            add_jar(energy_jars, energy_level, filename)
        case "rename":
            rename_jar(energy_jars, energy_level, filename)
        case "remove":
            remove_jar(energy_jars, energy_level, filename)
        case _:
            print ("Invalid choice, please try again.")
            return

def add_jar(energy_jars: dict, energy_level, filename):
    if energy_level in energy_jars:
        print (f"\nThe jar '{energy_level}' already exists.\n")
    else:
        energy_jars[energy_level] = []
        save_jars(energy_jars, filename)
        print (f"\nAdd successful! Current jars:\n{energy_jars}\n")

def rename_jar(energy_jars: dict, energy_level, filename):
    energy_level_present = energy_level in energy_jars
    if energy_level_present:
        raw_new_name = input(f"\nWhat would you like to rename [{energy_level}] to?\n")
        new_name = raw_new_name.lower()
        if new_name in energy_jars:
            print(f"\nError: A jar named '{new_name}' already exists!\n")
        else:
            energy_jars[new_name] = energy_jars.pop(energy_level)
            save_jars(energy_jars, filename)
            print (f"\nSuccess! Jar {energy_level} successfully renamed to {new_name}!\n")
    else:
        print (f"\nError: The jar {energy_level} does not exist.\n")

def remove_jar(energy_jars: dict, energy_level, filename):
    energy_level_present = energy_level in energy_jars
    if energy_level_present:
        del energy_jars[energy_level]
        save_jars(energy_jars, filename)
        print(f"\nSuccess! Jar {energy_level} has been removed!\n")
    else:
        print (f"\nError: The jar {energy_level} does not exist.\n")


def save_jars(energy_jars: dict, filename):
    with open(filename, 'w') as f:
        json.dump(energy_jars, f, indent=4)

def load_jars(filename):
    if os.path.exists(filename):
        with open (filename, 'r') as f:
            loaded_jars = json.load(f)
            print (f"Current Jars:\n{loaded_jars}\n")
            return loaded_jars
    else:
        with open(filename, 'w') as f:
                json.dump(energy_jars, f)
        return load_jars(filename)


def main():
    raw_filename = input("Please enter the jar(s) filename:\n")
    filename = raw_filename + ".json"
    loaded_jars = load_jars(filename)
            
    while True:
        x = input("What would you like to do today?\n[1] Pull idea\n[2] Add idea\n[3] Edit energy levels\n[4] Exit\n")
        match x:
            case "1":
                unfiltered_level = input("\nWhat is your energy level?\n")
                energy_level = unfiltered_level.lower()
                idea = pull_idea(loaded_jars, energy_level)
                if idea:
                    print(f"\nLet's try: [{idea}]\n")
            case "2":
                unfiltered_level = input("\nWhat energy level do you want to add to?\n")
                energy_level = unfiltered_level.lower()
                task_description = input("\nWhat is your idea?\n")
                add_idea(loaded_jars, energy_level, task_description, filename)
            case "3":
                raw_choice = input("\nWould you like to [add], [rename], or [remove] an energy level?\n")
                choice = raw_choice.lower()
                unfiltered_level = input("\nWhat energy level do you want to add or change?\n")
                energy_level = unfiltered_level.lower()
                edit_jars(loaded_jars, choice, energy_level, filename)
            case "4":
                print ("\nBye, see you soon!")
                return
            case _:
                print ("\nInvalid choice, please try again.\n")

main()