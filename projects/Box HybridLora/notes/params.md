# Box HybridLora — tham số và dữ liệu đầu vào

## Công dụng

Hộp chứa cụm mạch LoRa dùng ngoài trời, chịu mưa tạt trực tiếp. Nguồn cấp từ adapter 12 V; không có pin. Anten nhô ra ngoài. Hộp cần có nắp và giải pháp cho các vị trí xuyên vỏ; chưa xác nhận mức chống nước.

## Dữ liệu đã biết

| Mục | Giá trị | Nguồn |
| --- | --- | --- |
| Kích thước PCB | 100 × 100 mm | Người dùng xác nhận; [ảnh layout](../references/pcb-layout.png) |
| Đường kính bốn lỗ bắt vít PCB | 2 mm | Người dùng xác nhận; [ảnh chi tiết](../references/pcb-mounting-detail.png) |
| Khoảng cách tâm hai lỗ trên cạnh được đo | 94,679 mm | Kích thước ghi trong ảnh chi tiết PCB |
| Tâm lỗ dưới tới mép PCB | 2,436 mm | Kích thước ghi trong ảnh chi tiết PCB |
| Chiều cao cụm mạch/anten cần chứa | khoảng 50 mm; cần đo lại | Người dùng mô tả cụm 10 × 10 × 5 cm |
| Nguồn | Adapter 12 V, không có pin | Người dùng cung cấp |
| Vị trí nguồn trên layout | Góc dưới trái của ảnh PCB | Ảnh người dùng cung cấp |
| Hướng ra anten mong muốn | Góc trên phải, đối diện vị trí nguồn | Người dùng chỉ định |
| Môi trường | Ngoài trời, mưa tạt trực tiếp | Người dùng xác nhận |
| Máy in mặc định | Bambu Lab P2S Full Combo | Rule chung |
| Vật liệu in thử | Bambu PETG HF | Người dùng chọn 2026-10-20; màu chưa chọn |
| Nozzle in thử | 0,4 mm | Người dùng chọn 2026-10-20 |
| Loại bàn in đang lắp | Chưa xác định | Người dùng muốn dùng plate đi kèm Combo; chưa xác minh tên plate thực tế |

## Tham số Fusion cần chốt

Tất cả tham số dùng **mm**. Kích thước PCB 100 × 100 mm chưa bao gồm khoảng hở lắp ráp, thành, đường ron và không gian cho đầu nối. Các giá trị trong bản sơ bộ chỉ để dựng bố cục, chưa phải kích thước được chốt.

Người dùng đã duyệt dựng **bản sơ bộ thân và nắp rời**. Script dùng kích thước tạm `120 × 120 mm`, thân cao `65 mm`, nắp dày `5 mm`, thành và đáy `3 mm` chỉ để kiểm tra bố cục. Các giá trị này chưa được duyệt làm kích thước sản xuất. Nắp hiện là tấm phẳng, chưa có ngàm, vít hoặc đường ron; vỏ chưa chống nước. Vị trí nắp ban đầu ở Z = 65 mm; nếu đổi chiều cao thân qua tham số Fusion, cần chạy lại script để đặt lại nắp.

| Tên tham số | Ý nghĩa | Trạng thái |
| --- | --- | --- |
| `box_length` | Chiều dài ngoài của thân hộp | Tạm 120 mm |
| `box_width` | Chiều rộng ngoài của thân hộp | Tạm 120 mm |
| `body_height` | Chiều cao thân hộp | Tạm 65 mm |
| `lid_thickness` | Độ dày nắp phẳng | Tạm 5 mm |
| `wall_thickness` | Độ dày thành và đáy của shell sơ bộ | Tạm 3 mm; chưa xác minh theo vật liệu/profile |
| `corner_radius` | Bán kính bo bốn góc ngoài của thân và nắp | Tạm 4 mm; cần kiểm tra lại thành và đường nắp |
| `pcb_clearance_xy` | Khoảng hở giữa PCB và thành | Chưa chốt |
| `pcb_standoff_height` | Chiều cao đỡ PCB từ mặt trong đáy | Tạm 5 mm trong v3; cần kiểm tra linh kiện dưới PCB |
| `boss_diameter` | Đường kính ngoài trụ đỡ PCB | Tạm 5 mm trong v3 |
| `mount_hole_diameter` | Đường kính lỗ mù trên trụ | 2 mm trong v3; loại vít/chân bắt chưa chốt |
| `lid_overlap` | Phần nắp chồng lên thân | Chưa chốt |
| `seal_groove` | Hình học rãnh ron nếu chọn ron | Chưa chốt loại ron |
| `antenna_port` | Vị trí và hình học lỗ anten | Chưa chốt theo đầu nối thực tế |
| `power_port` | Vị trí và hình học lỗ dây 12 V | Chưa chốt theo đầu nối thực tế |

## Dữ liệu cần bổ sung trước khi chốt hình học

- Vị trí, đường kính lỗ bắt PCB hoặc cách giữ PCB nếu không có lỗ; ưu tiên file `.kicad_pcb` để đo chính xác.
- Đã biết đường kính lỗ PCB là 2 mm, hai tâm trên một cạnh cách nhau 94,679 mm và tâm dưới cách mép 2,436 mm. Với PCB cao 100 mm, tâm trên cách mép trên 2,885 mm (suy ra bằng phép trừ). Bốn góc có bố trí tương tự theo người dùng. Tọa độ theo phương ngang chưa có kích thước trực tiếp, nên nếu dùng giả định đối xứng phải ghi rõ và kiểm tra với PCB thật trước khi in.
- Chiều cao linh kiện cao nhất, phần nhô của domino nguồn, khoảng trống để cắm/rút dây và vùng cần thao tác.
- Kết cấu anten xuyên vỏ: đầu ren có ron hay cáp đi qua nút cao su; kích thước lắp thực tế.
- Thư viện [linh kiện](../../../library/README.md) lưu thông số text của jack DC và hai loại cáp IPEX–SMA khác nhau. Thông số PCB và vị trí lỗ nằm trong project này. Cáp YIC có ren `1/4-36 UNS` và O-ring, nhưng chưa có đường kính lỗ vỏ được chỉ định. Cần xác nhận mã cáp thực tế và đo đầu nối/ron trước khi khoét lỗ.
- Loại đầu nối dây nguồn 12 V, đường kính dây, hướng dây đi ra và cách làm kín lỗ xuyên vỏ.
- Vật liệu, biến thể, màu, nozzle, bàn in và profile dự kiến.
- Cách cố định hộp ngoài trời, mặt hướng lên khi lắp, yêu cầu về bảo trì và mức chống nước cần kiểm chứng.

## Bố trí thử trong v3

PCB được đặt giả định từ `(10, 10)` đến `(110, 110)` mm trong thân hộp 120 × 120 mm. Khoảng hở danh nghĩa từ cạnh PCB tới mặt trong thành là 7 mm. Bốn tâm trụ/lỗ mù trên thân là `(12,436; 12,436)`, `(107,564; 12,436)`, `(12,436; 107,115)` và `(107,564; 107,115)` mm, đo từ góc ngoài thân hộp. Phương đứng dùng số 94,679 mm tâm–tâm và 2,436 mm tới mép dưới trong ảnh; phương ngang **giả định đối xứng** với độ lùi 2,436 mm, chưa có kích thước trực tiếp. Trụ Ø5 mm, cao 5 mm trên mặt đáy trong; lỗ Ø2 mm sâu 4 mm và không xuyên đáy. Đây là bố trí thử, cần đối chiếu PCB thật trước khi chọn vít hoặc in vỏ sử dụng.
