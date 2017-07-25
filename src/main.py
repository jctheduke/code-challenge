from src import DataStructure
import json
from datetime import datetime
from collections import namedtuple


# Setting up Input and Output files
input_file = r"C:\Users\priyaranjanjc\Desktop\code-challenge\input\input.txt"
output_file = r"C:\Users\priyaranjanjc\Desktop\code-challenge\output\output.txt"

# Reading input file JSON file.
with open(input_file) as f:
    input_data = json.load(f)

# Intiating the DataStructure
data = DataStructure.DataStructure()


def ingest(event,database):
    """
     Executes ingest for given event and given datastructure.
    :param event: JSON format of the event.
    :param database: Datastructure passed as a object
    :return: None
    """

    # customer event
    if event['type'] == 'CUSTOMER':
        if event['verb'] == 'NEW':
            database.add_new_customer(event['key'],event['event_time'],event['last_name'],event['adr_city'],event['adr_state'])
        elif event['verb'] == 'UPDATE':
            database.update_customer(event['key'],event['event_time'],event['last_name'],event['adr_city'],event['adr_state'])

    # Site Visit event
    if event['type'] == 'SITE_VISIT':
        if event['verb']:
            database.add_site_visit(event['key'],event['event_time'],event['customer_id'],event['tags'])

    # Image Upload event
    if event['type'] == 'IMAGE':
        if event['verb'] == 'NEW':
            database.add_image_upload(event['key'],event['event_time'],event['customer_id'],event['camera_make'],event['camera_model'])

    # Order event
    if event['type'] == 'ORDER':
        if event['verb'] == 'NEW':
            database.add_new_order(event['key'],event['event_time'],event['customer_id'],event['total_amount'])
        elif event['type'] == 'UPDATE':
            database.update_order(event['key'],event['event_time'],event['customer_id'],event['total_amount'])

# Processing events in given JSON input file.
for event in input_data:
    ingest(event,data)


def compute_ltv(customer):
    """
    Computes LTV for given customer according to formula 52(a)*t.
    where:
        a - Average Customer revenue.
        t - Retention period of customer ( 10 years for shutter fly)
    :param customer: Customer object contains orders,site visits,Image Uploads and Customer details.
    :return: return LTV value of given customer.
    """

    # first and last order of the customer
    first_order = customer['Order'][0].event_time
    last_order  = datetime.now()
    site_visits = 0

    # total expenditure of the customer
    total_amount = 0

    # calcualte total number of site visits and total revenue for these visits.
    for order in customer['Order']:

        # converting and storing customer revenue
        try:
            amount = float(order.total_amount.partition(" ")[0])
            total_amount += amount
        except ValueError:
            print("Amount is not in the expected format")

        # getting first
        if first_order > order.event_time:
            first_order = order.event_time


        #  count of site visits
        site_visits += 1

    # calculating average customer value and visits per week
    no_of_weeks = last_order.isocalendar()[1] - first_order.isocalendar()[1] + 1
    average_customer_value_per_visit = total_amount / site_visits
    visits_per_week = site_visits * 1.0/ no_of_weeks

    # calculating customer lifetime value
    customer_lifetime_value = 52* average_customer_value_per_visit * visits_per_week

    return customer_lifetime_value



def top_x_ltv(x,database):
    """

    :param x: No of Top customers to be calcualted.
    :param database: Database containing customer data.
    :return: Return top x customers.
    """

    # customer ltv list
    customer_ltv = namedtuple('customer_ltv','key ltv')
    customers_ltvs = []

    # computing LTV for each customer
    for key,customer in database.items():
        customers_ltvs.append(customer_ltv(key,compute_ltv(customer)))

    # sorting customers based on their ltv
    sorted_customer_ltv = sorted(customers_ltvs, key=lambda customer:customer.ltv, reverse=True)

    # Top X LTV customers
    top_x_customers = sorted_customer_ltv[:x]

    # Printing top x customers
    with open(output_file,'w') as f:
        for key,value in top_x_customers:
            customer = database.get_customer(key)
            f.write("customer_id : {}, customer_lastname = {}, customer value :${:.2f}\n".format(key , customer['Customer'].last_name.ljust(20), value))
            print(key , customer['Customer'].last_name, value)

    return top_x_customers

print(data)
# Computing top 10 customers.
top_x_ltv(10,data)