from PIL import Image
import numpy as np
import imageio.v3 as iio

# Full paths to image files
filenames = [
    r"C:\Users\kalya\OneDrive\Desktop\GIF_1.png",
    r"C:\Users\kalya\OneDrive\Desktop\GIF_2.png", r"C:\Users\kalya\OneDrive\Desktop\GIF_3.png",
    r"C:\Users\kalya\OneDrive\Desktop\GIF_4.png",r"C:\Users\kalya\OneDrive\Desktop\GIF_5.png",
    r"C:\Users\kalya\OneDrive\Desktop\GIF_5.5.png",r"C:\Users\kalya\OneDrive\Desktop\GIF_6.0.png",
    r"C:\Users\kalya\OneDrive\Desktop\GIF_6.png",r"C:\Users\kalya\OneDrive\Desktop\GIF_6.5.png",
    r"C:\Users\kalya\OneDrive\Desktop\GIF_7.png",r"C:\Users\kalya\OneDrive\Desktop\GIF_8.png",
    r"C:\Users\kalya\OneDrive\Desktop\GIF_9.png"
]

images = []

# Use the size of the first image as the target size
target_size = Image.open(filenames[0]).size  # (width, height)

for filename in filenames:
    # Open with PIL
    img = Image.open(filename)

    # Resize to match target size
    img = img.resize(target_size)

    # Convert to RGB to ensure consistent shape
    img = img.convert("RGB")

    # Convert to NumPy array for imageio
    img_array = np.array(img)

    images.append(img_array)

# Write to GIF
iio.imwrite(r"C:\Users\kalya\OneDrive\Desktop\team.gif", images, duration=500, loop=0)
