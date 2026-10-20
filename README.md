# FusionDesign

Quy trình thiết kế tham số trong Autodesk Fusion, kiểm tra khả năng in, xuất model và chuẩn bị in trong Bambu Studio. Máy in mặc định của các project là **Bambu Lab P2S Full Combo**; vật liệu, nozzle, bàn in và profile được xác nhận theo từng lần in.

## Cấu trúc

- [AGENTS.md](AGENTS.md): rule điều phối chung cho người và AI.
- [docs/README.md](docs/README.md): mục lục tài liệu và rule chung.
- [Box HybridLora](projects/Box%20HybridLora/README.md): hồ sơ hộp LoRa ngoài trời, thiết kế, chuẩn bị in và lịch sử phiên bản.
- [scripts/fusion/README.md](scripts/fusion/README.md): nơi đặt script Fusion API khi thiết kế được chốt.
- [library/README.md](library/README.md): thông số linh kiện dùng lại, lưu dưới dạng text có cấu trúc.

## Quy trình

1. Ghi mục đích, kích thước, cách lắp, môi trường sử dụng, vật liệu và màu dự kiến trong hồ sơ project.
2. Đọc rule chung và cảnh báo rủi ro ngay trước khi thiết kế.
3. Chốt hình học, tạo model tham số trong Fusion, kiểm tra lại khi model thay đổi.
4. Xuất model, kiểm tra kích thước và preview slice trong Bambu Studio với profile thực tế.
5. In thử, đo kết quả và cập nhật checklist theo bằng chứng.

Các thông số chưa xác định được giữ ở trạng thái **Chưa chốt**. Không suy ra khả năng chống nước hay chất lượng in chỉ từ model hoặc kết quả slice.
