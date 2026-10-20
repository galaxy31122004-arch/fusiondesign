# Box HybridLora

Hộp tham số cho PCB LoRa 100 × 100 mm, nguồn adapter 12 V và anten ngoài. Version hiện tại là **v1.0.0** theo [rule phiên bản](../../docs/rules/versioning.md); đây vẫn là nguyên mẫu, chưa xác nhận độ kín nước hoặc lắp linh kiện thật. Máy in dự kiến: Bambu Lab P2S Full Combo, PETG HF, nozzle 0,4 mm, Textured PEI Plate.

## Bản đồ project

```text
box-hybrid-lora/
├── README.md          # Một bản dẫn hướng cho toàn project
├── design/            # F3D tham số hiện tại; mở/chỉnh trong Fusion
├── print/
│   ├── prepare/       # Hai 3MF hiện tại để mở và chỉnh trong Bambu Studio
│   └── sliced/        # Chỉ tạo khi có gói Bambu chứa G-code đã kiểm tra
├── notes/             # Tham số, checklist, kết quả đo và lịch sử
├── references/        # Ảnh/bản vẽ đầu vào để đối chiếu nguồn số đo
└── runs/              # Mesh, preset, log và bản thử tạm; Git bỏ qua
```

| Nơi lưu | File hiện tại | Chức năng |
| --- | --- | --- |
| `design/` | [box-hybrid-lora_v1.0.0.f3d](design/box-hybrid-lora_v1.0.0.f3d) | Nguồn CAD tham số dự phòng; không sửa nhị phân ngoài Fusion. Document đang mở trong Fusion còn tên làm việc `v04`, cùng hình học này. |
| `print/prepare/` | [thân](print/prepare/box-hybrid-lora_v1.0.0_body.3mf), [nắp](print/prepare/box-hybrid-lora_v1.0.0_lid.3mf) | Hai part 3MF đơn vị mm, mở được trong Bambu Studio để chọn profile, support/brim và slice. **Chưa chứa G-code được xác minh.** |
| `print/sliced/` | Chưa có bản v1.0.0 | Chỉ đặt gói đã slice thành công, mở lại được và kiểm tra G-code đúng máy/vật liệu/plate. |
| `notes/` | [params](notes/params.md), [checks](notes/checks.md), [results](notes/results.md), [HISTORY](notes/HISTORY.md) | Kích thước/giả định, trạng thái rủi ro, bằng chứng và cách quay lại. |
| `references/` | Ảnh PCB, bản vẽ jack DC và cáp IPEX–SMA | Nguồn tham khảo; số đo dùng lại của linh kiện cơ bản nằm ở [library](../../library/README.md). |
| `runs/` | File sinh trong lúc chạy Fusion/Bambu/MeshRight | Không phải bản phát hành; không đưa vào Git. |

File thân trong `print/prepare/` là 3MF mesh xuất từ Fusion nên Bambu Studio có thể hỏi ánh xạ một màu khi mở; chọn `1 Recommended`. File nắp đã được lưu lại như project Bambu chưa slice. Cả hai đã được nạp và slice thử, nhưng không có G-code bên trong các file chuẩn bị này.

[Script Fusion](../../scripts/fusion/README.md) tạo F3D và mesh; [script in và kiểm tra mesh](../../scripts/printing/README.md) giúp đọc preset và báo cáo mesh. Rule chung nằm ở [docs](../../docs/README.md).

## Trạng thái in

- Thân v1.0.0 cần support dưới vành trong: slice không support báo `floating cantilever`; bật `normal(auto)` bỏ warning nhưng ước tính tăng từ 181,6 g lên 267,5 g. Cần xem preview và khả năng tháo support khỏi khoang trước khi in.
- Nắp v1.0.0 slice thử không báo warning. Bambu CLI trên máy tạo G-code tạm nhưng lỗi khi xuất gói 3MF, vì vậy `print/sliced/` chưa có bản v1.0.0.
- Chưa có lỗ/giải pháp làm kín cho nguồn DC cắm trực tiếp; ron và đầu SMA chưa thử lắp. Không dùng nguyên mẫu này làm hộp ngoài trời có mạch đang cấp điện.

Hai gói v03 đã slice trước đây không khớp hình học hiện tại; chúng vẫn nằm trong lịch sử Git. Khi có gói v1.0.0 đã kiểm tra, thêm vào `print/sliced/` và cập nhật [results.md](notes/results.md), không đổi version nếu vẫn trong cùng lượt sửa này.
