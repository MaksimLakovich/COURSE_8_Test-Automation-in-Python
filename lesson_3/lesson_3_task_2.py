from smartphone import Smartphone

catalog = []
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79123456789"))
catalog.append(Smartphone("Apple", "iPhone 12", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Redmi 10", "+79345678901"))
catalog.append(Smartphone("Huawei", "P40 Pro", "+79456789012"))
catalog.append(Smartphone("Samsung", "Galaxy A32", "+79567890123"))

for user in catalog:
    print(f"{user.phone_brand} - {user.phone_model}. {user.subscriber_number}")