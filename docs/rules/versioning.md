# Rule phiên bản và dọn file trung gian

ID project dùng chữ thường và dấu gạch nối, không có dấu cách; tên hiển thị nằm trong README. Fusion là nguồn model tham số. Git lưu thay đổi của script, ghi chú và những file phát hành đã commit; không tạo một tập file F3D/mesh vĩnh viễn cho mỗi lần sửa.

## Tên phiên bản

- Tên phiên bản của project theo dạng `vMAJOR.MINOR.PATCH`, ví dụ `v1.0.0`. Project mới bắt đầu ở `v1.0.0` theo quyết định của người dùng, kể cả khi còn là nguyên mẫu; trạng thái sẵn sàng in/sử dụng được ghi **riêng** trong checklist, không suy ra từ số version.
- Mọi lần chỉnh trong cùng một đợt làm việc giữ nguyên số version. Git commit, Fusion timeline và bản ghi kiểm tra phân biệt các lần sửa nội bộ. Chỉ đổi version khi người dùng bắt đầu một lượt sử dụng/sửa khác và chỉ rõ việc tăng version; không tự suy ra MAJOR/MINOR/PATCH từ số lần chạy script hoặc slice.
- Tên file làm việc: `<id>_vX.Y.Z.f3d` cho Fusion và `<id>_vX.Y.Z_<part>_<material>.3mf` cho gói Bambu đã kiểm tra. Trong `notes/HISTORY.md`, ghi cả version và Git commit/Fusion document để truy lại các lần sửa cùng version.
- Không tự thêm hậu tố `-beta`/`-dev` của firmware vào file CAD. Trạng thái nguyên mẫu, thử in hay đã chốt nằm trong checklist thay vì tên version.

## Mỗi lần sửa model

1. Lưu document trong Fusion sau khi sửa; kiểm tra `isSaved = True` và ghi tên project/phiên bản Fusion vào `notes/HISTORY.md`. Timeline cho phép kiểm tra các feature; bản lưu Fusion và Git là hai cách khôi phục khác nhau.
2. Giữ **một bản F3D mới nhất** ở `design/` làm bản dự phòng mang đi được. Khi có bản mới, xác nhận đã lưu trên Fusion và F3D mới mở được trước khi xóa bản F3D cũ khỏi thư mục làm việc. Bản cũ đã commit vẫn còn trong Git history. Nếu Fusion không lưu được, giữ F3D dự phòng trước khi dọn.
3. Xuất mesh trung gian vào `runs/mesh/` (bị Git bỏ qua), kiểm tra kích thước/đơn vị rồi đưa sang Bambu Studio. Sau khi gói Bambu đã slice và kiểm tra xong, xóa mesh trung gian; xuất lại từ Fusion khi cần.
4. Giữ gói Bambu 3MF đã kiểm tra ở `print/sliced/` cho từng part/plate cần in, với tên `<id>_vX.Y.Z_<part>_<material>.3mf`. Gói này chứa cấu hình và G-code; không dựa vào lịch sử Undo của ứng dụng để tìm lại file in sau này. Khi thay model/profile trong cùng version, tạo gói mới, xác minh trước rồi mới xóa gói cũ khỏi thư mục làm việc.
5. Ghi thay đổi vào `notes/HISTORY.md`, trạng thái hiện tại vào `notes/checks.md`, số đo/kết quả vào `notes/results.md`. Sau khi đã ghi kết quả, dọn log và file thử trong `runs/`; giữ file lỗi lâu hơn chỉ khi đang cần chẩn đoán.
6. Sau khi bản mới đã lưu và xuất an toàn, đóng tab Fusion cũ **của đúng project**. Tab có chỉnh sửa chưa lưu phải được lưu hoặc sao lưu vào `runs/session_backups/` trước khi đóng. Không đóng tab project khác hoặc tab không xác định được nguồn gốc.

## Quay lại

1. Xem `notes/HISTORY.md` để tìm phiên bản và kết quả kiểm tra tương ứng.
2. Trong Fusion, mở phiên bản đã lưu hoặc quay tới feature cần sửa trong timeline. Với bản trước chỉ lưu local, lấy F3D từ Git history rồi mở trong Fusion; không coi Undo/timeline là bản sao lưu của toàn bộ quá trình in.
3. Lưu thay đổi được khôi phục thành phiên bản mới trong Fusion, xuất F3D dự phòng và slice lại. G-code và kết quả thử của phiên bản sau không tự áp dụng cho bản khôi phục.
