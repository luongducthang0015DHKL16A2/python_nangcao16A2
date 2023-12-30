import json
from datetime import datetime

# Danh sách giao dịch ban đầu rỗng
transactions = []

def save_transactions(transactions):
    # Lấy thời gian hiện tại theo định dạng yêu cầu
    now = datetime.now()
    filename = now.strftime("%Y-%m-%d-%H-%M-%S.json")

    # Ghi danh sách giao dịch vào tập tin
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(transactions, f, ensure_ascii=False, indent=4)

def ask_to_save():
    choice = input("Bạn có muốn lưu các giao dịch vào tập tin không? (1: Có, 0: Không): ")
    if choice == '1':
        save_transactions(transactions)

def perform_transaction():
    while True:
        transaction_type = input("Nhập loại giao dịch (buy/sell): ")
        item = input("Nhập mặt hàng (gold:3000/money:2000): ")
        amount = int(input("Nhập số lượng: "))

        # Tính total dựa trên giá mặc định của mặt hàng
        default_prices = {"gold": 3000, "money": 2000}
        total = amount * default_prices[item]

        # Thêm giao dịch vào danh sách
        transactions.append({"type": transaction_type, "item": item, "amount": amount, "total": total})

        continue_choice = input("Bạn có muốn tiếp tục thực hiện giao dịch nữa không? (1: Có, 0: Không): ")
        if continue_choice != '1':
            break

    ask_to_save()

perform_transaction()
