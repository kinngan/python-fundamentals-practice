## Project 1 (requests 2.28.0)
```powershell
cd project1
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install requests==2.28.0
python -c "import requests; print(requests.__version__)"

cd project2
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install requests
python -c "import requests; print(requests.__version__)"