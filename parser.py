import re
from collections import Counter
import os
import sys
import random

def tao_file_log(ten_file="access.log", so_dong=300):
    danh_sach_ip = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4", "10.0.0.5", "10.0.0.6", "10.0.0.7", "10.0.0.8", "10.0.0.9", "10.0.0.10"]
    danh_sach_phuong_thuc = ["GET", "POST"]
    danh_sach_duong_dan = ["/", "api/users", "login", "products"]
    danh_sach_trang_thai = [200, 401, 404]
    with open(ten_file, "w", encoding="utf-8") as tep:
        for i in range(so_dong):
            dia_chi_ip = random.choice(danh_sach_ip)
            phuong_thuc = random.choice(danh_sach_phuong_thuc)
            duong_dan = random.choice(danh_sach_duong_dan)
            trang_thai = random.choice(danh_sach_trang_thai)
            giay = f"{(i %59)+ 1:02d}"
            dong_log = f'{dia_chi_ip} -- [11/Aug/2026:10:00:{giay} +0700] "{phuong_thuc} {duong_dan}" {trang_thai}\n'
            tep.write(dong_log)

def phan_tich_log(ten_file="access.log"):
     if not os.path.exists(ten_file):
        tao_file_log(ten_file,300)
     mau_log = re.compile(
         r'^(?P<dia_chi_ip>\S+) \S+ \S+ \[(?P<thoi_gian>[^\]]+)\] "(?P<phuong_thuc>\S+) (?P<duong_dan>\S+)" (?P<trang_thai>\d+)'
     )

     danh_sach_ip = []
     danh_sach_trang_thai = []
     danh_sach_duong_dan = []

     with open(ten_file, "r", encoding="utf-8") as tep:
         for dong in tep:
             khop = mau_log.match(dong.strip())
             if khop:
                 du_lieu = khop.groupdict()
                 danh_sach_ip.append(du_lieu['dia_chi_ip'])
                 danh_sach_duong_dan.append(du_lieu['duong_dan'])
                 danh_sach_trang_thai.append(du_lieu['trang_thai'])

     top_5_ip = Counter(danh_sach_ip).most_common(5)
     thong_ke_trang_thai = Counter(danh_sach_trang_thai)
     duong_dan_nhieu_nhat = Counter(danh_sach_duong_dan).most_common(1)

     print("Sau khi phân tích")

     print("1.top 5 địa chỉ IP truy cập nhiều nhất:\n")
     for dia_chi_ip, so_lan in top_5_ip:
         print(f"địa chỉ IP: {dia_chi_ip} ({so_lan} lần)")

     print("2.số lượng yêu cầu theo từng trạng thái:\n")
     for trang_thai, so_lan in thong_ke_trang_thai.items():
         print(f"trạng thái {trang_thai}: {so_lan} yêu cầu")

     print("3.đường dẫn bị gọi nhiều nhất:\n")
     if duong_dan_nhieu_nhat:
         print(f"đường dẫn: {duong_dan_nhieu_nhat[0][0]} ({duong_dan_nhieu_nhat[0][1]} lần)")


if __name__ == "__main__":
    file_dau_vao = sys.argv[1] if len(sys.argv) > 1 else "access.log"
    phan_tich_log(file_dau_vao)