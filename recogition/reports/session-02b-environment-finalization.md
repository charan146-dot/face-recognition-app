# Session 02B — Environment Finalization

## Objective
Finish installation and verification of `face_recognition`.

## Initial State
Before installation:

```text
cv2       → working
numpy     → working
pytest    → working
face_recognition → missing
```

The active Python executable and pip were verified to belong to the project's
`.venv`:

- Python: `C:\Users\chara\OneDrive\Desktop\facerecoginiton\recogition\.venv\Scripts\python.exe`
- Python version: 3.11.0
- pip: 26.2.1 from the same `.venv`

## Installation
Ran `python -m pip install face_recognition` with the project virtual
environment active. Pip downloaded `face_recognition` 1.3.0 and attempted to
build its `dlib` dependency (20.0.1) from source as required. The build failed
during CMake configuration. CMake reported:

```text
You must use Visual Studio to build a python extension on windows.
If you are getting this error it means you have not installed Visual C++.
```

The attempted build selected `NMake Makefiles` and stopped before producing or
installing the `dlib` wheel. `face_recognition` was therefore not installed.
No global packages, alternate package, unofficial wheel, or Python downgrade
were used.

## Dependency Versions
- Python: 3.11.0
- OpenCV (`opencv-python`): 4.11.0
- NumPy: 1.26.4
- dlib: not installed; attempted source version 20.0.1
- face_recognition: not installed
- pytest: 9.1.1

## Validation

`python -m pip check`:

```text
No broken requirements found.
Exit code: 0
```

`python src\verify_environment.py`:

```text
Python: 3.11.0
opencv-python: OK (4.11.0)
face_recognition: IMPORT FAILED (No module named 'face_recognition')
numpy: OK (1.26.4)
Environment NOT READY. Packages that failed: face_recognition
Exit code: 1
```

`python -m pytest`:

```text
1 failed, 2 passed
Failed: tests\test_environment.py::test_required_package_is_importable[face_recognition]
ModuleNotFoundError: No module named 'face_recognition'
Exit code: 1
```

The `dlib` and `face_recognition` import checks were not run because pip did
not install either package.

## Problems
The Microsoft C++ build environment was not available to CMake for the dlib
source build. The attempted installation stopped at CMake configuration with
the Visual Studio / Visual C++ requirement message. The dependency remains
uninstalled, so environment verification and the associated import test fail.

## Current Project Status
> The development environment remains blocked. Application development must not begin yet.

## Next Session
Resolve the Visual Studio C++ Build Tools detection/configuration issue, then
retry installing `face_recognition` in this `.venv` and rerun all environment
checks. Do not begin application development unless verification reports the
environment is ready and all three tests pass.
