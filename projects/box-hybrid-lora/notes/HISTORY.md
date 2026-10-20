# Box HybridLora - lịch sử thiết kế

Máy mặc định: Bambu Lab P2S Full Combo. Tất cả kích thước dưới đây tính bằng mm. Các bản này là nguyên mẫu, chưa đạt yêu cầu chống nước hoặc sẵn sàng in ngoài trời. Thư mục làm việc chỉ giữ bản F3D hiện tại; file cũ đã commit vẫn tìm được trong lịch sử Git.

| Phiên bản | Nguồn hiện có | Thay đổi | Trạng thái |
| --- | --- | --- | --- |
| v01 | F3D trong Git commit `2ac1473` | Thân 120 × 120 × 65, nắp phẳng dày 5, thành/đáy 3 | Chưa có lỗ, trụ, ron |
| v02 | F3D trong Git commit `2ac1473` | Thêm bo bốn góc ngoài R4 | Chưa kiểm tra lắp thực tế |
| v03 | F3D trong Git và Fusion Default Project; [gói Bambu để in thử](../print/sliced/README.md) | Thêm bốn trụ Ø5, cao hơn đáy trong 5; lỗ mù Ø2, sâu 4 | Tọa độ ngang PCB là giả định; lỗ anten/nguồn chưa khoét |
| v04 | [F3D hiện tại](../design/box-hybrid-lora_v04.f3d) | Thân 146 × 146 × 68; vành và rãnh ron nhỏ trên thân, bốn vít nắp, bốn tai bắt vỏ, lỗ SMA góc phải, nắp bo viền | Đã xuất mesh đúng mm; chưa slice và chưa thử lắp/độ kín |

## Bản đang làm

`v04` là bản thiết kế mới nhất, đã xuất F3D local ngày 2026-10-20. Document v04 đang mở trong Fusion và còn hiện `Unsaved`; cần lưu vào Fusion Default Project nếu muốn tiếp tục bằng lịch sử cloud. Bản v03 đã lưu trong Fusion Default Project dưới tên cũ `box01_v3 - LoRa enclosure prototype`; F3D v03 vẫn truy xuất được từ Git. Áp dụng [rule phiên bản](../../../docs/rules/versioning.md) khi thay đổi tiếp.

Ngày 2026-10-20, v03 đã có [hai gói Bambu 3MF đã slice cho PETG HF](../print/sliced/README.md). Chúng **không khớp hình học v04** và chỉ là file in thử bố cục cũ. Mesh v04 nằm trong `runs/mesh/` để kiểm tra, chưa là file in.

## Những điểm chưa chốt

- Vị trí tâm lỗ PCB theo phương ngang và khoảng hở của đầu vít, linh kiện phía dưới PCB.
- Kích thước lỗ xuyên vỏ của đầu SMA thực tế, O-ring và cách ép ron.
- Khoảng hở để cắm adapter trực tiếp vào jack DC và phương án chống mưa cho vị trí cắm.
- Màu nhựa, dây ron thực tế và phép thử nước. PETG HF, nozzle 0,4 mm và Textured PEI đã chọn cho bản in thử.

## Cách quay lại

Với v04, mở F3D local hoặc document sau khi lưu vào Fusion. Với v03, mở document đã lưu trong Fusion hoặc lấy F3D từ Git; với v01/v02, lấy F3D từ Git commit `2ac1473`. Ghi "khôi phục từ vNN" trong bảng và slice lại; G-code v03 không dùng cho hình học v04.
