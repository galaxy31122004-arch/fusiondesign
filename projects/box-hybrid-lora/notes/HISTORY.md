# Box HybridLora - lịch sử thiết kế

Máy mặc định: Bambu Lab P2S Full Combo. Tất cả kích thước dưới đây tính bằng mm. Các bản này là nguyên mẫu, chưa đạt yêu cầu chống nước hoặc sẵn sàng in ngoài trời. Thư mục làm việc chỉ giữ bản F3D hiện tại; file cũ đã commit vẫn tìm được trong lịch sử Git.

| Phiên bản | Nguồn hiện có | Thay đổi | Trạng thái |
| --- | --- | --- | --- |
| v01 | F3D trong Git commit `2ac1473` | Thân 120 × 120 × 65, nắp phẳng dày 5, thành/đáy 3 | Chưa có lỗ, trụ, ron |
| v02 | F3D trong Git commit `2ac1473` | Thêm bo bốn góc ngoài R4 | Chưa kiểm tra lắp thực tế |
| v03 | F3D và hai gói Bambu trong Git; Fusion Default Project | Thêm bốn trụ Ø5, cao hơn đáy trong 5; lỗ mù Ø2, sâu 4 | Tọa độ ngang PCB là giả định; lỗ anten/nguồn chưa khoét |
| v1.0.0 (tên làm việc cũ: v04) | [F3D hiện tại](../design/box-hybrid-lora_v1.0.0.f3d) | Thân 146 × 146 × 68; vành và rãnh ron nhỏ trên thân, bốn vít nắp, bốn tai bắt vỏ, lỗ SMA góc phải, nắp bo viền | Đã xuất mesh đúng mm; slice thử nhưng chưa có gói Bambu mới đã kiểm tra |

## Bản đang làm

`v1.0.0` là nhãn thiết kế hiện tại theo yêu cầu người dùng; tên làm việc `v04` trong Fusion/Git commit `a8fb4ca` trỏ tới cùng hình học. F3D local đã xuất ngày 2026-10-20 và đổi tên theo rule mới. Document đang mở trong Fusion còn hiện `Unsaved`; cần lưu vào Fusion Default Project nếu muốn có lịch sử cloud. Bản v03 đã lưu trong Fusion Default Project dưới tên cũ `box01_v3 - LoRa enclosure prototype`; F3D v03 vẫn truy xuất được từ Git. Áp dụng [rule phiên bản](../../../docs/rules/versioning.md) khi thay đổi tiếp.

Ngày 2026-10-20, v03 từng có hai gói Bambu 3MF đã slice cho PETG HF. Chúng **không khớp hình học v1.0.0**, nên đã xóa khỏi thư mục làm việc; lấy lại bằng Git commit `a8fb4ca` khi cần đối chiếu. Mesh xuất lần đầu vẫn mang tên `v04` trong `runs/mesh/`; đó là file kiểm tra tạm, chưa là file in.

## Những điểm chưa chốt

- Vị trí tâm lỗ PCB theo phương ngang và khoảng hở của đầu vít, linh kiện phía dưới PCB.
- Kích thước lỗ xuyên vỏ của đầu SMA thực tế, O-ring và cách ép ron.
- Khoảng hở để cắm adapter trực tiếp vào jack DC và phương án chống mưa cho vị trí cắm.
- Màu nhựa, dây ron thực tế và phép thử nước. PETG HF, nozzle 0,4 mm và Textured PEI đã chọn cho bản in thử.

## Cách quay lại

Với v1.0.0, mở F3D local hoặc document sau khi lưu vào Fusion. Với v03, mở document đã lưu trong Fusion hoặc lấy F3D từ Git; với v01/v02, lấy F3D từ Git commit `2ac1473`. Ghi rõ mốc khôi phục trong bảng và slice lại; G-code v03 không dùng cho hình học v1.0.0.
