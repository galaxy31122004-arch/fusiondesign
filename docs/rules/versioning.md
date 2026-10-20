# Rule phiên bản và quay lại bản cũ

## Mỗi lần sửa model

1. Tạo mã phiên bản mới `vNN` và đặt tên document Fusion dạng `<project>_vNN - <mô tả>` ngay khi tạo; không để tab `Untitled`.
2. Xuất F3D và 3MF với tên có mã phiên bản vào thư mục project. Không ghi đè file phiên bản trước. Lưu document trong project Fusion với tên cùng mã phiên bản; xác nhận `isSaved = True` và ghi tên project đã lưu. Nếu dịch vụ Fusion không truy cập được, ghi rõ chỉ có bản local F3D.
3. Kiểm tra file tồn tại, đơn vị/kích thước mesh và ghi thay đổi, kết quả kiểm tra, cảnh báo còn lại vào `projects/<id>/notes/HISTORY.md` và `notes/checks.md`.
4. Khi bản mới đã xuất thành công, đóng các tab Fusion cũ **của đúng project** để tiết kiệm tài nguyên. Trước khi đóng một tab cũ có chỉnh sửa chưa được lưu, xuất bản sao phiên làm việc riêng trong `projects/<id>/runs/session_backups/`; nếu sao lưu lỗi, giữ tab mở và báo rõ.
5. Không tự đóng tab project khác hoặc tab không xác định được nguồn gốc. Nếu lần chạy mới lỗi, giữ tab của bản trước để tiếp tục làm việc.

## Quay lại phiên bản trước

1. Đọc `projects/<id>/notes/HISTORY.md` để chọn mã phiên bản và trạng thái phù hợp.
2. Mở F3D tương ứng trong Fusion; kiểm tra component và tham số trước khi sửa.
3. Tạo phiên bản **mới** từ bản cũ, ví dụ `v04` khôi phục hình học `v02`; ghi rõ nguồn khôi phục trong lịch sử. Không xóa hoặc ghi đè `v02`, `v03`.
4. Xuất lại 3MF, kiểm tra bằng rule chung và project. Kết quả slice/in của phiên bản sau không tự áp dụng cho bản khôi phục.

F3D là bản thiết kế có tham số dùng để quay lại; 3MF là mesh để kiểm tra/slice, không thay cho lịch sử model tham số.
