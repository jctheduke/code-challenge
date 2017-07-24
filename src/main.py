from src import DataStructure
import json

with open(r'C:\Users\priyaranjanjc\Desktop\code-challenge\input\input.txt') as f:
    input_data = json.load(f)

data = DataStructure.DataStructure()

def ingest(event,database):

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

for event in input_data:
    ingest(event,data)

def top_x_ltv(x,database):
    