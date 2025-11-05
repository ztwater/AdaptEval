import torchvision.transforms as transforms
import math

def _largest_rotated_rect(w, h, angle):
"""
Given a rectangle of size wxh that has been rotated by 'angle' (in
radians), computes the width and height of the largest possible
axis-aligned rectangle within the rotated rectangle.
Original JS code by 'Andri' and Magnus Hoff from Stack Overflow
Converted to Python by Aaron Snoswell
Source: http://stackoverflow.com/questions/16702966/rotate-image-and-crop-out-black-borders
"""

quadrant = int(math.floor(angle / (math.pi / 2))) & 3
sign_alpha = angle if ((quadrant & 1) == 0) else math.pi - angle
alpha = (sign_alpha % math.pi + math.pi) % math.pi

bb_w = w * math.cos(alpha) + h * math.sin(alpha)
bb_h = w * math.sin(alpha) + h * math.cos(alpha)

gamma = math.atan2(bb_w, bb_w) if (w < h) else math.atan2(bb_w, bb_w)

delta = math.pi - alpha - gamma

length = h if (w < h) else w

d = length * math.cos(alpha)
a = d * math.sin(alpha) / math.sin(delta)

y = a * math.cos(gamma)
x = y * math.tan(gamma)

return (
    bb_w - 2 * x,
    bb_h - 2 * y
)


def _rotate_and_crop(image, output_height=32, output_width=32):
"""Rotate the given image with the given rotation degree and crop for the black edges if necessary. For my case, image sizes are 32x32.
Args:
    image: A Batch of Tensors- normally from a dataloader.
    output_height: The height of the image after preprocessing.
    output_width: The width of the image after preprocessing.
Returns:
    A rotated image.
"""

# Rotate the given image with the given rotation degree
rotation_transform = transforms.RandomRotation((0, 360))
angle_rot = rotation_transform.angle_rot #you will have to read it from the pytorch library

lrr_width, lrr_height = _largest_rotated_rect(output_height, output_width, math.radians(angle_rot))
croped_image = transforms.CenterCrop((lrr_height, lrr_width))
resize_transform = transforms.Resize(size=(output_height, output_width))

transform = transforms.Compose([rotation_transform, croped_image, resize_transform, transforms.RandomHorizontalFlip(),
                                               transforms.ToTensor(),
                                               ])

image = transform(image)

return image
