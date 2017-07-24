from src import customer, ImageUpload, Order, SiteVisit
from dateutil import parser
from collections import defaultdict
import warnings


class DataStructure(object):
    def __init__(self):
        self.D = defaultdict(self.data_structure)


    def data_structure(self):
        return {'Customer':None,'SiteVisit':[],'ImageUpload':[],'Order':[],'OrderId':[]}

    def add_new_customer(self,*args):

        # Shows prompt to the user,if user didnt provide mandatory fields.
        # Assumption : Atleast key and event_time details are provided before passing last_name,adr_city,adr_state.

        if len(args) < 2:
            # Generates warning if there are less than two aruguments
            print("CustomerId and event_time are not provided for this event {}".format(' '.join(args)))
        else:
            # assigning argument values to corresponding attributes.
            customer_id = args[0]
            event_time = args[1]
            last_name = args[2] if len(args)>2 else None
            adr_city = args[3] if len(args)>3 else None
            adr_state = args[4] if len(args)>4 else None

            # If customer already present in the database.
            if customer_id in self.D.keys():
                print("Customer already present in the database.")

            else:
                # converting event_time from string to datetime format
                event_time = parser.parse(event_time)

                # adding new customer to the database
                new_customer = customer.Customer(customer_id,event_time,last_name,adr_city,adr_state)
                self.D[customer_id]['Customer'] = new_customer


    def update_customer(self,*args):

        if len(args) < 2:
            # Generates warning if there are less than two aruguments
            warnings.warn("CustomerId and event_time are not provided for this event {}".format(' '.join(args)))
        else:
            # assigning argument values to corresponding attributes.
            key = args[0]
            event_time = args[1]
            last_name = args[2] if len(args)>2 else None
            adr_city = args[3] if len(args)>3 else None
            adr_state = args[4] if len(args)>4 else None

            # converting event_time from string to datetime format
            event_time = parser.parse(event_time)

            # If customer is not present in the current raises a warning
            if key not in self.D.keys():
                warnings.warn("Current customer is not present in the Database,So adding new customer")
                self.add_new_customer(self,args)
            else:
                # Updating the existing customer
                updated_customer = customer.Customer(key, event_time, last_name, adr_city, adr_state)
                self.D[updated_customer.customer_id]['Customer'] = updated_customer


    def add_site_visit(self,*args):

        if len(args)<3:
            # Check if the required arguments are not passed.If not produce a warning
            warnings.warn("Required arguments page_id,event_time,customer_id are passed")

        else:
            key = args[0]
            event_time = args[1]
            customer_id = args[2] if len(args) > 2 else None
            tags = args[3] if len(args) > 3 else None

            # coversting event time to data time format
            event_time = parser.parse(event_time)
            if customer_id not in self.D.keys():
                # Checking if customer if present in the database
                print("Customer is not present in the database")
            else:
                # Adding site visit to customer.
                site_vist = SiteVisit.SiteVisit(key,event_time,customer_id,tags)
                self.D[customer_id]['SiteVisit'].append(site_vist)

    def add_image_upload(self,*args):

        if len(args)<3:
            # Check if the required arguments are not passed.If not produce a warning
            print("Required arguments image_id,event_time,customer_id are passed")


        else:
            key = args[0]
            event_time = args[1]
            customer_id = args[2] if len(args) > 2 else None
            camera_make = args[3] if len(args) > 3 else None
            camera_model = args[4] if len(args)>4 else None

            # coversting event time to data time format
            event_time = parser.parse(event_time)
            if customer_id not in self.D.keys():
                # Checking if customer if present in the database
                print("Customer is not present in the database")
            else:
                # Adding site visit to customer.
                image_upload = ImageUpload.ImageUpload(key,event_time,customer_id,camera_make,camera_model)
                self.D[customer_id]['ImageUpload'].append(image_upload)


    def add_new_order(self,*args):

        if len(args) != 4:
            # Check if the required arguments are not passed.If not produce a warning
            print("Required arguments image_id,event_time,customer_id are passed")


        else:
            order_id = args[0]
            event_time = args[1]
            customer_id = args[2]
            total_amount = args[3]

            # coversting event time to data time format
            event_time = parser.parse(event_time)

            if customer_id not in self.D.keys():
                # Checking if customer if present in the database
                print("Customer is not present in the database")

            elif order_id in self.D[customer_id]['OrderId']:
                print("This order is already present for this customer")

            else:
                # Adding order to customer.
                new_order = Order.Order(order_id, event_time, customer_id, total_amount)
                self.D[customer_id]['Order'].append(new_order)
                self.D[customer_id]['OrderId'].append(order_id)

    def update_order(self,*args):

        if len(args) != 4:
            # Check if the required arguments are not passed.If not produce a warning
            print("Required arguments image_id,event_time,customer_id are passed")

        else:
            order_id = args[0]
            event_time = args[1]
            customer_id = args[2]
            total_amount = args[3]

            # coversting event time to data time format
            event_time = parser.parse(event_time)

            if customer_id not in self.D.keys():
                # Checking if customer if present in the database
                print("Customer is not present in the database")

            elif order_id not in self.D[customer_id]['OrderId']:
                print("This order is not present for this customer")

            else:
                # Adding order to customer.
                update_order = Order.Order(order_id, event_time, customer_id, total_amount)

                # Getting the index of current order ID.
                for i in range(len(self.D[customer_id]['Order'])):
                    # If order_id found, update the order
                    if order_id == self.D[customer_id]['Order'][i]:
                        self.D[customer_id]['Order'][i] = update_order


    def __str__(self):
        return "{}".format(self.D)