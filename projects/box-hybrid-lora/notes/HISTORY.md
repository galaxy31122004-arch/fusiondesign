# Box HybridLora - lịch sử thiết kế

Máy mặc định: Bambu Lab P2S Full Combo. Tất cả kích thước dưới đây tính bằng mm. Mỗi phiên bản có file Fusion riêng; các bản này là nguyên mẫu, chưa đạt yêu cầu chống nước hoặc sẵn sàng in ngoài trời.

| Phiên bản | F3D | 3MF | Thay đổi | Trạng thái |
| --- | --- | --- | --- | --- |
| v01 | [F3D](../design/box-hybrid-lora_v01.f3d) | [thân](../print/mesh/box-hybrid-lora_v01_body.3mf), [nắp](../print/mesh/box-hybrid-lora_v01_lid.3mf) | Thân 120 × 120 × 65, nắp phẳng dày 5, thành/đáy 3 | Đã xuất; chưa có lỗ, trụ, ron |
| v02 | [F3D](../design/box-hybrid-lora_v02.f3d) | [thân](../print/mesh/box-hybrid-lora_v02_body.3mf), [nắp](../print/mesh/box-hybrid-lora_v02_lid.3mf) | Thêm bo bốn góc ngoài R4 | Đã xuất; chưa kiểm tra lắp thực tế |
| v03 | [F3D](../design/box-hybrid-lora_v03.f3d) | [thân](../print/mesh/box-hybrid-lora_v03_body.3mf), [nắp](../print/mesh/box-hybrid-lora_v03_lid.3mf) | Thêm bốn trụ Ø5, cao hơn đáy trong 5; lỗ mù Ø2, sâu 4 | Đã slice PETG HF để thử; tọa độ ngang PCB là giả định; lỗ anten/nguồn chưa khoét |

## Bản đang làm

`v03` là bản mới nhất. Ngày 2026-10-20, document này đã được lưu trong **Fusion > Default Project** với tên cũ `box01_v3 - LoRa enclosure prototype`; Fusion API xác nhận `Saved: True`. Tên file trong repo đã đổi theo ID mới; tên document trên Fusion chưa đổi. Bản F3D local trong bảng là bản lưu độc lập để khôi phục. Sau khi tạo bản mới, đóng tab cũ theo [rule phiên bản](../../../docs/rules/versioning.md).

Ngày 2026-10-20, v03 đã có thêm [hai gói Bambu 3MF đã slice cho PETG HF](../print/sliced/README.md). Đây là file in thử bố cục, chưa phải bản vỏ dùng ngoài trời.

## Những điểm chưa chốt

- Vị trí tâm lỗ PCB theo phương ngang và khoảng hở của đầu vít, linh kiện phía dưới PCB.
- Kích thước lỗ xuyên vỏ của đầu SMA thực tế, O-ring và cách ép ron.
- Khoảng hở để cắm adapter trực tiếp vào jack DC và phương án chống mưa cho vị trí cắm.
- Vật liệu, màu, nozzle, profile, kết cấu nắp/ron và phép thử nước.

## Cách quay lại

Mở F3D của phiên bản cần dùng. Nếu sửa từ bản đó, xuất dưới mã phiên bản **mới** và ghi "khôi phục từ vNN" trong bảng; không ghi đè F3D cũ. Chạy lại kiểm tra hình học, vật liệu và preview slice theo cấu hình in hiện tại.
