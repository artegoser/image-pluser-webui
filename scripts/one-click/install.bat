@echo off

git clone https://github.com/artegoser/image-pluser-webui.git
cd image-pluser-webui
python -m venv venv
call ./venv/Scripts/activate.bat
pip install -r requirements.txt