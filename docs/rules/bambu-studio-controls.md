# Rule chọn thông số trong Bambu Studio

Áp dụng cho các mục `Quality`, `Strength`, `Support` và `Others` của Bambu Studio. Đây là **quy trình chọn và kiểm tra**, không phải một preset cố định cho P2S. Tên và tác dụng một số mục có thể đổi theo phiên bản Studio; kiểm tra lại tooltip và Preview trên bản đang dùng. Các giải thích về chức năng đối chiếu với [mã nguồn Bambu Studio](https://github.com/bambulab/BambuStudio/blob/master/src/libslic3r/PrintConfig.cpp) (đọc 2026-10-21; RSCH-20261021-0001).

## Cách áp dụng

1. Chọn đúng máy, nozzle, filament, plate, hướng đặt và process. Giữ giá trị preset làm mốc; ghi lại mọi mục khác preset. Trường đang mờ hoặc không tạo đường in trong Preview không được coi là đã tác động tới bản in.
2. Đánh dấu bề mặt chức năng: lỗ, mặt ghép, vùng ron, trụ vít, thành chịu lực, mặt ngoài cần đẹp. Đổi một nhóm thông số theo một mục tiêu cụ thể, slice lại và xem Preview từng lớp ở các vùng đó.
3. So cảnh báo, đường in, support/brim/prime tower thực tế, thời gian và vật liệu. Chọn theo khả năng in và chức năng của part trước khi tối ưu thời gian/nhựa. In mẫu để xác nhận bám bàn, độ bền, độ khít hoặc độ kín; Preview không chứng minh các tính chất này.
4. Sau khi lưu gói, đọc lại cấu hình/G-code hiệu lực theo [rule file](versioning.md). Khi đổi model, vật liệu, nozzle, plate, layer hoặc hướng in, đánh giá lại các mục liên quan. Ghi các thử nghiệm và lý do chốt vào `projects/<id>/notes/results.md`.

## Quality

| Mục | Khi nào giữ hoặc chỉnh | Kiểm tra sau slice |
| --- | --- | --- |
| `Layer height` | Bắt đầu từ process khớp nozzle; giảm khi bề mặt cong/chi tiết nhỏ cần rõ hơn, tăng khi ưu tiên thời gian và hình học cho phép. Theo dải nozzle trong [process-settings.md](process-settings.md). | Đường thành, lỗ, overhang, số lớp vỏ và thời gian; không dùng lớp mỏng để thay dung sai thiết kế. |
| `Initial layer height` | Giữ preset nếu lớp đầu bám ổn; chỉ đổi khi cần giải quyết lỗi lớp đầu đã quan sát trên đúng plate/vật liệu. | Footprint, độ ép lớp đầu, lỗ/rãnh sát bàn và khả năng tháo. |
| `Mixed color sublayer` | Chỉ xét khi một lớp có nhiều màu và cần chia lớp con; bản một màu giữ tắt. | Màu từng lớp, số lần đổi màu, thời gian và nhựa xả. |
| `Seam position` | Chọn vị trí để tránh mặt ghép, mặt ron, lỗ và mặt trưng bày; `Aligned` gom vết vào một đường, các cách khác phải so trên hình thật. | Đường seam trên từng lớp và chỗ bắt đầu/kết thúc gần bề mặt chức năng. |
| `Only one wall on top surfaces` | Có thể tạo thêm chỗ cho top infill trên mặt phẳng; với mặt ghép, vành, trụ vít hoặc vùng cần kín/bền, so với chế độ không áp dụng trước khi giữ. | Số đường thành thực tế tại từng mặt trên chức năng. |
| `Only one wall on first layer` | Chỉ thử khi có mục tiêu rõ ở lớp đầu; với vỏ và chân bắt vít, giữ preset tắt trừ khi Preview và mẫu thử chứng minh phù hợp. | Số đường quanh chân/tai/lỗ trên lớp đầu và độ bám bàn. |

## Strength

| Mục | Khi nào giữ hoặc chỉnh | Kiểm tra sau slice |
| --- | --- | --- |
| `Wall loops` | Chọn theo độ dày thành thực tế, tải và độ kín; tăng infill không bù được thành/trụ chỉ có ít đường vỏ. Không đặt một số vòng chung cho mọi model. | Số đường thành tại chỗ mỏng nhất, quanh lỗ/vít, seam và đường ghép. |
| `Alternate extra wall` | Chỉ thử khi cần thêm đường vỏ xen kẽ ở vùng slicer có chỗ; không coi là thay thế tăng bề dày CAD. | Vùng nào thực sự thêm tường, vật liệu/thời gian và khe chức năng. |
| `Embedding the wall into the infill` | Xét khi Preview cho thấy vùng thiếu wall loops cần nối liền với infill; giữ preset nếu không có vấn đề đó. | Mối nối thành–infill ở mặt cắt, không phát sinh bề mặt lồi hoặc chiếm khe. |
| `Top/Bottom surface pattern` | Chọn theo bề mặt cần đẹp hoặc tiếp xúc; đổi pattern chỉ khi Preview cho thấy đường chạy phù hợp, không dùng để giải quyết thiếu lớp đặc. | Đường mặt trên/dưới, vùng quanh lỗ và mặt ghép. |
| `Top shell layers` và `Top shell thickness` | Chọn cùng nhau theo **độ dày đặc hiệu lực** của mặt trên ở layer đang dùng; khi đổi layer phải tính/kiểm tra lại. | Số lớp đặc và độ dày thực ở mặt trên, vùng trên infill và trụ. |
| `Bottom shell layers` và `Bottom shell thickness` | Tương tự cho đáy. Giá trị thickness `0` trong UI không có nghĩa đáy không có lớp đặc khi `Bottom shell layers` vẫn lớn hơn 0. | Số lớp đặc và độ dày đáy thực trong Preview/G-code, nhất là dưới PCB và chân vít. |
| `Top/Bottom paint penetration layers` | Chỉ chỉnh khi tô màu bề mặt nhiều màu và cần kiểm soát màu xuyên xuống bao nhiêu lớp; với part một màu không tối ưu bằng mục này. | Màu ở mặt cắt/lớp và thời gian, vật liệu đổi màu. |
| `Internal solid infill pattern` | Đổi khi đường đặc bên trong ảnh hưởng bề mặt/độ bền hoặc thời gian; giữ preset khi không có vấn đề quan sát được. | Đường in đặc quanh đáy, trụ và vùng chuyển tiếp. |
| `Sparse infill density` | Chọn theo tải của vùng rỗng; với vỏ điện tử, kiểm tra wall loops, đáy, nắp và trụ riêng trước khi tăng phần trăm infill. | Pattern, mức đỡ lớp trên, vật liệu/thời gian; thử cơ học khi cần. |
| `Fill multiline` | Chỉ đổi khi cần thay cách tạo nhiều đường infill và có bằng chứng Preview/thử in; không dùng làm nút tăng độ bền mặc định. | Đường infill hiệu lực, chỗ giao với thành và thời gian. |
| `Sparse infill pattern` | Giữ pattern của preset nếu không thấy vấn đề; thử pattern khác khi cần đổi đường chịu lực, thời gian hoặc tránh đường giao gây cọ nozzle trên bản in thử. | Đường giao, liên kết với thành, lớp trên và vật liệu. |

Chi tiết về layer, infill và nhiệt độ nằm trong [process-settings.md](process-settings.md). Không kết luận kín nước chỉ từ nhiều wall loops hoặc nhiều infill; phải thử trên vỏ thật.

## Support

| Mục | Khi nào giữ hoặc chỉnh | Kiểm tra sau slice |
| --- | --- | --- |
| `Enable support` | Tắt khi vùng nhô/cầu không cần đỡ theo Preview và mẫu thử; bật khi có vùng thiếu đỡ hoặc cảnh báo cần xử lý. | Vùng dưới overhang/cầu, cảnh báo và chỗ support tiếp xúc. |
| `Type` | So `tree(auto)`, `normal(auto)` và manual trên cùng model/profile theo [support-selection.md](support-selection.md). | Phạm vi đỡ, khả năng tháo, khối lượng support và thời gian. |
| `Threshold angle` | Giữ preset làm mốc; chỉ đổi để điều chỉnh vùng phát sinh support sau khi nhìn thấy overhang cụ thể. Không áp góc chung cho mọi hình học/vật liệu. | Vùng nào mới được đỡ hoặc bị bỏ đỡ; không kết luận từ con số góc riêng lẻ. |
| `On build plate only` | Chỉ bật nếu mọi support cần thiết có thể bắt đầu từ plate; khoang có support mọc từ đáy bên trong model cần kiểm tra đặc biệt. | Mặt dưới vẫn được đỡ và không còn cảnh báo do mất support. |
| `Support/raft base` và `Support/raft interface` | Giữ `Default` nếu dùng cùng vật liệu. Chỉ chọn vật liệu support riêng khi thật sự có cuộn/AMS phù hợp, profile tương thích và mục tiêu tháo/mặt dưới rõ ràng. | Vật liệu hiệu lực, vùng interface, đổi vật liệu, prime/purge và khả năng tháo. |

## Others

| Mục | Khi nào giữ hoặc chỉnh | Kiểm tra sau slice |
| --- | --- | --- |
| `Skirt loops` và `Skirt height` | Skirt tạo đường quanh vật để quan sát dòng nhựa/ổn định trước khi vào chi tiết; `0` tắt skirt. Không dùng skirt thay brim để giữ chân nhỏ. | Skirt có xuất hiện, chiếm chỗ plate và có chồng brim/part khác không. |
| `Brim type` và `Brim width` | Bắt đầu `Auto`; khi footprint nhỏ hoặc chân/tai dễ bong, thử brim ngoài/ở vùng rủi ro theo [plate-layout.md](plate-layout.md). Không lấy `5 mm` trên ảnh làm ngưỡng chung. | Brim thật ở lớp đầu, khoảng trống tới mép/part khác, khả năng tháo khỏi mặt chức năng. |
| `Prime tower: Enable`, `Width`, `Rib wall` | Chỉ đánh giá khi có đổi filament/màu/vật liệu hoặc chức năng khác thực sự làm tower xuất hiện. Bật trong UI ở bản một màu **không chứng minh** tower được in. Khi tower có thật, giữ kích thước/rib preset trừ khi có vấn đề về ổn định hoặc khoảng trống plate. | Có tower trong Preview/G-code không; diện tích, ổn định và va chạm với brim/support/part. |
| `Purge into objects' infill/support` | Chỉ có ý nghĩa khi đổi filament và có prime tower. Dùng để giảm nhựa xả khi vật liệu/màu tương thích; tránh xả vào vùng có thể lộ màu, infill dưới mặt mỏng, support cần gỡ sạch hoặc vật liệu không tương thích. | Đường purge thực, màu/vật liệu trong infill/support, thời gian và vật liệu. |
| `Print sequence` | Giữ `By layer` làm mốc. Chỉ thử `By object` khi có nhiều part và Bambu Studio xác nhận khoảng hở đầu in/chiều cao theo [plate-layout.md](plate-layout.md). | Vùng clearance, thứ tự in, brim/support/tower và nguy cơ va chạm. |
| `Spiral vase` | Chỉ cho vật đơn vỏ liên tục, không cần nắp, trụ, đáy nhiều lớp, infill hoặc support; không dùng cho hộp điện tử lắp vít/ron. | Đường vỏ liên tục và các feature chức năng còn hay đã mất. |
| `Timelapse` | Chọn theo nhu cầu ghi hình; không dùng làm cách sửa lỗi in. Một số chế độ có thể yêu cầu tower hoặc thay chuyển động, nên xem Preview và thời gian nếu bật. | Tower/chuyển động bổ sung, thời gian và khoảng trống trên plate. |
| `Fuzzy Skin` | Chỉ bật cho mặt trang trí có chủ ý; tắt ở mặt ghép, đường ron, lỗ, ren và bề mặt cần đo kích thước. | Phạm vi mặt nhám trong Preview và khoảng hở lắp. |
| `Fuzzy skin generator mode`, `noise type`, `point distance`, `thickness`, `first layer` | Chỉ chỉnh sau khi bật Fuzzy Skin và in mẫu bề mặt; khi Fuzzy Skin là `None`, các giá trị bên dưới không phải thông số hiệu lực của part. | Bề mặt được áp dụng, lớp đầu, kích thước bao và khả năng lắp. |

## Bản ghi tối thiểu

Ghi trong project: mục tiêu chức năng, preset gốc, các giá trị đã đổi, vùng bị ảnh hưởng, ảnh/mô tả Preview lớp đầu và vùng chức năng, cảnh báo, tổng vật liệu/thời gian, kết quả in thử và mục còn `Chưa xác minh`. Với nhiều màu/vật liệu, ghi thêm tower, đường purge và vật liệu support thực tế. Mọi giá trị trong ảnh chụp UI là **giá trị đang chọn**, chỉ trở thành cấu hình file in sau khi slice, lưu gói và kiểm tra lại G-code.
