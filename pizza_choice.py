# Esu siaip labai alkanas, tai parasiau programa apie pizza. Gali paredaguoti ja ir padaryt idomesne jeigu noresi.

pizza_toppings = ['anchovies', 'salami', 'cheese', 'mushroom']
requested_pizza = []

topping_num = 0
while True:
    u_inp = input('What kind of topping would you like? You can have a maximum of 3. '
                  'Press enter if you\'ve had enough. ')
    if not u_inp:
        break
    if u_inp.strip().lower() not in pizza_toppings:
        print('Sorry, we don\'t have that kind of topping.')
        continue
    if u_inp in requested_pizza:
        print('You\'ve already had that.')
        continue  # Gali prideti papildoma pasirinkima jeigu klientas nori dvigubini ar trigubini papilda.
    requested_pizza.append(u_inp)
    topping_num += 1
    if topping_num == 3:
        print('That\'s it. You\'ve reached 3 toppings.')
        break
if not requested_pizza:
    print('So you didn\'t want anything? Alright.')
else:
    print(f'Alright, your {", ".join(requested_pizza)} pizza is ready!')
