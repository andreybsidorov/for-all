import json
from multiprocessing.resource_tracker import unregister

with open("data.json","r",encoding = "utf-8") as f:
    orders = json.load(f)
# 1.Какой номер самого дорого заказа за июль?
# 2.Какой номер заказа с самым большим количеством товаров?
# 3.В какой день в июле было сделано больше всего заказов?
# 4.Какой пользователь сделал самое большое количество заказов за июль?
# 5.У какого пользователя самая большая суммарная стоимость заказов за июль?
# 6.Какая средняя стоимость заказа была в июле?
# 7.Какая средняя стоимость товаров в июле?

max_price = 0
max_order = ''
max_price_orders_lis = []
for order_num, orders_data in orders.items():
    price = orders_data['price']
    if price > max_price:
        max_order = order_num
        max_price = price
for order_num, orders_data in orders.items():
    if max_price == orders_data['price']:
        max_price_orders_lis.append(max_order)
m_orders_num = ', '.join(max_price_orders_lis)

print(f'1. Номер(а) заказа(ов) с самой большой стоимостью: {m_orders_num}, стоимость заказа: {max_price}')

# №2
max_quantity = 0
max_lis_quantity = []
for orders_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        max_quantity = quantity
for orders_num, orders_data in orders.items():
    if max_quantity == orders_data['quantity']:
        max_lis_quantity.append(orders_num)
m_quantity = ', '.join(max_lis_quantity)


print(f'2. Номер(а) заказа(ов) с самым большим количеством товаров: {m_quantity}, самое большое количество товаров {max_quantity}')

# №3
max_q_date = ''
max_count = 0
dic_dates = {}
for orders_num, orders_data in orders.items():
    date = orders_data['date']
    if date not in dic_dates:
        dic_dates[date] = 0
    dic_dates[date] += 1

for date, count in dic_dates.items():
    if count > max_count:
        max_count = count
        max_q_date = date

print(f'3. {max_q_date} было сделано больше всего заказов {max_count} ')

# №4
count_by_user = {}
max_count = 0
for orders_num, orders_data in orders.items():
    user_id = orders_data['user_id']
    if user_id not in count_by_user:
        count_by_user[user_id] = 0
    count_by_user[user_id] += 1
for  user, count in count_by_user.items():
    if max_count < count:
        max_count = count
for user, count in count_by_user.items():
    if max_count == count:
        print(f'4. Пользователь {user} сделал наибольшее количество заказов {max_count} в июле ')

# №5
max_sum_orders = 0
sum_by_user = {}
for orders_num, orders_data in orders.items():
    user_id = orders_data['user_id']
    price = orders_data['price']
    if user_id not in sum_by_user:
        sum_by_user[user_id] = 0
    sum_by_user[user_id] += price

for user,summ in sum_by_user.items():
    if summ > max_sum_orders:
        max_sum_orders = summ
for user,summ in sum_by_user.items():
    if max_sum_orders == summ:
        print(f'5. У пользователя {user} самая большая суммарная стоимость заказов {max_sum_orders} в июле ')

# №6
count_orders = 0
sum_price = 0
for orders_num, orders_data in orders.items():
    price = orders_data['price']
    num_order = orders_num
    sum_price += price
    if num_order:
        count_orders += 1
avg_price_order = sum_price / count_orders
f_avg_price_order = f'{avg_price_order:.2f}'
print(f'6. Средняя стоимость заказа в июле составила: {f_avg_price_order}')

# №7
count_quantity = 0
total_sum_orders = 0
for orders_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    price = orders_data['price']
    count_quantity += quantity
    total_sum_orders += price
    avg_price_product = total_sum_orders / count_quantity
    f_avg_price_product = f'{avg_price_product:.2f}'
print(f'7. Средняя цена товара в июле составила: {f_avg_price_product}')

