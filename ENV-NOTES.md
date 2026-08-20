# Hai môi trường, hai phiên bản
### Project 1 (requests 2.28.0)
cd project1
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install requests==2.28.0
python -c "import requests; print(requests.__version__)"
## Project 2 (request 2.34.2)
cd project2
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install requests
python -c "import requests; print(requests.__version__)"

# Tái tạo môi trường từ requirements.txt
các bước em làm :
1. em tạo môi trường bằng lệnh : python -m venv kinvenv
2. sau đó em kích hoạt môi trường: .\kinvenv\Scripts\Activate.ps1
3. em cài 3 cái package: pip install requests pandas rich
4. làm cho cái cấu hinh thành file thì em : pip freeze > requirements.txt
5. cái em bấm vô file kinvenv xóa file
6. tạo môi trường như bước 1 2 em đặt tên khác thêm số 2:python -m venv kinvenv2  ||  .\kinvenv2\Scripts\Activate.ps1  ||  pip install -r requirements.txt
7. em bấm pip freeze để check phiên bản của cái môi trường em mới tạo thấy nó khớp với file requirements.txt mới lưu