'''
Created on Nov 21, 2016

@author: beta
'''
import pickle
import time

def appendbills(billrecord):
    fd = file('./bills.pkl','rb')
    bills = pickle.load(fd)
    fd.close()
    
    bills.append(billrecord)
    
    fd = file('./bills.pkl','wb')
    pickle.dump(bills, fd)
    fd.close()    


def updateaccount(account, quota, cache):
    fd = file('./accounts.pkl','rb')
    accounts = pickle.load(fd)
    fd.close()
        
    accounts[account]['quota'] = quota
    accounts[account]['cache'] = cache
    
    fd = file('./accounts.pkl','wb')
    pickle.dump(accounts, fd)
    fd.close()    
              

def shopping(account):
    fd = file('./commodities.pkl','rb')
    commodities = pickle.load(fd)
    fd.close() 
    fd = file('./accounts.pkl','rb')
    accounts = pickle.load(fd)
    fd.close()       

    cache = accounts[account]['cache']
    quota = accounts[account]['quota']
       
    while True:     
        print commodities
        commodity = raw_input('enter 0 to exit, enter product to buy:').strip() 
        if commodity == '0': break
        for k,v in commodities.items():
            price = v            
            if commodity == k:
                if cache + quota < price:
                    print 'not sufficient funds, select again.'
                    break
                else:
                    if price <= cache:
                        cache -= price
                        print 'has buy one %s quota: %d cache: %d'%(commodity, quota, cache)
                        appendbills([account, 'buy', k, -v, time.ctime()])
                        break
                    else:    
                        cache = 0
                        quota = quota + cache - price
                        print 'has buy one %s quota: %d cache: %d'%(commodity, quota, cache)
                        appendbills([account, 'buy', k, -v,  time.ctime()])
                        break 
                               
    updateaccount(account, quota, cache)
    return True

def save(account):
    fd = file('./accounts.pkl','rb')
    accounts = pickle.load(fd)
    fd.close()       

    cache = accounts[account]['cache']
    quota = accounts[account]['quota']
    
    while True:
        saving = int(raw_input('enter 0 to exit, enter int to save:').strip()) 
        if saving == 0:
            break;
        else:
            quota += saving
            if quota > 15000:
                cache += quota - 15000
                quota = 15000
            print 'has saved $ %s quota: %d cache: %d'%(saving, quota, cache)
            appendbills([account, 'save', 'saving', saving, time.ctime()])
    
    updateaccount(account, quota, cache); 
            
def withdraw(account):
    fd = file('./accounts.pkl','rb')
    accounts = pickle.load(fd)
    fd.close()       

    cache = accounts[account]['cache']
    quota = accounts[account]['quota']
    
    while True:
        drawing = int(raw_input('enter 0 to exit, enter int to withdraw:').strip()) 
        if drawing == 0:
            break;
        else:
            if drawing > cache + quota:
                print 'not sufficient funds'
                continue
            else:
                quota = quota + cache - drawing;
                if quota > 15000:
                    cache = quota - 15000
                    quota = 15000
                print 'has withdrawed $ %s quota: %d cache: %d'%(drawing, quota, cache)
                appendbills([account, 'withdraw', 'drawing', drawing, time.ctime()])
    
    updateaccount(account, quota, cache); 

def inquire(account):
    pass

def genbill(account):
    pass


    