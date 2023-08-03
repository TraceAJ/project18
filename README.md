运行环境：

安装bitcoinlib库即可在pycharm中运行。

实现方式：

（1）导入需要的库，包括bitcoinlib.wallets用于创建钱包，以及bitcoinlib.transactions用于处理交易。

定义名为send_transaction的函数来发送交易。该函数接受发送者地址、发送者私钥、接收者地址和金额作为参数。

在函数内部使用发送者的私钥创建了发送者的钱包对象，创建了一个新的交易对象。

获取发送者地址上的未花费输出（UTXO）列表，并计算出总输入金额。然后，将这些未花费输出添加到交易的输入中。

添加交易的输出，包括接收者地址和金额。如果在发送交易后还有余额，将余额发送回发送者地址。

最后使用发送者的私钥对交易进行签名，并将其广播到比特币测试网络中。

（2）只需替换代码中的占位符（<sender_address>、<sender_private_key>、<recipient_address>、<amount_in_satoshis>）为实际值，就可以使用该函数发送交易了。

运行结果：

<img width="415" alt="image" src="https://github.com/TraceAJ/project18/assets/110471272/6237e486-06d9-4c11-a16a-a1d7c86b7cb4">
