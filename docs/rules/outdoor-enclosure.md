# Rule cho hộp điện tử ngoài trời

Áp dụng cho các hộp chứa mạch điện tử tiếp xúc mưa, bụi hoặc nước tạt. Đây là quy trình kiểm tra thiết kế, không phải chứng nhận IP hay bảo đảm kín nước.

1. Đường ron giữa thân và nắp phải **liên tục** và bao quanh khoang điện tử. Bố trí lỗ vít nắp ở **phía ngoài** đường ron hoặc thiết kế phương án làm kín riêng cho từng lỗ đi vào vùng được bảo vệ. Kiểm tra tại mọi góc và đoạn giao với tai/trụ.
2. Chọn ron thực tế trước khi chốt rãnh: tiết diện, vật liệu, độ cứng và cách nối hai đầu nếu dùng dây ron. Ghi kích thước rãnh, mức ép dự kiến và dung sai từ datasheet hoặc mẫu thử của đúng ron. Rãnh vẽ bằng kích thước giả định chỉ được ghi là mẫu thử.
3. Mỗi lỗ xuyên vỏ (anten, nguồn, nút, cáp) cần linh kiện/đường làm kín riêng. O-ring của một đầu nối không làm kín cho lỗ khác; đầu DC cắm trực tiếp không tự có khả năng chống mưa. Xác nhận vùng phẳng để ép gioăng, hướng lắp và khoảng hở thao tác.
4. Kiểm tra mặt tiếp xúc ron sau khi in: rãnh không bị mất trong preview, bề mặt không có đường hở/biến dạng lớn, không bị vít làm nắp cong. Thử lắp và quan sát ron có bị lệch/kẹp đứt không.
5. Chỉ đánh dấu đạt yêu cầu chống nước sau khi thử trên vỏ **không cấp điện**, với cách thử phù hợp tình huống sử dụng và ghi rõ điểm rò, hướng nước, thời gian cùng bản model. Không công bố cấp IP nếu chưa thử theo phương pháp tương ứng.

Khi một mục thiếu số đo hoặc mẫu thử, báo `Chưa xác minh` trong checklist của project ngay từ lúc thiết kế. Không dùng kết quả slice thành công để đóng cảnh báo kín nước.
