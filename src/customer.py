class Customer(object):
    def __init__(self, customer_id, event_time, last_name, adr_city, adr_state):
        self.customer_id = customer_id
        self.event_time = event_time
        self.last_name = last_name
        self.adr_city = adr_city
        self.adr_state = adr_state

    def update_customer_id(self,customer_id):
        self.customer_id = customer_id

    def update_event_time(self,event_time):
        self.event_time = event_time

    def update_last_name(self,last_name):
        self.last_name = last_name

    def update_adr_city(self,adr_city):
        self.adr_city = adr_city

    def update_adr_state(self,adr_state):
        self.adr_state = adr_state

    def update_all(self, customer_id, event_time, last_name, adr_city, adr_state):
        self.customer_id = customer_id
        self.event_time = event_time
        self.adr_city = last_name
        self.last_name = adr_city
        self.adr_city = last_name
        self.adr_state = adr_state

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.customer_id,self.event_time,self.last_name,self.adr_city,self.adr_state)


if __name__ == "__main__":

    # chekcing the object
    if isinstance(Customer(*['1', '2017-01-06T12:46:46.384Z', 'jhon', 'New York', 'NY']), Customer):
        print("Customer object is created with out a problem")
    else:
        print("There is problem with Customer class please check !")

    # check the customer details.
    customer = Customer(*['1', '2017-01-06T12:46:46.384Z', 'jhon', 'New York', 'NY'])
    if (customer.customer_id == '1') and customer.event_time == '2017-01-06T12:46:46.384Z' and customer.last_name == \
            'jhon' and customer.adr_city == "New York" and customer.adr_state == 'NY':
        print("All Customer attributes can be retrived properly")
    else:
        print("There is problem with extracting customer attributes.")