# Rule ghi và thêm linh kiện vào thư viện

## Phạm vi

`library/components/` chỉ chứa loại linh kiện cơ bản có thể dùng lại giữa nhiều project: jack nguồn, đầu nối, cáp, công tắc, vít, ron và linh kiện tương tự. PCB riêng, vị trí linh kiện trên PCB, tọa độ lỗ, kích thước vỏ và cách lắp của một sản phẩm nằm trong `projects/<id>/`.

## Khi thêm linh kiện

1. Kiểm tra thư viện có cùng mã linh kiện và revision chưa. Cùng chức năng nhưng khác hãng, mã hoặc revision thì tạo mục mới.
2. Tạo `library/components/<id>/component.json` chứa `id`, `name`, `part_number`, `source`, `dimensions`, `notes`. Dùng trường đơn vị trong tên kích thước, ví dụ `front_width_mm`; không ghi số thiếu đơn vị.
3. Với mỗi giá trị, ghi `status`: `confirmed` nếu đo trên đúng linh kiện; `drawing` nếu đọc từ bản vẽ; `estimate` nếu là giả định; `pending` và `value: null` nếu chưa có số đo. Ghi dung sai khi bản vẽ có nêu.
4. `source` ghi tên tài liệu, hãng, revision, ngày, URL công khai nếu có và ngày trích xuất. Không buộc người dùng mở ảnh/PDF để biết thông số đã trích.
5. Ghi bằng text ý nghĩa của kích thước, điều kiện lắp và giới hạn sử dụng. Không tự coi đường kính một chi tiết trên bản vẽ là đường kính lỗ vỏ nếu bản vẽ không chỉ định lỗ khoét.
6. Lưu ảnh/PDF gốc trong `projects/<id>/references/` khi một project cần truy vết nguồn. Thư viện chung chỉ giữ text có cấu trúc.
7. Project tham chiếu `id` linh kiện đã chọn và ghi riêng vị trí, hướng lắp, khoảng hở, lỗ vỏ, vật liệu, cách làm kín và kết quả thử. Đổi linh kiện phải chạy lại các kiểm tra liên quan.

## Kiểm tra trước khi dùng trong Fusion

- Mã và revision có đúng linh kiện thực tế không?
- Kích thước dùng cho hình học có nguồn và trạng thái rõ ràng không?
- Mọi kích thước `pending` hoặc `estimate` được hiển thị là chưa chốt chưa?
- Lỗ xuyên vỏ, gioăng và khoảng hở cắm/rút có dữ liệu riêng hay chỉ đang suy từ kích thước linh kiện?
- Project có lưu kết quả lắp thử và rủi ro còn lại không?

Không dùng `estimate` để công bố kích thước sản xuất hoặc khả năng chống nước. Khi đo được kích thước thật, cập nhật bản ghi kèm nguồn và giữ lịch sử trong project nếu thay đổi ảnh hưởng model đã xuất.
