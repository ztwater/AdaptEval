from PIL import Image

def zoom_at(img: Image.Image, x: int, y: int, zoom: float) -> Image.Image:
    """
    PIL helper that combines crop and resize to zoom into an image at a point. From
    https://stackoverflow.com/questions/46149003/pil-zoom-into-image-at-a-particular-point

    :param img: image to transform
    :param x: x coord to zoom into
    :param y: y coord to zoom into
    :param zoom: zoom factor
    :return: zoomed in image
    """
    w, h = img.size
    zoom2 = zoom * 2
    img = img.crop((int(x - w / zoom2), int(y - h / zoom2),
                    int(x + w / zoom2), int(y + h / zoom2)))
    return img.resize((w, h), Image.LANCZOS)
