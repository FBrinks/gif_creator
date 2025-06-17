def process_images(images, size=(800, 600), filter_type=None):
    from PIL import Image
    import cv2
    import numpy as np

    processed_images = []

    for image in images:
        # Open image using Pillow
        img = Image.open(image)

        # Resize image
        img = img.resize(size, Image.ANTIALIAS)

        # Apply filter if specified
        if filter_type == 'blur':
            img = img.filter(ImageFilter.BLUR)
        elif filter_type == 'sharpen':
            img = img.filter(ImageFilter.SHARPEN)

        # Convert to numpy array for OpenCV processing if needed
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Additional OpenCV processing can be done here if needed

        # Convert back to PIL Image
        processed_images.append(Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)))

    return processed_images