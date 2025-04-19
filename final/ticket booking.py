class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0 
        
        self.ticket_trice = 500

    def available_seats(self):
        "returns unbooked seats"
        return self.total_seats - self.booked_seats

    def book_seat(self):
        " books if seats available "
        if self.available_seats():
            self.booked_seats += 1
            return True
        else:
            print("[!] Seat not available. ")
        return False

    def __repr__(self):
        return f"BUS: {self.number}, Route: {self.route}, ticket_price: {self.ticket_trice}, Seat avilable:{self.available_seats()}/{self.total_seats}"


class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = str(phone)
        self.bus = bus

    def __repr__(self):
        # return f"Name: {self.name}, Phone: {self.phone[:4]}....{self.phone[-3:], }, Bus:{self.bus.number}"
        return f"Name: {self.name}, Phone: {self.phone}, Bus_number:{self.bus.number}"

class BusSystem:
    def __init__(self):
        self.buses:list = []
        self.passengers:list = []
    
    def book_ticket(self, bus_number, name, phone):
        for bus in self.buses:
            if bus_number!=bus.number: continue
            
            if bus.book_seat():# auto prompt on seat sortage
                self.passengers.append(Passenger(name, phone, bus))
            
            break

    def show_buses(self):
        print("\n[+] Showing all available buses")
        for i in self.buses:
            print("\t", i)
        print()

    def show_passenger(self):
        print("\n[+] Showing all Passenger list")
        for i in self.passengers:
            print("\t", i)
        print()


bd_buses = BusSystem()
bd_buses.buses.append(Bus(2222, "dha-chi", 30))# debug

class Admin:
    def __init__(self):
        self.__username = "admin"
        self.__password = "1234"
        self.is_login = False
    
    def login(self, username, password):
        if self.is_login: return
        if username==self.__username and password==self.__password:
            print("[+] Log-in sucessfull ")
            self.is_login = True
        else:
            print("[!] Wrong cridential.")
        
        return self.is_login

    def add_bus(self, number, route, seats):
        "abdim only method"
        if not self.is_login:
            print("[!] Please log in as admin first")
            return 
        
        bd_buses.buses.append(Bus(number, route, seats))


def int_input(prompt):
    while 1:
        choise = input(prompt)
        if choise.isdigit():
            break
        print("[!] Only numeric inputs are allowed. ")
    
    return int(choise)

def show_obtions(l):
    print()
    for i in range(len(l)):
        print(f" {i+1}. {l[i]}")

    while 1:    
        choise = int_input(f"Choise a option between (1, {len(l)}): ")

        if choise<=0 or choise>len(l):
            print("[!] wrong option chosen. ")
            continue

        return choise-1


user_option = ["Admin Login", "Book Ticket", "View Buses", "Exit"]
admin_option = ["Add Bus", "View All Buses", "Passenter list", "Logout"]
while 1:
    choise = show_obtions(user_option)

    if choise==0:# Adim login
        admin = Admin()
        if not admin.login(
            input("[-] Username: "),
            input("[-] Password: ")
        ): continue
            
        while 1:
            choise = show_obtions(admin_option)
            if choise==0:
                admin.add_bus(
                    int_input("[-] Enter Bus number: "),
                    input("[-] Enter Route: "),
                    int_input("[-] Enter total seat number: ")
                )
            elif choise==1:
                bd_buses.show_buses()
                input("[-] Press Enter to continue..")
            elif choise==2:
                bd_buses.show_passenger()
                input("[-] Press Enter to continue..")
            elif choise==3:# logout
                break
    
    elif choise==1:
        if not bd_buses.buses:
            print(f"[!] Ask your admin to add some buses first")
            continue
        
        choise = show_obtions(bd_buses.buses+["back manue"])
        if choise==len(bd_buses.buses):# back manue
            continue
        
        bd_buses.book_ticket(
            bd_buses.buses[choise].number, 
            input("[-] Enter your name: "),
            input("[-] Enter your phone number: ")# NOTE: int_input not possible, user might input with country code cointaining + sign +880
        )# TODO: validation checks for name & phone
    elif choise==2:
        bd_buses.show_buses()
        input("[-] Press Enter to continue..")
    elif choise==3:
        break




    

