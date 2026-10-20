# Box HybridLora - checklist

Áp dụng [rule khả năng in](../../../docs/rules/printability.md) và [rule vật liệu](../../../docs/rules/material.md). Bằng chứng theo từng lần kiểm tra nằm trong [results.md](results.md).

| Rule ID | Kiểm tra | Trạng thái hiện tại | Điều kiện để đóng |
| --- | --- | --- | --- |
| BOX-001 | PCB 100 × 100 mm có khoảng hở lắp, không va thành/nắp | Chưa xác minh | Lắp thử PCB và đo khoảng hở linh kiện |
| BOX-002 | Trụ và lỗ bắt PCB không chạm linh kiện/đường mạch | Chưa xác minh | Xác nhận tọa độ ngang, đầu vít và mặt dưới PCB |
| BOX-003 | Nắp và đường ghép chống mưa tạt | Chưa xác minh | Chốt ron, kết cấu khóa và thử nước |
| BOX-004 | Anten xuyên vỏ đúng vị trí và kín nước | Chưa chốt | Chốt đầu SMA, lỗ panel, O-ring và thử lắp |
| BOX-005 | Jack nguồn 12 V xuyên vỏ đúng vị trí và kín nước | Chưa chốt | Chốt đầu cắm, lỗ vỏ và cách làm kín |
| BOX-006 | Vật liệu và profile P2S phù hợp | Đạt ở mức slice thử | Xác nhận màu, plate/nozzle đang lắp và thử in |
| BOX-007 | Hướng lắp ngoài trời và đường nước chảy | Chưa chốt | Có tư thế lắp và kiểm tra đọng nước |
| BOX-008 | Bo góc giữ độ dày thành và khoảng hở | Kiểm tra mesh sơ bộ | Đo thành, nắp, PCB và lỗ sau bo trên mẫu thật |

**Cảnh báo dùng thử:** bản v03 đã slice thành công nhưng chưa có lỗ anten, lỗ nguồn, ron hoặc khóa nắp. Chỉ dùng để thử kích thước và lắp ráp; không đặt mạch ngoài mưa.

## Trong Fusion

- [ ] Đo khoảng hở PCB/linh kiện, nhất là khu vực jack nguồn và anten.
- [ ] Đối chiếu bốn trụ Ø5/lỗ mù Ø2 với PCB thật trước khi bắt vít.
- [ ] Thiết kế, đo và thử đường ghép nắp, ron và vít.
- [ ] Kiểm tra lỗ anten/nguồn không cắt vào PCB, trụ hay đường ron.
- [ ] Đo lại thành và khoảng hở sau khi bo góc hoặc đổi tham số.

## Trước và sau in

- [ ] Xác nhận tấm Textured PEI và nozzle 0,4 mm đang lắp, cuộn PETG HF và màu thực tế.
- [ ] Mở gói 3MF trong Bambu Studio, xem preview từng lớp, support, đáy, thành và lỗ mù.
- [ ] In thử, lắp PCB/anten/nguồn và đo độ khít; ghi kết quả vào `results.md`.
- [ ] Sau khi hoàn thiện vỏ, thử nước trên vỏ không cấp điện rồi ghi điểm rò; chưa công bố mức IP khi chưa có phép thử tương ứng.
