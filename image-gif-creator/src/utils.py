def get_default_display_time():
    return 100  # Default display time in milliseconds

def validate_microseconds(microseconds):
    if microseconds < 0:
        raise ValueError("Display time must be a non-negative integer.")
    return microseconds

def convert_microseconds_to_milliseconds(microseconds):
    return microseconds / 1000  # Convert microseconds to milliseconds

def is_image_file(filename):
    valid_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
    return any(filename.lower().endswith(ext) for ext in valid_extensions)