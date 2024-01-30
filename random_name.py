import os
import random
import string

# Rename all images in a folder with a random alphanumeric name

def generate_random_filename():
    length = 6
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string + ".png" # Replace with the appropriate file extension

directory = "~/MyDirectory" # Replace with the desired directory
directory = os.path.expanduser(directory)

print(f"Looking in directory: {directory}")
files = os.listdir(directory)

for filename in files:
    if filename.endswith(".png"): # Replace with the appropriate file extension
        new_filename = generate_random_filename()

        # Ensure the new filename doesn't already exist
        while os.path.exists(os.path.join(directory, new_filename)):
            new_filename = generate_random_filename()

        print(f"Renaming {filename} to {new_filename}")
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
