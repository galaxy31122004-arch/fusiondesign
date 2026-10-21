# Rule kiểm tra khả năng in 3D

## Mục đích và phạm vi

File này quy định cách phát hiện sớm rủi ro thiết kế và in trên Bambu Lab P2S. Áp dụng cho mọi project. Rule hoạt động từ lúc nhận yêu cầu, tiếp tục khi tạo hoặc sửa hình học trong Fusion, rồi kiểm tra lại sau khi đưa model sang Bambu Studio.

Các kiểm tra phụ thuộc vật liệu phải áp dụng thêm [material.md](material.md) ngay từ lúc nhận yêu cầu và chạy lại khi đổi vật liệu, màu, nozzle hoặc profile.

Với nhiều part, áp dụng thêm [plate-layout.md](plate-layout.md) để quyết định bố cục in và kiểm tra brim/support, mép plate cùng trình tự in.

Khi model cần support, áp dụng [support-selection.md](support-selection.md) để chọn kiểu trong Bambu Studio và ghi kết quả so sánh theo từng part.

Máy mặc định là **Bambu Lab P2S Full Combo** theo lựa chọn của người dùng. Tên cấu hình này không tự xác định nozzle, vật liệu, bàn in, phụ kiện đang lắp hay profile; các mục đó vẫn phải được ghi hoặc đánh dấu `Chưa chọn` cho từng lần in.

Không coi việc Fusion tạo được model hoặc Bambu Studio slice thành công là bằng chứng chi tiết sẽ in đạt yêu cầu. Một cảnh báo chỉ được đóng khi đã sửa, đã kiểm chứng bằng dữ liệu phù hợp, hoặc người dùng chấp nhận rủi ro có ghi lại.

## Dữ liệu đầu vào cần ghi cho mỗi project

- Mục đích sử dụng, kích thước chức năng, tải hoặc yêu cầu chịu lực nếu có.
- Máy in (mặc định: Bambu Lab P2S Full Combo), nozzle, vật liệu, màu, yêu cầu nhiều màu, profile in và loại bàn in dự kiến; đánh dấu `Chưa chọn` cho mục chưa biết.
- Hướng đặt dự kiến và yêu cầu đối với mặt ngoài, mặt lắp ghép, độ chính xác, độ kín hoặc độ bền nếu có.
- Nguồn của mọi ngưỡng kỹ thuật được dùng: tài liệu chính thức, thông số profile, phép đo trên model hoặc mẫu in thử. Ghi ngày và điều kiện áp dụng.

Thiếu dữ liệu không được tự biến thành giá trị mặc định của P2S. Có thể dùng giả định tạm để dựng mẫu, nhưng phải hiển thị rõ giả định đó và không tuyên bố đã kiểm chứng khả năng in.

Vật liệu cần được chọn trước khi chốt các rule phụ thuộc vật liệu và trước khi slice. Có thể bắt đầu phác thảo hình học khi vật liệu chưa chọn, nhưng cảnh báo khả năng in phải giữ trạng thái `Chưa xác minh`. Màu nên được chọn sớm nếu người dùng quan tâm đến ngoại hình, cần in nhiều màu hoặc cần phân chia bề mặt/part theo màu. Với hộp đơn sắc thông thường, có thể chọn màu sau khi đã dựng hình; vẫn phải ghi màu thực tế trước khi in và không suy từ màu ra thông số kỹ thuật của vật liệu.

## Ba thời điểm kiểm tra bắt buộc

### 1. Trước khi thiết kế

- Hỏi vật liệu dự kiến, màu và yêu cầu in nhiều màu. Nếu chưa chọn vật liệu, chỉ được dựng bản phác thảo; các kết luận phụ thuộc vật liệu phải để `Chưa xác minh`.
- Kiểm tra kích thước ngoài dự kiến so với vùng in của đúng cấu hình máy và hướng đặt. Nếu chưa có thông số máy đã xác minh, gắn `Chưa xác minh`.
- Kiểm tra yêu cầu chức năng có thể xung đột với cách in dự kiến: thành mỏng, lắp ghép chặt, chi tiết chịu lực, yêu cầu mặt đẹp hoặc độ kín.
- Nêu rủi ro có thể thấy từ mô tả trước khi tạo hình. Đề xuất tham số thiết kế hoặc mẫu thử cần xác nhận.
- Nếu yêu cầu không đủ để chọn một kích thước chức năng hoặc xác định vùng/part cần in nhiều màu, hỏi người dùng trước khi quyết định thay họ.

### 2. Trong khi thiết kế trong Fusion

- Sau khi tạo hoặc sửa feature, đo lại hình học liên quan: thành, đáy, khe, lỗ, phần nhô, diện tích tiếp xúc bàn in và kích thước tổng thể khi có thể đo bằng API.
- So sánh kết quả với rule có căn cứ cho đúng vật liệu, nozzle, profile và hướng in. Nếu chưa có ngưỡng, báo `Cần thử nghiệm`, không tự kết luận đạt hoặc lỗi.
- Khi phát hiện rủi ro, cảnh báo ngay tại bước đang làm: vị trí trên model, giá trị đo được, điều kiện áp dụng, hậu quả có thể xảy ra và các cách xử lý trong thiết kế hoặc khi in.
- Sau mỗi thay đổi ảnh hưởng đến hình dạng hoặc hướng in, chạy lại các rule bị ảnh hưởng. Không dùng kết quả kiểm tra cũ cho phiên bản model mới.

### 3. Trước khi in

- Nếu có MeshRight, chạy kiểm tra **chỉ đọc** trên mesh vừa xuất để đo đơn vị/kích thước, số khối và lỗi topology; lưu báo cáo theo project. Kết quả mesh kín không đóng cảnh báo support, brim, lắp ghép, vật liệu hoặc chống nước. Adapter nằm tại `scripts/printing/check_mesh.py` ([MeshRight CLI](https://github.com/Huzy85/MeshRight/blob/main/src/meshright/cli.py), đọc 2026-10-20; RSCH-20261020-0005).

- Sau khi xuất, xác nhận đơn vị, kích thước, số part và hướng đặt trong Bambu Studio khớp model Fusion.
- Dùng preview sau khi slice để kiểm tra đường chạy, support, lớp đầu, thành mỏng, khoảng trống và các vùng có nguy cơ. Đánh dấu những mục không thể kết luận từ preview.
- Nếu slice bằng CLI hoặc công cụ tự động, đọc lại metadata/G-code đầu ra: đúng model máy, nozzle, loại vật liệu, loại bàn in, nhiệt độ và lệnh khởi động máy. Tên preset ở lệnh chạy không đủ chứng minh profile kế thừa đã được nạp; file sai một mục thiết yếu phải cách ly, không đưa vào thư mục file in.
- Chỉ xác nhận một khuyến nghị profile khi đã biết profile thực tế. Nếu đổi máy, nozzle, vật liệu, profile hoặc hướng đặt, đánh giá lại các rule liên quan.
- Ghi lại rủi ro còn mở trước khi người dùng quyết định in.

## Danh mục rule kiểm tra

| ID | Nhóm | Dấu hiệu cần kiểm tra | Hướng xử lý có thể đề xuất |
| --- | --- | --- | --- |
| PRT-001 | Kích thước máy | Model hoặc cách đặt vượt vùng in đã xác minh | Xoay, chia part hoặc đổi kích thước nếu chức năng cho phép |
| PRT-002 | Thành và đáy | Vùng mỏng hoặc không đồng đều so với yêu cầu sử dụng và profile | Tăng bề dày, đổi hình học, điều chỉnh wall hoặc thử mẫu |
| PRT-003 | Lỗ và khe lắp | Kích thước danh nghĩa có thể không đạt sau in | Thêm dung sai dựa trên mẫu thử, đổi hướng in hoặc gia công sau in |
| PRT-004 | Phần nhô và cầu | Vùng cần support hoặc có nguy cơ võng | Chọn và kiểm tra kiểu support theo [rule support](support-selection.md); đổi hướng, sửa hình dạng hoặc chia part khi cần |
| PRT-005 | Bám bàn và ổn định | Diện tích tiếp xúc nhỏ, chi tiết cao hoặc dễ dịch chuyển | Đổi hướng đặt, thêm brim hoặc sửa mặt đáy nếu phù hợp |
| PRT-006 | Độ bền theo hướng lớp | Hướng lớp có thể bất lợi cho tải sử dụng | Đổi hướng in, tăng tiết diện hoặc đổi kết cấu |
| PRT-007 | Chất lượng bề mặt | Mặt cần đẹp hoặc lắp ghép nằm trên support, seam hay mặt chạm bàn | Đổi hướng in, vị trí seam, support hoặc tách chi tiết |
| PRT-008 | Hình học mesh | Mesh hở, giao nhau, sai đơn vị hoặc mất chi tiết khi xuất | Sửa model hoặc cách export rồi kiểm tra lại trong slicer |
| PRT-009 | Góc của vật thể dạng hộp | Góc ngoài sắc ở thân hoặc nắp; bo góc có thể làm giảm khoảng hở, bề dày thành hay ảnh hưởng đường ghép | Tạo bán kính bo góc thành tham số; kiểm tra lại lòng hộp, thành, nắp, ron và lỗ sau khi bo |

Các hàng trên là **nhóm kiểm tra**, không phải kết luận rằng P2S sẽ gặp lỗi. Chỉ gắn cảnh báo cụ thể khi quan sát được dấu hiệu trên project hoặc có điều kiện in liên quan.

Với sản phẩm dạng hộp, xem xét bo các góc ngoài ngay trong giai đoạn thiết kế thay vì thêm vào sau khi đã đặt lỗ, trụ hoặc đường ron. Chọn bán kính theo kích thước và chức năng thực tế; không có bán kính chung cho mọi hộp. Giữ góc vuông ở vị trí cần lắp ghép nếu có lý do chức năng. Sau khi bo, đo lại bề dày nhỏ nhất, khoảng hở PCB/linh kiện, hình học nắp và vị trí lỗ; không coi bo góc là bằng chứng hộp kín nước hoặc in đạt.

## Định dạng một rule cụ thể

Khi bổ sung một ngưỡng hoặc lỗi đã hiểu rõ, ghi đủ các trường sau:

```text
ID:
Tên và lỗi có thể xảy ra:
Thời điểm kiểm tra: trước thiết kế / trong Fusion / trước in
Điều kiện áp dụng: máy, nozzle, vật liệu, profile, hướng in
Dữ liệu cần đo:
Điều kiện kích hoạt và ngưỡng:
Nguồn bằng chứng, ngày kiểm tra:
Mức độ: chặn / cảnh báo / thông tin / chưa xác minh
Hướng xử lý trong thiết kế:
Hướng xử lý khi in:
Cách xác nhận đã khắc phục:
```

Một ngưỡng chưa có nguồn hoặc chưa biết điều kiện áp dụng không được dùng để chặn thiết kế. Có thể dùng nó như giả thuyết thử nghiệm, với nhãn `Chưa xác minh`.

## Cách báo cảnh báo

Mỗi cảnh báo phải có: `rule ID`, giai đoạn phát hiện, vị trí/feature, giá trị đo được hoặc dữ liệu còn thiếu, nguyên nhân có thể xảy ra, mức độ, bằng chứng, phương án sửa trong Fusion, phương án chỉnh trong Bambu Studio và cách kiểm tra lại. Nêu rõ khi nguyên nhân chưa chắc chắn hoặc có nhiều nguyên nhân khả dĩ.

Không tự ý đổi kích thước chức năng để xóa cảnh báo. Đưa các phương án cho người dùng chọn nếu chúng ảnh hưởng đến mục đích sử dụng, độ chính xác hoặc hình dáng mong muốn.

