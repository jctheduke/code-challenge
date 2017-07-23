class Order:

    def __int__(self, key, event_time, customer_id, total_amount):
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
