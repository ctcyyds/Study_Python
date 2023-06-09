class Bank:
    def __init__(self, number, blance):
        self.__blance = blance
        self.number = number

    def __str__(self):
        return f"账户名：{self.number} 余额：{self.__blance}"

    def add(self, amount):
        """
        存钱
        :param amount:存入的金额
        :return:
        """
        self.__blance += amount
        return +amount

    def dell(self, amount):
        """
        提现
        :param amount:要取出的金额
        :return:
        """
        # 判断余额够不够取钱
        if self.__blance >= amount:
            self.__blance -= amount
            return -amount
        else:
            print("余额不足")
            return -amount


bank = Bank("VIP", 100)
print(bank)
print(bank.add(1000))
print(bank)
print(bank.dell(500))
print(bank)
print(bank.dell(800))
print(bank)
