
class Bank:
    def __init__(self,name,address,balance=0) -> None:
        self.name =name
        self.address = address
        self.accounts = {}
        self.admin = []
        self.total_balance = balance
        self.total_loan_amount = 0
        self.loan_feature = True

    def add_account(self,account):
        self.accounts[account.user_name] = account

    def add_admin(self,id):
        self.admin.append(id)
    

    def display_accounts(self):
        if self.accounts:
            for account in self.accounts:
                print(account)
        else:
            print('No account found')

    
class User:
    def __init__(self,name,password,balance=0) -> None:
        self.user_name = name
        self.password = password
        self.balance = balance
        self.transaction_history = []

    
    def deposit(self,amount):
        if amount > 0 :
            self.balance += amount
            bank.total_balance += amount
            self.transaction_history.append(Transaction(len(self.transaction_history)+ 1, amount,'Deposit'))
            print(f'{amount} deposit successfully')
        else:
            print('Invalid deposit amount')

    def withdraw(self,amount):
        if amount <= bank.total_balance:
            if amount <= self.balance:
                self.balance -= amount
                bank.total_balance -= amount
                self.transaction_history.append(Transaction(len(self.transaction_history)+ 1, amount,'Withdrawl'))
                print(f'withdrawl transaction done')
            else:
                print('Insufficient balance ')
        else:
            print('Cant withdrawl the money  !!! bank is bankrupt')
    def transfer(self,name,amount):
        if amount <= self.balance:
            self.balance -= amount
            bank.total_balance -= amount
            name.deposit(amount)
            self.transaction_history.append(Transaction(len(self.transaction_history)+ 1, amount,'Transfer'))
            print('Transaction Successsful')
        else:
            print('Insufficient balance')

    def take_loan(self,amount):
        if bank.loan_feature:
            if amount <= self.balance * 2:
                bank.total_loan_amount += amount
                self.balance += amount
                self.transaction_history.append(Transaction(len(self.transaction_history)+ 1, amount,'Loan taken'))
                print('Loan Approved')
            else:
                print('Invalid Load amount')
        else:
            print('Loan feature is currently off')
            


    def check_transaction_history(self):
        if self.transaction_history:
            for transection in self.transaction_history:
                print(transection,'\n')
        else:
            print('No Transaction History')
    def __repr__(self) -> str:
        return f' name : {self.user_name} number : {self.password} balance : {self.balance}'

    def check_balance(self):
        print(f'name : {self.user_name} balance : {self.balance}')



class Transaction:
    def __init__(self,id,amount,type) -> None:
        self.transaction_id = id
        self.amount = amount
        self.type = type   
    def __repr__(self) -> str:
        return f' transaction no : {self.transaction_id}    amount :  {self.amount}    type : {self.type}'



class Admin:
    def __init__(self,email,name) -> None:
        self.admin_id = email
        self.name = name

    def check_total_balance(self):
        total_balance = bank.total_balance
        print(f'Total available balance of the bank bank: {total_balance}')

   
    def check_total_loan(self):
        total_loan = bank.total_loan_amount
        print(f'Total available balance of the bank bank: {total_loan}')
    
    def change_loan_feature(self):
        if bank.loan_feature:
            bank.loan_feature = False
            print('Loan Feature is off now')
        else:
            bank.loan_feature = True

    def tk_mere_dilam(self):
        bank.total_balance = 0
# check...
bank = Bank('My_bank','Motijhil')

user_1 = User('sdm',123,1000)
bank.add_account(user_1)
user_1.deposit(15000)

# bank.display_accounts()

account_name = "sdm"
account_details = bank.accounts.get(account_name)
account_details.check_balance()
account_details.take_loan(20000)
user_2 = User('hsn',456,3000)
bank.add_account(user_2)



user_1.transfer(user_2,2000)

account_name = "sdm"
account_details = bank.accounts.get(account_name)
account_details.check_balance()
account_details.check_transaction_history()
account_name ="hsn"
account_details = bank.accounts.get(account_name)
account_details.check_balance()

admin = Admin('khan@ali.com','khan')
bank.add_admin(admin)
admin.check_total_balance()
admin.check_total_loan()
admin.tk_mere_dilam()
admin.check_total_balance()
user_1.withdraw(2000)