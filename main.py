import random
import tkinter as tk

categories = ['Tech', 'Space', 'Nature', 'Fantasy', 'Unique', 'Microsoft', 'Phone Carriers', 'Linux', 'Canada', 'Math', 'Misc']  # Add your own categories
words = {
    'Tech': ['Byte', 'Code', 'Algorithm', 'Node', 'Cyber', 'Nano'],
    'Space': ['Galaxy', 'Orbit', 'Star', 'Nebula', 'Cosmic', 'Quasar', 'Cluster'],
    'Nature': ['Forest', 'River', 'Mountain', 'Sunset', 'Wild', 'Zen'],
    'Fantasy': ['Dragon', 'Wizard', 'Realm', 'Sorcerer', 'Enchant', 'Mythic'],
    'Unique': ['Null', 'Ultra', 'Divide', 'Diverse', 'Ultimate', 'Piranha'],
    'Microsoft': ['Neptune', 'Memphis', 'Longhorn', 'Whistler', 'Vista', 'Chicago'],
    'Phone Carriers': ['Sprint', 'Circular', 'AT&T', 'TracFone', 'T-Mobile', 'metroPCS', 'Orange', 'Vodafone', 'Boost'],
    'Linux': ['Bookworm', 'Debian', 'Fedora', 'Red Hat', 'Ubuntu', 'Arch', 'Arch Linux', 'GNOME', 'KDE', 'Plasma', 'Mint', 'Linux Mint'],
    'Canada': ['Ontario', 'Quebec', 'Alberta', 'Saskatchewan', 'Manitoba', 'British Columbia', 'Nunavat', 'Yukon', 'Northwest' 'Prince Edward Island'],
    'Math': ['Addition', 'Subtraction', 'Multiplication', 'Division'],
    'Misc': ['Visine', 'Millennium', 'Dreamweaver', 'Rover', 'Cupertino', 'Coffee', 'Waterbay', 'Seaside', 'Shore', 'Jersey']
    # Add more words for each category
}

def get_random_element(arr):
    random_index = random.randint(0, len(arr) - 1)
    return arr[random_index]

def generate_code_name():
    selected_categories = random.sample(categories, 3)
    generated_words = [get_random_element(words[category]) for category in selected_categories]
    return ' '.join(generated_words)

def update_label():
    code_name = generate_code_name()
    label.config(text=code_name)

root = tk.Tk()
root.title("Python Codename Generator")

label = tk.Label(root, text="")
label.pack()

button = tk.Button(root, text="Generate Codename", command=update_label)
button.pack()

root.mainloop()
