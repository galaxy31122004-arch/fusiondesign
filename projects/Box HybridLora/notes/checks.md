# Box HybridLora — kiểm tra thiết kế và in

Áp dụng [rule khả năng in](../../../docs/rules/printability.md) và [rule vật liệu](../../../docs/rules/material.md). Các mục dưới đây là kiểm tra riêng cho hộp mạch LoRa ngoài trời. Trạng thái ban đầu là **Chưa kiểm tra** hoặc **Chưa xác minh**, chưa được xem là đạt.

## Trước khi thiết kế

| Rule ID | Kiểm tra | Trạng thái | Điều kiện để đóng |
| --- | --- | --- | --- |
| BOX-001 | PCB 100 × 100 mm có khoảng hở lắp, không va thành hoặc nắp | Chưa chốt | Có kích thước bo, vị trí linh kiện và khoảng hở được duyệt |
| BOX-002 | Vị trí giữ PCB không chạm linh kiện hoặc đường mạch | Chưa chốt | Đã biết 4 lỗ PCB Ø2 mm, hai tâm trên một cạnh cách 94,679 mm và tâm dưới cách mép 2,436 mm; cần xác nhận tọa độ ngang, vùng đầu vít và mặt PCB trước khi in |
| BOX-003 | Nắp và đường ghép thân–nắp phù hợp với mưa tạt trực tiếp | Chưa xác minh | Chốt kết cấu, ron, vật liệu và kế hoạch thử nước |
| BOX-004 | Anten ra góc trên phải, lỗ xuyên vỏ được làm kín | Chưa chốt | Có kích thước cụm anten/ron và cách lắp thực tế |
| BOX-005 | Dây nguồn 12 V ra góc dưới trái, lỗ xuyên vỏ được làm kín | Chưa chốt | Có kích thước dây/đầu nối và cách lắp thực tế |
| BOX-006 | Vật liệu phù hợp mục đích ngoài trời và profile P2S | Chưa chọn | Có tên cuộn, màu, nozzle, bàn in và profile khớp |
| BOX-007 | Cách lắp hộp ngoài trời, hướng nước chảy và chỗ có thể đọng nước | Chưa chốt | Có tư thế lắp thực tế và phương án kiểm tra |
| BOX-008 | Bo bốn góc ngoài của thân và nắp không làm mỏng thành hoặc cản lắp PCB, nắp, lỗ | Chưa kiểm tra | Có model sau bo, đo lại thành và khoảng hở; bán kính được duyệt |

`box01_v2.py` và `box01_v3.py` đã chạy trong Fusion. Mesh v3 của thân và nắp dùng đơn vị mm, kích thước bao ngoài lần lượt là 120 × 120 × 65 mm và 120 × 120 × 5 mm; khi kiểm tra các cạnh tam giác của hai mesh, không có cạnh biên hoặc cạnh không manifold. Kết quả này chỉ xác nhận file mesh kín về mặt hình học, không xác nhận độ kín nước hoặc khả năng in đạt.

- **BOX-002, trong Fusion, chưa xác minh:** v3 có bốn trụ Ø5 với lỗ mù Ø2, sâu 4 mm; tọa độ tâm ghi tại [params.md](params.md). Phương ngang và vùng đầu vít còn giả định; cần đặt PCB thật hoặc đo trực tiếp trước khi in sử dụng.
- **BOX-008, trong Fusion, kiểm tra hình học sơ bộ:** v3 có bo góc ngoài R4 ở thân và nắp, hai mesh không có cạnh biên. Chưa kiểm tra ảnh hưởng lên nắp/ron, khoảng hở linh kiện và vật liệu in; chưa đóng rule này.
- **BOX-004/BOX-005, trước in, chưa chốt:** v3 chưa khoét lỗ anten hoặc jack DC. Cần kích thước lắp xuyên vỏ, vị trí theo PCB thật và giải pháp chống mưa trước khi tạo feature cắt.
- **MAT-001, cập nhật 2026-10-20:** người dùng đã chọn Bambu PETG HF, nozzle 0,4 mm cho bản in thử; màu và loại bàn in thực tế chưa biết. Cảnh báo về plate vẫn mở; chưa có file in được xác nhận.
- **MAT-002/PRT-008, slice CLI thử, không đạt:** Bambu Studio CLI tạo `plate_1.gcode` cho thân nhưng metadata ghi `filament_type = PLA`, `gcode_flavor = marlin`, `filament_density = 0` và `curr_bed_type = Cool Plate` dù lệnh chọn preset PETG HF/P2S. File này đã chuyển vào `runs/invalid_cli_slice/` (không phát hành, không in). Cần nạp đầy đủ preset kế thừa, xác nhận plate đang lắp, kiểm tra lại G-code và preview trước khi tạo file in mới.

**Cảnh báo sớm:** thiết kế hộp hở đã nêu ở ví dụ ban đầu không đáp ứng mục đích chịu mưa tạt trực tiếp; `box01` phải có nắp và xử lý các lỗ xuyên vỏ. Ron cao su được mô tả nhưng chưa đủ dữ liệu để kết luận kín nước. Đầu nối IPEX ở phía mạch không thay thế việc làm kín tại thành hộp.

## Kết quả bản dựng sơ bộ 2026-10-20

- **BOX-001, trong Fusion, chưa xác minh:** thân ngoài 120 × 120 × 65 mm, shell thành/đáy danh nghĩa 3 mm. Lòng hộp danh nghĩa 114 × 114 mm, tức khoảng hở mỗi cạnh 7 mm nếu PCB 100 × 100 mm đặt giữa. Chưa có file PCB và số đo linh kiện để xác nhận lắp vừa. Bằng chứng: `box01_prototype.f3d`, mesh `box01_body_prototype.3mf` (mm; giới hạn X/Y 0–120, Z 0–65). Người chấp nhận rủi ro: chưa có.
- **BOX-003, trong Fusion, chưa xác minh:** nắp là tấm phẳng 120 × 120 × 5 mm, chưa có ngàm, vít, rãnh ron hoặc phép thử nước. Bằng chứng: `box01_prototype.f3d`, mesh `box01_lid_prototype.3mf` (mm; giới hạn X/Y 0–120, Z 0–5). Không dùng bản dựng này ngoài trời. Người chấp nhận rủi ro: chưa có.
- **MAT-001, trước in, chưa xác minh:** chưa chọn cuộn vật liệu, màu, nozzle, bàn in hoặc profile thực tế. Chưa kiểm tra 3MF trong Bambu Studio hoặc slice. Người chấp nhận rủi ro: chưa có.

Các file mesh chỉ chứng minh kích thước xuất và hình học sơ bộ; chưa có kết quả lắp PCB, kín nước hay in thử. Nếu sửa tham số hoặc chọn vật liệu, đánh giá lại ba mục trên và thêm bản ghi mới.

**Nguồn bổ sung 2026-10-20:** người dùng xác nhận bốn lỗ PCB đường kính 2 mm và gửi ảnh cho hai lỗ cùng cạnh; tọa độ tâm chưa xác nhận. Thư viện có [SOMECONN SC-RG178-IPEX-SMAF](../../../library/components/ipex-sma-rg178/component.json) và [YIC IPEX-1.13B-150-SMAF](../../../library/components/ipex-sma-yic/component.json) là hai bản vẽ khác nhau; đầu SMA YIC có O-ring nhưng chưa có đường kính lỗ xuyên panel được chỉ định. Jack DC [trong thư viện](../../../library/components/dc-jack/component.json) là loại chân hàn PCB; người dùng muốn cắm adapter trực tiếp qua thành hộp, cách làm kín khi mưa tạt chưa xác định. BOX-002, BOX-004 và BOX-005 vẫn `Chưa chốt`; chưa thể đặt trụ/lỗ sản xuất.

**Hiệu chỉnh số đo PCB:** ảnh chi tiết ghi 94,679 mm tâm–tâm và 2,436 mm từ tâm dưới tới mép dưới. Tâm trên tới mép trên là 2,885 mm nếu PCB cao đúng 100 mm. Trước đó phần mô tả "tọa độ tâm chưa xác nhận" áp dụng cho phương ngang và ba lỗ còn lại, không áp dụng cho hai số đo vừa nêu.

## Trong khi dựng trong Fusion

- [ ] Đo lại kích thước trong lòng hộp và khoảng hở quanh toàn bộ PCB, đặc biệt vùng domino nguồn và anten.
- [ ] Kiểm tra trụ/điểm giữ PCB với file hoặc số đo lỗ thật; không đặt trụ dựa trên ảnh không có tọa độ.
- [ ] Kiểm tra đường ghép nắp, rãnh ron, vị trí vít và phần ép ron theo đúng linh kiện làm kín đã chọn.
- [ ] Kiểm tra lỗ anten và lỗ nguồn không cắt vào trụ, PCB, đường ghép nắp hoặc nhau.
- [ ] Kiểm tra bán kính bo góc của thân và nắp; đo lại thành, khoảng hở PCB và vị trí lỗ sau khi bo.
- [ ] Kiểm tra model sau mỗi thay đổi tham số; chạy lại các rule vật liệu và khả năng in bị ảnh hưởng.

## Trước khi in và sau khi in thử

- [ ] So kích thước và số part giữa Fusion và Bambu Studio; xác nhận đúng vật liệu và profile P2S.
- [ ] Xem preview lớp đầu, thành, đáy, nắp, lỗ và rãnh ron; ghi vùng support hoặc chi tiết bị mất.
- [ ] In mẫu, lắp PCB, anten, dây nguồn và ron; đo độ khít và khả năng thao tác bảo trì.
- [ ] Thử nước bằng quy trình phù hợp khi mạch không cấp điện và có biện pháp bảo vệ mạch; ghi vị trí nước lọt nếu có. Chưa công bố mức IP nếu chưa thử theo phương pháp tương ứng.
- [ ] Ghi lỗi in hoặc lỗi lắp thực tế cùng vật liệu, nozzle, profile, hướng đặt và bản model để sửa có căn cứ.

## Bản ghi kết quả theo rule ID

Tạo **một bản ghi cho mỗi lần đánh giá** một rule `BOX-*`, `MAT-*` hoặc rule chung có ID. Giữ bản ghi cũ khi model, vật liệu hay profile thay đổi; thêm bản ghi mới để thấy điều gì đã được kiểm tra lại. Checklist ở trên chỉ là danh sách việc cần làm, không thay thế kết quả đo.

```text
Rule ID:
Ngày kiểm tra:
Giai đoạn: trước thiết kế / trong Fusion / sau slice / sau in thử
Phiên bản model và file liên quan:
Máy, nozzle, vật liệu, màu, bàn in, profile:
Vị trí hoặc feature được kiểm tra:
Giá trị đo được và đơn vị / dữ liệu còn thiếu:
Điều kiện áp dụng và ngưỡng dùng để so sánh:
Nguồn bằng chứng: file/ảnh, phép đo, preset hoặc tài liệu; ngày nguồn
Kết quả: đạt / cảnh báo / chưa xác minh / không áp dụng
Rủi ro còn lại và tác động:
Hành động sửa trong Fusion hoặc Bambu Studio:
Cách và kết quả kiểm tra lại:
Người thực hiện:
Người chấp nhận rủi ro còn lại và ngày chấp nhận: chưa có nếu chưa được chấp nhận
```

Một kết quả `Đạt` cần có giá trị đo và bằng chứng phù hợp. `Chưa xác minh` không được đổi thành `Đạt` chỉ vì model dựng được hoặc slice thành công. Nếu người dùng chấp nhận rủi ro, ghi rõ phiên bản model và điều kiện in được chấp nhận; việc chấp nhận không biến rủi ro thành đã khắc phục.
