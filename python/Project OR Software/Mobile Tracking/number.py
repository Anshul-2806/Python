import phonenumbers
from phonenumbers import timezone, geocoder, carrier
number = input("ENter your number with +91 :")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
carr = carrier.name_for_number(phone,"en")  #en uses for in english
reg = geocoder.description_for_number(phone,"en")

print(phone)
print(time)
print(carr)
print(reg)