@echo off
set /p notebook_name=Enter the name for the new notebook (without extension): 
set notebook_name=%notebook_name%.ipynb
python -c "import json; json.dump({'cells': [], 'metadata': {}, 'nbformat': 4, 'nbformat_minor': 5}, open('%notebook_name%', 'w'))"
echo Notebook '%notebook_name%' has been created in %cd%.
pause
