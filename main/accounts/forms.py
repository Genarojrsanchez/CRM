from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta: 
        model = Order
        # you can use [] to list what you want in feilds we will be using all methods to call all options
        fields = '__all__'