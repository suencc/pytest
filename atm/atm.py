'''
Created on Nov 9, 2016

@author: beta
'''
import prompt
import login
import manager
import user

def manager_entry():
    if not login.loginmanager() :
        return False

    while True:
        operating = raw_input( prompt.manager_option).strip()        
        if operating == '1':
            manager.add_user()                       
        elif operating == '2':
            manager.del_user()   
        elif operating == '3':
            manager.add_commodity()         
        elif operating == '4':
            manager.del_commodity()
        elif operating == '0':
            save_quit()
            break
        else:    
            continue
                    
    
def user_entry():
    account = login.loginuser();
    if account is None :
        return False
    while True:
        operating = raw_input( prompt.user_option).strip() 
        if operating == '1':
            user.shopping(account)
        elif operating == '2':
            user.save(account)
        elif operating == '3':
            user.withdraw(account)
        elif operating == '4':
            user.inquire(account)
        elif operating == '5':
            user.genbill(account)
        elif operating == '0':
            break
        else:
            continue
                


def save_quit():
    pass


def main():
    while True:
        account_type = raw_input( prompt.entry).strip()        
        if account_type == '1':
            user_entry()                       
        elif account_type == '2':
            manager_entry()            
        elif account_type == '0':
            save_quit()
            break
        else:    
            continue
                
    
if __name__ == '__main__':
    main();