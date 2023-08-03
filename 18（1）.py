from bitcoinlib.wallets import Wallet
from bitcoinlib.transactions import Transaction
def send_transaction(sender_address, sender_private_key, recipient_address, amount):
    sender_wallet = Wallet(private_key=sender_private_key)
    tx = Transaction()
    unspent_outputs = sender_wallet.unspent
    total_input_amount = 0

    for output in unspent_outputs:
        total_input_amount += output['value']
        tx.add_input(output['txid'], output['output_n'])
    tx.add_output(recipient_address, amount)
    change_amount = total_input_amount - amount
    if change_amount > 0:
        tx.add_output(sender_address, change_amount)

    tx.sign(sender_wallet)

    tx.send(testnet=True)

    return tx.txid


