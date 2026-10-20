# Rule vật liệu và cách in cho P2S Full Combo

## Nguồn dữ liệu và mức tin cậy

Máy in mặc định: **Bambu Lab P2S Full Combo** theo lựa chọn của người dùng. Ví dụ tra cứu cục bộ: Bambu Studio cài trên máy hiện có preset P2S ở `%APPDATA%\BambuStudio\system\BBL\machine`, `filament` và `process`. Khi kiểm tra ngày 2026-10-20, preset `Bambu Lab P2S 0.4 nozzle.json` đặt `Bambu PLA Basic @BBL P2S` làm filament mặc định và `0.20mm Standard @BBL P2S` làm process mặc định. Đường dẫn này thay đổi theo máy và user nên chỉ là ví dụ; nguồn chính thức là profile đang mở trong Bambu Studio và tài liệu Bambu Lab hiện hành. Nội dung preset cục bộ không xác nhận cuộn nhựa, nozzle hay phụ kiện nào đang thực sự lắp trên máy.

Tài liệu web chính thức chưa truy cập được trong lần kiểm tra này. Vì vậy, trước khi biến một nhận định vật liệu thành ngưỡng chặn thiết kế hoặc khuyến nghị bảo đảm, phải xác minh thêm từ tài liệu Bambu Lab hiện hành hoặc mẫu in thử của đúng cấu hình.

## Trình tự chọn vật liệu

1. Ghi mục đích sử dụng: cần đẹp, chịu lực, chịu nhiệt, ngoài trời, mềm dẻo, tiếp xúc hóa chất hay lắp ghép. Không suy ra vật liệu chỉ từ tên chi tiết.
2. Ghi **hãng, tên đầy đủ, biến thể và màu** của cuộn nhựa. Các biến thể như Basic, HF, Silk, Matte, CF và `for AMS` phải được xem là vật liệu/profile khác nhau cho đến khi kiểm tra.
3. Ghi đường cấp liệu dự kiến của Full Combo. Xác minh khả năng dùng cuộn đó với đường cấp liệu đã chọn; không mặc định mọi vật liệu đều chạy qua AMS chỉ vì máy là bản Combo.
4. Ghi nozzle và bàn in đang lắp. Tìm preset khớp **máy + nozzle + vật liệu** trong Bambu Studio. Nếu chỉ có preset `Generic`, ghi rõ đang dùng generic và cần hiệu chỉnh/thử mẫu cho cuộn thực tế.
5. Đọc giá trị hiệu lực của profile sau khi giải quyết `inherits` và profile người dùng chỉnh sửa; không chỉ đọc một file JSON lẻ rồi coi các trường còn thiếu là không có cấu hình.
6. Chọn process profile phù hợp với nozzle và mục tiêu chất lượng. Kiểm tra layer height, wall, infill, support, cooling, nhiệt độ, tốc độ/flow, bàn in và các yêu cầu xử lý vật liệu do profile hoặc nguồn đã xác minh nêu ra.
7. Khi đổi vật liệu, màu có profile riêng, nozzle, bàn in hoặc process profile, chạy lại các kiểm tra thiết kế và preview slice bị ảnh hưởng.

Trước khi xuất file in, xác nhận loại bàn in **đang lắp thực tế** rồi chọn đúng mục trong Bambu Studio. Nếu chưa biết loại bàn, chỉ được tạo mesh để xem hoặc thử slice để chẩn đoán; chưa phát hành G-code để in. Với công cụ CLI, kiểm tra G-code đã giải quyết đầy đủ profile kế thừa và không rơi về giá trị mặc định của vật liệu/máy khác.

## Nhóm rủi ro theo vật liệu để kiểm tra sớm

| Nhóm vật liệu | Câu hỏi phải kiểm tra trước khi chốt thiết kế và in |
| --- | --- |
| PLA và biến thể | Chi tiết có yêu cầu chịu nhiệt hoặc tải lâu dài không? Biến thể màu/hiệu ứng có profile riêng không? Thành, lỗ và bề mặt quan trọng có phù hợp với nozzle và process đã chọn không? |
| PETG và biến thể | Có vùng bridge/overhang, mặt cần đẹp hoặc khe lắp cần thử mẫu không? Bàn in và profile đúng với biến thể, ví dụ Basic hoặc HF, chưa? |
| ABS/ASA | Hộp có đáy lớn, thành cao hoặc yêu cầu kích thước chặt cần kiểm tra nguy cơ cong vênh/co ngót không? Điều kiện buồng in, bàn in và thông gió đã được xác nhận chưa? |
| TPU | Độ mềm có làm thành hộp biến dạng ngoài ý muốn không? Đường cấp liệu có phù hợp đúng biến thể TPU đang dùng không? Profile tốc độ/flow có khớp không? |
| Vật liệu gia cường hoặc kỹ thuật | Nozzle, đường cấp liệu, điều kiện bảo quản/sấy và profile có đáp ứng yêu cầu của đúng cuộn nhựa không? Chi tiết có cần mẫu thử kích thước hoặc độ bền trước khi dùng không? |
| Vật liệu support | Có thực sự cần support không? Vật liệu support có tương thích với vật liệu chính, đường cấp liệu và profile đang dùng không? |

Bảng này là **danh sách câu hỏi**, chưa phải khẳng định một vật liệu chắc chắn in tốt hay lỗi trên P2S. Chỉ gắn cảnh báo khi có dữ liệu project hoặc nguồn kỹ thuật xác minh điều kiện cụ thể.

## Rule cảnh báo khi thiết kế

- **MAT-001 — Thiếu vật liệu:** cho phép dựng bản phác thảo, nhưng gắn `Chưa xác minh` cho mọi đánh giá phụ thuộc vật liệu. Chưa chốt profile hoặc tuyên bố model in được.
- **MAT-002 — Profile không khớp:** cảnh báo nếu tên cuộn, biến thể, máy hoặc nozzle không khớp preset được chọn. Đưa ra preset khớp nếu có; nếu không có, dùng quy trình hiệu chỉnh mẫu thử, không tự sao chép preset của vật liệu khác.
- **MAT-003 — Đường cấp liệu chưa xác minh:** cảnh báo trước khi lập kế hoạch in nhiều màu hoặc support nhiều vật liệu nếu khả năng cấp liệu của từng cuộn chưa được xác nhận.
- **MAT-004 — Yêu cầu chức năng xung đột vật liệu:** nếu yêu cầu về nhiệt, tải, mềm dẻo, ngoài trời hoặc độ chính xác chưa có bằng chứng vật liệu đáp ứng, nêu rủi ro ngay trước khi chốt hình học.
- **MAT-005 — Đổi vật liệu sau khi dựng:** đánh dấu các kết luận cũ cần kiểm tra lại; đánh giá lại bề dày, khe lắp, hướng in, support, bám bàn và kích thước sau slice theo profile mới.
- **MAT-006 — Profile thay đổi:** trước khi in, so thông số thực tế trong Bambu Studio với profile đã dùng khi phân tích. Nếu khác, cập nhật báo cáo và chạy lại preview.

Mỗi cảnh báo theo định dạng trong [printability.md](printability.md): vị trí hoặc feature liên quan, dữ liệu đo, điều kiện áp dụng, bằng chứng, mức độ và phương án xử lý trong thiết kế hoặc khi in. Không tự thay đổi kích thước chức năng để phù hợp với vật liệu mới.
