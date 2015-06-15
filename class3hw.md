'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the data with csv.reader() and store it in a list of lists called 'data'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
https://docs.python.org/2/library/csv.html
'''

```with open('chipotle.tsv', 'rU') as tsv:
data = [row for row in tsv] ```


BASIC LEVEL
PART 2: Separate the header and data into two different lists.

``` header = data[0]
data = data[1:] ```


'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''

orders = len(set([row[0] for row in data]))
orderprice=[float(row[4][1:-1] for row in data)] #This does not allow me to convert string to float
sum(orderprice/orders) # was not able to reach this point

'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''
# did not work.. I think I was close but not sure what I'm missing
sodas = []
for row in data:
if row[2] == 'Canned Soda' or row[2] == 'Canned Soft Drink':
sodas.append(data(row[2]))

sodas2 = set(sodas)

'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''



'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''



'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''