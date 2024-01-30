import os

# Rename all images in a folder numerically

directory = "~/MyDirectory" # Replace with the desired directory
directory = os.path.expanduser(directory)
counter = 1

for filename in os.listdir(directory):
    if filename.endswith(".png"): # Replace with the appropriate file extension
        new_filename = f"{counter:04d}.png"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        counter += 1
