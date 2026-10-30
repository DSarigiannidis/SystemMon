# SystemMon

Small tkinter GUI that shows live CPU and RAM usage, built with Python and psutil.

## Run from source

    pip install psutil
    python3 SystemMon.py

## Build (Linux)

    python -m PyInstaller --noconfirm --onedir --windowed --name SystemMon SystemMon.py

## Package as .deb

Copy `dist/SystemMon/*` into `pkg/opt/systemmon/`, then:

    dpkg-deb --build --root-owner-group pkg systemmon_1.0.0_amd64.deb
    sudo apt install ./systemmon_1.0.0_amd64.deb

## Uninstall

    sudo apt remove systemmon
