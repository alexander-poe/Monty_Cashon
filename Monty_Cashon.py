from time import gmtime, strftime

class bank:
    def __init__(self):
        self.gift_bank = []
        self.transaction = []
      
    # check format
    def add_cash(self, c):
        return {
            'save': c * .2, 
            'spend': c * .3, 
            'utility': c * .5
        }   
    
    # add check using check format
    def deposit_gift(self, gift):
        self.gift_bank.append(self.add_cash(gift))
        self.transaction.append({
            'type': 'GIFT_DEPOSIT', 
            'amount': gift, 
            'date': strftime("%Y-%m-%d %H:%M:%S", gmtime())
        })
    
    # withdraw from prop of check
    def take_from_env(self, id, envelope, amount, title):
        c = self.gift_bank[id]
        if c[envelope] - amount < 0:
            print(envelope, 'envelope only has', c[envelope], 'dollers try again.')
        else:
            c[envelope] = c[envelope] - amount
            self.transaction.append({
                'type': 'TRANSACTION', 
                'amount': amount,
                'envelope': envelope,
                'title' : title,
                'gift': self.transaction[id],
                'date': strftime("%Y-%m-%d %H:%M:%S", gmtime())
            })
            
    def analyze_take(self):
        data_ab = []
        for x in self.transaction:
            if x['type'] == 'TRANSACTION': 
                data_ab.append(x['title'])
            
    def display_bank(self):
        total = 0
        save = 0
        spend = 0
        utility = 0
        print('Transactions')
        print('-----------------------')
        for v in self.transaction:
            total = total + v["amount"]
            if v["type"] == "GIFT_DEPOSIT":
                print('    ')
                print("Date:",v["date"])
                print("Deposited:", v["amount"])
                print('    ')
            elif v["type"] == "TRANSACTION":
                print('    ')
                print("Date:",v["date"])
                print("Withdraw: -", v["amount"])
                print("Title:", v["title"])
                print("Envelope:", v["envelope"])
                print('    ')
                
        
        for x in self.gift_bank:
            save = save + x["save"] 
            spend = spend + x["spend"] 
            utility = utility + x["utility"]   
        
        print('Overview')
        print('----------------------')
        print('    ')
        print('savings-total:', save)
        print('    ')
        print('spending-total:', spend)
        print('    ')
        print('utility-total:', utility)
        print('    ')
        print('account-balance-total:', total)
        print('    '),