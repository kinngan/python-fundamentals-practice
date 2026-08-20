import random


def doan_so():
    so_bi_mat = random.randint(1, 100)
    so_lan_doan = 0
    print("Đoán số")
    print("Nhập một số từ 1 đến 100.")
    print("Nhập 'ff' nếu bạn muốn dừng chơi.")

    while True:
        du_lieu_nhap = input("Số bạn đoán là: ").strip()
        if du_lieu_nhap.lower() == 'ff':
            print("eeeee, thua r nha")
            break
        if not du_lieu_nhap.isdigit():
            print("Nhập sai, nhập lại đi")
            continue

        so_doan = int(du_lieu_nhap)
        so_lan_doan += 1

        if so_doan < so_bi_mat:
            print("Số nhỏ z ní")
        elif so_doan > so_bi_mat:
            print("Số bự z ní")
        else:
            print(f"Đù ní đoán đúng số {so_bi_mat} sau {so_lan_doan} lần nhấp luôn nha.")
            break


if __name__ == "__main__":
    doan_so()