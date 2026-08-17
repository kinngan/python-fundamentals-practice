import re
from collections import Counter


def dem_tan_suat_tu(van_ban):
    """
    Hàm nhận vào đoạn văn bản, trả về từ điển (dict) đếm số lần xuất hiện của từ
    và in ra top 10 từ xuất hiện nhiều nhất.
    """
    van_ban_chu_thuong = van_ban.lower()
    van_ban_sach_dau_cau = re.sub(r'[^\w\s]', '', van_ban_chu_thuong)
    danh_sach_tu = van_ban_sach_dau_cau.split()
    so_luong_tu = Counter(danh_sach_tu)

    print("--- Top 10 từ xuất hiện nhiều nhất ---")
    for tu, so_lan in so_luong_tu.most_common(10):
        print(f"Từ '{tu}': {so_lan} lần")

    return dict(so_luong_tu)


doan_van_mau = """
    Thanh xuân của mỗi người thường được đo bằng những năm tháng ngồi dưới giảng đường đại học, bằng những buổi chiều nắng vàng rực rỡ hắt qua khung cửa sổ phòng thí nghiệm, hay bằng những rung động đầu đời trong trẻo mà sâu sắc. Đối với Bạch Lăng Khê, khoảng thời gian ấy gắn liền với một cái tên, một hình bóng mà thoạt đầu chỉ tồn tại qua những dòng tin nhắn ẩn hiện trên màn hình máy tính: "Yêu phi bất khả cứu" – Dương Lam Hàng.

Họ gặp nhau trong thế giới ảo nhưng lại chạm đến trái tim nhau bằng thứ chân tình thật nhất. Anh là một giáo sư tài hoa, một nhà khoa học với tư duy logic sắc bén, tưởng chừng như trái tim đã bị đóng băng bởi những công thức khô khan và những tiêu chuẩn nghiêm ngặt của giới học thuật. Còn cô là một cô gái sinh viên khoa sợi, tinh nghịch, lãng mạn và đôi khi có chút vụng về. Khoảng cách giữa họ không chỉ là hàng vạn cây số địa lý khi anh ở tận nước Mỹ xa xôi còn cô ở trong nước, mà còn là khoảng cách của học vị, của tuổi tác và của cả những định kiến xã hội lúc bấy giờ.

Có những đêm, dưới ánh đèn bàn heo hắt, Lăng Khê nhìn chằm chằm vào màn hình, tự hỏi liệu thứ tình cảm này có thực sự có kết quả hay chỉ là một ảo ảnh đẹp đẽ được dệt nên bởi sự cô đơn. Thế nhưng, chính sự kiên nhẫn, dịu dàng và âm thầm bảo bọc của anh đã từng bước phá vỡ lớp vỏ bọc lo âu của cô. Anh biến mọi khoảng cách trở nên nhỏ bé bằng sự quan tâm tỉ mỉ, bằng những lời khuyên chân thành trong học tập và cuộc sống, và trên hết là bằng một lời hứa không cần thề thốt đao to búa lớn nhưng lại nặng tựa thái sơn.

"Dương Lam Hàng, mãi mãi là bao xa?" – đó từng là câu hỏi chứa đựng đầy sự hoài nghi, bất an của một cô gái trẻ đứng trước ngưỡng cửa tình yêu đầy biến động. Đối với một người nghiên cứu khoa học như anh, khái niệm "mãi mãi" vốn dĩ là một biến số không thể đo lường bằng các định luật vật lý hay toán học. Thế nhưng, câu trả lời của anh lại giản dị đến nao lòng: "Từ đây cho đến trái tim em, chính là mãi mãi."

Khoảnh khắc anh thực sự bước ra từ thế giới ảo, đứng trước mặt cô bằng xương bằng thịt tại góc phố quen thuộc, mọi khoảng cách không gian bỗng chốc thu bé lại vừa đúng bằng một cái ôm. Những giọt nước mắt tủi hờn của sự chờ đợi, những đêm dài đằng đằng nhớ nhung cuối cùng cũng được đền đáp trọn vẹn bằng hơi ấm thực sự từ bàn tay anh. Hóa ra, tình yêu đích thực không sợ khoảng cách, không sợ thời gian, bởi vì khi hai trái tim đã hướng về nhau, thì dù biên giới có xa xôi đến đâu, hai người cuối cùng vẫn sẽ tìm thấy đường về bên nhau.

Câu chuyện tình yêu ấy khép lại nhưng dư âm của nó vẫn đọng lại mãi trong lòng những ai từng lật từng trang sách. Nó dạy cho chúng ta biết cách kiên nhẫn chờ đợi một người, biết trân trọng những chân tình ẩn giấu sau bề ngoài lạnh lùng, và quan trọng nhất là dám dũng cảm bước qua mọi giới hạn để chạm đến hạnh phúc đích thực của đời mình.
    """

ket_qua = dem_tan_suat_tu(doan_van_mau)