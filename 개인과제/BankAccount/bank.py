class Account:
    def __init__(self,user_id,user_name,user_balance,user_pw):
        self.__user_id = user_id
        self.__user_name = user_name
        self.__user_balance = user_balance
        self.__user_pw = user_pw
    def get_UserId(self):                                      
        return self.__user_id
    
    def get_UserName(self):
        return self.__user_name
    
    def get_UserBalance(self):
        return self.__user_balance
    
    def get_UserPassWord(self):
        return self.__user_pw
    
    
    def deposit(self,money):     
        print(money,'원이 입금되었습니다.')
        self.__user_balance += money 
        print("잔액:",self.__user_balance)

    def withdraw(self,money):
        if self.__user_balance < money:
            print("돈이 부족합니다.")
        else:
            print(money,"원이 출금되었습니다.")
            self.__user_balance -= money
            print("잔액:",self.__user_balance)

  
class Bank:
    def __init__(self):
        self.accountlist = []
        
    def create_account(self): 
        user_id = input("계좌번호: ")
        user_name = input("이름: ")
        user_balance =int(input("예금: "))
        user_pw = input("비밀번호 : ")
        print('##계좌개설을 완료하였습니다##')

        self.accountlist.append(Account(user_id,user_name,user_balance,user_pw))
      
    def deposit(self):
        user_id = input("입금할 계좌번호를 입력해주세요: ")
        for i in range(len(self.accountlist)):
            if self.accountlist[i].get_UserId() == user_id:
                self.accountlist[i].deposit(int(input("입금할 금액을 입력해주세요: ")))
                break
            else:
                print("계좌를 찾을수 없습니다.")
                
    def withdraw(self): 
        user_id = input("출금할 계좌번호를 입력해주세요: \n")
        user_pw = input("출금할 계좌의 비밀번호를 입력해주세요: \n")

        for i in range(len(self.accountlist)):
            if self.accountlist[i].get_UserPassWord() == user_pw:
              if self.accountlist[i].get_UserId() == user_id:
                self.accountlist[i].withdraw(int(input("출금하실 금액을 입력해주세요: ")))
                break
            else:
                print("비밀번호가 맞지 않습니다.")
                
    def show_all(self):
        for i in range(len(self.accountlist)):
            print("계좌번호:",self.accountlist[i].get_UserId(),"/ 이름:",self.accountlist[i].get_UserName(),"/ 잔액:",self.accountlist[i].get_UserBalance)
    
