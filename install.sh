#!/bin/bash

python3.6 -m venv pmenu_venv;
source pmenu_venv/bin/activate;
pip install --upgrade pip && pip install -r requirements.txt;
python3.6 -m PyInstaller pmenu/pmenu.py --onefile;
cp pmenu/.pmenu.ini $HOME/.pmenu.ini;
sudo cp dist/pmenu /usr/local/bin/pmenu;
pmenu "welcome to" pmenu app press escape "to exit"
