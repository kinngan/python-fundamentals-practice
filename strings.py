def normalize_name(raw):
    danh_sach_tu = raw.split()
    ten_da_chuan_hoa = " ".join([tu.capitalize() for tu in danh_sach_tu])
    return ten_da_chuan_hoa

assert normalize_name(" nGuYỄN vĂn a ") == "Nguyễn Văn A"
assert normalize_name("   thiên   DƯƠNG   ") == "Thiên Dương"
assert normalize_name("trần hà linh") == "Trần Hà Linh"
assert normalize_name("eM    bUồn   NgỦ qUá") == "Em Buồn Ngủ Quá"
assert normalize_name("    ") == ""

print("ok")