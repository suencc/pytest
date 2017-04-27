'''
Created on Nov 11, 2016

@author: beta
'''
import pickle


def add_user():
    fd = file('./accounts.pkl','rb')
    accounts = pickle.load(fd)
    fd.close()    
    #input account name
    while True:
        name = raw_input('please enter account name:').strip()
        if len(name) > 0:
            if accounts.has_key(name): 
                print 'used account name, try again.'
                continue
            else:
                break
        else:
            print 'enter empty,try again.'
            continue
    #input  password
    while True:
        passwd = raw_input('please enter password:').strip()
        if len(passwd) > 0:
            break
        else:
            print 'enter empty,try again.'
            continue  
    
    accounts[name] = {'passwd':passwd, 'quota':15000, 'cache':0}
    fd = file('./accounts.pkl','wb')
    pickle.dump(accounts,fd)
    fd.close()
                
        
def del_user():
    print 'unsupported function.'

def add_commodity():
    fd = file('./commodities.pkl','rb')
    commodities = pickle.load(fd)
    fd.close()    
    #input product
    while True:
        product = raw_input("please enty product:").strip()
        if len(product) > 0:
            if commodities.has_key(product):
                print 'exist product,try again.'
                continue
            else:
                break
        else:
            print 'enter empty,try again.'
    #input price
    while True:
        price = int(raw_input('please enty the price:').strip())
        if price is not None:
            break
        else:
            print 'error price format,try again.'
            continue        
    
    commodities[product] = price
    fd = file('./commodities.pkl','wb')
    pickle.dump(commodities, fd)
    fd.close()        
                


def del_commodity():
    print 'unsupported function.'
    

