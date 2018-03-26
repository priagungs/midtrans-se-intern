# assumption :
# when there comes transaction which used same email or phone or card with customer a
# and that transaction also used same email or phone or card with customer b
# then that transaction will be merged only to one of customer

class transaction:
    def __init__(self, id, email, phone, card):
        self.id = [id]
        self.email = [email]
        self.phone = [phone]
        self.card = [card]

class transactions:
    def __init__(self):
        self.elements = []
    def addTransaction(self, transaction):
        added = False
        for i in range(len(self.elements)):
            if (self.elements[i].phone[0] == transaction.phone[0] and len(self.elements[i].id) == 1):
                self.elements[i].email += transaction.email
                self.elements[i].email = list(set(self.elements[i].email))

                self.elements[i].id += transaction.id
                self.elements[i].id = list(set(self.elements[i].id))

                self.elements[i].card += transaction.card
                self.elements[i].card = list(set(self.elements[i].card))
                added = True
                break
            elif (self.elements[i].email[0] == transaction.email[0] and len(self.elements[i].email) == 1):
                self.elements[i].phone += transaction.phone
                self.elements[i].phone = list(set(self.elements[i].phone))
                
                self.elements[i].id += transaction.id
                self.elements[i].id = list(set(self.elements[i].id))

                self.elements[i].card += transaction.card
                self.elements[i].card = list(set(self.elements[i].card))
                added = True
                break
            elif(self.elements[i].card[0] == transaction.card[0] and len(self.elements[i].card) == 1):
                self.elements[i].phone += transaction.phone
                self.elements[i].phone = list(set(self.elements[i].phone))
                
                self.elements[i].id += transaction.id
                self.elements[i].id = list(set(self.elements[i].id))

                self.elements[i].email += transaction.email
                self.elements[i].email = list(set(self.elements[i].email))
                added = True
                break
        if not added:
            self.elements.append(transaction)
    
    def printTransactions(self):
        i = 1
        for transaction in self.elements:
            print('customer' + str(i) + ':')
            print('transactions: ', transaction.id)
            print('emails: ', transaction.email)
            print('phones: ', transaction.phone)
            print('cards: ', transaction.card)
            print()
            i+=1

# test case
trx = transactions()
trx.addTransaction(transaction(1,'e1','p1','c1'))
trx.addTransaction(transaction(2,'e2','p2','c2'))
trx.addTransaction(transaction(3,'e1','p3','c3'))
trx.addTransaction(transaction(4,'e4','p4','c4'))
trx.addTransaction(transaction(5, 'e2', 'p4', 'c5'))
trx.printTransactions()