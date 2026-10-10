import random
import json
import os

# Template for new files
# low, medium, and high can be adjusted
## in_process is built into functions, be sure to rename all instances
energy_jars = {
    "low": [],
    "medium": [],
    "high": [],
    "in_process": [],
}

# The main flow for "pull"
def handle_pull_workflow(loaded_jars: dict, filename: str):
    energy_level = input("\nWhat is your energy level?\n").strip().lower()
    
    # Keep rolling ideas as long as the user wants a new one
    while True:

        idea = pull_idea(loaded_jars, energy_level)
        if not idea:
            return  # pull_idea already alerted them if empty or invalid

        print(f"\nLet's try: [{idea}]\n")
        
        want_new = ask_yes_no("New idea?")
        if not want_new:
            break

    # Once they settle on an idea, handle the outcome:
    if ask_yes_no(f"Did you complete '{idea}'?"):
        remove_idea(loaded_jars, energy_level, idea, filename)
        print(f"\nCongrats on completing '{idea}'! It has been removed.\n")
        return

    if ask_yes_no("Have you started?"):
        if energy_level == "in_process":
            print(f"\nThe idea '{idea}' has been stored for later.\n") # 
        else:
            store_idea(loaded_jars, idea, energy_level, filename)
            print(f"\nThe idea '{idea}' has been stored for later.\n")
    else:
        print("\nNo worries!\n")

# Return and print a random idea from the given "energy level"
def pull_idea(energy_jars: dict, energy_level):
    if energy_level in energy_jars:
        content = energy_jars[energy_level]
        if content:
            return (random.choice(content))
        else:
            print ("\nError, please add an idea\n")
    else:
        print ("\nError, invalid energy level\n")

def ask_yes_no(prompt: str) -> bool:
    # Helper to keep asking until the user answers yes or no.
    while True:
        answer = input(f"{prompt} (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Invalid response, please type 'yes' or 'no'.")

# Add or remove ideas from the given "energy level"
def edit_ideas(energy_jars: dict, choice, filename):
    unfiltered_level = input("\nWhat energy level is your idea in?: ")
    energy_level = unfiltered_level.lower()
    if energy_level in energy_jars:
        raw_idea = input("\nWhat is your idea?: ")
        idea = raw_idea.lower()
        match choice:
                case "add":
                    add_idea(energy_jars, energy_level, idea, filename)
                case "remove":
                    remove_idea(energy_jars, energy_level, idea, filename)
                case _:
                    print ("\nInvalid choice, please try again.\n")
                    return
    else:
        print ("\nError, invalid energy level\n")

# Helper function for adding ideas to the given "energy level"
def add_idea(energy_jars: dict, energy_level, task_description, filename):
    if energy_level in energy_jars:
        if task_description in energy_jars[energy_level]:
            print (f"Error: The idea {task_description} already in the {energy_level} energy jar.")
        else:
            content = energy_jars[energy_level]
            content.append(task_description)
            save_jars(energy_jars, filename)
            print (f"\nAdd successful! Current {energy_level} energy tasks:\n{energy_jars[energy_level]}\n")
    else:
        print ("\nError, invalid energy level\n")

# Helper function for aremoving ideas from the given "energy level"
def remove_idea(energy_jars, energy_level, idea, filename):
    if energy_level in energy_jars:
        if idea in energy_jars[energy_level]:
            energy_jars[energy_level].remove(idea)
            save_jars(energy_jars, filename)
            print (f"Successfully removed {idea}!")
        else:
            print (f"Error: The idea {idea} not in the {energy_level} energy jar.")
    else:
        print (f"Error: The {energy_level} energy jar does not exist.")
        
def store_idea(energy_jars: dict, idea, energy_level, filename):
    energy_jars["in_process"].append(idea)
    remove_idea(energy_jars, energy_level, idea, filename)
    

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
        if energy_level == "in_process":
            print (f"\nError: Cannot rename dedicated '{energy_level}' jar\n")
            return
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
        if energy_level == "in_process":
            print (f"\nError: Cannot remove dedicated '{energy_level}' jar\n")
        else:
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
        x = input("What would you like to do today?\n[1] Pull idea\n[2] Add or edit ideas\n[3] Edit energy levels\n[4] Exit\n")
        match x:
            case "1":
                print (f"\nYour current jars and ideas: {loaded_jars}\n")
                handle_pull_workflow(loaded_jars, filename)
            case "2":
                print (f"\nYour current jars and ideas: {loaded_jars}\n")
                raw_choice = input("\nWould you like to [add] or [remove]?: ")
                choice = raw_choice.lower()
                edit_ideas(loaded_jars, choice, filename)
            case "3":
                print (f"\nYour current jars and ideas: {loaded_jars}\n")
                raw_choice = input("\nWould you like to [add], [rename], or [remove] an energy level?: ")
                choice = raw_choice.lower()
                unfiltered_level = input("\nWhat energy level do you want to add or change?: ")
                energy_level = unfiltered_level.lower()
                edit_jars(loaded_jars, choice, energy_level, filename)
            case "4":
                print ("\nBye, see you soon!")
                return
            case _:
                print ("\nInvalid choice, please try again.\n")

main()