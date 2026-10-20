# Box HybridLora - lịch sử thiết kế

Máy mặc định: Bambu Lab P2S Full Combo. Tất cả kích thước dưới đây tính bằng mm. Các bản này là nguyên mẫu, chưa đạt yêu cầu chống nước hoặc sẵn sàng in ngoài trời. Thư mục làm việc chỉ giữ bản F3D hiện tại; file cũ đã commit vẫn tìm được trong lịch sử Git.

| Phiên bản | Nguồn hiện có | Thay đổi | Trạng thái |
| --- | --- | --- | --- |
| v01 | F3D trong Git commit `2ac1473` | Thân 120 × 120 × 65, nắp phẳng dày 5, thành/đáy 3 | Chưa có lỗ, trụ, ron |
| v02 | F3D trong Git commit `2ac1473` | Thêm bo bốn góc ngoài R4 | Chưa kiểm tra lắp thực tế |
| v03 | [F3D hiện tại](../design/box-hybrid-lora_v03.f3d), [gói Bambu để in thử](../print/sliced/README.md), Fusion Default Project | Thêm bốn trụ Ø5, cao hơn đáy trong 5; lỗ mù Ø2, sâu 4 | Tọa độ ngang PCB là giả định; lỗ anten/nguồn chưa khoét |

## Bản đang làm

`v03` là bản mới nhất. Ngày 2026-10-20, document này đã được lưu trong **Fusion > Default Project** với tên cũ `box01_v3 - LoRa enclosure prototype`; Fusion API xác nhận `Saved: True`. Tên file trong repo đã đổi theo ID mới; tên document trên Fusion chưa đổi. Bản F3D local trong bảng là bản dự phòng. Sau khi tạo bản mới, áp dụng [rule phiên bản](../../../docs/rules/versioning.md) và dọn file xuất cũ.

Ngày 2026-10-20, v03 đã có [hai gói Bambu 3MF đã slice cho PETG HF](../print/sliced/README.md). Mesh trung gian và log CLI đã được dọn sau khi ghi kết quả; đây là file in thử bố cục, chưa phải bản vỏ dùng ngoài trời.

## Những điểm chưa chốt

- Vị trí tâm lỗ PCB theo phương ngang và khoảng hở của đầu vít, linh kiện phía dưới PCB.
- Kích thước lỗ xuyên vỏ của đầu SMA thực tế, O-ring và cách ép ron.
- Khoảng hở để cắm adapter trực tiếp vào jack DC và phương án chống mưa cho vị trí cắm.
- Màu nhựa, kết cấu nắp/ron và phép thử nước. PETG HF, nozzle 0,4 mm và Textured PEI đã chọn cho bản in thử.

## Cách quay lại

Với v03, mở document đã lưu trong Fusion hoặc F3D local. Với v01/v02, lấy F3D từ Git commit `2ac1473`, mở trong Fusion rồi lưu thành phiên bản mới. Ghi "khôi phục từ vNN" trong bảng và slice lại; G-code v03 không dùng cho hình học cũ.
