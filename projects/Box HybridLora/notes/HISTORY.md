# Box HybridLora - lịch sử thiết kế

Máy mặc định: Bambu Lab P2S Full Combo. Tất cả kích thước dưới đây tính bằng mm. Mỗi phiên bản có file Fusion riêng; các bản này là nguyên mẫu, chưa đạt yêu cầu chống nước hoặc sẵn sàng in ngoài trời.

| Phiên bản | F3D | 3MF | Thay đổi | Trạng thái |
| --- | --- | --- | --- | --- |
| v01 | [box01_prototype.f3d](../design/box01_prototype.f3d) | [thân](../print/mesh/box01_body_prototype.3mf), [nắp](../print/mesh/box01_lid_prototype.3mf) | Thân 120 × 120 × 65, nắp phẳng dày 5, thành/đáy 3 | Đã xuất; chưa có lỗ, trụ, ron |
| v02 | [box01_v2.f3d](../design/box01_v2.f3d) | [thân](../print/mesh/box01_body_v2.3mf), [nắp](../print/mesh/box01_lid_v2.3mf) | Thêm bo bốn góc ngoài R4 | Đã xuất; chưa kiểm tra lắp thực tế |
| v03 | [box01_v3.f3d](../design/box01_v3.f3d) | [thân](../print/mesh/box01_body_v3.3mf), [nắp](../print/mesh/box01_lid_v3.3mf) | Thêm bốn trụ Ø5, cao hơn đáy trong 5; lỗ mù Ø2, sâu 4 | Đã xuất; chưa có file slice hợp lệ; tọa độ ngang PCB là giả định; lỗ anten/nguồn chưa khoét |

## Bản đang làm

`v03` là bản mới nhất. Ngày 2026-10-20, document này cũng đã được lưu trong **Fusion > Default Project** với tên `box01_v3 - LoRa enclosure prototype`; Fusion API xác nhận `Saved: True`. Bản F3D local trong bảng là bản lưu độc lập để khôi phục. Sau khi tạo bản mới, đóng tab cũ theo [rule phiên bản](../../../docs/rules/versioning.md).

## Những điểm chưa chốt

- Vị trí tâm lỗ PCB theo phương ngang và khoảng hở của đầu vít, linh kiện phía dưới PCB.
- Kích thước lỗ xuyên vỏ của đầu SMA thực tế, O-ring và cách ép ron.
- Khoảng hở để cắm adapter trực tiếp vào jack DC và phương án chống mưa cho vị trí cắm.
- Vật liệu, màu, nozzle, profile, kết cấu nắp/ron và phép thử nước.

## Cách quay lại

Mở F3D của phiên bản cần dùng. Nếu sửa từ bản đó, xuất dưới mã phiên bản **mới** và ghi "khôi phục từ vNN" trong bảng; không ghi đè F3D cũ. Chạy lại kiểm tra hình học, vật liệu và preview slice theo cấu hình in hiện tại.
