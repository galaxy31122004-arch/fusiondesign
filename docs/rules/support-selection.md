# Rule chọn support trong Bambu Studio

Áp dụng cho mọi part có phần nhô, cầu hoặc vùng slicer cảnh báo thiếu đỡ. Bambu Studio tạo đường support theo profile và các vùng người thiết kế chọn; rule này quyết định **khi nào dùng kiểu nào** và cách kiểm tra kết quả. Không tự tạo support bằng script hoặc coi một kiểu là tối ưu cho mọi model.

## Trình tự chọn

1. Giữ đúng hướng in, máy, nozzle, vật liệu, plate và process của lần in dự kiến. Slice thử với support tắt để xác định vị trí thực sự cần đỡ qua cảnh báo và Preview. Nếu không có vùng thiếu đỡ, giữ support tắt; vẫn kiểm tra bridge, mặt dưới và lớp đầu.
2. Nếu cần đỡ, thử `tree(auto)` và `normal(auto)` trên **cùng** model/profile/hướng in. Với vùng cục bộ trong khoang hoặc nhiều nhánh rời, ưu tiên thử tree trước; với mặt dưới rộng, tương đối phẳng và cần đỡ liên tục, thử normal trước. Đây là thứ tự thử, không phải kết luận về chất lượng in.
3. Khi tự động đặt support vào lỗ, mặt lắp, bề mặt ron, khe khó gỡ hoặc bỏ sót vùng cần đỡ, dùng chế độ manual/paint hoặc vùng chặn support có sẵn trong Bambu Studio rồi slice lại. Chỉ giữ phương án thủ công khi Preview cho thấy vùng cần đỡ vẫn được phủ đủ.
4. Chỉ bật `On build plate only` sau khi kiểm tra toàn bộ support cần thiết có thể bắt đầu từ plate. Với khoang có vành nhô được đỡ từ đáy **bên trong model**, tùy chọn này có thể xóa phần đỡ cần thiết; phải xem lại Preview và cảnh báo.
5. So các phương án bằng vùng tiếp xúc với model, khả năng lấy support ra, nguy cơ hỏng bề mặt chức năng, lớp đầu/độ bám bàn, cảnh báo slicer, khối lượng support và thời gian. Ưu tiên phương án bảo vệ chức năng và tháo được; không chọn chỉ theo số gram ít nhất. Nếu không phương án nào đạt, nêu phương án đổi hướng hoặc sửa hình học để người dùng quyết định.

Không đặt chung một góc ngưỡng, mật độ hay kiểu support cho mọi vật liệu và profile. Mỗi lần đổi hình học, hướng in, layer height, nozzle, vật liệu hoặc support setting phải slice lại. Kết quả Preview chỉ là dự đoán; khả năng gỡ support và chất lượng mặt dưới phải xác nhận bằng mẫu in.

## Bản ghi cho mỗi part

Trong `projects/<id>/notes/results.md`, ghi phiên bản model, Bambu Studio/profile, hướng in, vùng cần đỡ, các kiểu đã thử (`off`, `tree`, `normal`, manual), phạm vi support và lý do loại/chọn, trạng thái `On build plate only`, cảnh báo, khối lượng support, tổng vật liệu, thời gian, ảnh hoặc mô tả Preview ở bề mặt chức năng, rủi ro khi tháo và kết quả in thử. Số liệu chỉ so trực tiếp khi các điều kiện slice giống nhau. Gói in chỉ đưa vào `print/sliced/` sau các checkpoint trong [versioning.md](versioning.md).
