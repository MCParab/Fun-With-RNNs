#Python list implementations 

grocery_list=['juice','Tomatoes','Potatoes',"Bananas"];

print("First item : ",grocery_list[0]); ##First item :  juice

grocery_list[0]='Green Juice';

print(grocery_list[0:3]);  ##['Green Juice', 'Tomatoes', 'Potatoes']


other_events=['Wash car','Pick Veg','Cash Check'];

to_do_list=[other_events,grocery_list];

print(to_do_list[1][1]); ##Tomatoes


grocery_list.append('Onions');

grocery_list.remove('Potatoes');

print(grocery_list[0:5]); ##['Green Juice', 'Tomatoes', 'Bananas', 'Onions']

grocery_list.sort();

print(grocery_list[0:5]); ##['Bananas', 'Green Juice', 'Onions', 'Tomatoes']

grocery_list.reverse();

print(grocery_list[0:5]); ##['Tomatoes', 'Onions', 'Green Juice', 'Bananas']

print(len(grocery_list)); ##4

del(grocery_list[3]);

print(grocery_list[0:2]); ##['Tomatoes', 'Onions']


num_list=[2,3,4,5,6];

print(max(num_list)); ##6

print(min(num_list)); ##2


      






