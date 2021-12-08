from mess import message
# Food List 
food = ["Wings","Cookies","Spring Rolls",
"Salmon","Steak","Meat Tornado","A Literal Garden","Ice Cream", "Cake","Pie",
"Coffee", "Tea","Unicorn Tears"]


print(message)
order_list = []
def ordering_food () :
    order = input("> ")
    print(order_list)
#    If statement to determine if food is in food list
    if order in food:
        order_list.append(order)
        cnt = order_list.count(order)
        for y in order_list:
            if cnt > 1:
                print(f'**{cnt} order of {order} have been added to your meal**')
                ordering_food()
            else:
                print(f'**{cnt} order of {order} have been added to your meal**')
                ordering_food()
    elif order == 'quit':
        cnt = order_list.count(order)
        print('Your Order:')
        for item in order_list:
            print(f'**{item}**')
        quit()

        
    else:
        print('**Please select something from the menu above**')
        ordering_food()
        

ordering_food()