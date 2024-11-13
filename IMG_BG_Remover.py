from PIL import Image
import numpy as np

def remove_background_and_set_new(image_path, new_background_color):
    """
    Removes the background of an image and sets a new background color.

    Args:
    image_path (str): Path to the image.
    new_background_color (tuple): RGB values of the new background color. (e.g., (255, 0, 0) for red)

    Returns:
    None
    """

    # Open the image
    image = Image.open(image_path)

    # Convert the image to RGBA mode (required for transparency)
    image = image.convert('RGBA')

    # Load the image data
    image_data = np.array(image)

    # Define the threshold for background transparency (adjust as needed)
    threshold = 100

    # Create a mask for transparent pixels (assuming white background)
    mask = np.where((image_data[:, :, 0] > threshold) & 
                    (image_data[:, :, 1] > threshold) & 
                    (image_data[:, :, 2] > threshold),
                    0, 255)

    # Apply the mask to the image data
    image_data[:, :, 3] = mask

    # Create a new background image
    background_image = Image.new('RGBA', image.size, new_background_color)

    # Paste the foreground image onto the background image
    background_image.paste(image, mask=Image.fromarray(image_data[:, :, 3]))

    # Display the result
    background_image.show()

    # Save the result
    background_image.save('result.png')


# Get the image path and new background color from the user
image_path = input("Enter the image path: ")
red = int(input("Enter the red value (0-255): "))
green = int(input("Enter the green value (0-255): "))
blue = int(input("Enter the blue value (0-255): "))

new_background_color = (red, green, blue)

remove_background_and_set_new(image_path, new_background_color)
