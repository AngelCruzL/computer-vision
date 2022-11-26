import os


def load_image(image_name):
    """Loads an image from the images folder
    Args:
            image_name (str): The name of the image to load with the file extension

    Returns:
            The image path
    """

    path = os.getcwd()
    if path.__contains__('01_images_pixels'):
        path = path.replace('01_images_pixels', '')

    image_path = os.path.join(path, '01_images_pixels',
                              image_name)

    return image_path
