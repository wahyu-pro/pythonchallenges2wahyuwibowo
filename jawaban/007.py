import datetime, operator
data = [
    {
        "order_id": "SO-921",
        "created_at": "2018-02-17T03:24:12",
        "customer": { "id": 33, "name": "Ari" },
        "items": [
        { "id": 24, "name": "Sapu Lidi", "qty": 2, "price": 13200 }, 
        { "id": 73, "name": "Sprei 160x200 polos", "qty": 1, "price": 149000 }
        ]
    },
    {
        "order_id": "SO-922",
        "created_at": "2018-02-20T13:10:32",
        "customer": { "id": 40, "name": "Ririn" },
        "items": [
        { "id": 83, "name": "Rice Cooker", "qty": 1, "price": 258000 },
        { "id": 24, "name": "Sapu Lidi", "qty": 1, "price": 13200 }, 
        { "id": 30, "name": "Teflon", "qty": 1, "price": 190000 }
        ]
    },
    {
        "order_id": "SO-923",
        "created_at": "2018-02-28T15:20:43",
        "customer": { "id": 33, "name": "Ari" },
        "items": [
        { "id": 303, "name": "Pematik Api", "qty": 1, "price": 12000 }, 
        { "id": 49, "name": "Panci", "qty": 2, "price": 70000 }
        ]
    },
    {
        "order_id": "SO-924",
        "created_at": "2018-03-02T14:30:54",
        "customer": { "id": 40, "name": "Ririn" },
        "items": [
        { "id": 986, "name": "TV LCD 40 inch", "qty": 1, "price": 6000000 }
        ]
    },
    {
        "order_id": "SO-925",
        "created_at": "2018-03-03T14:52:22",
        "customer": { "id": 33, "name": "Ari" },
        "items": [
        { "id": 1033, "name": "Nintendo Switch", "qty": 1, "price": 4990000 }, 
        { "id": 2003, "name": "Macbook Air 11 inch 128 GB", "qty": 1, "price": 12000000 },
        { "id": 23, "name": "Pocari Sweat 600ML", "qty": 5, "price": 7000 }
        ]
    },
    {
        "order_id": "SO-926",
        "created_at": "2018-03-05T16:23:20",
        "customer": { "id": 58, "name": "Annis" },
        "items": [
        { "id": 24, "name": "Sapu Lidi", "qty": 3, "price": 13200 }
        ]
    }
]
def find_all_purchases_in_february(data, month):
    print("Existing purchases in February")
    for i in data:
        date_str = i['created_at']
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
        date = date_obj.month
        if date == month:
            id = i['order_id']
            createdAt = i['created_at']
            customer = i['customer']['name']
            item = i['items']

            print(id,createdAt,customer,item)

def find_all_purchases_by_ari(name, data):
    grandTotal = 0
    for i in data:
        customer = i['customer']['name']
        items = i['items']
        if customer == name:
            for item in items:
                itemName = item['name']
                qty = item['qty']
                price = item['price']
                totalPriceItems = qty * price
                print(itemName, qty, price, "Total harga adalah: ", totalPriceItems)
                grandTotal += totalPriceItems

    print("Grand Total = ", grandTotal)


# def find_people_300000(data, minimal = 300000):
#     grandTotal = 0
#     for i in data:
#         customer = i['customer']['name']
#         items = i['items']
#         if customer in data:
#             for x in data:
#             for item in items:
#                 qty = item['qty']
#                 price = item['price']
#                 totalPriceItems = qty * price
#                 print(itemName, qty, price, "Total harga adalah: ", totalPriceItems)
#         print(customer)
#     print(grandTotal)



find_all_purchases_in_february(data, 2)
print("\n")
find_all_purchases_by_ari("Ari", data)
# find_people_300000(data)