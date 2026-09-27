import random


energy_jars = {
    "low": ["clean dishes", "vacuum", "fold laundry", "coding lesson - easy"],
    "medium": ["organize desk", "organize bedroom", "coding lesson - medium"],
    "high": [],
}

def pull_idea(energy_jars: dict, energy_level):
    if energy_level in energy_jars:
        content = energy_jars[energy_level]
        if content:
            return (random.choice(content))
        else:
            print ("Error, please add an idea")
    else:
        print ("Error, invalid energy level")

def add_idea(energy_jars: dict, energy_level, task_description):
    if energy_level in energy_jars:
        content = energy_jars[energy_level]
        content.append(task_description)
        print (f"Add successful! Current tasks:\n{energy_jars[energy_level]}")
    else:
        print ("Error, invalid energy level")

def main():
    while True:
        x = input("What would you like to do today?\n[1] Pull idea\n[2] Add idea\n[3] Exit\n")
        match x:
            case "1":
                energy_level = input("What is your energy level?\n")
                idea = pull_idea(energy_jars, energy_level)
                print (f"Let's try: {idea}")
            case "2":
                energy_level = input("What energy level do you want to add to?\n")
                task_description = input("What is your idea?\n")
                add_idea(energy_jars, energy_level, task_description)
            case "3":
                print ("Bye, see you soon!")
                return

main()