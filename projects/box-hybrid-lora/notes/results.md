# Box HybridLora - kết quả kiểm tra

## V1.0.0 (tên làm việc v04) - bố trí Fusion, 2026-10-20

- **Nguồn model:** script tham số `scripts/fusion/box_hybrid_lora/box_hybrid_lora.py`; F3D local `design/box-hybrid-lora_v1.0.0.f3d`. Script khóa gốc sketch ngoài tại `(0, 0)` và tâm các lỗ/tai, rồi từ chối xuất nếu footprint thân/nắp lệch hoặc tai bắt không nối thành một khối.
- **Hình học đã đo từ hai mesh 3MF Fusion trong `runs/mesh/`:** đơn vị `millimeter`; mỗi file có một đối tượng. Thân có giới hạn X = -11,466 đến 157,466 mm (gồm tai), Y = 0 đến 146 mm, Z = 0 đến 68 mm. Nắp X/Y = 0 đến 146 mm, Z = 0 đến 5 mm. Mesh là file kiểm tra tạm, chưa slice.
- **Bố trí dự kiến:** bốn tâm vít nắp `(10,5; 10,5)`, `(135,5; 10,5)`, `(10,5; 135,5)`, `(135,5; 135,5)` mm; rãnh dây ron nhỏ ở vành thân, nằm phía trong lỗ vít; lỗ SMA Ø6,6 mm thử ở thành phải, Y = 122, Z = 55 mm. Các tâm và đường kính là tham số/script, **chưa đo lại trên mẫu vật lý**.
- **Còn mở:** chưa có dây ron thực tế, chưa thử độ ép/kín nước, chưa thử lắp đầu SMA, chưa có phương án kín nước cho nguồn DC cắm trực tiếp. Chưa có gói Bambu mới đã xác minh cho v1.0.0, chưa phải vỏ dùng ngoài trời.

## V1.0.0 - kiểm tra mesh và slice thử, 2026-10-20

- **MeshRight 0.2.0, chỉ kiểm tra hình học:** adapter `scripts/printing/check_mesh.py` đọc hai mesh xuất từ Fusion. Thân: 3.296 tam giác, một khối kín, bbox 168,932 × 146 × 68 mm (gồm tai). Nắp: 2.084 tam giác, một khối kín, 146 × 146 × 5 mm. Không có issue topology. Điểm `100/100` và khối lượng PLA đặc do MeshRight tính **không dùng** để kết luận khả năng in P2S; support/vật liệu/độ kín vẫn kiểm tra riêng. Báo cáo JSON tạm ở `runs/mesh_check_v1.0.0.json` ([MeshRight CLI](https://github.com/Huzy85/MeshRight/blob/main/src/meshright/cli.py), đọc 2026-10-20; RSCH-20261020-0005).
- **Bambu Studio 02.08.02.61, P2S 0,4 mm, PETG HF, Textured PEI:** G-code thử ghi lớp 0,20 mm, nozzle 230°C lớp đầu/245°C sau đó, plate 70°C, 2 vòng thành, infill 15%, `auto_brim` với bề rộng profile 5 mm và khe 0,1 mm. Đây là thông số hiệu lực từ lần slice CLI trên máy, chưa xác nhận cuộn/màu hoặc plate đang lắp vật lý.
- **Thân không support:** slicer tính 181,6 g, khoảng 4 giờ 18 phút và báo `floating cantilever` ở vành trong; không chọn phương án này để in thử.
- **Thân bật `normal(auto)` support, cho phép mọc từ mặt trong đáy:** warning rỗng; khoảng 267,5 g và 6 giờ 01 phút. Tăng 85,9 g và khoảng 1 giờ 43 phút so với không support. Cần xem preview vùng support, kiểm tra có tháo được khỏi khoang và có chạm bề mặt ron hay không; chưa in thử.
- **Nắp không support:** slice thành công, warning rỗng; khoảng 58,7 g và 1 giờ 13 phút. Chưa xem từng lớp trong GUI.
- **Đóng gói:** CLI xuất `plate_1.gcode` nhưng bước `--export-3mf` trả `-13` (`Failed exporting 3mf files`) với đầu vào Fusion 3MF/STL. Các G-code trong `runs/` chỉ là bản thử, **không đưa vào `print/sliced/`**. Hai file trong `print/prepare/` mở được trong Bambu Studio nhưng chưa có G-code đã kiểm tra. Hai gói v03 cũ được lấy khỏi thư mục làm việc để tránh nhầm; Git giữ lịch sử.

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
- **MAT-002/PRT-008, lần CLI đầu không đạt:** G-code ghi `filament_type = PLA`, `filament_density = 0`, `curr_bed_type = Cool Plate` do CLI chưa nạp `inherits`/`include`. File thử lỗi đã được xóa sau khi ghi nhận, không dùng để in.
- **MAT-002/PRT-008, slice lại đạt ở mức slicer:** thân/nắp dùng profile P2S 0,4 mm, PETG HF, Textured PEI, layer 0,20 mm đã giải quyết đầy đủ kế thừa. Hai lần slice có `return_code = 0` và không có warning. G-code trong [hai gói in thử](../print/sliced/README.md) ghi đúng P2S/PETG/plate, density 1,28 g/cm³, bàn 70°C. Thumbnail cho thấy thân đặt đáy xuống, nắp nằm phẳng. Ước tính thân 2 giờ 16 phút/105,2 g; nắp 51 phút/39,9 g. Chưa xem từng lớp trong GUI, xác nhận màu, lắp PCB hoặc in thử.
- **PRT-005, thử xếp chung một plate:** Bambu Studio CLI slice thành công cả thân và nắp, không báo warning. Bbox thân X=68–188, Y=129–249 mm; nắp X=68–188, Y=7–127 mm. Hai vật cách nhau khoảng 2 mm theo Y và chỉ còn khoảng 7 mm tới hai mép plate. Tổng ước tính khoảng 2 giờ 59 phút 54 giây, 145,1 g; tiết kiệm khoảng 7 phút so với hai lần slice riêng. Giữ **hai plate riêng** làm phương án in thử mặc định để còn chỗ điều chỉnh bám bàn/brim và in lại từng phần; file thử chung đã xóa sau khi ghi kết quả.
- **Rule bố cục chung:** quyết định trên theo [plate-layout.md](../../../docs/rules/plate-layout.md). Số 2 mm là khoảng cách mesh đo từ bbox CLI của lần thử này, **chưa tính brim/support** và không phải ngưỡng tối thiểu áp dụng cho project khác.

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
