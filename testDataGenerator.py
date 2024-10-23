import json
import random
from faker import Faker
from faker.contrib.pytest.plugin import faker

ID = {"PA1": "Personal_Revenue_Prepaid_Non_visitor", "PA2": "Personal_Revenue_Prepaid_Visitor",
          "PA3": "Personal_Non Revenue_Postpaid_Non_visitor", }

DOA = {
    "Personal_Revenue_Prepaid_Non_visitor": {"accountType": "PERSONAL",
                                            "category": "REVENUE",
                                            "paymentModel": "PREPAID",
                                            "visitor": False, },

    "Personal_Revenue_Prepaid_Visitor": {"accountType": "PERSONAL",
                                         "category": "REVENUE",
                                         "paymentModel": "PREPAID",
                                         "visitor": True, },

    "Personal_Non Revenue_Postpaid_Non_visitor": {"accountType": "PERSONAL",
                                                 "category": "NON_REVENUE",
                                                 "paymentModel": "POSTPAID",
                                                 "visitor": False, },
}

TENANT_ID = "10102020"

class FakeDataGenerator:
    fake = Faker()
    def __init__(self,doa_key=""):
        if doa_key =="":
            self.doa_key = random.choice(list(ID.keys()))
            print("Generating test data for DOA ID (random) is :",self.doa_key)
            self.doa_id = ID.get(self.doa_key)
            print("Generating test data for DOA ID (random) is :", self.doa_id)
            self.doa_data = DOA.get(self.doa_id)
            print("Generating test data for DOA Data (random) is :", self.doa_data)

        else:
            print("Generating test data for DOA ID is :",doa_key)
            self.doa_id = ID.get(doa_key)
            print("Generating test data for DOA ID is :",self.doa_id)
            self.doa_data = DOA.get(self.doa_id)
            print("Generating test data for DOA Data is :", self.doa_data)


    def get_address(self):
        return { "country": self.fake.country(),
                "address1": self.fake.street_address(),
                "address2": self.fake.street_name(),
                "city": self.fake.city(),
                "state": self.fake.city(),
                "zipCode": self.fake.zipcode(),
                "isCurrentAddress": random.choice([True,False])
                }

    @property
    def generate_vehicle_info(self):
        vehicles = ["Car", "Truck", "Motorcycle", "Bicycle", "Bus"]
        makes = ["Toyota", "Ford", "BMW", "Honda", "Tesla"]
        colors = ["Red", "Blue", "Green", "Black", "White"]
        return {
            "type": random.choice(vehicles),
            "make": random.choice(makes),
            "model": "Model " + str(random.randint(1, 100)),
            "color": random.choice(colors),
            "license_plate": "{}-{}-{}".format(chr(random.randint(65, 90)), random.randint(1000, 9999),
                                               chr(random.randint(65, 90)))
        }

    @property
    def generate_toll_info(self):
        locations = ["Highway 1", "Bridge A", "Tunnel 5", "Toll Plaza 3"]
        return {
            "location": random.choice(locations),
            "amount": round(random.uniform(1.0, 50.0), 2),
            "date": "2023-10-{} {}:{}:{}".format(random.randint(1, 31), random.randint(0, 23), random.randint(0, 59),
                                                 random.randint(0, 59))
        }

    @property
    def generate_demographic_info(self):
        email = self.fake.email()
        if "PERSONAL" in self.doa_data.get("accountType"):
            demographic = {
                "name": {
                    "prefix": self.fake.prefix(),
                    "firstName": self.fake.first_name(),
                    "middleName": self.fake.name().split(" ")[0],
                    "lastName": self.fake.last_name(),
                    "suffix": self.fake.suffix()
                },
                "addressReferenceId": 0,
                "email": email,
                "confirmEmail": email,
                "alternateEmail": self.fake.email(),
                "mobileNumber": self.fake.phone_number(),
                "phoneNumber": self.fake.phone_number(),
                "companyName": self.fake.company(),
                "companyCode": self.fake.random_number(5)
            }
        else:
            demographic = {
    "accountType": "BUSINESS",
    "category": "REVENUE",
    "paymentModel": "PREPAID",
    "fleet": True,
    "subfleet": "DEALERSHIP",
    "rentalType": "CUSTOMER_PAYS",
    "visitor": True,
    "visitorStartDate": "2024-10-07T09:16:29.658Z",
    "visitorEndDate": "2024-10-07T09:16:29.658Z",
    "name": {
      "prefix": "MR.",
      "firstName": "Rock",
      "middleName": "M",
      "lastName": "Forever",
      "suffix": "Sr"
    },
    "addressReferenceId": 0,
    "email": "whatever@gmail.com",
    "confirmEmail": "whatever@gmail.com",
    "alternateEmail": "whatever12@gmail.com",
    "mobileNumber": "9182455417",
    "phoneNumber": "string",
    "companyName": "ROCKER",
    "companyCode": "9090"
  }
        return self.doa_data|demographic

    @property
    def generate_payment_card_info(self):
        card_types = ["CREDIT", "DEBIT"]
        return {

            "cardId": "{}{}{}{}".format(random.randint(1000, 9999), random.randint(1000, 9999),
                                             random.randint(1000, 9999), random.randint(1000, 9999)),
            "paymentMethod": random.choice(card_types),
            "cardAlias": " ".join(self.fake.words())
        }

    @property
    def address_details(self):
        return {"addressReferenceId": 0,
    "billingAddress": [ self.get_address() ],
    "mailingAddress": [ self.get_address() ],
    "shippingAddress": [ self.get_address() ] }

    def generate_all_data(self):
        data = {
            #"vehicle_info": self.generate_vehicle_info,
           # "toll_info": self.generate_toll_info,
            "tenantId": TENANT_ID,
            "demographicInfo": self.generate_demographic_info,
            "addressDetails": self.address_details,
            "paymentInfo": [self.generate_payment_card_info,self.generate_payment_card_info]
        }
        return json.dumps(data, indent=4)

if __name__ == "__main__":
    testdata_1 = FakeDataGenerator("PA1")
    print(testdata_1.generate_all_data())
    testdata_2 = FakeDataGenerator()
    print(testdata_2.generate_all_data())
    testdata_3 = FakeDataGenerator()
    print(testdata_3.generate_all_data())