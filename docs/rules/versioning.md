# Rule phiên bản và dọn file trung gian

ID project dùng chữ thường và dấu gạch nối, không có dấu cách; tên hiển thị nằm trong README. Fusion là nguồn model tham số. Git lưu thay đổi của script, ghi chú và những file phát hành đã commit; không tạo một tập file F3D/mesh vĩnh viễn cho mỗi lần sửa.

## Tên phiên bản

- Tên phiên bản của project theo dạng `vMAJOR.MINOR.PATCH`, ví dụ `v1.0.0`. Project mới bắt đầu ở `v1.0.0` theo quyết định của người dùng, kể cả khi còn là nguyên mẫu; trạng thái sẵn sàng in/sử dụng được ghi **riêng** trong checklist, không suy ra từ số version.
- Mọi lần chỉnh trong cùng một đợt làm việc giữ nguyên số version. Git commit, Fusion timeline và bản ghi kiểm tra phân biệt các lần sửa nội bộ. Chỉ đổi version khi người dùng bắt đầu một lượt sử dụng/sửa khác và chỉ rõ việc tăng version; không tự suy ra MAJOR/MINOR/PATCH từ số lần chạy script hoặc slice.
- Tên file làm việc: `<id>_vX.Y.Z.f3d` cho Fusion, `<id>_vX.Y.Z_<part>.3mf` trong `print/prepare/` khi chưa gắn cấu hình vật liệu, và `<id>_vX.Y.Z_<part>_<material>.3mf` trong `print/sliced/` khi có profile và G-code đã kiểm tra. Trong `notes/HISTORY.md`, ghi cả version và Git commit/Fusion document để truy lại các lần sửa cùng version.
- Không tự thêm hậu tố `-beta`/`-dev` của firmware vào file CAD. Trạng thái nguyên mẫu, thử in hay đã chốt nằm trong checklist thay vì tên version.

## Mỗi lần sửa model

1. Lưu document trong Fusion sau khi sửa; kiểm tra `isSaved = True` và ghi tên project/phiên bản Fusion vào `notes/HISTORY.md`. Timeline cho phép kiểm tra các feature; bản lưu Fusion và Git là hai cách khôi phục khác nhau.
2. Giữ **một bản F3D mới nhất** ở `design/` làm bản dự phòng mang đi được. Khi có bản mới, xác nhận đã lưu trên Fusion và F3D mới mở được trước khi xóa bản F3D cũ khỏi thư mục làm việc. Bản cũ đã commit vẫn còn trong Git history. Nếu Fusion không lưu được, giữ F3D dự phòng trước khi dọn.
3. Xuất mesh trung gian vào `runs/<yyyymmdd>-<mục-đích>/mesh/` (bị Git bỏ qua), kiểm tra kích thước/đơn vị rồi đưa sang Bambu Studio. Nếu chưa có gói sliced đạt, giữ hai file 3MF hiện tại ở `print/prepare/` để người dùng mở và chỉnh trong Bambu Studio. Khi gói sliced mới đã mở lại được và khớp hình học, xóa file prepare tương ứng nếu không còn cần sửa; giữ file prepare nếu gói sliced chỉ chứa G-code hoặc không thể chỉnh model. Ghi lựa chọn vào README project.
4. Giữ gói Bambu 3MF đã kiểm tra ở `print/sliced/` cho từng part/plate cần in, với tên `<id>_vX.Y.Z_<part>_<material>.3mf`. Gói này chứa cấu hình và G-code; không dựa vào lịch sử Undo của ứng dụng để tìm lại file in sau này. Khi thay model/profile trong cùng version, tạo gói mới, xác minh trước rồi mới xóa gói cũ khỏi thư mục làm việc.
5. Ghi thay đổi vào `notes/HISTORY.md`, trạng thái hiện tại vào `notes/checks.md`, số đo/kết quả vào `notes/results.md`. Sau khi đã ghi kết quả, dọn file thử theo quy tắc `runs/` bên dưới.
6. Sau khi bản mới đã lưu và xuất an toàn, đóng tab Fusion cũ **của đúng project**. Tab có chỉnh sửa chưa lưu phải được lưu hoặc sao lưu vào `runs/session_backups/` trước khi đóng. Không đóng tab project khác hoặc tab không xác định được nguồn gốc.

## Vòng đời file

- `print/sliced/` chỉ chứa gói của model hiện tại đã kiểm tra; thư mục rỗng được giữ bằng `.gitkeep`. Gói cũ đã commit lấy lại từ Git theo commit ghi trong `notes/HISTORY.md`, **không** để zip hoặc G-code cũ cạnh bản hiện tại. Nếu cần một bản lưu ngoài Git, đặt vào kho lưu trữ riêng có nhãn version/commit, trạng thái "không dùng để in model mới" và thời hạn giữ do project ghi rõ.
- Mỗi lần chạy tạo một thư mục `runs/<yyyymmdd>-<mục-đích>/` với tên ngắn, chữ thường và dấu gạch nối. Trong đó đặt `mesh/`, `logs/`, `screenshots/`, `presets/` hoặc `diagnostics/` khi cần; không để ảnh, `result.json`, G-code, zip thử hay log rời ở root repo hoặc root `runs/`. Nếu công cụ chỉ xuất vào working directory, chuyển ngay kết quả vào thư mục lần chạy và ghi nguồn lệnh.
- File thử thành công dọn sau khi số đo cần thiết đã chép sang `notes/results.md` và file chính đã kiểm chứng. File lỗi chỉ giữ khi còn đang chẩn đoán: dùng thư mục `runs/<yyyymmdd>-<mục-đích>/diagnostics/` cùng một `README.md` ngắn ghi lỗi, lệnh tạo, bước tái hiện và ngày xem lại; dọn ở lần hoàn tất/chuyển giao tiếp theo. Backup của document chưa lưu được giữ đến khi có bản Fusion/F3D thay thế an toàn, không dọn theo thời hạn máy móc.
- `references/` giữ bản nguồn theo tên `<loại>-<mã-hoặc-chủ-đề>-<revision>.<ext>` khi có revision; nếu nguồn không ghi revision, dùng ngày nhận `yyyymmdd`. Ghi URL/người cung cấp, ngày nhận, mã/revision và kích thước đã rút ra trong `notes/` hoặc `component.json`. Khi đã chép số đo sang text trong library, giữ ảnh/PDF gốc nếu còn là bằng chứng của số đo; chỉ bỏ ảnh trùng khi đã xác nhận cùng nguồn/revision và cập nhật link tham chiếu.

## Kiểm tra trước commit

- `design/*.f3d`: file khác rỗng, Fusion mở được; ghi document, kích thước ngoài và tình trạng đã lưu cloud/local. Không chỉnh byte F3D trực tiếp.
- `print/prepare/*.3mf`: file khác rỗng, 3MF đọc được, đơn vị mm, số part và bbox khớp `notes/params.md`; kiểm tra mesh kín/số khối bằng công cụ hình học và mở lại trong Bambu Studio. Kiểm tra mesh không thay cho kiểm tra feature chức năng.
- `print/sliced/*.3mf`: thỏa các kiểm tra prepare, đồng thời có G-code đúng part, máy/nozzle/vật liệu/plate/layer/support/brim; Bambu Studio mở lại và preview các vùng rủi ro. Ghi warning, thời gian, vật liệu và phép kiểm tra vào `notes/results.md`. File chưa qua đủ checkpoint ở `runs/` hoặc `print/prepare/`, không vào `print/sliced/`.
- Tên file, link README và version phải khớp; sau khi thay file, kiểm tra `git diff --check` và xác nhận chỉ có một bản hiện hành mỗi part. Không dùng dung lượng file hoặc slice thành công đơn lẻ để kết luận đạt.

## Quay lại

1. Xem `notes/HISTORY.md` để tìm phiên bản và kết quả kiểm tra tương ứng.
2. Trong Fusion, mở phiên bản đã lưu hoặc quay tới feature cần sửa trong timeline. Với bản trước chỉ lưu local, lấy F3D từ Git history rồi mở trong Fusion; không coi Undo/timeline là bản sao lưu của toàn bộ quá trình in.
3. Lưu thay đổi được khôi phục thành phiên bản mới trong Fusion, xuất F3D dự phòng và slice lại. G-code và kết quả thử của phiên bản sau không tự áp dụng cho bản khôi phục.
