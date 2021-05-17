import phonenumbers
from phonenumbers import geocoder, carrier, timezone

user_number = input("Enter your phone number: ")
phone_number = phonenumbers.parse(user_number)

# check if number is valid or not
valid = phonenumbers.is_valid_number(phone_number)

# check is number possible or not.
possible = phonenumbers.is_possible_number(phone_number)
print(f" Number valid :{valid}")
print(f"Number possible:{possible}")

print(geocoder.description_for_number(phone_number, "en"))

print(carrier.name_for_number(phone_number, "en"))

print(timezone.time_zones_for_number(phone_number))

# print(phonenumbers.PhoneMetadata.load_all())
