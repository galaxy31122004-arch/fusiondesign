# Fusion scripts

Các script nguyên mẫu cho [Box HybridLora](../../projects/box-hybrid-lora/README.md) tạo document mới theo từng phiên bản. Tên thư mục Python dùng dấu gạch dưới; file F3D/3MF dùng ID project `box-hybrid-lora`.

| Script | Kết quả |
| --- | --- |
| [v01](box_hybrid_lora_v01/box_hybrid_lora_v01.py) | Thân và nắp phẳng sơ bộ |
| [v02](box_hybrid_lora_v02/box_hybrid_lora_v02.py) | Thêm bo góc ngoài R4 |
| [v03](box_hybrid_lora_v03/box_hybrid_lora_v03.py) | Thêm bốn trụ PCB Ø5 với lỗ mù Ø2 |

Mở **Utilities > Scripts and Add-Ins** trong Fusion, chọn script tương ứng rồi **Run**. Script xuất F3D vào `design/`, mesh 3MF vào `print/mesh/` và báo cáo cục bộ vào `runs/`. Nó không ghi đè phiên bản đã có. Lịch sử và trạng thái lắp/in nằm trong [HISTORY.md](../../projects/box-hybrid-lora/notes/HISTORY.md) và [results.md](../../projects/box-hybrid-lora/notes/results.md).

Các script v01-v03 là mã dựng lại bản cũ, chưa hỗ trợ sửa trực tiếp document đang mở. v03 đóng tab cũ của đúng project sau khi xuất thành công và sao lưu tab có thay đổi chưa lưu. Document v03 trên Fusion Default Project vẫn mang tên lịch sử `box01_v3 - LoRa enclosure prototype`; tên file repo đã thống nhất theo ID mới.
