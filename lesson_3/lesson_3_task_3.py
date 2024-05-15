from address import Address
from mailing import Mailing

to_address = Address(83283, "Москва", "Мира", "10А", 93)
from_address = Address(12100, "Сочи", "Мира", "84", 7)

delivery_1 = Mailing(to_address, from_address, 8102.17, "DE2332HDJ01048MS")
print(f"Отправление {delivery_1.track} из {delivery_1.from_address.postcode}, {delivery_1.from_address.city}, {delivery_1.from_address.street}, {delivery_1.from_address.building} - {delivery_1.from_address.apartment} в {delivery_1.to_address.postcode}, {delivery_1.to_address.city}, {delivery_1.to_address.street}, {delivery_1.to_address.building} - {delivery_1.to_address.apartment}. Стоимость {delivery_1.cost} рублей")
