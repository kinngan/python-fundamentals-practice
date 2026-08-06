def tinh_bmi():
    try:
        chieu_cao = float(input("Chiều cao của bạn (m): "))
        can_nang = float(input("Cân nặng của bạn là (kg): "))
        bmi = can_nang / (chieu_cao ** 2)
        if bmi < 18.5:
            phan_loai = "ốm"
        elif 18.5 <= bmi < 25:
            phan_loai = "bình thường"
        else:
            phan_loai = "mập"
        print(f"Chỉ số BMI: {bmi:.2f}") #2f:lay 2 chu so sau thap phan
        print(f"Phân loại: {phan_loai}")

    except ValueError:
        print("Lỗi ròi bạn ơi, nhập lại đi")
tinh_bmi()