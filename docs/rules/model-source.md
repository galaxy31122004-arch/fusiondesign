# Rule chọn nguồn model 3D

Áp dụng khi bắt đầu project hoặc đưa model từ AI, kho mẫu, người khác hay một ứng dụng khác vào Fusion.

1. Với chi tiết có kích thước chức năng, lỗ, ren, khe lắp, ron, vị trí PCB hoặc yêu cầu kín nước, ưu tiên tạo bằng tham số và feature có thể sửa trong Fusion. Ghi kích thước gốc và điều kiện kiểm tra trong project trước khi tạo hình.
2. Model lấy từ ngoài có thể dùng để tham khảo kiểu dáng hoặc làm nền thiết kế. Trước khi sửa, ghi nguồn, quyền sử dụng, định dạng, đơn vị, phiên bản gốc và những kích thước đã đo. Không coi hình đẹp hoặc khả năng mở file là bằng chứng lắp vừa hay in được.
3. Nếu nguồn là mesh STL/3MF, xác định phần nào có thể chỉnh sửa chính xác. Các mặt lắp ghép, lỗ và rãnh chức năng cần được đo và dựng lại bằng hình học tham số khi mesh không có feature/constraint đáng tin cậy. Giữ bản nhập gốc trong project để đối chiếu, không thay nó bằng một bản đã sửa mà mất nguồn.
4. Model AI tạo nhanh chỉ là hình tham khảo cho các phần thiên về tạo dáng. Với phần kỹ thuật, kiểm tra kích thước, độ kín của mesh, số khối, hướng đặt và khả năng gia công/in như với mọi model ngoài.
5. Chọn cách làm theo công sửa và kiểm chứng thực tế. Nếu hình rất đơn giản hoặc cần nhiều lần đổi kích thước, tạo tham số từ đầu. Nếu model ngoài đã có file CAD tham số, kích thước phù hợp và quyền dùng rõ, có thể nhập rồi chỉnh. Ghi quyết định trong `projects/<id>/notes/`.

Luồng hỗn hợp được phép: lấy mẫu ngoài cho dáng vỏ, dựng lại mặt ghép và mọi chi tiết chức năng trong Fusion, rồi kiểm tra và slice theo rule chung. Không chuyển mesh ngoài thành nguồn kích thước chính khi chưa đo lại.
