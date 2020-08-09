#!/bin/bash

python3 -m venv pmenu_venv;
source pmenu_venv/bin/activate;
pip install -r requirements.txt;
PyInstaller pmenu.py --onefile;
cp .pmenu.ini $HOME/.pmenu.ini;
rm -rf pmenu_venv
sudo cp dist/pmenu /usr/local/bin/pmenu;
pmenu "welcome to" pmenu app press escape "to exit"
