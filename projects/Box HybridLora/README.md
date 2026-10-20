# Box HybridLora

Hộp tham số cho mạch LoRa 100 × 100 mm, nguồn adapter 12 V và anten ngoài. Máy mặc định: Bambu Lab P2S Full Combo. Các bản hiện có chỉ là nguyên mẫu để thử kích thước; chưa hoàn thiện lỗ xuyên vỏ, ron hoặc khả năng chống mưa.

## Hồ sơ

- [Tham số và dữ liệu đầu vào](notes/params.md)
- [Kiểm tra thiết kế và in](notes/checks.md)
- [Lịch sử và quay lại](notes/HISTORY.md)

## File

- `design/`: các bản Fusion F3D có tham số.
- `print/mesh/`: 3MF xuất từ Fusion cho từng chi tiết.
- `print/sliced/`: chỉ chứa file đã slice và kiểm tra đúng máy, vật liệu, nozzle.
- `references/`: bản vẽ và ảnh nguồn của lần thiết kế này.
- `notes/`: quyết định, số đo, cảnh báo và lịch sử.
- `runs/`: log và file thử nghiệm; không đưa vào Git.

Không dùng file trong `runs/invalid_cli_slice/` để in: lần thử CLI đầu tiên đã nạp sai profile kế thừa và xuất G-code có `filament_type = PLA`.
