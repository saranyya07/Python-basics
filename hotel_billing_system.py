# Global Variable
hotel_name = "Grand Palace Hotel"

def calculate_bill(room_charge, food_charge, service_charge):
    total=room_charge+food_charge+service_charge
    return total
    

def apply_discount(total_amount):
    if total_amount>5000:
        total_amount=total_amount-(0.15*total_amount)
    return total_amount
    
    

def display_bill(guest_name, final_amount):
    print("Hotel Name : ",hotel_name)
    print("Guest Name : ",guest_name)
    print("Final Bill : ",float(final_amount))

def main():
    guest_name = input()
    room_charge = float(input())
    food_charge = float(input())
    service_charge = float(input())

    total_amount = calculate_bill(room_charge, food_charge, service_charge)
    final_amount = apply_discount(total_amount)
    display_bill(guest_name, final_amount)

if __name__ == "__main__":
    main()
