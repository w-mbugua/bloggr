from . import create_app
from .models import Subscription

subbies = Subscription.query.all()

print(subbies)