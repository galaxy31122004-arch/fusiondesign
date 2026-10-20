# Box HybridLora - kết quả kiểm tra

Mỗi lần đánh giá rule tạo bản ghi mới. [checks.md](checks.md) chỉ giữ checklist và trạng thái hiện tại. Slice thành công không xác nhận khả năng chống nước hoặc lắp PCB thực tế.

## Bản dựng v01, 2026-10-20

- **BOX-001, chưa xác minh:** thân ngoài 120 × 120 × 65 mm, thành/đáy danh nghĩa 3 mm; lòng hộp danh nghĩa 114 × 114 mm, khoảng hở mỗi cạnh 7 mm nếu PCB đặt giữa. Chưa đo vùng linh kiện. Bằng chứng: F3D và mesh v01. Người chấp nhận rủi ro: chưa có.
- **BOX-003, chưa xác minh:** nắp phẳng 120 × 120 × 5 mm, chưa có khóa, ron hoặc thử nước. Bằng chứng: F3D và mesh v01.
- **MAT-001, chưa xác minh:** lúc dựng v01 chưa chọn vật liệu, nozzle, plate hoặc profile; chưa slice.

## Bản dựng v03, 2026-10-20

- **BOX-002, chưa xác minh:** bốn trụ Ø5 mm, lỗ mù Ø2 mm sâu 4 mm; tọa độ ở [params.md](params.md). Phương ngang và vùng đầu vít còn giả định; cần đo PCB thật.
- **BOX-008, kiểm tra sơ bộ:** thân/nắp bo ngoài R4; mesh v03 dùng mm, kích thước bao 120 × 120 × 65 mm và 120 × 120 × 5 mm, không thấy cạnh biên hoặc cạnh không manifold. Chưa kiểm tra lắp nắp/ron hoặc độ bền in.
- **BOX-004/BOX-005, chưa chốt:** chưa khoét lỗ anten và jack DC; chưa có dữ liệu lắp xuyên vỏ hoặc giải pháp chống mưa.
- **BOX-002, dữ liệu PCB:** người dùng xác nhận bốn lỗ Ø2 mm. Ảnh chi tiết cho hai tâm cùng cạnh cách 94,679 mm và tâm dưới cách mép 2,436 mm. Tâm trên cách mép trên 2,885 mm nếu PCB cao đúng 100 mm. Tọa độ ngang chưa có kích thước trực tiếp.
- **BOX-004, linh kiện:** bản vẽ SOMECONN và YIC là hai mã cáp khác nhau. Bản YIC có O-ring nhưng không chỉ định lỗ panel; chưa xác nhận mã cáp thực tế.
- **BOX-005, linh kiện:** jack DC chân hàn PCB, người dùng muốn cắm adapter trực tiếp qua vỏ; chưa xác định lỗ cắm và cách làm kín khi mưa tạt.

## Vật liệu và slice, 2026-10-20

- **MAT-001:** người dùng chọn Bambu PETG HF và nozzle 0,4 mm để in thử. Màu chưa xác định.
- **MAT-002:** ảnh người dùng gửi ghi `Bambu Textured PEI Plate`; preset PETG HF trên máy ghi 70°C cho plate này. Cần xác nhận đúng tấm đang lắp trước khi in.
- **MAT-002/PRT-008, lần CLI đầu không đạt:** G-code ghi `filament_type = PLA`, `filament_density = 0`, `curr_bed_type = Cool Plate` do CLI chưa nạp `inherits`/`include`. File ở `runs/invalid_cli_slice/`, không dùng để in.
- **MAT-002/PRT-008, slice lại đạt ở mức slicer:** thân/nắp dùng profile P2S 0,4 mm, PETG HF, Textured PEI, layer 0,20 mm đã giải quyết đầy đủ kế thừa. Hai lần slice có `return_code = 0` và không có warning. G-code trong [hai gói in thử](../print/sliced/README.md) ghi đúng P2S/PETG/plate, density 1,28 g/cm³, bàn 70°C. Thumbnail cho thấy thân đặt đáy xuống, nắp nằm phẳng. Ước tính thân 2 giờ 16 phút/105,2 g; nắp 51 phút/39,9 g. Chưa xem từng lớp trong GUI, xác nhận màu, lắp PCB hoặc in thử.

## Mẫu bản ghi tiếp theo

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

Kết quả `Đạt` cần giá trị đo và bằng chứng phù hợp. Chấp nhận rủi ro phải gắn với phiên bản model và cấu hình in cụ thể.
