# Face Recognition App

A beginner Python project setup for a future face recognition app. The project
currently includes development-environment verification only; face detection
and recognition are not implemented.

## Project structure

```text
facerecoginiton/
|-- .venv/                 # Local Python virtual environment (created on this computer)
|-- data/
|   |-- known_faces/        # Reference images can go here in a later session
|   `-- test_images/        # Test images can go here in a later session
|-- reports/                # Session reports
|-- src/                    # Environment verification script
|-- tests/                  # Automated import test
|-- .gitignore
|-- README.md
|-- requirements.txt        # Application dependencies
`-- requirements-dev.txt    # Application and development dependencies
```

## Session reports

Save a plain-text report in `reports/` at the end of each project session. Use
a descriptive name in the format `session-NN-short-topic.txt`, for example
`session-01-development-environment-verification.txt`. Include completed work,
validation results, any blockers, and follow-up steps.

## Activate the virtual environment

Open a PowerShell terminal in this project folder. The existing `.venv` uses
Python 3.11. If you need to create it again on another computer, run:

```powershell
py -3.11 -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can skip activation and run project commands using `.\.venv\Scripts\python.exe` directly. The virtual environment keeps this project's packages separate from other Python projects.

## Install the libraries

With the virtual environment active, install the application and development
dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

`requirements.txt` lists OpenCV (`opencv-python`), `face_recognition`, and
NumPy. The `numpy<2` limit avoids compatibility surprises with older packages
in this stack. `requirements-dev.txt` includes pytest for the import test.

### Windows prerequisite for `face_recognition`

`face_recognition` depends on `dlib`, which contains a native C++ extension.
When pip cannot find a compatible prebuilt `dlib` wheel, it builds `dlib` from
source. On Windows, install Microsoft Visual Studio Build Tools with the
**Desktop development with C++** workload (including the MSVC C++ build tools
and a Windows SDK) before installing the project dependencies. Then open a new
PowerShell terminal, activate `.venv`, and run the install command above.

## Verify the installation

Run the environment verification script:

```powershell
python src\verify_environment.py
```

Run the automated import test with:

```powershell
python -m pytest
```

Both checks require all three packages to import successfully. On Windows,
installing `face_recognition` may fail while building its `dlib` dependency if
compatible Visual C++ build tools or a wheel are unavailable.

## What's next

The next session can start with a small camera/image-loading check. Face detection and recognition functionality will be added only after that step is discussed.
