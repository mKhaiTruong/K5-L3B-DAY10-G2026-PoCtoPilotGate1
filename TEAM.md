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
