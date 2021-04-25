from BankAccount import bank
print('hi')
if __name__ == '__main__':

        x = bank.Bank()
        
        while (1):
            num = input(" ======== Bank Menu ========\n 1. 계좌개설\n 2. 입금하기\n 3. 출금하기 \n 4. 전체조회\n 5. 종료하기\n ===========================\n")
            if num == "1":
                print(" ===========================")                
                x.create_account()         
                print(" ===========================")                
                
            elif num == "2":
                print(" ===========================")                
                x.deposit()
                print(" ===========================")                
                
            elif num == "3":
                print(" ===========================")                
                x.withdraw()
                print(" ===========================")                
                
            elif num == "4":
                print(" ===========================")                
                x.show_all()
                print(" ===========================")                
                
            elif num == "5":
                print(" ===========================")                
                print("종료하시겠습니까?")
                print("1. 네  2. 아니요")
                exit = int(input())
                if exit == 1:
                    break
                elif exit == 2:
                    print(" ===========================")                
                else:
                    print("1과 2중 하나를 입력하세요.")
                print(" ===========================")  
