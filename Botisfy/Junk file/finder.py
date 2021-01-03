import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
number = "+2510939167494"

my_number = phonenumbers.parse(number, "CH")
name = geocoder.description_for_number(my_number, "en")
print(name)

service_provider = phonenumbers.parse(number, "RO")
service = carrier.name_for_number(service_provider,"en")

print(service)
