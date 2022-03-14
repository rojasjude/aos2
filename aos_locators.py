from faker import Faker

fake = Faker(locale='en_CA')

# ------------------ locators section-------------------------------
app = 'Advantage Online Shopping'
aos_url = 'https://advantageonlineshopping.com/#/'
aos_home_page_title = ' Advantage Shopping'
aos_add_user = 'https://advantageonlineshopping.com/#/register'
aos_add_user_title = ' Advantage Shopping'

#------------------------Text--------------------------
speaker = f'Speaker'.upper()
tablets = f'Tablets'.upper()
laptop = f'Laptops'.upper()
mice = f'Mice'.upper()
headphone = f'Headphone'.upper()
#--------------------Nav Link-------------------------
special_offers = f'Special\ Offers'.upper()
popular_items = f'Popular Items'.upper()
contact_us = f'Contact Us'.upper()

# -------------------- Text ---------------------------------
speakers = f'Speakers'.upper()
tablets = f'Tablets'.upper()
laptops = f'Laptops'.upper()
mice = f'Mice'.upper()
headphones = f'Headphones'.upper()

# -------------------- Nav Link ---------------------------------
special_offers = f'Special Offers'.upper()
popular_items = f'Popular Items'.upper()
contact_us = f'Contact Us'.upper()

# -------------------- Messages ---------------------------------
messages = fake.text()

# -------------------- Buttons ---------------------------------
continue_shopping = f' CONTINUE SHOPPING '


# -------------------- data section ---------------------------------
firstname = fake.first_name()
lastname = fake.last_name()
phone = fake.phone_number()
username = f'{firstname}{lastname}'.lower()[:10]
password = fake.password()
confirm_password = f'{password}'
email = fake.email()
country = fake.current_country()
city = fake.city()
address = fake.street_address()
province = fake.province_abbr()
postcode = fake.postcode()

print(firstname, lastname, phone, username, password, email)
