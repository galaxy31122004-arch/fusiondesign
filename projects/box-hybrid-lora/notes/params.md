# Box HybridLora — tham số và dữ liệu đầu vào

## Bố trí v1.0.0 đang kiểm tra

Đơn vị mm, gốc `(0, 0)` tại góc ngoài dưới trái của thân khi nhìn từ trên. Đây là bố trí nguyên mẫu trong script, **chưa xác minh trên model Fusion hoặc mẫu in**. Rãnh nhỏ chỉ nằm ở **thân hộp**, dành cho dây ron tròn 2 mm thử nghiệm; chưa chọn ron thực tế.

| Chi tiết | Kích thước/vị trí dự kiến |
| --- | --- |
| Thân ngoài | 146 × 146 × 68; thành và đáy 5 |
| Nắp | 146 × 146 × 5; bo viền mặt trên R1,2 |
| PCB giả định | từ `(23, 23)` tới `(123, 123)`; lòng miệng sau vành từ `(20, 20)` tới `(126, 126)` |
| Rãnh ron trên vành thân | đường vuông liên tục giữa biên `(16,2; 16,2)`–`(129,8; 129,8)` và `(18,4; 18,4)`–`(127,6; 127,6)`; rộng 2,2, sâu 1,5 |
| Tâm vít nắp | `(10,5; 10,5)`, `(135,5; 10,5)`, `(10,5; 135,5)`, `(135,5; 135,5)`; nằm ngoài đường ron |
| Tâm tai bắt vỏ | `(-4,5; 28)`, `(-4,5; 118)`, `(150,5; 28)`, `(150,5; 118)`; lỗ thử Ø4,5 |
| Tâm lỗ SMA | thành phải X = 146, Y = 122, Z = 55; lỗ thử Ø6,6 |

Script kiểm tra hình chữ nhật gốc bắt đầu tại `(0, 0)` và các tai là một khối liền với thân trước khi xuất. Cần đo lại lỗ SMA, rãnh và đối chiếu đầu cáp thật; tuyệt đối chưa coi bản này là vỏ chống nước.

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
| Loại bàn in dự kiến | Bambu Textured PEI Plate | Chữ trên ảnh plate người dùng gửi 2026-10-20; xác nhận tấm đang lắp trước khi in |

## Tham số Fusion cần chốt

Tất cả tham số dùng **mm**. Kích thước PCB 100 × 100 mm chưa bao gồm khoảng hở lắp ráp, thành, đường ron và không gian cho đầu nối. Các giá trị trong bản sơ bộ chỉ để dựng bố cục, chưa phải kích thước được chốt.

Bản v1.0.0 được tạo tham số trực tiếp trong Fusion vì lỗ, trụ, nắp và đường ron cần kích thước chức năng. Kích thước vẫn là bố trí thử, chưa duyệt sản xuất. Các giá trị v03 nằm ở mục lịch sử bên dưới.

| Tên tham số | Ý nghĩa | Trạng thái |
| --- | --- | --- |
| `box_length`, `box_width` | Kích thước ngoài thân/nắp | Tạm 146 × 146 mm |
| `body_height` | Chiều cao thân | Tạm 68 mm |
| `lid_thickness` | Độ dày nắp | Tạm 5 mm |
| `wall_thickness` | Thành và đáy | Tạm 5 mm; chưa xác minh theo mẫu in |
| `corner_radius`, `lid_top_radius` | Bo góc ngoài và mép trên nắp | Tạm R4 và R1,2 mm |
| `pcb_standoff_height`, `boss_diameter` | Trụ đỡ PCB | Tạm cao hơn đáy trong 5 mm, Ø5 mm |
| `mount_hole_diameter` | Lỗ mù trên trụ PCB | Ø2 mm; loại vít/chân bắt chưa chốt |
| `lid_post_diameter`, `lid_pilot_diameter` | Trụ và lỗ mù vít nắp | Tạm Ø9 và Ø2,5 mm |
| `gasket_cord_diameter`, `gasket_groove_width`, `gasket_groove_depth` | Dây ron và rãnh thử trên thân | Tạm Ø2; rộng 2,2; sâu 1,5 mm; chưa có dây thực tế |
| `antenna_panel_hole` | Lỗ SMA trên thành phải | Tạm Ø6,6 mm; chưa thử đầu SMA thực tế |
| `ear_diameter`, `ear_hole_diameter` | Tai bắt ngoài và lỗ | Tạm Ø14 và Ø4,5 mm |
| Lỗ nguồn DC | Vị trí/kích thước nguồn 12 V | Chưa thiết kế vì chưa chốt cách làm kín |

## Dữ liệu cần bổ sung trước khi chốt hình học

- Vị trí, đường kính lỗ bắt PCB hoặc cách giữ PCB nếu không có lỗ; ưu tiên file `.kicad_pcb` để đo chính xác.
- Đã biết đường kính lỗ PCB là 2 mm, hai tâm trên một cạnh cách nhau 94,679 mm và tâm dưới cách mép 2,436 mm. Với PCB cao 100 mm, tâm trên cách mép trên 2,885 mm (suy ra bằng phép trừ). Bốn góc có bố trí tương tự theo người dùng. Tọa độ theo phương ngang chưa có kích thước trực tiếp, nên nếu dùng giả định đối xứng phải ghi rõ và kiểm tra với PCB thật trước khi in.
- Chiều cao linh kiện cao nhất, phần nhô của domino nguồn, khoảng trống để cắm/rút dây và vùng cần thao tác.
- Kết cấu anten xuyên vỏ: đầu ren có ron hay cáp đi qua nút cao su; kích thước lắp thực tế.
- Thư viện [linh kiện](../../../library/README.md) lưu thông số text của jack DC và hai loại cáp IPEX–SMA khác nhau. Thông số PCB và vị trí lỗ nằm trong project này. Cáp YIC có ren `1/4-36 UNS` và O-ring, nhưng chưa có đường kính lỗ vỏ được chỉ định. Cần xác nhận mã cáp thực tế và đo đầu nối/ron trước khi khoét lỗ.
- Loại đầu nối dây nguồn 12 V, đường kính dây, hướng dây đi ra và cách làm kín lỗ xuyên vỏ.
- Vật liệu, biến thể, màu, nozzle, bàn in và profile dự kiến.
- Cách cố định hộp ngoài trời, mặt hướng lên khi lắp, yêu cầu về bảo trì và mức chống nước cần kiểm chứng.

## Bố trí thử trong v3 (lịch sử)

PCB được đặt giả định từ `(10, 10)` đến `(110, 110)` mm trong thân hộp 120 × 120 mm. Khoảng hở danh nghĩa từ cạnh PCB tới mặt trong thành là 7 mm. Bốn tâm trụ/lỗ mù trên thân là `(12,436; 12,436)`, `(107,564; 12,436)`, `(12,436; 107,115)` và `(107,564; 107,115)` mm, đo từ góc ngoài thân hộp. Phương đứng dùng số 94,679 mm tâm–tâm và 2,436 mm tới mép dưới trong ảnh; phương ngang **giả định đối xứng** với độ lùi 2,436 mm, chưa có kích thước trực tiếp. Trụ Ø5 mm, cao 5 mm trên mặt đáy trong; lỗ Ø2 mm sâu 4 mm và không xuyên đáy. Đây là bố trí thử, cần đối chiếu PCB thật trước khi chọn vít hoặc in vỏ sử dụng.
