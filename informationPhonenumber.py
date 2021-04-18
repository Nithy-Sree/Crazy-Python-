#pip install phonenumbers

import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# phone_number = input("Enter your number with country code: ").strip()
phone_number = '+918637695440'
phone_num = phonenumbers.parse(phone_number)

print(phone_num)

# used to print the place where phone number is registered
print(geocoder.description_for_number(phone_num, 'en'))

# print the service provider
print(carrier.name_for_number(phone_num, 'en'))

# print the timezone which it follows
print(timezone.time_zones_for_number(phone_num))
