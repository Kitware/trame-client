import random
import numpy as np
from PIL import Image
import pytest

from trame_client.utils.testing import assert_images_match


def test_assert_images_match(ref_dir):
    ref_image_path = ref_dir.joinpath("ref1.png")
    assert ref_image_path.exists()

    image = Image.open(ref_image_path)
    assert_images_match(image, ref_image_path, 0.0)

    W, H = image.size
    target_error = int(0.09 * H * W)
    coordinates = [
        (int(random.random() * H), int(random.random() * W))
        for _ in range(target_error)
    ]
    np_img = np.array(image)
    for y, x in coordinates:
        np_img[y, x] = random.randint(0, 255)
    assert_images_match(Image.fromarray(np_img), ref_image_path, 0.1)

    with pytest.raises(AssertionError):
        assert_images_match(Image.fromarray(np_img), ref_image_path, 0.05)
