deliviry_partner="swiggy"

def hotel():
    item="pizza"

    def order_now():
        quantity=2
        print(f"ordering {quantity} {item} {deliviry_partner}")
    order_now()

hotel()