class SiteVisit(object):

    def __init__(self,key,event_time,customer_id,tags):
        self.key = key
        self.event_time = event_time
        self.customer_id = customer_id
        self.tags = tags

    def __str__(self):
        return "{}, {}, {}, {}".format(self.key,self.event_time,self.customer_id,self.tags)

    