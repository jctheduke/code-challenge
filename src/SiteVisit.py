class SiteVisit(object):

    def __init__(self,key,event_time,customer_id,tags):
        self.key = key
        self.event_time = event_time
        self.customer_id = customer_id
        self.tags = tags

    def __str__(self):
        return "{}, {}, {}, {}".format(self.key,self.event_time,self.customer_id,self.tags)


if __name__ == "__main__":

    # chekcing the object
    if isinstance(SiteVisit(*['1', '2017-01-06T12:46:46.384Z', '101',['Posters','Frames']]), SiteVisit):
        print("SiteVisit object is created with out a problem")
    else:
        print("There is problem with SiteVisit class please check !")

    # check the customer details.
    site_visit = SiteVisit(*['1', '2017-01-06T12:46:46.384Z', '101',['Posters','Frames']])
    if (site_visit.key == '1') and site_visit.event_time == '2017-01-06T12:46:46.384Z' and site_visit.customer_id == \
            '101' and site_visit.tags == ['Posters','Frames'] :
        print("All SiteVisit attributes can be retrived properly")
    else:
        print("There is problem with extracting SiteVisit attributes.")