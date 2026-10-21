# Box HybridLora - checklist

Áp dụng [rule khả năng in](../../../docs/rules/printability.md), [rule vật liệu](../../../docs/rules/material.md) và [rule hộp ngoài trời](../../../docs/rules/outdoor-enclosure.md). Bằng chứng theo từng lần kiểm tra nằm trong [results.md](results.md).

| Rule ID | Kiểm tra | Trạng thái hiện tại | Điều kiện để đóng |
| --- | --- | --- | --- |
| BOX-001 | PCB 100 × 100 mm có khoảng hở lắp, không va thành/nắp | Chưa xác minh | Lắp thử PCB và đo khoảng hở linh kiện |
| BOX-002 | Trụ và lỗ bắt PCB không chạm linh kiện/đường mạch | Chưa xác minh | Xác nhận tọa độ ngang, đầu vít và mặt dưới PCB |
| BOX-003 | Nắp và đường ghép chống mưa tạt | Có rãnh/vít nguyên mẫu v1.0.0; chưa xác minh | Chốt ron, kiểm tra độ ép và thử nước |
| BOX-004 | Anten xuyên vỏ đúng vị trí và kín nước | Có lỗ SMA thử v1.0.0; chưa xác minh | Đo đầu SMA, lỗ panel, O-ring và thử lắp |
| BOX-005 | Jack nguồn 12 V xuyên vỏ đúng vị trí và kín nước | Chưa chốt | Chốt đầu cắm, lỗ vỏ và cách làm kín |
| BOX-006 | Vật liệu và profile P2S phù hợp | Slice thử v1.0.0; chưa có gói in | Xem preview GUI, xác nhận màu/plate/nozzle thực và xuất gói 3MF |
| BOX-007 | Hướng lắp ngoài trời và đường nước chảy | Chưa chốt | Có tư thế lắp và kiểm tra đọng nước |
| BOX-008 | Bo góc giữ độ dày thành và khoảng hở | Mesh kín, chưa thử lắp | Đo thành, nắp, PCB và lỗ sau bo trên mẫu thật |
| BOX-009 | Vành trong thân in được và tháo support được | Đã xem Preview `tree(auto)`; chưa lưu gói in hoặc thử tháo | So kiểu support theo [rule chung](../../../docs/rules/support-selection.md), xem từng lớp và in thử vùng vành/ron |

**Cảnh báo dùng thử:** bản v1.0.0 có lỗ anten và rãnh ron nhỏ nhưng chưa đo đầu SMA, chưa chọn ron, chưa có lỗ/giải pháp kín cho nguồn DC và chưa có gói Bambu chứa G-code đã xác minh. Hai file `print/prepare/` để mở/chỉnh trong Studio, không phải file gửi máy. Không đặt mạch ngoài mưa.

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
