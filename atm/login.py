'''
Created on Nov 9, 2016

@author: beta
'''
import getpass
import pickle


managers = {'beta':{'passwd':'beta', 'desc':'Root manager user'}}

def loginmanager():
    count = 0
    while count < 3:
        user = raw_input('please enter your user name:').strip()
        if len(user) == 0:
            continue
        
        if managers.has_key(user):
            return inputpasswd(managers[user]['passwd']) 
        else:
            count += 1 
            if count >= 3:
                print 'error exceed tree times.'
                exit()
            else:
                print 'error user name, try again.'
                continue    
    
    return False
        

def loginuser():
    fd = file('./accounts.pkl','rb')
    accounts = pickle.load(fd)
    fd.close()
    
    count = 0
    while count < 3:
        account = raw_input('please enter your account name:').strip()
        if len(account) == 0:
            continue
        
        if accounts.has_key(account):
            if inputpasswd(accounts[account]['passwd']):
                return account
            else:
                return None 
        else:
            count += 1 
            if count >= 3:
                print 'error exceed tree times.'
                exit()
            else:
                print 'error account name, try again.'
                continue    
    
    return None   
    


def inputpasswd(pd):    
    for i in range(1,4):
        passwd = getpass.getpass('please enter your password:').strip()
        if passwd == pd:
            print 'welcome:'
            return True
        
        else:
            if i >= 3: 
                print 'exceed tree times, exit.'
                return False
            else:
                print 'error password,try again.'
        
