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
