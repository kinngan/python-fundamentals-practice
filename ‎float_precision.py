from decimal import Decimal

tong_float = 0.1 + 0.2
print(f"0.1 + 0.2 = {tong_float}")
print(f"so sanh (0.1 + 0.2 == 0.3: {tong_float == 0.3})")

tong_decimal = Decimal('0.1') + Decimal('0.2')
print(f"0.1 + 0.2 = {tong_decimal}")
print(f"so sanh (0.1 + 0.2 == 0.3: {tong_decimal == Decimal('0.3')})")

#máy tính lưu dữ liệu ở nhị phân trong khi mấy số 0.1 0.2 là thập phân
#float trong python lưu trữ 64 bit nên cộng mấy này sai số ở cuối, 0.1+0.2 không ra được 0.3 tại nó làm tròn bị sai số
#tại có sai số nhỏ nên ở trên ra false