from PIL import Image

def load_image_points(image_path, width, height, step=4):

    img = Image.open(image_path).convert("RGB")

    img.thumbnail((width * 0.6, height * 0.8))

    img_width, img_height = img.size

    offset_x = (width - img_width) // 2
    offset_y = (height - img_height) // 2

    pixels = img.load()

    points = []

    for y in range(0, img_height, step):
        for x in range(0, img_width, step):

            r, g, b = pixels[x, y]

            brightness = (r + g + b) / 3

            if brightness > 40:
                points.append(
                    (
                        x + offset_x,
                        y + offset_y,
                           (r, g, b)
                    )
                )

    return points