# Quy tắc dự án FusionDesign

## Mục tiêu

Xây quy trình thống nhất từ thiết kế tham số trong Autodesk Fusion đến chuẩn bị in trong Bambu Studio. Máy in mặc định là Bambu Lab P2S Full Combo. Xem [README.md](README.md) để biết cấu trúc repo và quy trình.

## Nguyên tắc chung

- Mọi kích thước thiết kế dùng milimét và ghi rõ đơn vị. Không lấy kích thước ví dụ hoặc kích thước PCB làm kích thước vỏ khi chưa có khoảng hở lắp ráp.
- Mỗi project ghi tham số và kiểm tra riêng trong `projects/<tên-project>/`. Không đặt trường hợp riêng của một project trong rule chung.
- Khi người dùng ghi chú hoặc sửa một quy tắc áp dụng cho nhiều project, cập nhật ngay file rule chung tương ứng trong `docs/rules/` và kiểm tra các project bị ảnh hưởng. Nếu thay đổi chỉ thuộc một project, chỉ cập nhật `projects/<tên-project>/notes/` và model/script liên quan; không thêm vào rule chung.
- Thông số loại linh kiện cơ bản có thể tái dùng nằm dưới dạng text trong [library/](library/README.md); lần sau không cần đọc ảnh để lấy lại thông số đã ghi. Kích thước, số lỗ và vị trí đặt riêng của PCB hoặc vỏ nằm trong project; không sao chép số đo giữa hai mã linh kiện khác nhau.
- Khi thêm hoặc cập nhật linh kiện, áp dụng [docs/rules/component-library.md](docs/rules/component-library.md) và ghi nguồn cùng trạng thái xác nhận cho từng kích thước.
- Mỗi lần sửa model phải áp dụng [docs/rules/versioning.md](docs/rules/versioning.md): phiên bản mới có F3D/3MF riêng, ghi lịch sử trong `notes/HISTORY.md` và đóng tab Fusion cũ của đúng project sau khi bản mới đã xuất thành công. Sao lưu tab cũ có chỉnh sửa chưa lưu trước khi đóng.
- Nếu yêu cầu mới thay đổi công dụng hoặc môi trường sử dụng, cập nhật thiết kế và checklist trước khi dựng model; không giữ giả định cũ đã mâu thuẫn.

## Ranh giới trách nhiệm

- Fusion giữ model tham số và là nguồn dữ liệu thiết kế chính. Đọc và sửa project qua Fusion API; không sửa trực tiếp dữ liệu nhị phân của file `.f3d`.
- Bộ phân tích in kiểm tra model, ghi rõ vấn đề, vị trí, nguyên nhân và đề xuất. Phân biệt kết quả đo được với ước lượng hoặc kinh nghiệm.
- Bambu Studio chịu trách nhiệm chọn profile thực tế, xem preview, slice và tạo dữ liệu cho máy in.
- Một giao diện điều phối có thể bao phủ toàn bộ quy trình, nhưng phần tích hợp Fusion và Bambu Studio phải có ranh giới rõ ràng để mỗi bên vẫn kiểm tra được độc lập.

## Rule kiểm tra khả năng in

- Đọc [docs/rules/printability.md](docs/rules/printability.md) trước khi lập kế hoạch tạo hoặc sửa bất kỳ model nào. File này quy định kiểm tra từ lúc nhận yêu cầu, trong lúc thiết kế và trước khi chuyển sang Bambu Studio.
- Đọc [docs/rules/material.md](docs/rules/material.md) khi chọn vật liệu hoặc profile in. Dùng đúng cấu hình P2S, nozzle và vật liệu của project; không chép cứng thông số của một preset làm mặc định cho mọi cuộn nhựa.
- Mỗi project phải tạo một bản ghi kiểm tra theo các giai đoạn trong file đó. Không bỏ qua cảnh báo chỉ vì model tạo được trong Fusion hoặc slice thành công.
- Chỉ áp dụng ngưỡng cụ thể khi nguồn và điều kiện áp dụng đã được ghi rõ. Nếu chưa có căn cứ, giữ trạng thái `Chưa xác minh` và đề xuất phép kiểm tra hoặc mẫu in thử.

## Quy trình bắt buộc

1. Nhận kích thước, mục đích sử dụng, vật liệu dự kiến, màu và yêu cầu nhiều màu nếu có, nozzle và profile in nếu người dùng đã chọn; nếu chưa chọn máy thì dùng Bambu Lab P2S Full Combo. Chạy kiểm tra đầu vào theo `docs/rules/printability.md` trước khi dựng hình.
2. Kiểm tra giá trị đầu vào: tất cả kích thước phải dương (đơn vị mm); với hộp phải thỏa `0 < day_day < H_ngoai` và `0 < day_thanh < min(L, W) / 2`; nếu thiếu thông tin có ảnh hưởng đến kết quả, hỏi người dùng hoặc ghi rõ giả định.
3. Tạo hoặc cập nhật model tham số trong Fusion theo hồ sơ project. Trước khi sửa project hiện có, tạo điểm có thể khôi phục, hiển thị thay đổi dự kiến và cho phép người dùng xác nhận.
4. Kiểm tra tính hợp lệ của hình học và chạy lại các rule khả năng in trong lúc dựng hình, sau mỗi thay đổi có liên quan, và trước khi xuất file.
5. Xuất mesh định dạng 3MF, đơn vị mm, để mở trong Bambu Studio; kiểm tra đơn vị, kích thước, hướng đặt và số lượng part sau khi xuất. Nếu dùng định dạng khác phải ghi rõ lý do trong bản ghi kiểm tra.
6. Xem preview sau khi slice, gồm vùng support, thời gian và lượng vật liệu theo kết quả Bambu Studio. Chỉ coi số liệu này là chính thức sau khi slice thành công.
7. Người dùng xác nhận trước khi gửi lệnh in. Ghi lại tham số thiết kế, thiết lập in, cảnh báo và kết quả in để cải thiện vòng sau.

## Quy tắc về P2S và khả năng in

- Không tự đặt giới hạn P2S, ngưỡng overhang, độ dày tối thiểu, dung sai lắp ghép hay thông số nhiệt độ. Tra tài liệu chính thức hoặc xác nhận bằng phép thử với đúng máy, nozzle, vật liệu và profile đang dùng.
- Mọi khuyến nghị về thành, đáy, support, góc đặt, layer height và tốc độ phải nêu điều kiện áp dụng. Khi thiếu dữ liệu, trình bày là đề xuất cần thử, không phải bảo đảm in thành công.
- Phân loại lỗi theo nguyên nhân có thể xử lý bằng **thiết kế** (ví dụ: thành yếu, khe hở thiếu) hoặc bằng **thiết lập/quy trình in** (ví dụ: hướng đặt, support, adhesion). Một lỗi có thể cần cả hai hướng xử lý.
- Khi gặp lỗi in thực tế, lưu ảnh hoặc mô tả lỗi, vị trí trên mẫu, vật liệu, nozzle, profile và thay đổi đã thử. Không suy ra nguyên nhân duy nhất nếu chưa đủ bằng chứng.
- Không tự sửa model để khắc phục lỗi in nếu thay đổi đó làm sai kích thước chức năng hoặc mục đích sử dụng của chi tiết; trình bày phương án và xin xác nhận.

## Quy tắc AI và thay đổi model

- AI đề xuất một kế hoạch thay đổi có thể đọc được: đối tượng, giá trị cũ, giá trị mới, lý do và tác động dự kiến.
- Ưu tiên sửa user parameters và feature có sẵn. Không xóa feature, component hoặc timeline item khi chưa xác định được tác động và chưa có xác nhận.
- Trước khi áp dụng thay đổi, tạo điểm có thể khôi phục bằng cơ chế của Fusion hoặc một bản lưu riêng. Kiểm tra model sau thay đổi; nếu lỗi, khôi phục và báo lỗi cụ thể.
- Không gửi toàn bộ project hoặc thông tin nhạy cảm tới dịch vụ AI ngoài máy nếu người dùng chưa chọn rõ cách xử lý dữ liệu.

## Tiêu chí hoàn thành từng project

- Model Fusion hợp lệ và kích thước đo lại khớp tham số đã chốt.
- File xuất mở được trong Bambu Studio với đúng kích thước và hướng dự kiến.
- Bambu Studio slice thành công; người dùng kiểm tra preview trước khi in.
- Báo cáo phân biệt rõ kiểm tra đã thực hiện, cảnh báo còn lại và giả định chưa được xác minh.
- Tiêu chí riêng của project nằm trong `projects/<tên-project>/notes/checks.md`.
