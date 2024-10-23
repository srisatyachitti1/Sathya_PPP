import json
import colorsys
import random
import string
from faker import Faker
from datetime import datetime, timedelta, timezone


# Initialize the Faker object
fake = Faker()
makes = ["Toyota", "Ford", "Honda", "Chevrolet", "Nissan", "Volkswagen", "BMW", "Mercedes-Benz"]
models = ["Model S", "Focus", "Civic", "Impala", "Altima", "Passat", "3 Series", "C-Class"]
vehicle_color = ["red", "green", "blue", "yellow"]
vehicle_class = ["Sedan", "SUV", "Truck"]
comments_list = [
   "Please handle with care.",
   "This tag is for a new vehicle.",
   "Deliver as soon as possible.",
   "Customer prefers morning delivery.",
   "Verify the address before shipping.",
   "Ensure the tag is properly affixed.",
   "Contact customer if any issues arise.",
   "Include a tracking number with the delivery.",
   "Confirm delivery with the recipient.",
   "This is a rush order, prioritize it."
]
subfleet_options = ["RENTAL", "LEASE", "DEALERSHIP"]
rental_type_options = ["BILL_THE_CUSTOMER", "CUSTOMER_PAYS"]
item_type_options = ["STICKER_TAG", "LICENSE_PLATE_TAG", "HARD_CASE_TAG", "INTEGRATED"]
tag_type_options = ["STICKER", "MOUNTED"]
tag_delivery_method_options = [
   "HAND_TO_CUSTOMER",
   "MAIL_TO_CUSTOMER",
   "CUSTOMER_ALREADY_HAS_TRANSPONDER"
]
plate_types = ["COMMERCIAL", "PERSONAL", "ELECTRIC"]


def generate_fake_data():
   # Creating fake data for addresses and vehicle details
   email = fake.email()
   billing_address = fake.address()
   billing_city = fake.city()
   billing_state = fake.state()
   billing_zip_code = fake.zipcode()
   shipping_address = fake.address()
   shipping_city = fake.city()
   shipping_state = fake.state()
   shipping_zip_code = fake.zipcode()
   mailing_address = fake.address()
   mailing_city = fake.city()
   mailing_state = fake.state()
   mailing_zip_code = fake.zipcode()


   # Helper function to return the current datetime in ISO 8601 with Z (UTC)
   def iso8601_z_format(dt):
       return dt.replace(tzinfo=timezone.utc).isoformat().replace("+00:00", "Z")


   data = {
       "tenantId": 0,
       "tollingMethod": "TAG",
       "accountStartTimestamp": iso8601_z_format(datetime.now()),  # Z added for UTC
       "accountEndTimestamp": iso8601_z_format(datetime.now() + timedelta(days=365)),  # Z added for UTC
       "accountStartDate": datetime.date(datetime.today() + timedelta(days=2)).isoformat(),
       "accountEndDate": datetime.date(datetime.today() + timedelta(days=400)).isoformat(),
       "listOfVehicles": [
           {
               "vehicleReferenceId": 0,
               "tagReferenceId": 0,
               "videoReferenceId": 0,
               "tollingMethod": "TAG",
               "vehicleDetails": {
                   "hamRadioOperator": True,
                   "temporary": True,
                   "plateNumber": fake.license_plate(),
                   "plateState": fake.state(),
                   "plateCountry": fake.country(),
                   "plateType": random.choice(plate_types),
                   "domestic": True,
                   "yearOfRegistration": fake.year(),
                   "vehicleMake": random.choice(makes),
                   "vehicleModel": random.choice(models),
                   "vehicleColor": random.choice(vehicle_color),
                   "vehicleClass": random.choice(vehicle_class),
                   "plateRegistrationStartDate": datetime.date(datetime.today() + timedelta(days=60)).isoformat(),
                   "plateRegistrationEndDate": datetime.date(datetime.today() + timedelta(days=3500)).isoformat(),
                   "vehicleAccountActivationDate": datetime.date(datetime.today() + timedelta(days=2)).isoformat(),
                   "vehicleAccountEndDate": datetime.date(datetime.today() + timedelta(days=400)).isoformat(),
               }
           }
       ],
       "tagInfo": [
           {
               "tagReferenceId": 0,
               "hasTag": True,
               "tagAgencyId": "AGENCY_" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)),
               "tagId": "TAG_" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)),
               "item_type": random.choice(item_type_options),
               "tag_type": random.choice(tag_type_options),
               "mounting": "NO",
               "tag_delivery_method":  random.choice(tag_delivery_method_options),
               "tag_alias_name": fake.name(),
               "shippingAddress": fake.address(),
               "comments": random.choice(comments_list)
           }
       ],
       "videoInfo": [
           {
               "videoReferenceId": 0,
               "plateNumber": "PLATE_" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
           }
       ],
       "demographicInfo": {
           "accountType": "PERSONAL",
           "category": "REVENUE",
           "paymentModel": "PREPAID",
           "fleet": True,
           "subfleet": random.choice(subfleet_options),
           "rentalType": random.choice(rental_type_options),
           "visitor": True,
           "visitorStartDate": iso8601_z_format(datetime.now() + timedelta(days=-60)),
           "visitorEndDate": iso8601_z_format(datetime.now() + timedelta(days=3500)),
           "name": {
               "prefix": fake.prefix(),
               "firstName": fake.first_name(),
               "middleName": random.choice(string.ascii_uppercase),
               "lastName": fake.last_name(),
               "suffix": fake.suffix(),
           },
           "addressReferenceId": 0,
           "email": email,
           "confirmEmail": email,
           "alternateEmail": fake.email(),
           "mobileNumber": ''.join(filter(str.isdigit, fake.phone_number()))[:10],
           "phoneNumber": ''.join(filter(str.isdigit, fake.phone_number()))[:10],
           "companyName": fake.company(),
           "companyCode": ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
       },
       "addressDetails": {
           "addressReferenceId": 0,
           "billingAddress": [
               {
                   "country": fake.country(),
                   "address1": billing_address,
                   "address2": fake.secondary_address(),
                   "city": billing_city,
                   "state": billing_state,
                   "zipCode": billing_zip_code,
                   "isCurrentAddress": True,
                   "lastUpdatedDate": iso8601_z_format(datetime.now()+ timedelta(days=3000)),
               }
           ],
           "mailingAddress": [
               {
                   "country": fake.country(),
                   "address1": mailing_address,
                   "address2": fake.secondary_address(),
                   "city": mailing_city,
                   "state": mailing_state,
                   "zipCode": mailing_zip_code,
                   "isCurrentAddress": True,
                   "lastUpdatedDate": iso8601_z_format(datetime.now() + timedelta(days=3900)),
               }
           ],
           "shippingAddress": [
               {
                   "country": fake.country(),
                   "address1": shipping_address,
                   "address2": fake.secondary_address(),
                   "city": shipping_city,
                   "state": shipping_state,
                   "zipCode": shipping_zip_code,
                   "isCurrentAddress": True,
                   "lastUpdatedDate": iso8601_z_format(datetime.now() + timedelta(days=2000)),
               }
           ]
       },
       "paymentInfo": [
           {
               "cardId": fake.credit_card_number(),
               "paymentMethod": fake.credit_card_provider(),
               "cardAlias": fake.credit_card_number(),
           }
       ]
   }


   print(data)
   # Returning the JSON response
   return json.dumps(data, indent=4)




if __name__ == "__main__":
   fake_data_json = generate_fake_data()
   print(fake_data_json)

