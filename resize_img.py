import os
from PIL import Image

directory = "~/Desktop/Test"  # Change this to your directory path
directory = os.path.expanduser(directory)

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        file_path = os.path.join(directory, filename)

        with Image.open(file_path) as img:
            # Calculate the new size (20% of the original size)
            new_width = int(img.width * 0.2)
            new_height = int(img.height * 0.2)

            # Resize the image
            resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)

            # Save the resized image back to the directory
            # Note that this will overwrite the original
            resized_img.save(file_path)
