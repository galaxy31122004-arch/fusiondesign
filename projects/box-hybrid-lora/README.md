# Box HybridLora

Hộp tham số cho mạch LoRa 100 × 100 mm, nguồn adapter 12 V và anten ngoài. Máy mặc định: Bambu Lab P2S Full Combo. Các bản hiện có chỉ là nguyên mẫu để thử kích thước; chưa hoàn thiện lỗ xuyên vỏ, ron hoặc khả năng chống mưa.

## Hồ sơ

- [Tham số và dữ liệu đầu vào](notes/params.md)
- [Kiểm tra thiết kế và in](notes/checks.md)
- [Kết quả kiểm tra theo phiên bản](notes/results.md)
- [Lịch sử và quay lại](notes/HISTORY.md)

## File

- `design/`: một bản Fusion F3D mới nhất để dự phòng; model chính đã lưu trên Fusion.
- `print/sliced/`: chỉ chứa file đã slice và kiểm tra đúng máy, vật liệu, nozzle.
- `references/`: bản vẽ và ảnh nguồn của lần thiết kế này.
- `notes/`: quyết định, số đo, checklist, kết quả và lịch sử.
- `runs/`: mesh, log và file thử tạm thời; không đưa vào Git và dọn sau khi ghi kết quả.

Lần slice CLI đầu từng nạp sai profile và xuất G-code có `filament_type = PLA`; file lỗi đã được xóa sau khi ghi bằng chứng tại [results.md](notes/results.md). Chỉ dùng gói trong `print/sliced/` đã qua kiểm tra.

ID project và tên file là `box-hybrid-lora`; **Box HybridLora** là tên hiển thị. F3D hiện tại là v04; hai gói slice hiện tại là v03 và **không khớp v04**. Gói slice chỉ dùng thử bố cục cũ, chưa dùng làm hộp ngoài trời.
