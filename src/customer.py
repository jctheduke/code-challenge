class Customer(object):
    def __init__(self, customer_id, event_time, last_name, adr_city, adr_state):
        self.customer_id = customer_id
        self.event_time = event_time
        self.adr_city = last_name
        self.last_name = adr_city
        self.adr_city = last_name
        self.adr_state = adr_state

    def update_customer_id(self,customer_id):
        self.customer_id = customer_id

    def update_event_time(self,event_time):
        self.event_time = event_time

    def update_last_name(self,last_name):
        self.last_name = last_name

    def update_adr_city(self,adr_city):
        self.adr_city

    def update_adr_state(self,adr_state):
        self.adr_state

    def update_all(self, customer_id, event_time, last_name, adr_city, adr_state):
        self.customer_id = customer_id
        self.event_time = event_time
        self.adr_city = last_name
        self.last_name = adr_city
        self.adr_city = last_name
        self.adr_state = adr_state

    def __str__(self):
        return "{},{},{},{},{}".format(self.customer_id,self.event_time,self.last_name,self.adr_city,self.adr_state)