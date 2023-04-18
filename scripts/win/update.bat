@echo off

cd ../../

git pull
call ./venv/Scripts/activate.bat
pip install -r requirements.txt --upgrade