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
|   1 |    Khuê       |      | Kỹ sư cổng (viết cổng) |      ✅      |
|   2 |    Trịnh Tuấn Phong       | 2A202603781 | Sản phẩm và kinh doanh |             |
|   3 |       Triệu Quốc Khánh    | 2A202603749 | Kỹ sư cổng (đo + dò lỗi) |             |
|   4 | Nguyễn Nam Khánh | 2A202603871 | Vận hành và pháp lý |             |

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
