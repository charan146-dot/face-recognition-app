# Session 02 — Environment Blocker Resolution

## Objective

Resolve the `face_recognition` installation blocker in the project's existing
Python 3.11 virtual environment without replacing the dependency or starting
application implementation.

## Initial Problem

`face_recognition` depends on `dlib`. pip downloaded the `dlib` 20.0.1 source
archive and attempted to build its native C++ extension. The build stopped
during CMake configuration because Visual C++ build tools are not installed.

## Diagnosis

- Python: 3.11.0
- Operating system: Windows
- Architecture: AMD64 / 64-bit
- pip: 26.2.1 from the project's `.venv`
- Installed versions: NumPy 1.26.4 and opencv-python 4.11.0.86
- `pip show dlib` and `pip show face-recognition`: neither package is
  installed.
- `cl`, `cmake`, and `nmake` were not found on the current command PATH.
- A pip binary-only download probe found no compatible `dlib` wheel in the
  configured package index.
- Retried `python -m pip install face_recognition`. pip selected
  `dlib-20.0.1.tar.gz`; building its wheel failed with:

  > You must use Visual Studio to build a python extension on windows. If you
  > are getting this error it means you have not installed Visual C++.

## Resolution

The blocker remains unresolved. No unofficial wheel was installed, no package
was removed or substituted, and project requirements were left unchanged.

Manual action required: install Microsoft Visual Studio Build Tools with the
**Desktop development with C++** workload, including MSVC C++ build tools and
a Windows SDK. Then start a new PowerShell terminal, activate the project
`.venv`, and run:

```powershell
python -m pip install -r requirements-dev.txt
```

If that installation fails, retain the full error output; do not bypass the
native build or install packages globally.

The requested reference
`reports/session-01-environment-setup.md` did not exist. The available prior
session record was `reports/session-01-development-environment-verification.txt`.

## Validation

All checks below were run with the existing project `.venv` after updating the
installation guidance in `README.md`.

- `python -m pip check`: passed — `No broken requirements found.`
- `python src\verify_environment.py`: failed with exit code 1. OpenCV 4.11.0
  and NumPy 1.26.4 imported; `face_recognition` import failed because the
  package is not installed. Result: `Environment NOT READY`.
- `python -m pytest`: 2 passed, 1 failed. The `face_recognition` import test
  failed with `ModuleNotFoundError: No module named 'face_recognition'`.
- `python -c "import cv2; print(cv2.__version__)"`: passed — `4.11.0`.
- `python -c "import numpy; print(numpy.__version__)"`: passed — `1.26.4`.
- `python -c "import face_recognition; print(face_recognition.__version__)"`:
  failed with `ModuleNotFoundError: No module named 'face_recognition'`.

## Files Changed

- `README.md` — documented the Windows Visual Studio C++ Build Tools
  prerequisite for installing `dlib` / `face_recognition`.
- `reports/session-02-environment-blocker-resolution.md` — this report.

## Current Project Status

The development environment is **not ready** for application development
because the required `face_recognition` package cannot yet be imported. The
existing `.venv` remains in use; no face detection, recognition, camera, or
image pipeline functionality was implemented.

## Next Session

Before Session 3, install Microsoft Visual Studio Build Tools with the **Desktop
development with C++** workload, including MSVC and a Windows SDK. Then install
the dependencies into `.venv` and rerun the verification script and pytest.
Do not begin application or input-pipeline implementation until all required
environment checks pass.
