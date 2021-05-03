from flask import Flask
from mailchimp3 import MailChimp


# Getting api key
api_key = None
# Getting the movie base url
list_id = None

def configure_request(app):
    global api_key, list_id
    api_key = app.config['MAILCHIMP_API_KEY']
    list_id = app.config['MAILCHIMP_AUD_ID']



print("Here", api_key, list_id)
# print(client.lists.members.all(list_id, get_all=True, fields="members.email_address,members.id"))

# response = mailchimp.ping.get()
# print(response)

# client = MailChimp(mc_api=api_key)

# client.lists.members.create(list_id, {
#     'email_address': 'wacumbugua@gmail.com',
#     'status': 'subscribed',
#     'merge_fields': {
#         'FNAME': 'Wacu',
#         'LNAME': 'Mbugua',
#     },
# })