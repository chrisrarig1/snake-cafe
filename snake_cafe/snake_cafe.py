from mess import message

food = ["Wings","Cookies","Spring Rolls",
"Salmon","Steak","Meat Tornado","A Literal Garden","Ice Cream", "Cake","Pie",
"Coffee", "Tea","Unicorn Tears"]


print(message)
def ordering_food () :
    order = input("> ")
    order_list = []
    while order != 'quit':
        if order in food:
            order_list.append(order)
            cnt = order_list.count(order)
            for y in order_list:
                print(order_list)
                print(f'**{cnt} order of {y} have been added to your meal**')
            order = input("> ")
        elif order == 'quit':
            break
        else:
            print('**Please select something from the menu above**')
ordering_food()