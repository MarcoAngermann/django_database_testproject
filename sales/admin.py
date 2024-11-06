from django.contrib import admin
from .models import Customer
from .models import Order
from .models import Product
from .models import ProductType
from .models import Bill

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_filter = ['first_name', 'last_name', 'newsletter_abo', 'email_address', 'account']
    list_display = ['first_name', 'last_name', 'newsletter_abo', 'email_address', 'account']
    #readonly_fields = ['account'] #Beispiel wenn man nur ein Feld lesen soll

    fieldsets = [
        (
            None,
            {
                "fields": ["first_name", "last_name","account"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["newsletter_abo"],
            },
        ),
    ]



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(Bill)