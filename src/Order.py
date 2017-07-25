class Order:

    def __init__(self, key, event_time, customer_id, total_amount):
        self.key = key
        self.event_time = event_time
        self.customer_id = customer_id
        self.total_amount = total_amount

    def update_key(self, key):
        self.key = key

    def update_event_time(self, event_time):
        self.event_time = event_time

    def update_customer_id(self, customer_id):
        self.customer_id = customer_id

    def update_total_amount(self, total_amount):
        self.total_amount = total_amount

    def update_all(self, key, event_time, customer_id, total_amount):
        self.key = key
        self.event_time = event_time
        self.customer_id = customer_id
        self.total_amount = total_amount

    def __str__(self):
        return "{}, {}, {}, {}".format(self.key, self.event_time, self.customer_id, self.total_amount)

if __name__ == "__main__":

    # chekcing the object
    if isinstance(Order(*['1', '2017-01-06T12:46:46.384Z', '101','17.34 USD']), Order):
        print("Order object is created with out a problem")
    else:
        print("There is problem with Order class please check !")

    # check the customer details.
    order = Order(*['1', '2017-01-06T12:46:46.384Z', '101','17.34 USD'])
    if (order.key == '1') and order.event_time == '2017-01-06T12:46:46.384Z' and order.customer_id == \
            '101' and order.total_amount == "17.34 USD" :
        print("All Order attributes can be retrived properly")
    else:
        print("There is problem with extracting Order attributes.")