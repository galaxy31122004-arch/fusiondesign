# Rule bố trí part trên bàn in

Áp dụng khi một project có từ hai part trở lên. Một project Bambu Studio có thể chứa nhiều plate; **số project không bắt buộc bằng số plate**. Mặc định đánh giá cả phương án xếp chung và tách plate trước khi phát hành file in.

## Dữ liệu cần có

- Máy, nozzle, vật liệu, màu, plate đang lắp và process profile cho từng part.
- Hướng in, vùng tiếp xúc bàn, chiều cao, support, brim/skirt, wipe tower nếu có và vùng plate không thể in.
- Ước tính thời gian/vật liệu của hai phương án, giá trị của từng part nếu phải in lại và lỗi bám bàn đã từng gặp.
- Chế độ trình tự: **by layer** hoặc **by object**. Đây là lựa chọn khác với việc xếp một hay nhiều plate.

## Quyết định bố cục

1. Kiểm tra mỗi part riêng: đúng kích thước, hướng in, lớp đầu, support và profile. Part vốn không ổn khi in riêng không được coi là ổn chỉ vì xếp chung.
2. Với phương án chung plate, dùng **Arrange**, sau đó kiểm tra lại vị trí thực tế trên plate. Đo khoảng cách giữa footprint sau khi tính **brim/support/skirt/wipe tower** và khoảng trống tới biên/vùng loại trừ. Không lấy khoảng cách giữa hai mesh trần làm khoảng cách an toàn. Auto-brim có thể khiến slicer cần nhiều chỗ hơn dự tính ([diễn đàn: arrange và brim](https://forum.bambulab.com/t/why-does-bambu-studio-struggle-to-fit-items-on-one-bed/96943), [ví dụ spacing](https://forum.bambulab.com/t/arrange-object-spacing-does-nothing/16586), đọc 2026-10-20; RSCH-20261020-0002).
3. Nếu dùng **print by object**, kiểm tra vùng quét và giới hạn chiều cao đầu in ngay trong Bambu Studio. Phương án xếp vừa plate ở chế độ **by layer** không tự động hợp lệ ở chế độ **by object** ([thảo luận về clearance](https://forum.bambulab.com/t/print-all-objects-on-plate-or-one-object-at-a-time/256480), đọc 2026-10-20; RSCH-20261020-0003).
4. Chỉ chọn chung plate khi slicer không báo xung đột, preview từng lớp hợp lý, có khoảng dự phòng sau các cấu trúc phụ và rủi ro hỏng cả mẻ được chấp nhận. Các part có thể cần profile khác nhau; nếu khác vật liệu/nhiệt bàn hoặc yêu cầu bề mặt, phải chứng minh cấu hình in chung tương thích trước khi gộp.
5. Ưu tiên tách plate khi bố cục sát mép/sát nhau, cần brim rộng, part cao hoặc dễ bong, một part khó in/đắt tiền, hay việc in lại riêng quan trọng hơn thời gian tiết kiệm. Đây là cách quản lý rủi ro được thành viên diễn đàn mô tả khi một part lỗi có thể ảnh hưởng phần còn lại ([nhiều plate hay một plate](https://forum.bambulab.com/t/why-multiple-plates-when-it-fits-on-one/42932), đọc 2026-10-20; RSCH-20261020-0001). Một trường hợp part cao bong bàn dù in nhiều vật trên một plate được thảo luận [tại đây](https://forum.bambulab.com/t/problem-printing-multiple-tall-object/50349) (đọc 2026-10-20; RSCH-20261020-0003).
6. So thời gian và vật liệu ước tính, số lần khởi động máy, công tháo plate và chi phí in lại. Không kết luận chung plate tốt hơn chỉ vì có ít plate hơn; cũng không mặc định tách là tốt hơn khi part nhỏ, ổn định và còn nhiều không gian.

## Không đặt ngưỡng chung

Các bài diễn đàn trên là kinh nghiệm cộng đồng, không phải thông số kỹ thuật chính thức cho P2S. **Không có ngưỡng mm chung** cho khoảng cách hai part hoặc mép plate từ những nguồn này. Khoảng cách cần kiểm tra theo hình học thật, brim/support, chế độ in và preview của đúng profile đang dùng. Slice thành công chỉ xác nhận phần mềm tạo đường in; nó không bảo đảm bám bàn hoặc không có lỗi khi in.

## Bản ghi bắt buộc cho mỗi lựa chọn

Ghi trong `projects/<id>/notes/results.md`: part và phiên bản, máy/vật liệu/plate, số plate, tọa độ hoặc bbox từng part, khoảng cách nhỏ nhất **sau khi tính cấu trúc phụ**, trình tự in, cảnh báo của slicer, ước tính thời gian/vật liệu, lý do chọn chung/tách và điều cần quan sát khi in thử. Khi đổi part, hướng đặt, brim/support, vật liệu hoặc profile, đánh giá lại quyết định này.
