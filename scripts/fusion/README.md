# Fusion scripts

Thư mục dành cho script Fusion API tạo và chỉnh model tham số. [box01_prototype.py](box01_prototype/box01_prototype.py) tạo một bản vỏ sơ bộ với kích thước tạm; bản này chưa có chi tiết lắp PCB, lỗ đầu nối hay đường làm kín.

Để chạy trong Fusion: mở **Utilities > Scripts and Add-Ins**, chọn `box01_prototype` rồi **Run**. Nếu script chưa có trong danh sách, chọn **Add > Script or add-in from device** và trỏ tới thư mục `scripts/fusion/box01_prototype`. Script tạo document mới và xuất `.f3d` vào `projects/Box HybridLora/design/`, hai file `.3mf` riêng cho thân và nắp vào `print/mesh/`, và log vào `runs/`. Script không ghi đè file xuất đã có.

Script đã chạy trong Fusion ngày 2026-10-20. Kết quả và giới hạn của bản sơ bộ được ghi tại [checks.md](../../projects/Box%20HybridLora/notes/checks.md). Trước khi chạy lại, lưu hoặc chuyển các file xuất hiện có sang một phiên bản khác; script sẽ không ghi đè chúng.

[box01_v2.py](box01_v2/box01_v2.py) đã tạo bản bo góc ngoài R4. [box01_v3.py](box01_v3/box01_v3.py) đã tạo thêm bốn trụ Ø5 với lỗ mù Ø2 theo thông số PCB. Các lỗ xuyên vỏ vẫn chưa thêm vì kích thước lắp thực tế chưa đủ. Lịch sử và đường dẫn các bản xuất nằm trong [HISTORY.md](../../projects/Box%20HybridLora/notes/HISTORY.md).

Các script nguyên mẫu hiện tạo document mới cho mỗi phiên bản; chưa hỗ trợ sửa trực tiếp model hiện có. Từ phiên bản mới, script đặt tên tab, xuất F3D/3MF rồi đóng tab cũ của `box01` theo [rule phiên bản](../../docs/rules/versioning.md). Tab cũ có chỉnh sửa được sao lưu riêng trước khi đóng. Chỉ khi đủ số đo lắp thật mới phát triển bước sửa model hiện có.

Document `box01_v3` đã được lưu thêm trong Fusion `Default Project` với tên `box01_v3 - LoRa enclosure prototype`. Các phiên bản script kế tiếp phải lưu document trong Fusion và ghi trạng thái `isSaved`, đồng thời giữ F3D local để quay lại bản cũ.
