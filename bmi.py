def tinh_bmi():
    try:
        chieu_cao = float(input("Nhập chiều cao (m): "))
        can_nang = float(input("Nhập cân nặng (kg): "))

        if chieu_cao <= 0 or can_nang <= 0:
            print("Lỗi")
            return

        chi_so_bmi = can_nang / (chieu_cao ** 2)

        if chi_so_bmi < 18.5:
            phan_loai = "gầy"
        elif 18.5 <= chi_so_bmi < 25:
            phan_loai = "bình thường"
        else:
            phan_loai = "thừa cân"

        print(f"Chỉ số BMI: {chi_so_bmi:.2f}")
        print(f"Phân loại: {phan_loai}")

    except ValueError:
        print("Lỗi")