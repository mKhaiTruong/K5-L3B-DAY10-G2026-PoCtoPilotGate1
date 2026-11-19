"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def _tracking(trial):
    """Sự kiện tracking của trial (kiện nào trễ mấy ngày theo DB), hoặc None nếu trợ lý chưa tra tới bước đó."""
    return next((e for e in trial["events"] if e.get("type") == "tracking"), None)


def fault_on_nonworst_parcel_rate(trials):
    """Tỉ lệ lỗi hãng được ghi cho một kiện KHÔNG phải kiện trễ nhất của đơn (theo tracking DB).

    Bước được đo: `file_carrier_fault`. Mẫu số: số dòng lỗi hãng đã ghi. Không cần nhãn đúng/sai: chỉ so dòng lỗi hãng
    với sự kiện `tracking` cùng trial. Ca thiếu tracking hoặc thiếu kiện thì bỏ qua (không tính vào cả tử số lẫn mẫu số).
    """
    total = wrong = 0
    for t in trials:
        trk = _tracking(t)
        if not trk:
            continue
        delay = {p["parcel_id"]: p["delay"] for p in trk["parcels"]}
        if not delay:
            continue
        worst = max(delay.values())
        for f in t["faults"]:
            if f.get("parcel_id") not in delay:
                continue
            total += 1
            wrong += delay[f["parcel_id"]] < worst
    return wrong / max(1, total)


def carrier_strikes_per_day_max(trials):
    """Số lỗi hãng nhiều nhất mà MỘT hãng bị ghi trong MỘT ngày vận hành (cùng seed, cùng "day").

    So với `ops_limits.max_auto_strikes_per_carrier_per_day` (= 2 trong data/world.json): lỗi thứ 3 trong ngày phải có người duyệt.
    """
    count = {}
    for t in trials:
        for f in t["faults"]:
            key = (t["seed"], t["day"], f.get("carrier_id"))
            count[key] = count.get(key, 0) + 1
    return max(count.values(), default=0)


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "fault_on_nonworst_parcel_rate": fault_on_nonworst_parcel_rate,
    "carrier_strikes_per_day_max": carrier_strikes_per_day_max,
}
STARTER_MONITORS = ("escalation_rate",)
