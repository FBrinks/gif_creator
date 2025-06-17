import imageio.v2 as imageio

def create_gif(image_paths, duration_ms, output_path):
    """Skapar en GIF från en lista av bildsökvägar."""
    duration_sec = duration_ms / 1000  # Sätter standardtid i millisekunder, funktionen kan utökas i framtiden och ge användaren möjlighet att ange en egen tid
    with imageio.get_writer(output_path, mode='I', duration=duration_sec) as writer:
        for path in image_paths:
            image = imageio.imread(path)
            writer.append_data(image)