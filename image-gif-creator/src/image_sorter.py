def sort_images(images, criteria='filename'):
    if criteria == 'filename':
        return sorted(images, key=lambda img: img.filename)
    elif criteria == 'size':
        return sorted(images, key=lambda img: img.size)
    elif criteria == 'date':
        return sorted(images, key=lambda img: img.date)
    else:
        raise ValueError("Invalid sorting criteria. Use 'filename', 'size', or 'date'.")

def move_up(image_list, index):
    """Flytta upp bilden på angiven index i listan."""
    if index > 0:
        image_list[index - 1], image_list[index] = image_list[index], image_list[index - 1]
        return index - 1  # Returnera nya index
    return index

def move_down(image_list, index):
    """Flytta ned bilden på angiven index i listan."""
    if index < len(image_list) - 1:
        image_list[index + 1], image_list[index] = image_list[index], image_list[index + 1]
        return index + 1  # Returnera nya index
    return index