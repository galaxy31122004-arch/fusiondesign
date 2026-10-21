# Rule chọn nhiệt độ, layer height và infill

Áp dụng cho mọi project trước khi slice và sau khi đổi máy, nozzle, vật liệu, plate hoặc mục tiêu cơ học. Bambu Studio profile **đang chọn** là điểm xuất phát; không sao chép nhiệt độ hay mật độ infill từ một project sang project khác.

## Nhiệt độ

1. Chọn đúng hãng/biến thể filament, máy, nozzle và plate đang lắp. Đọc **giá trị hiệu lực** sau khi giải quyết preset kế thừa và sửa đổi của người dùng: nhiệt nozzle lớp đầu/lớp sau, nhiệt plate theo đúng loại mặt, làm mát và giới hạn lưu lượng.
2. Bắt đầu bằng nhiệt độ trong profile tương thích. Chỉ điều chỉnh khi có mục tiêu hoặc lỗi quan sát được như bám lớp đầu, stringing hay bám giữa các lớp; ghi thay đổi, mẫu thử và kết quả. Không suy nguyên nhân từ một dấu hiệu duy nhất.
3. Không đặt nhiệt ngoài dải vật liệu/nozzle được profile hoặc tài liệu của đúng cuộn cho phép. Nếu dữ liệu xung đột hoặc không có, đánh dấu `Chưa xác minh` và thử mẫu trước khi in chi tiết chức năng.
4. Sau khi slice, đối chiếu nhiệt nozzle, nhiệt đúng loại plate và các lệnh khởi động máy trong G-code. Tên preset trong UI không chứng minh G-code đã nhận đủ thông số.

## Layer height theo nozzle

1. Xác nhận nozzle đang **lắp thực tế**, rồi đọc `min_layer_height` và `max_layer_height` của profile máy đó. Layer của process profile, lớp đầu và vùng adaptive/variable layer phải nằm trong dải hiệu lực; các preset có thể thay đổi theo phiên bản Bambu Studio.
2. Chọn profile process tương thích với nozzle. Layer mỏng hơn khi cần bề mặt cong/chi tiết nhỏ sau khi preview chứng minh nó còn được tạo thành đường in; layer dày hơn khi ưu tiên thời gian và hình học phù hợp. Layer nhỏ không sửa được một lỗ hoặc thành đã bị mất do nozzle/line width.
3. Đổi layer height phải chạy lại preview để kiểm tra số lớp đáy/mặt trên, bridge, overhang, thời gian và đường thành. Không giữ số lớp cũ mà không kiểm tra **độ dày vật lý** của đáy/mặt trên.

### Mặt cong và bậc lớp

1. Trước khi chốt layer, đánh dấu các mặt cong/mặt nghiêng lộ ra ngoài hoặc dùng để lắp ghép. Xem mặt đó có thay đổi hình dạng theo chiều cao **Z của hướng in hiện tại** không. Nếu có, layer dày có thể tạo bậc thang thấy được; đây là cảnh báo về độ mịn bề mặt, không phải một bán kính hay góc cấm chung.
2. Slice bằng layer của preset làm mốc, xem các lớp ở vùng cong và mức bậc dự kiến. Khi bậc không phù hợp mục tiêu, so một phương án layer mỏng toàn part với `adaptive/variable layer height` tập trung ở vùng cong nếu Bambu Studio của phiên bản đang dùng hỗ trợ. Giữ layer lớp đầu và mọi lớp biến thiên trong dải nozzle/profile; không tự lấy một giá trị mm cố định làm chuẩn cho mọi vật.
3. Chọn phương án theo độ mịn ở vùng cần nhìn/chạm/lắp, số lớp đặc hiệu lực, overhang/support, thời gian và vật liệu sau khi slice. Adaptive layer chỉ có ích nếu Preview cho thấy lớp thật sự mỏng hơn ở vùng mục tiêu; in mẫu khi yêu cầu thẩm mỹ hoặc độ khít quan trọng.
4. Phân biệt nguyên nhân: mặt cong bị đa giác theo **XY** cần kiểm tra độ mịn mesh/export hoặc hình học CAD; đường dọc tại seam cần chỉnh seam; mặt dưới xấu do support cần kiểm tra support/interface. Giảm layer theo Z không tự sửa ba vấn đề này.

Ghi vào `notes/results.md`: vùng bề mặt, hướng in, layer gốc, phương án layer mỏng/adaptive đã thử, dải lớp hiệu lực, ảnh hoặc mô tả Preview, chênh lệch thời gian/vật liệu và kết quả mẫu in. Khi đổi hướng đặt hoặc model, đánh giá lại bậc lớp.

Ví dụ **từ preset P2S cục bộ ngày 2026-10-20**, chỉ để đối chiếu, không phải giới hạn vĩnh viễn:

| Nozzle | Dải layer height trong machine preset | Process preset có sẵn trên máy |
| --- | --- | --- |
| 0,2 mm | 0,04–0,14 mm | 0,08 / 0,10 / 0,12 mm |
| 0,4 mm | 0,08–0,28 mm | 0,08 / 0,12 / 0,16 / 0,20 / 0,24 mm |
| 0,6 mm | 0,12–0,42 mm | 0,18 / 0,24 / 0,30 mm |
| 0,8 mm | 0,16–0,56 mm | 0,24 / 0,32 / 0,40 mm |

Nguồn: preset JSON cài trong `%APPDATA%/BambuStudio/system/BBL/machine/` và `process/` trên máy làm việc, kiểm tra 2026-10-20. Khi chạy ở máy khác hoặc sau cập nhật Bambu Studio, đọc lại preset thay vì dùng bảng này làm ngưỡng chặn.

## Infill và độ bền

1. Ghi nhiệm vụ chi tiết: trang trí, vỏ bảo vệ, chịu tải, bắt vít, kín nước hay lắp ghép. Chọn pattern và mật độ từ profile làm mốc; không lấy một phần trăm infill làm quy tắc chung.
2. Kiểm tra riêng **wall loops/độ dày thành**, lớp đáy/mặt trên, trụ vít và hướng lớp. Với thành mỏng hoặc lỗ bắt vít, tăng infill của vùng rỗng không tự sửa được thành yếu, ren yếu hoặc đường nước lọt qua mối ghép.
3. Nếu tăng/giảm infill, ghi mục tiêu, pattern, phần trăm, vật liệu, wall loops, layer height và kết quả thử. So lượng vật liệu/thời gian từ slicer. Chỉ dùng modifier theo vùng khi có lý do và preview đường in chứng minh vùng đó nhận đúng cấu hình.
4. Trước in, xem preview tại trụ, góc, đáy, mặt trên và vùng chuyển từ thành sang infill; không kết luận độ bền hoặc kín nước chỉ từ mật độ infill.

## Bản ghi bắt buộc

Trong `projects/<id>/notes/results.md`, ghi tên preset và phiên bản Bambu Studio, nozzle, loại plate, filament/màu, nhiệt nozzle/lớp đầu/bàn, layer height thường/lớp đầu, wall loops, top/bottom, pattern và mật độ infill. Nếu dùng adaptive layer hoặc modifier, ghi vùng và giá trị. Ghi kết quả preview, in thử và mọi lần thay đổi so với preset.
