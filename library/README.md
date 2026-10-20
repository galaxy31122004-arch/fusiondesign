# Thư viện linh kiện

Lưu thông số dạng text của các loại linh kiện cơ bản có thể tái dùng khi thiết kế nhiều project: jack DC, đầu nối SMA, cáp và các biến thể của chúng. Mỗi linh kiện nằm trong `components/<id>/component.json`; không cần mở ảnh hoặc PDF để đọc những thông số đã ghi. Script Fusion chỉ được dùng kích thước có nguồn và đúng `part_number`; các mục `pending` phải được hiển thị là chưa chốt.

Kích thước sản phẩm riêng như PCB 100 × 100 mm, số lỗ, đường kính lỗ, khoảng cách tâm lỗ và vị trí đặt linh kiện trên vỏ nằm trong `projects/<tên-project>/`, không đưa vào thư viện chung.

## Thành phần hiện có

| ID | Loại linh kiện | Dữ liệu có sẵn |
| --- | --- | --- |
| [dc-jack](components/dc-jack/component.json) | Jack nguồn DC chân hàn | Kích thước mặt trước; lỗ khoét vỏ chưa có |
| [ipex-sma-yic](components/ipex-sma-yic/component.json) | Cáp I-PEX–SMA Female YIC có O-ring | Kích thước ren, đầu SMA và chiều dài cáp |
| [ipex-sma-rg178](components/ipex-sma-rg178/component.json) | Cáp IPEX/U.FL–SMA Female SOMECONN RG178 | Kích thước đầu nối được ghi trên bản vẽ |

Quy tắc cập nhật: ghi giá trị, đơn vị, nguồn (tên bản vẽ, mã, revision/ngày nếu có) và trạng thái xác nhận cho từng kích thước. File ảnh/PDF gốc của lần sử dụng **Box HybridLora** được lưu trong `projects/box-hybrid-lora/references/` để truy vết, không thuộc thư viện dùng chung. Nếu đổi mã linh kiện, tạo mục mới hoặc phiên bản mới; không sửa ngầm thông số của linh kiện cũ.

Quy trình chi tiết để thêm mục mới nằm trong [rule thư viện linh kiện](../docs/rules/component-library.md).
