import os

# Rename all photos in a folder numerically

directory = "~/Desktop/Test"
directory = os.path.expanduser(directory)
counter = 1

for filename in os.listdir(directory):
    if filename.endswith(".png"):
        new_filename = f"{counter:04d}.png"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        counter += 1
