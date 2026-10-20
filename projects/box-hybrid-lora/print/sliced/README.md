# File đã slice cho bản in thử v03

| Chi tiết | File Bambu 3MF có G-code | Ước tính slicer |
| --- | --- | --- |
| Thân | [box-hybrid-lora_v03_body_petg-hf.3mf](box-hybrid-lora_v03_body_petg-hf.3mf) | 2 giờ 16 phút, 105,2 g |
| Nắp | [box-hybrid-lora_v03_lid_petg-hf.3mf](box-hybrid-lora_v03_lid_petg-hf.3mf) | 51 phút, 39,9 g |

Đã slice bằng Bambu Studio 02.08.02.61 với profile **Bambu Lab P2S, nozzle 0,4 mm; Bambu PETG HF; Textured PEI Plate; layer 0,20 mm**. Mỗi gói 3MF chứa một `Metadata/plate_1.gcode`. Slicer trả `Success` và không có warning; metadata của G-code khớp P2S/PETG/plate, density 1,28 g/cm³ và nhiệt bàn Textured PEI theo preset là 70°C. Preview dạng thumbnail cho thấy thân đặt đáy xuống, nắp nằm phẳng.

**Chọn in riêng từng part:** thử xếp chung trên một plate chỉ chừa khoảng 2 mm giữa hai vật và khoảng 7 mm tới mép ngoài, trong khi thời gian tiết kiệm khoảng 7 phút. Giữ hai gói trên là lựa chọn mặc định cho lần in thử; file xếp chung là kết quả thử tạm đã được xóa sau khi ghi số đo trong `notes/results.md`.

Đây là **bản in thử bố cục**. Model chưa có lỗ anten/nguồn, ron và kết cấu khóa nắp; tọa độ ngang lỗ PCB còn giả định. Không dùng nó làm hộp chống mưa. Màu PETG HF và tình trạng tấm Textured PEI đang lắp thực tế cần xác nhận trên máy trước khi gửi lệnh in. File CLI lỗi có `filament_type = PLA` đã được xóa; tuyệt đối không in bản đó nếu khôi phục từ log ngoài thư mục này.
