# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Related Workspaces

| Workspace | Path / URL |
| --------- | ---------- |
| **Fusion** (Autodesk Fusion, CAD tham số) | Fusion cloud project + `projects/<id>/design/` |
| **Bambu Studio** (slicer, máy P2S Full Combo mặc định) | Bambu Studio + `projects/<id>/print/` |
| **MeshRight** (kiểm mesh read-only) | CLI ngoài, gọi qua `scripts/printing/check_mesh.py` |

Khi cần kiểm tra hình học tham số → đọc script trong `scripts/fusion/<module>/` và F3D trong `projects/<id>/design/`. Khi cần kiểm tra profile/G-code → đọc `projects/<id>/notes/results.md` và preset đã resolve trong `runs/`. Khi cần số đo linh kiện → đọc `library/components/<id>/component.json`, không đo lại từ ảnh.

**KHÔNG sửa trực tiếp file nhị phân `.f3d`.** Mọi thay đổi hình học đi qua Fusion API script trong `scripts/fusion/`. **KHÔNG gửi lệnh in từ script.** Script chỉ dựng, xuất và kiểm tra; người dùng xác nhận trước khi in.

### Notes trước, model sau

Tham số và kiểm tra nằm ở `projects/<id>/notes/` (`params.md`, `checks.md`, `results.md`, `HISTORY.md`). **Trước khi đổi hình học, lỗ, ron, vị trí PCB hoặc lỗ xuyên vỏ: đọc notes đối chiếu với model, cập nhật notes TRƯỚC.** Khi notes và model lệch nhau thì model là bên sai, không phải notes. Không coi mesh xuất được là bằng chứng lắp vừa hay in đạt.

**Quy ước version — bám lượt sử dụng, không bám số lần chạy:**

- Version project dạng `vMAJOR.MINOR.PATCH`, project mới bắt đầu ở `v1.0.0` kể cả khi còn nguyên mẫu.
- Mọi lần chỉnh trong cùng một đợt làm việc giữ nguyên số version. Git commit, Fusion timeline và bản ghi kiểm tra phân biệt các lần sửa nội bộ.
- Trạng thái nguyên mẫu / thử in / đã chốt nằm trong `notes/checks.md`, không suy ra từ số version, không thêm hậu tố `-beta`/`-dev` vào tên file CAD.

**Cạm bẫy — chỉ nổ ở khâu slice/in, không phải lúc xuất mesh.** Mesh kín, không biên, đúng mm không chứng minh in được hay kín nước. Tên preset trong UI không chứng minh G-code đã nhận đủ thông số (ví dụ sai do chưa giải kế thừa `inherits`). **Đối chiếu metadata G-code TRƯỚC khi đưa file vào `print/sliced/`.**

---

## Workspace: FusionDesign (this repo)

Quy trình thống nhất từ thiết kế tham số trong Fusion đến chuẩn bị in trong Bambu Studio. Máy in mặc định mọi project là **Bambu Lab P2S Full Combo**; vật liệu, nozzle, bàn in và profile xác nhận theo từng lần in. Mọi kích thước dùng mm và ghi rõ đơn vị.

### Script Fusion: `scripts/fusion/<module>/`

Mỗi project có một module script trong `scripts/fusion/<module>/` (tên module dùng gạch dưới vì identifier Python không dùng dấu gạch nối; ID project dùng gạch nối). Chi tiết script, tham số dựng và lịch sử của từng project nằm trong `projects/<id>/notes/` và `scripts/fusion/README.md`, không nằm ở file này.

```powershell
# Chạy trong Fusion: Utilities > Scripts and Add-Ins > chọn <module> > Run
# Kiểm mesh sau khi xuất:
py -3 scripts/printing/check_mesh.py --meshright path/to/meshright.exe --output projects/<id>/runs/<yyyymmdd>-mesh-check/mesh-check.json path/to/body.3mf path/to/lid.3mf
# Resolve preset Bambu (không slice, không in):
py -3 scripts/printing/prepare_presets.py
```

**Quy tắc chạy:**

- Script tạo document mới từ đầu, không sửa document đang mở, không ghi đè F3D đã có; trùng tên file xuất thì dừng.
- Xuất F3D local vào `design/`, mesh trung gian vào `runs/<yyyymmdd>-<mục-đích>/mesh/`; sau khi gói slice xong thì xóa mesh trung gian, xuất lại từ Fusion khi cần.
- Document mới còn `Unsaved` trong Fusion; lưu vào Fusion cloud project nếu cần lịch sử cloud, ghi tên document + `isSaved = True` vào `notes/HISTORY.md`.
- Mọi giá trị cần giữ (tham số, tọa độ, file xuất, lỗi, kết quả kiểm tra) phải chép sang `notes/results.md`; không lấy log tạm trong `runs/` làm nguồn lâu dài.

### Script in: `prepare_presets.py` + `check_mesh.py`

- `prepare_presets.py` giải kế thừa profile máy + filament + process đang chọn, ghi JSON tạm vào run dir (`FUSIONDESIGN_RUN_DIR` hoặc `projects/<id>/runs/<yyyymmdd>-preset-check/presets/`). Đổi nguồn profile qua `BAMBU_STUDIO_PROFILE_ROOT`.
- Bambu CLI luôn đặt `--outputdir` vào `runs/<yyyymmdd>-<mục-đích>/` có tên rõ. Copy giá trị hiệu lực, warning và tên file nguồn vào `notes/results.md` rồi mới dọn run.
- `check_mesh.py` chỉ đọc (`check --json`): watertight, mảnh rời, kích thước, lỗi hình học. Cố ý bỏ qua score và khối lượng vật liệu đặc của MeshRight vì không chứng minh in được. Không sửa mesh.
- Không script nào trong thư mục này slice hộ hay gửi lệnh in. MeshRight là tool ngoài, gọi CLI, không copy source vào repo.

### Project Structure

```
FusionDesign/
├── CLAUDE.md              # File này: quy ước chung, không chứa chi tiết project nào
├── README.md              # Giới thiệu quy trình và link vào các project
├── docs/rules/            # Rule chung: printability, material, process-settings,
│                          # plate-layout, outdoor-enclosure, model-source,
│                          # component-library, versioning
├── library/components/<id>/component.json  # Linh kiện dùng chung dạng text
├── projects/<id>/
│   ├── README.md          # Bản dẫn hướng + trạng thái in của project
│   ├── design/            # Một F3D mới nhất làm bản dự phòng mang đi được
│   ├── print/prepare/     # 3MF mesh chưa G-code, để mở/chỉnh trong Studio
│   ├── print/sliced/      # Chỉ gói Bambu đã slice + kiểm G-code đúng máy/vật liệu
│   ├── notes/             # params.md, checks.md, results.md, HISTORY.md
│   ├── references/        # Ảnh/bản vẽ gốc để truy vết nguồn số đo
│   └── runs/              # File tạm, Git bỏ qua (mesh, preset, log, ảnh chụp)
└── scripts/fusion/ + scripts/printing/
```

### Thư viện linh kiện — text là nguồn, ảnh chỉ để truy vết

- Mỗi linh kiện một thư mục `library/components/<id>/component.json` với `id`, `name`, `part_number`, `source`, `dimensions`, `notes`. Đơn vị nằm trong tên trường (`front_width_mm`); không ghi số thiếu đơn vị.
- Mỗi giá trị có `status`: `confirmed` (đo trên linh kiện thật), `drawing` (đọc từ bản vẽ), `estimate` (giả định), `pending` + `value: null` (chưa có số). Ghi dung sai khi bản vẽ có nêu.
- Cùng chức năng nhưng khác hãng/mã/revision thì tạo mục mới, không sửa ngầm thông số mục cũ. Kích thước riêng của sản phẩm (PCB, tọa độ lỗ, kích thước vỏ, vị trí lắp) nằm trong `projects/<id>/`, không đưa vào thư viện chung.
- Ảnh/PDF gốc lưu ở `projects/<id>/references/` để truy vết; `component.json` trỏ về qua `project_archive`. Không suy đường kính lỗ vỏ từ đường kính chi tiết khi bản vẽ không chỉ định lỗ khoét.

### Rule áp dụng theo thứ tự

1. `docs/rules/printability.md` (PRT-001–PRT-009) và `docs/rules/support-selection.md`: kiểm tra trước thiết kế, trong Fusion, trước in; chọn support qua Preview của Bambu Studio.
2. `docs/rules/material.md` (MAT-001–MAT-006): chọn vật liệu, khớp preset máy + nozzle + vật liệu, chạy lại khi đổi cấu hình.
3. `docs/rules/process-settings.md`: nhiệt, layer theo nozzle, wall/top/bottom, infill; ghi mọi lệch preset.
   `docs/rules/bambu-studio-controls.md`: bảng quyết định cho từng mục Quality, Strength, Support và Others trong Bambu Studio.
4. `docs/rules/outdoor-enclosure.md`: hộp điện tử ngoài trời — ron liên tục, vít ngoài đường ron, mỗi lỗ xuyên vỏ có cách kín riêng, thử nước trên vỏ không cấp điện, không công bố IP khi chưa thử đúng phương pháp.
5. `docs/rules/plate-layout.md`: nhiều part thì đánh giá cả chung và tách plate; khoảng cách đo sau brim/support/skirt/wipe tower, không dùng bbox mesh trần làm khoảng an toàn.
6. `docs/rules/model-source.md`: tự dựng tham số hay nhập model ngoài/AI; kích thước chức năng phải đo lại.
7. `docs/rules/component-library.md` + `docs/rules/versioning.md`: thêm linh kiện, đặt tên file, giữ một F3D mới nhất, dọn mesh trung gian, đóng tab Fusion đúng project.

### Quy trình bắt buộc (tóm tắt, chi tiết ở các rule)

1. Nhận kích thước, mục đích, vật liệu/màu, nozzle/profile; mặc định P2S Full Combo. Chạy kiểm tra đầu vào trước khi dựng.
2. Validate kích thước: tất cả dương, đơn vị mm; với hộp kiểm thêm quan hệ thành/đáy với kích thước ngoài và giao/va giữa các feature (tai, trụ, lỗ, rãnh ron) với thành, nắp, PCB và vùng kín nước.
3. Dựng/sửa trong Fusion theo hồ sơ project; tạo điểm khôi phục và hiện diff để người dùng xác nhận trước khi sửa bản hiện có.
4. Kiểm tra hình học sau mỗi thay đổi liên quan và trước khi xuất; chạy lại rule bị ảnh hưởng.
5. Xuất 3MF đơn vị mm; kiểm tra đơn vị, kích thước, hướng đặt, số part. Định dạng khác phải ghi lý do.
6. Slice rồi xem preview: support, lớp đầu, thành mỏng, lỗ, rãnh. Số liệu thời gian/vật liệu chỉ chính thức sau slice thành công.
7. Người dùng xác nhận trước khi in. Ghi tham số, cấu hình in, cảnh báo và kết quả in vào notes.

### Ranh giới trách nhiệm

- Fusion giữ model tham số, là nguồn thiết kế chính. Bộ phân tích in ghi rõ vấn đề + vị trí + nguyên nhân + đề xuất, phân biệt đo được với ước lượng.
- Bambu Studio quyết định profile thực tế, preview, slice và dữ liệu máy in. Slice thành công không đóng cảnh báo cơ khí/kín nước.
- Ngưỡng chưa có nguồn + điều kiện áp dụng rõ ràng thì giữ `Chưa xác minh`, không dùng để chặn thiết kế; đóng cảnh báo chỉ khi đã sửa, đã kiểm chứng, hoặc người dùng chấp nhận rủi ro có ghi phiên bản + cấu hình.
