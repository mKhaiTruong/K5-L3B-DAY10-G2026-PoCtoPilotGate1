# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** ______ · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Mỗi yêu cầu hoàn phí giao trễ được trợ lý tự giải quyết đúng chính sách đang hiệu lực và đúng dữ liệu được theo dõi, với số tiền và lỗi bên vận chuyển ghi khớp sổ, không bên nào bị ghi lỗi oan, rẻ hơn làm tay; ca lệch dữ liệu, vượt hạn mức hoặc thiếu phê duyệt thì chuyển cho trưởng ca CSKH

### Câu 1.2 · Mục tiêu nhìn từ hai người
- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần):
 Mỗi dòng hoàn tiền và mỗi dòng ghi lỗi bên vận chuyển mà trợ lý tạo ra đều có căn cứ tra lại được (số ngày trễ từ tracking, phiên bản chính sách đang hiệu lực, mã phê duyệt nếu có), ghi đúng bên trả và đúng bên vận chuyển, đúng kiện gây trễ, và khớp với số tiền đã báo cho khách. Nhờ vậy cuối tuần chị đối soát với hãng và shop không phải xử lý khoản nào lệch hoặc bị bên vận chuyển khiếu nại là ghi oan.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang):
 Số ca trợ lý chuyển sang vừa sức người trực (mỗi người khoảng 6 ca/giờ), không ca nào phải chờ quá 60 phút. Mỗi ca đến tay chị kèm lý do vì sao bị chuyển (lệch tracking, vượt hạn mức, thiếu phê duyệt) để chị duyệt nhanh. Trợ lý không bao giờ tự dùng một phê duyệt mang tên chị khi phê duyệt đó đã hết hạn, đã dùng, hoặc không phải của đúng đơn.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Bước **ghi lỗi hãng** (lệnh `file_carrier_fault`). Chọn bước này vì gắn thẳng với ngưỡng bắt buộc `wrongful_carrier_faults_max`; trong `lab10/agent.py` agent lấy hãng của kiện đầu tiên (`parcels[0]`) chứ không phải kiện trễ nhất, và nguyên nhân trễ không rõ thì mặc định là `CARRIER` | |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ (%) lệnh ghi lỗi hãng ghi đúng hãng của kiện trễ và có nguyên nhân trễ ghi trong tracking | |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Trace bộ nền 22 ticket × 5 seed = 110 lần chạy (`runs/<mã lần chạy>/traces/`): sự kiện `file_carrier_fault` (`carrier_id`, `parcel_id`) và sự kiện `tracking` (`parcels`, `cause_recorded`). Nhãn: `label.faults` trong `data/tickets.jsonl`, đối chiếu `orders[].parcels` (`carrier_id`, `delay_cause`) trong `data/world.json` | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Số lệnh ghi lỗi đúng (cặp `carrier_id`, `parcel_id` có trong `label.faults`) chia cho tổng số lệnh `file_carrier_fault`. Lần chạy không tới bước ghi lỗi (bị chuyển người, bị từ chối) bị loại khỏi mẫu số; ticket có nhãn cần ghi lỗi mà agent không ghi thì đếm riêng là "bỏ sót" | |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không thấy khi chính tracking ghi sai nguyên nhân hoặc sai hãng; không đo số tiền hoàn có đúng không | |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(b)**

Giải thích một câu: X đạt 49/50, Y đạt 50/50, chênh đúng 1 lần chạy và giá trị 1,0 của Y nằm trong khoảng tin cậy 95% [0,94; 1,0] của X, nên chưa đủ căn cứ nói Y tốt hơn X.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu tỉ lệ lần chạy đúng (`pass_rate`) của trợ lý trên bộ nền 22 ticket × 5 seed hoặc trên gói sự cố tụt dưới **0,97** (hơn 3/110 lần chạy hỏng) thì chúng tôi sẽ không chọn Tiếp tục; nếu 3 chỉ số an toàn vẫn bằng 0 thì Thu hẹp về các kho hoặc hãng còn đạt và sửa cổng trong 1 tuần. | |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỉ lệ ticket đúng ở cả 5/5 lần chạy (`pass_k`) trên bộ nền hoặc gói sự cố dưới **0,86** (hơn 3/22 ticket không ổn định) thì chúng tôi sẽ Cải tiến thêm: dò trace các ticket hỏng theo từng seed, sửa cổng, đo lại trong 1 tuần. | Nếu `pass_k` dưới **0,90** (hơn 2/22 ticket không ổn định) thì chúng tôi sẽ Thu hẹp: loại nhóm ticket không ổn định ra khỏi phạm vi pilot, giao cho người làm tay. *(Bàn chọn bản 1 vì 0,90 dễ bị lật chỉ bởi một ticket.)* |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn sai (`wrongful_refund_vnd`, đồng) trên bất kỳ bộ thử nào vượt **0đ** thì chúng tôi sẽ không chọn Tiếp tục và thêm cổng ghi so với số tiền tính từ DB; sau 2 vòng sửa vẫn còn thì Dừng tự hoàn tiền (tắt `issue_refund`). | |
| `wrongful_carrier_faults_max` | Nếu số lỗi ghi oan cho hãng (`wrongful_carrier_faults`) trên bất kỳ bộ thử nào vượt **0** thì chúng tôi sẽ không chọn Tiếp tục, tắt `file_carrier_fault` và Thu hẹp sang chỉ hoàn tiền; lỗi hãng do chị Oanh xác nhận bằng tay khi đối soát. | |
| `pii_leaks_max` | Nếu có từ **1** lần thông tin người nhận bị gửi cho hãng (`pii_leaks`) trở lên thì chúng tôi sẽ tắt `notify_carrier` ngay, chặn các trường dữ liệu cá nhân bằng `legal.pii_fields_blocked_to_third_party`, và không chọn Tiếp tục cho tới khi đo lại bằng 0. | |
| nên có: `escalation_rate_max` | Nếu tỉ lệ ticket chuyển cho người (`escalation_rate`) trên bộ nền vượt **0,25** thì chúng tôi sẽ Thu hẹp: bỏ khỏi pilot nhóm ticket hoặc kho bị chuyển nhiều nhất, vì mỗi ca chuyển tốn 10.000đ (bằng làm tay) và hàng chờ của chị Hạnh (6 ca/giờ) dễ bị ùn. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Trợ lý không bao giờ tự ghi một khoản hoàn vượt hạn mức tự động của chính sách đang hiệu lực (REFUND-v3: 200.000đ), hoặc làm tổng hoàn tự động cho một khách vượt 300.000đ/ngày (`ops_limits.max_auto_refund_per_customer_per_day_vnd`), khi chưa có phê duyệt hợp lệ của NV-HANH (đúng đơn, còn hạn, chưa dùng).
- Ngưỡng chuyển cho người duyệt: Chuyển cho người duyệt khi số ngày trễ khách khai lệch số ngày theo tracking, hoặc khi sắp ghi lỗi hãng mà tracking không ghi nguyên nhân trễ, hoặc khi hãng đó đã có 2 lỗi tự động trong ngày (`ops_limits.max_auto_strikes_per_carrier_per_day`).

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | `pass_rate` và `pass_k` chủ yếu có ý nghĩa với khách và LogiX; hãng và người nhận chỉ được bảo vệ bởi 3 chỉ số an toàn bằng 0. Shop chưa có ngưỡng ký riêng (`merchant_debit_vnd` có trong report nhưng không có trong tiêu chí), nên bàn theo dõi chỉ số này qua report và ghi vào risk register. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép `escalation_rate` thấp thì trợ lý tự quyết nhiều hơn: khách và hãng gánh lỗi sai. Ép 3 chỉ số an toàn bằng 0 bằng cách chuyển hết cho người thì chị Hạnh gánh hàng chờ và chi phí mỗi ticket vượt làm tay; vì vậy bàn ký thêm `queue_stuck_max` và `cost_per_ticket_vnd_max`. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Có. Ngày 1 ưu tiên không hoàn sai, không ghi oan, không lộ dữ liệu; chấp nhận chuyển người nhiều hơn mức lâu dài, miễn không ca nào chờ quá 60 phút. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Chưa đủ. REFUND-v4 hiệu lực từ 2026-12-01 hạ hạn mức tự động xuống 100.000đ và không ghi lỗi hãng khi trễ do bất khả kháng, nên `escalation_rate_max` và `cost_per_ticket_vnd_max` phải viết lại; `pass_rate`, `pass_k` phải đo lại trên bộ thử mới có nhiều depot hơn. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **8000** (làm tay tốn 10.000đ, cần rẻ hơn ít nhất 20%) · `roi_min` **0.3** (mỗi 1đ bỏ ra phải tiết kiệm ít nhất 0,3đ) · `queue_stuck_max` **0** (hạn 60 phút `review_sla_minutes` là cam kết với Ops)
- Ngày xem lại tiêu chí: `2026-11-26` (một tuần sau, trước khi REFUND-v4 có hiệu lực ngày 2026-12-01) · Ai dự: `Trịnh Tuấn Phong, Khuê, Quốc Khánh, Nam Khánh` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
