# tax_calculator.py

# ======================
# 1. CẤU HÌNH GIẢM TRỪ
# ======================
DEDUCTION_SELF = 11_000_000
DEDUCTION_DEPENDENT = 4_400_000

# Biểu thuế lũy tiến (giới hạn, thuế suất)
TAX_BRACKETS = [
    (5_000_000, 0.05),
    (10_000_000, 0.10),
    (18_000_000, 0.15),
    (32_000_000, 0.20),
    (52_000_000, 0.25),
    (80_000_000, 0.30),
    (float("inf"), 0.35)
]

# ======================
# 2. HÀM TÍNH THUẾ
# ======================
def calculate_tax(taxable_income):
    if taxable_income <= 0:
        return 0

    tax = 0
    previous_limit = 0

    for limit, rate in TAX_BRACKETS:
        if taxable_income > limit:
            tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            tax += (taxable_income - previous_limit) * rate
            break

    return tax


# ======================
# 3. CHƯƠNG TRÌNH CHÍNH
# ======================
def main():
    print("=== PHẦN MỀM TÍNH THUẾ TNCN ===")

    name = input("Tên người lao động: ")
    year = input("Năm tính thuế: ")
    dependents = int(input("Số người phụ thuộc: "))

    income_by_month = {}

    print("\nNhập thu nhập từng tháng (VND):")
    for month in range(1, 13):
        value = input(f"Tháng {month}: ")
        income_by_month[month] = int(value) if value else 0

    print("\nKẾT QUẢ QUYẾT TOÁN THUẾ")
    print(f"Người lao động: {name} | Năm: {year} | Số NPT: {dependents}")
    print("-" * 60)
    print(f"{'Tháng':<10}{'Thu nhập':<20}{'Thuế TNCN'}")

    total_tax_paid = 0

    for month in range(1, 13):
        income = income_by_month.get(month, 0)

        taxable_income = (
            income
            - DEDUCTION_SELF
            - dependents * DEDUCTION_DEPENDENT
        )

        tax = calculate_tax(taxable_income)
        total_tax_paid += tax

        print(f"{month:<10}{income:<20,}{tax:,.0f}")

    print("-" * 60)
    print(f"Tổng thuế TNCN đã tạm nộp: {total_tax_paid:,.0f} VND")

    # Quyết toán năm (giả sử thuế thực tế = tổng thuế tháng)
    print(f"Thuế TNCN thực tế: {total_tax_paid:,.0f} VND")
    print("Tiền thuế nhận lại: 0 VND")


if __name__ == "__main__":
    main()
