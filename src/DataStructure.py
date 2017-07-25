from src import customer, ImageUpload, Order, SiteVisit
from dateutil import parser
from collections import defaultdict
import warnings


class DataStructure(object):
    """
    Data Structure for holding customer and customer transaction details.
    """

    def __init__(self):
        # Data structure D is defaultdict with predefined data structure
        self.D = defaultdict(self.data_structure)

    def items(self):
        return self.D.items()

    def data_structure(self):
        # Pre defined data structure for default dict.
        return {'Customer':None,'SiteVisit':[],'ImageUpload':[],'Order':[],'OrderId':[]}

    def get_customer(self,customer_id):
        # Return a customer based on his customer id.
        return self.D[customer_id]

    def add_new_customer(self,*args):
        """
        Adds new customer to the database only if customer is not present in the database.
        :param args: (customer_id, event_time, last_name, adr_city, adr_state)
        :return: None
        """

        # Shows prompt to the user,if user didnt provide mandatory fields.
        # Assumption : Atleast customer_id and event_time details are provided before passing last_name,adr_city,adr_state.

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
                print("Customer:{} already present in the database".format(customer_id))

            else:
                # Checks for invalid event time format.
                try:
                    # converting event_time from string to datetime format
                    event_time = parser.parse(event_time)

                    # adding new customer to the database
                    new_customer = customer.Customer(customer_id, event_time, last_name, adr_city, adr_state)
                    self.D[customer_id]['Customer'] = new_customer

                except ValueError :
                    print ("Given event_time  {} is not the correct format".format(event_time))

    def update_customer(self,*args):
        """
        Updates the customer if customer exists in the database, else creates a new customer.
        :param args: (customer_id, event_time, last_name, adr_city, adr_state)
        :return: None
        """

        if len(args) < 2:
            # Generates warning if there are less than two aruguments
            warnings.warn("CustomerId and event_time are not provided for this event {}".format(' '.join(args)))
        else:
            # assigning argument values to corresponding attributes.
            customer_id = args[0]
            event_time = args[1]
            last_name = args[2] if len(args)>2 else None
            adr_city = args[3] if len(args)>3 else None
            adr_state = args[4] if len(args)>4 else None

            try:
                # converting event_time from string to datetime format
                event_time = parser.parse(event_time)

                # If customer is not present in the current raises a warning
                if customer_id not in self.D.keys():
                    warnings.warn("Current customer {} is not present in the Database,So adding new customer".format(customer_id))
                    self.add_new_customer(self,args)
                else:
                    # Updating the existing customer
                    updated_customer = customer.Customer(customer_id, event_time, last_name, adr_city, adr_state)
                    self.D[updated_customer.customer_id]['Customer'] = updated_customer

            except ValueError:
                print("Given event_time  {} is not the correct format".format(event_time))

    def add_site_visit(self,*args):
        """
        Add site visit to customer if customer exists.
        :param args: (page_id, event_time, customer_id, tags)
        :return: None
        """

        if len(args)<3:
            # Check if the required arguments are not passed.If not produce a warning
            warnings.warn("Required arguments page_id,event_time,customer_id are passed")

        else:
            # Storing the arguments
            key = args[0]
            event_time = args[1]
            customer_id = args[2] if len(args) > 2 else None
            tags = args[3] if len(args) > 3 else None

            # Checking for compatible event time.
            try:
                # coversting event time to data time format
                event_time = parser.parse(event_time)

                if customer_id not in self.D.keys():
                    # Checking if customer if present in the database
                    print("Customer is not present in the database")
                else:
                    # Adding site visit to customer.
                    site_vist = SiteVisit.SiteVisit(key,event_time,customer_id,tags)
                    self.D[customer_id]['SiteVisit'].append(site_vist)

            except ValueError:
                print("Given event_time  {} is not the correct format".format(event_time))

    def add_image_upload(self,*args):
        """
        Adds image upload details to the customer, if customer exists.
        :param args: (image_id, event_time, customer_id, camera_make, camera_model)
        :return: None
        """

        if len(args)<3:
            # Check if the required arguments are not passed.If not produce a warning
            print("Required arguments image_id,event_time,customer_id are passed")


        else:
            key = args[0]
            event_time = args[1]
            customer_id = args[2] if len(args) > 2 else None
            camera_make = args[3] if len(args) > 3 else None
            camera_model = args[4] if len(args)>4 else None

            # Catches imperfect event time format
            try:
                # coversting event time to data time format
                event_time = parser.parse(event_time)
                if customer_id not in self.D.keys():
                    # Checking if customer if present in the database
                    print("Customer is not present in the database")
                else:
                    # Adding site visit to customer.
                    image_upload = ImageUpload.ImageUpload(key,event_time,customer_id,camera_make,camera_model)
                    self.D[customer_id]['ImageUpload'].append(image_upload)

            except ValueError:
                print("Given event_time  {} is not the correct format".format(event_time))

    def add_new_order(self,*args):
        """
        Adds new order to customer orders, if customer exists and order is not present.
        :param args: (order_id, event_time, customer_id, total_amount)
        :return: None
        """

        if len(args) != 4:
            # Check if the required arguments are not passed.If not produce a warning
            print("Required arguments image_id,event_time,customer_id are passed")


        else:
            order_id = args[0]
            event_time = args[1]
            customer_id = args[2]
            total_amount = args[3]

            # Checks for event time format
            try:
                # coversting event time to data time format and checking amount format.
                event_time = parser.parse(event_time)
                amount = float(total_amount.partition(" ")[0])

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

            except ValueError:
                print("Either event_time  {} or total amount {} is not the correct format".format(event_time,total_amount))

    def update_order(self,*args):
        """
        Updates the order ,if customer exists and Order is present.
        :param args: (order_id, event_time, customer_id, total_amount)
        :return: None
        """

        if len(args) != 4:
            # Check if the required arguments are not passed.If not produce a warning
            print("Required arguments image_id,event_time,customer_id are passed")

        else:
            order_id = args[0]
            event_time = args[1]
            customer_id = args[2]
            total_amount = args[3]

            # Checks for event time format
            try:
                # coversting event time to data time format and checking the amount format.
                event_time = parser.parse(event_time)
                amount = float(total_amount.partition(" ")[0])

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

            except ValueError:
                print("Either event_time  {} or total amount {} is not the correct format".format(event_time,total_amount))


    def __str__(self):
        """
        Printing the Customer database in pretty format.
        :return: Return formatted string format of database.
        """
        string = "Customer Deails \n"

        # Printing Customer details.
        for key,customer in self.D.items():
            customer_details = customer['Customer']
            string += "customer ID, customer added date, last name, city, state \n" \
                      "{}\n".format(customer_details)

            # Printing customer visiting details.
            string += "Customer Site Visits \n" \
                      "page_id, visit_time,customer_id,tags\n"
            for visit in customer['SiteVisit']:
                string += str(visit)
            string +="\n"

            # Printing Image Upload Details.
            string += "Customer Image Uploads \n" \
                      "image_id, Upload time, customer_id, camera_make, camera_model\n"
            for image in customer['ImageUpload']:
                string += str(ImageUpload)
            string += "\n"

            # Printing Order Details
            string +="Customer Order Details \n" \
                     "order_id, order time, customer id, order amount\n"
            for order in customer['Order']:
                string += str(order)

            string +="\n\n"
        return string