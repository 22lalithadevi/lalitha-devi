class bank:
    def bankroi(self):
        return 10;
class sbi(bank):
    def bankroi(self):
        return 9;
class rbi(bank):
    def bankroi(self):
        return 8;
b1=bank()
print(b1.bankroi())
b2=sbi()
print(b2.bankroi())
b3=rbi()
print(b3.bankroi())
