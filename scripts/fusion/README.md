# Fusion script

[box_hybrid_lora.py](box_hybrid_lora/box_hybrid_lora.py) là script v04 hiện tại cho [Box HybridLora](../../projects/box-hybrid-lora/README.md): dựng thân, nắp bo mép, trụ PCB, vít nắp, tai bắt ngoài, rãnh dây ron nhỏ trên thân và lỗ SMA thử. Mã script cũ vẫn có trong lịch sử Git, không để nhiều bản script trong thư mục làm việc.

Mở **Utilities > Scripts and Add-Ins**, chọn `box_hybrid_lora` trỏ tới thư mục repo rồi **Run**. Script tạo document mới từ đầu, không sửa document đang mở. Nó xuất một F3D local ở `design/`, mesh trung gian ở `runs/mesh/` và báo cáo ở `runs/`; không ghi đè F3D đã có. Document mới còn `Unsaved` trong Fusion; lưu vào Fusion Default Project nếu cần lịch sử cloud. Sau khi chuyển mesh qua Bambu Studio và kiểm tra gói slice, xóa mesh trung gian. Lịch sử và giới hạn nằm trong [HISTORY.md](../../projects/box-hybrid-lora/notes/HISTORY.md) và [results.md](../../projects/box-hybrid-lora/notes/results.md).

Document v03 trên Fusion Default Project vẫn mang tên lịch sử `box01_v3 - LoRa enclosure prototype`. Nếu cần chạy lại script v04, trước tiên lưu/chuyển F3D v04 hiện có vào lịch sử hoặc chọn tên phiên bản mới; script chủ động dừng khi phát hiện file xuất trùng tên.
