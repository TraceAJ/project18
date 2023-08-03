
sender_address = "<sender_address>"
sender_private_key = "<sender_private_key>"
recipient_address = "<recipient_address>"
amount = <amount_in_satoshis>  # e.g., 0.001 BTC = 100000 satoshis

transaction_id = send_transaction(sender_address, sender_private_key, recipient_address, amount)
print("Transaction sent! Transaction ID:", transaction_id)
