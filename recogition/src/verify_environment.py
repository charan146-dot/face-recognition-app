"""Check that the project's required Python packages can be imported."""

import importlib
import platform
import sys


REQUIRED_MODULES = {
    "cv2": "opencv-python",
    "face_recognition": "face_recognition",
    "numpy": "numpy",
}


def main() -> int:
    print(f"Python: {platform.python_version()}")
    failures = []

    for module_name, package_name in REQUIRED_MODULES.items():
        try:
            module = importlib.import_module(module_name)
        except (ImportError, OSError) as error:
            failures.append(package_name)
            print(f"{package_name}: IMPORT FAILED ({error})")
        else:
            version = getattr(module, "__version__", "version unavailable")
            print(f"{package_name}: OK ({version})")

    if failures:
        print(f"Environment NOT READY. Packages that failed: {', '.join(failures)}")
        return 1

    print("Environment READY.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
