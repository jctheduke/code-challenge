from src import customer, ImageUpload, Order, SiteVisit
from dateutil import parser
from collections import defaultdict
import warnings


class DataStructure(object):



    def __int__(self):
        self.D = defaultdict(self.data_structure)

    def data_structure(self):
        return {'Customer':None,'SiteVisit':[],'ImageUpload':[],'Order':[]}

    def customer_new(self,*args):

        # Shows prompt to the user,if user didnt provide mandatory fields.
        # Assumption : Atleast key and event_time details are provided before passing last_name,adr_city,adr_state.

        if len(args) < 2:
            # Generates warning if there are less than two aruguments
            warnings.warn("CustomerId and event_time are not provided for this event {}".format(' '.join(args)))
        else:
            # assigning argument values to corresponding attributes.
            key = args[0]
            event_time = args[1]
            last_name = args[2] if args[2] else None
            adr_city = args[3] if args[3] else None
            adr_state = args[4] if args[4] else None

            # converting event_time from string to datetime format
            event_time = parser.parse(event_time)

            # adding new customer to the database
            new_customer = customer.Customer(key,event_time,last_name,adr_city,adr_state)
            self.D[new_customer.customer_id]['Customer'] = new_customer

    def customer_update(self,*args):

        if len(args) < 2:
            # Generates warning if there are less than two aruguments
            warnings.warn("CustomerId and event_time are not provided for this event {}".format(' '.join(args)))
        else:
            # assigning argument values to corresponding attributes.
            key = args[0]
            event_time = args[1]
            last_name = args[2] if args[2] else None
            adr_city = args[3] if args[3] else None
            adr_state = args[4] if args[4] else None

            # converting event_time from string to datetime format
            event_time = parser.parse(event_time)

            # If customer is not present in the current raises a warning
            if key not in self.D.keys():
                warnings.warn("Current customer is not present in the Database,So adding new customer")
                self.customer_new(self,args)
            else:
                # Updating the existing customer
                updated_customer = customer.Customer(key, event_time, last_name, adr_city, adr_state)
                self.D[updated_customer.customer_id]['Customer'] = updated_customer
