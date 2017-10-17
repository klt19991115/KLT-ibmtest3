''' A SIMPLE CASHIER SYSTEM '''
commodity_list = dict()
cashier_list = dict()
class item(object):
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
    def _add(self):
        commodity_list[self.code] = [self.name, self.price]
        cashier_list[self.code] = 0
def inlist(num):
    if num in commodity_list :
        return True
    else :
        return False
def cashier():
    print "You are now at cashier desk!"
    bill = 0
    while True :
        instruction = raw_input("/cashier Please input the instruction(input 'help' to get help):")
        if instruction == "return":
            for i in cashier_list:
                cashier_list[i] = 0
            break
        elif instruction == "help":
            print "input 'add' to add commodity"
            print "input 'del' to del commodity"
            print "input 'bill' to get bill"
            print "input 'return' to back to main"
        elif instruction == "add":
            code = input("input commodity's code:")
            if inlist(code) :
                number = input("input commodity's number:")
                cashier_list[code] += number
                bill += number * commodity_list[code][1]
            else :
                print "The code is not in the commodity_list!"
        elif instruction == "del":
            code = input("input commodity's code:")
            if inlist(code) :
                number = input("input commodity's number:")
                if number > cashier_list[code]:
                    number = cashier_list[code]
                cashier_list[code] -= number
                bill -= number * commodity_list[code][1]
            else :
                print "The code is not in the commodity_list!"
        elif instruction == "bill":
            print "Totally need money %d" %bill
            if raw_input("Do you need to print your bill?(Y for yes ,others for no)") == "Y":
                fff = open("bill.txt", "w")
                fff.write("Code  Name  Price  Number \n")
                for i in cashier_list :
                    if cashier_list[i] != 0 :
                        fff.write(str(i)+"  "+commodity_list[i][0]+"  "+str(commodity_list[i][1])+"  "+str(cashier_list[i])+"\n")
                fff.close()
                print "Bill print finished!The bill is saved in bill.txt."
        else :
            print "ERROR! This is not an effective instruction!"

print "Welcome to cashier system!"
while True :
    command = raw_input("/main Please input the instruction(input 'help' to get help):")
    if command == "ESC":
        break
    elif command == "help":
        print "input 'add' to add an item"
        print "input 'del' to del an item"
        print "input 'cas' to enter cashier desk"
        print "input 'ESC' to exit the system"
    elif command == "add":
        code = input("input commodity's code:")
        if inlist(code):
            print "The code is already in the commodity_list"
        else :
            name = raw_input("input commodity's name:")
            price = input("input commodity's price:")
            item(code, name, price)._add()
    elif command == "del":
        code = input("input commodity's code you want to delete:")
        if inlist(code) :
            del commodity_list[code]
            del cashier_list[code]
        else :
            print "The code is not in the commodity_list!"
    elif command == "cas":
        cashier()
        print "You are back to main now!"
    else :
        print "ERROR! This is not an effective command!"

'''KLT FOR WHUIBM-TEST3'''