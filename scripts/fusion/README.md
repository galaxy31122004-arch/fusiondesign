# Fusion script

[box_hybrid_lora.py](box_hybrid_lora/box_hybrid_lora.py) là script hiện tại cho [Box HybridLora](../../projects/box-hybrid-lora/README.md): dựng thân và nắp R4 cùng bốn trụ PCB Ø5/lỗ mù Ø2. Mã script cũ vẫn có trong lịch sử Git commit `2ac1473`, không để nhiều bản script trong thư mục làm việc.

Mở **Utilities > Scripts and Add-Ins**, chọn `box_hybrid_lora` rồi **Run**. Script hiện tạo document mới từ đầu, không sửa document đang mở. Nó xuất một F3D dự phòng ở `design/`, mesh trung gian ở `runs/mesh/` và báo cáo ở `runs/`; không ghi đè F3D đã có. Sau khi chuyển mesh qua Bambu Studio và kiểm tra gói slice, xóa mesh trung gian. Lịch sử và giới hạn nằm trong [HISTORY.md](../../projects/box-hybrid-lora/notes/HISTORY.md) và [results.md](../../projects/box-hybrid-lora/notes/results.md).

Document v03 trên Fusion Default Project vẫn mang tên lịch sử `box01_v3 - LoRa enclosure prototype`; tên file repo đã thống nhất theo ID mới. Khi phát triển script tiếp, sửa file hiện tại và dùng Git history để quay lại mã cũ.
