import importlib

import pytest


@pytest.mark.parametrize("module_name", ("cv2", "face_recognition", "numpy"))
def test_required_package_is_importable(module_name: str) -> None:
    importlib.import_module(module_name)
