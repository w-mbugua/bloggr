from . import client

client.lists.members.create('d9d5f5d03f', {
    'email_address': 'john.doe@example.com',
    'status': 'subscribed',
    'merge_fields': {
        'FNAME': 'John',
        'LNAME': 'Doe',
    },
})
