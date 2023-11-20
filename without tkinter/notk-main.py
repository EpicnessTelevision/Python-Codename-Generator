import random

categories = ['Tech', 'Space', 'Nature', 'Fantasy', 'Unique']  # Add your own categories
words = {
    'Tech': ['Byte', 'Code', 'Algorithm', 'Node', 'Cyber', 'Nano'],
    'Space': ['Galaxy', 'Orbit', 'Star', 'Nebula', 'Cosmic', 'Quasar'],
    'Nature': ['Forest', 'River', 'Mountain', 'Sunset', 'Wild', 'Zen'],
    'Fantasy': ['Dragon', 'Wizard', 'Realm', 'Sorcerer', 'Enchant', 'Mythic'],
    'Unique': ['Null', 'Ultra', 'Divide', 'Diverse', 'Ultimate', 'Piranha']
    # Add more words for each category
}

def get_random_element(arr):
    random_index = random.randint(0, len(arr) - 1)
    return arr[random_index]

def generate_code_name():
    selected_category = get_random_element(categories)
    generated_word = get_random_element(words[selected_category])
    unique_suffix = random.randint(0, 999)  # Add a unique number to enhance uniqueness
    code_name = f"{selected_category}-{generated_word}-{unique_suffix}"
    return code_name

print(generate_code_name())
