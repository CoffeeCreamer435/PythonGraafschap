import random

items = ['fiets','kroeg','kreng','school','python','grens','friet']

item_to_show = random.choice(items)

print('op positie', items.index(item_to_show), 'staat het woord' , item_to_show)