# Shortener, written in Flask

## Technology
- Flask
- Flask WTF
- Flask SQLAlchemy

## Installation
1. Clone repo 
2. Creating venv
   ```shell
   python3 -m venv venv
   
   # windows
   venv/Scripts/activate.bat
   
   # Unix like
   . venv/bin/activate
   ```
3. Install deps
   ```shell
   pip install -r requirements.txt
   ```
4. Setup `.env` file
   ```shell
   SECRET_KEY="SECRET_KEY"
   DATABASE_URI="sqlite3:///db.sqlite"
   ```
5. Run project
   ```shell
   flask run
   ```