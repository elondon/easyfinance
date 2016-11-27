#!/bin/bash
cd /home/easyfinance-api/app
source /home/easyfinance-api/.venv/bin/activate
gunicorn easyfinance:app -w 3 -b localhost:8000 --user=easyfinance-api --access-logfile=/home/easyfinance-api/logs/access.log --error-logfile=/home/easyfinance-api/logs/error.log
