# Fusion script

[box_hybrid_lora.py](box_hybrid_lora/box_hybrid_lora.py) là script `v1.0.0` hiện tại cho [Box HybridLora](../../projects/box-hybrid-lora/README.md): dựng thân, nắp bo mép, trụ PCB, vít nắp, tai bắt ngoài, rãnh dây ron nhỏ trên thân và lỗ SMA thử. Mã script cũ vẫn có trong lịch sử Git, không để nhiều bản script trong thư mục làm việc.

ID thư mục project là `box-hybrid-lora` (tên file và link); tên module Fusion/Python là `box_hybrid_lora` vì identifier Python không dùng dấu gạch nối. Cả hai trỏ cùng một project.

`box_hybrid_lora.manifest` là manifest Fusion cần có ở cạnh script: `autodeskProduct`, `type`, `author`, `description`, `supportedOS`, `version` và `editEnabled`. `version` của manifest là phiên bản script tích hợp, không tự thay version model của project. Khi script chạy, báo cáo/mesh tạm đi vào `projects/box-hybrid-lora/runs/<yyyymmdd>-<mục-đích>/` theo [rule file](../../docs/rules/versioning.md); các giá trị cần giữ (tham số, tọa độ, file xuất, lỗi, kết quả kiểm tra) phải chép sang `notes/results.md`, không lấy log tạm làm nguồn lâu dài.

Mở **Utilities > Scripts and Add-Ins**, chọn `box_hybrid_lora` trỏ tới thư mục repo rồi **Run**. Script tạo document mới từ đầu, không sửa document đang mở. Nó xuất một F3D local ở `design/`, mesh trung gian ở `runs/mesh/` và báo cáo ở `runs/`; không ghi đè F3D đã có. Document mới còn `Unsaved` trong Fusion; lưu vào Fusion Default Project nếu cần lịch sử cloud. Sau khi chuyển mesh qua Bambu Studio và kiểm tra gói slice, xóa mesh trung gian. Lịch sử và giới hạn nằm trong [HISTORY.md](../../projects/box-hybrid-lora/notes/HISTORY.md) và [results.md](../../projects/box-hybrid-lora/notes/results.md).

Document v03 trên Fusion Default Project vẫn mang tên lịch sử `box01_v3 - LoRa enclosure prototype`. Document hiện mở trong Fusion vẫn mang tên `v04` từ lúc tạo, còn F3D local đã chuẩn hóa thành `v1.0.0`; đây là cùng một hình học. Nếu cần chạy lại script, trước tiên lưu/chuyển F3D hiện có vào lịch sử; script chủ động dừng khi phát hiện file xuất trùng tên.
