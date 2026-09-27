import random


energy_jars = {
    "low": ["clean dishes", "vacuum", "fold laundry", "coding lesson - easy"],
    "medium": ["organize desk", "organize bedroom", "coding lesson - medium"],
    "high": [],
}

def pull_idea(energy_jars, energy_level):
    if energy_level in energy_jars:
        content = energy_jars[energy_level]
        if content:
            print (random.choice(content))
        else:
            print ("Error, please add an idea")
    else:
        print ("Error, invalid energy level")


pull_idea(energy_jars, "ok")