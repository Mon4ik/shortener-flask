# Shortener, written in Flask

## Technology
- Flask
- Flask WTF
- Flask SQLAlchemy

## Installation
1. Clone repo
2. Install deps
   ```shell
   pip install -r requirements.txt
   ```
3. Setup `.env` file
   ```shell
   SECRET_KEY="SECRET_KEY"
   DATABASE_URI="sqlite3:///db.sqlite"
   ```
4. Run project
   ```shell
   flask run
   ```