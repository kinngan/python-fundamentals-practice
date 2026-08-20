def so_sanh_san_pham(sp_a, sp_b):
    dict_a = {san_pham['món']: san_pham for san_pham in sp_a}
    dict_b = {san_pham['món']: san_pham for san_pham in sp_b}

    tap_hop_a = set(dict_a.keys())
    tap_hop_b = set(dict_b.keys())

    chi_o_a = [dict_a[ma_so] for ma_so in (tap_hop_a - tap_hop_b)]
    chi_o_b = [dict_b[ma_so] for ma_so in (tap_hop_b - tap_hop_a)]

    mon_chung = tap_hop_a & tap_hop_b
    khac_gia = [dict_a[ma_so] for ma_so in mon_chung if dict_a[ma_so]['giá'] != dict_b[ma_so]['giá']]
    return chi_o_a, chi_o_b, khac_gia
if __name__ == "__main__":
    sp_a = [
        {'món': 1, 'là': 'gà rán', 'giá': 25},
        {'món': 2, 'là': 'bún riu', 'giá': 30},
        {'món': 3, 'là': 'mì ý', 'giá': 50}
    ]

    sp_b = [
        {'món': 2, 'là': 'bún riu', 'giá': 40},
        {'món': 3, 'là': 'mì ý', 'giá': 50},
        {'món': 4, 'là': 'bánh su kem', 'giá': 20}
    ]

    ket_qua_a, ket_qua_b, ket_qua_khac = so_sanh_san_pham(sp_a, sp_b)

    assert len(ket_qua_a) == 1 and ket_qua_a[0]['món'] == 1, "Kiểm tra sản phẩm chỉ có ở A bị lỗi"
    assert len(ket_qua_b) == 1 and ket_qua_b[0]['món'] == 4, "Kiểm tra sản phẩm chỉ có ở B bị lỗi"
    assert len(ket_qua_khac) == 1 and ket_qua_khac[0]['món'] == 2, "Kiểm tra sản phẩm khác giá bị lỗi"

    print("Chạy được")