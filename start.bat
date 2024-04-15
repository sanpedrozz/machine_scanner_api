@echo off
timeout /t 60
cd "C:\scanner_api"
call "C:\venv\Scripts\activate"
pip install -r requirements.txt
uvicorn run:app --host 0.0.0.0 --port 8000
pause
