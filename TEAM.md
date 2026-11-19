# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): G2026
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-G2026-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |    Trương Đặng Minh Khuê       | 2A202603785 | Kỹ sư cổng (viết cổng) |      ✅      |
|   2 |    Trịnh Tuấn Phong       | 2A202603781 | Sản phẩm và kinh doanh |             |
|   3 |       Triệu Quốc Khánh    | 2A202603749 | Kỹ sư cổng (đo + dò lỗi) |             |
|   4 |      Nguyễn Nam Khánh     | 2A202603871 | Vận hành và pháp lý |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## TrinhTuanPhong-2A202603781

### Phần việc phụ trách

Vai **Sản phẩm và kinh doanh**: tiêu chí chấp nhận, chi phí và quyết định Gate 1.

- Phiếu A: câu 1.1, 1.2, 1.3, 1.5, 1.6 (A4), A5. Điền và ký `config/acceptance_criteria.json` thay mặt bàn.
- Phiếu B: B3 (câu 2.3, bản đồ dữ liệu và drift), lăng kính Kinh doanh của pre-mortem B6, B7.4 (câu 2.9), B8 quyết định v1.
- `config/operating_gates.json`, chỉ mục `business`.
- Phiếu C (thẻ S6): C1 (câu 3.0), C5 câu 3.2, C6 (câu 3.4), C7 dòng `business` (câu 3.5), C9 (câu 3.7), C12 quyết định v2 và ba dòng bắt buộc, `submission/submission.json`.

### Đóng góp cụ thể

- Đặt ngưỡng đã ký: 5 ngưỡng bắt buộc, escalation ≤ 0,25, business_ops (≤ 8.000đ/ticket, ROI ≥ 0,3, 0 ca ùn) và `decision_rule` 4 dòng.
- Đặt cổng kinh doanh: `daily_refund_cap_vnd` 500.000, `cost_budget_per_ticket_vnd` 1.500, `pilot_scope` all, `roi_min` 0,3. Mỗi số có lý do lấy từ `ops_limits` và `ops_facts`.
- Quyết định v1 "Tiếp tục có điều kiện": mới đo bộ nền, chưa đo gói sự cố.
- Thẻ S6: vẽ fault tree trước và sau khi sửa, 4 nhánh ở 3 tầng. Chỉ ra nhánh còn hở: trần lỗi tính theo ngày, còn ngưỡng đình chỉ tính theo 7 ngày.
- Quyết định v2 "Tiếp tục": khớp đủ bốn vế của dòng "Tiếp tục" trong `decision_rule`.

### Bằng chứng

- Commit: `43c2b92` (Sign acceptance criteria), `4cec516` (cổng business), `35833aa`, `1dbe43a` (B6, B7.4), `7adb34d` (B8 v1), `1878ae6` (Phiếu C). PR #5, #8, #12, #18, #22.
- Mã lần chạy: v1 `R-base-prepared-20261119-173345-1b1054`. v2 `R-S6-after-20261119-205547-ce8bfe`, grade `R-S6-grade-20261119-205546-ce8bfe`.
- Dòng trong phiếu: Phiếu B mục B8. Phiếu C mục C1, C6, C7 dòng [3], C9, C12.

### Có dùng AI không

Có. Mình dùng Claude Code (Anthropic) để đọc tài liệu lab, chạy lệnh (`lab10.eval`, `lab10.gate`, `lab10.trace`, `lab10.grade`, `lab10.check_submission`), soạn nháp các mục phiếu ở trên từ số liệu trong report và trace, và làm thao tác git (branch, commit, push). Mình tự chọn các ngưỡng, các con số trong mục `business` và quyết định v1, v2. Mình đọc và sửa lại mọi bản nháp trước khi mở PR. Mọi PR đều được bạn khác trong bàn review.

### Exit ticket

- Học được: phải ký tiêu chí trước khi đo, và quyết định phải khớp đúng dòng đã ký. v1 chỉ đo bộ nền nên chưa đủ để chọn "Tiếp tục", phải ghi rõ là có điều kiện.
- Còn chưa chắc: bộ thử chỉ có "ngày" giả lập, nên chưa biết trần 2 lỗi/hãng/ngày có giữ được hãng nhỏ khỏi ngưỡng đình chỉ 3 lỗi/7 ngày khi chạy thật hay không.

## NguyenNamKhanh-2A202603871

### Phần việc phụ trách

Vận hành và pháp lý. Vòng 1 phụ trách Phiếu B mục B4–B5 (2.4), phần pháp lý ở B6 (2.5), và B7.5–B7.6 (2.10). Vòng 2 phụ trách Phiếu C mục C3.2–C4 (3.1), C5 câu 3.3, các dòng vận hành và pháp lý ở C7 (3.5), C10–C11 (3.7).

### Đóng góp cụ thể

- Phân tích rủi ro của thao tác hoàn tiền, điền checklist sẵn sàng và bổ sung hai tình huống pháp lý. Đặt người phụ trách, giới hạn chờ duyệt và quy tắc chia sẻ dữ liệu trong `config/operating_gates.json`. Viết runbook phần 1–3 và dùng hai lần chạy cùng bộ nền để so chi phí, ROI và hàng chờ khi có một hoặc hai người duyệt.
- Với S6, đối chiếu trace ghi lỗi hãng với tracking từng kiện và nêu giả định khách luôn xác định đúng kiện. Bật ghi chú quyết định và kiểm mẫu 10%, giữ các cổng pháp lý đã có, ghi rủi ro lỗi hãng tích lũy trong 7 ngày và cập nhật checklist cùng runbook phần 4–5.

### Bằng chứng

- Phiếu B: PR #4 (B4–B5 và cài đặt vận hành/pháp lý), PR #14 (hai dòng pháp lý ở B6), PR #19 (B7.5–B7.6). Hai lượt so nhân sự: `R-base-after-20261119-174002-65a8a4` và `R-base-after-20261119-174003-3f05f4`.
- Phiếu C: PR #21 (C3.2, C4, C5 câu 3.3), PR #25 (C7, C10, C11), đối chiếu mốc after chính thức ở C0: `R-S6-after-20261119-205547-ce8bfe`.

### Sử dụng AI

Có dùng ChatGPT/Codex để đọc tài liệu và trace, hỗ trợ soạn và soát Phiếu B/C, chuẩn bị thay đổi cấu hình và chạy kiểm tra. Có dùng AI để soạn nháp mục đóng góp này từ các PR và báo cáo đã có.

### Exit ticket

- Một điều học được: Có những tình huống nghe như khó có thể xảy ra, nhưng mô hình vẫn có thể gặp phải.
- Một điều còn chưa chắc: Liệu các biện pháp nhóm đã làm có bao quát hết các tình huống có thể xảy ra hay chưa?

## TruongDangMinhKhue-2A202603785

### Phần việc phụ trách

Vai **Kỹ sư cổng 1 (viết cổng)**, trưởng nhóm: code cổng trong `lab10/guards.py`, chạy các lệnh chốt mốc, điều phối và review PR.

- Phiếu A: chia vai CP1, Phiếu A CP2 (PR #1, #2).
- Phiếu B: B6 lăng kính Con người và vận hành, B7.1 (câu 2.6, ba cổng vòng 1); lệnh 5 chốt cổng vòng 1 và lần chạy prepared.
- `lab10/guards.py`: ba cổng vòng 1 và hai nhánh vòng 2 cho thẻ S6.
- Phiếu C (thẻ S6): C0 (nhận thẻ, mốc prepared, mốc after cuối), C7 dòng code (câu 3.5).
- Điều phối: viết issue phân việc CP3, CP4, CP5 (#7, #17, #23), review và merge PR, gỡ conflict khi ghép nhánh, chạy lệnh 7 và đẩy bài.

### Đóng góp cụ thể

- Vòng 1: Cổng 1 giới hạn tiền hoàn theo quyền lợi tính từ tracking; Cổng 2 chỉ ghi lỗi đúng kiện, đúng hãng, đúng số ngày tracking; Cổng 3 bỏ chữ khách gõ khỏi thông báo gửi hãng. Chốt bằng lệnh 5 (prepared `2d59c8c3`).
- Vòng 2 (thẻ S6): nhánh `ambiguous_parcel` trong `_gate_refund` (ticket không nêu kiện mà có từ 2 kiện trễ thì chuyển người trước lệnh ghi đầu tiên) và nhánh `carrier_strike_cap` trong `_gate_carrier_fault` (từ lỗi tự động thứ 3 của một hãng trong ngày phải có người duyệt, theo `ops_limits`).
- Kết quả trên S6: lỗi ghi oan cho hãng 40 → 20 → 0, hoàn sai 270.000đ → 0đ, bộ nền không có ca mới hỏng.

### Bằng chứng

- Commit: `b4ba27a` (câu 2.6), `b75edb3` (B6), `6e5b4da` (chốt vòng 1), `731e208` (nhận thẻ S6), `f87274e` (câu 3.5), `27b97f7` (giữ byte bản chốt khớp `round1.lock`), `47537b4` (C0 mốc after). PR #1, #2, #15, #16, #20, #26.
- Mã lần chạy: prepared `R-S6-prepared-20261119-174403-65a8a4`; mốc chính thức base `R-S6-before-20261119-205547-ce8bfe`, prepared `R-S6-prepared-20261119-205547-ce8bfe`, after `R-S6-after-20261119-205547-ce8bfe`, grade `R-S6-grade-20261119-205546-ce8bfe` (PASS-VISIBLE).
- Dòng trong phiếu: Phiếu B mục B6, B7.1. Phiếu C mục C0, C7.

### Có dùng AI không

Có. Tôi dùng Claude Code (Anthropic) để đọc tài liệu lab, kiểm tra trạng thái và khả năng merge của PR, gỡ conflict khi ghép nhánh, soạn nháp issue phân việc và mục C0 từ report, và thao tác git, GitHub (branch, commit, push, mở PR, comment). Tôi tự quyết định cách sửa cổng, duyệt mọi thay đổi trước khi merge và tự chạy các lệnh `lab10`.

### Exit ticket

- Học được: cổng nằm ngoài model chỉ đáng tin khi mỗi lần sửa có số đo lại trên cả gói sự cố lẫn bộ nền; sửa mà không chạy lại thì không biết mình vừa làm hỏng ca nào.
- Còn chưa chắc: trần lỗi theo ngày có thật sự bảo vệ hãng nhỏ trước ngưỡng đình chỉ theo 7 ngày khi chạy thật hay không, vì bộ thử không có lịch sử nhiều ngày.

## TrieuQuocKhanh-2A202603749

### Phần việc phụ trách

Vai **Kỹ sư cổng 2 (đo và dò lỗi)**: chạy đánh giá, trace lỗi và viết chỉ số theo dõi trong `lab10/monitors.py`.

- Phiếu B: B0, B1 (câu 2.1, lần chạy baseline), B2 (câu 2.2, trace `T-002@55`), B6 lăng kính Kỹ thuật, B7.2, B7.3 (câu 2.7, 2.8).
- `lab10/monitors.py`: hai chỉ số mới cho thẻ S6.
- Phiếu C (thẻ S6): C2 (câu 3.1, bảng soát lỗi), C8 (câu 3.6), tên monitor ở bảng C9.

### Đóng góp cụ thể

- Lần chạy baseline và bảng soát lỗi `T-002@55` làm đầu vào cho cổng vòng 1.
- Hai bước tránh rò rỉ dữ liệu và behavioral test bằng `--adhoc` với ticket hiểm (B7.2, B7.3).
- Trace thẻ S6 theo hai kiểu hỏng khác nhau: `S6-01` (ghi lỗi cho kiện không trễ), `S6-20` (nhiều kiện cùng trễ, không nêu kiện), `S6-40` … `S6-43` (dồn lỗi về một hãng trong ngày).
- Hai monitor: `fault_on_nonworst_parcel_rate` (base 0,0 · S6 trước khi sửa 0,4167 · sau 0,0) và `carrier_strikes_per_day_max` (1 · 4 · 2), giúp ô `6 monitor` của `grade` đạt.

### Bằng chứng

- Commit: `6c0768c`, `270c8a1` (B0, B1), `3948e96` (B2), `1f48e3b` (B7.2, B7.3), `55d41dd` (B6), `25b4748` (monitor, C2, C8, C9). PR #3, #10, #11, #13, #24.
- Mã lần chạy: baseline `R-base-before-20261119-162853-bde05c`; monitor trong grade `R-S6-grade-20261119-205546-ce8bfe`.
- Dòng trong phiếu: Phiếu B mục B0, B1, B2, B6, B7.2, B7.3. Phiếu C mục C2, C8, C9.

### Có dùng AI không

_(Khánh tự điền: có dùng AI cho phần nào không.)_

### Exit ticket

_(Khánh tự điền: một điều học được, một điều còn chưa chắc.)_
