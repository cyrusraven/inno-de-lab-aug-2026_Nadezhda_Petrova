raw_transactions = ["SUCCESS:100", "SUCCESS:0", "SUCCESS:250", "FAILED:50",
                    "SUCCESS:-10", "ERROR:200"]
result = [int(i[len("SUCCESS:"):]) for i in raw_transactions
                    if i.startswith("SUCCESS:") and int(i[len("SUCCESS:"):]) > 0]
print(f'Очищенные транзакции: {result}')
