import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in sentence:
		if i == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse():

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	
		#print_items(self.items)

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)
		pass

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		max_stock = 0
		max_stock_items = None
		#loop thru
		for items in self.items:
			if items.stock > max_stock:
				max_stock = items.stock
				max_stack_items= items
		return max_stock_items
		
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		max_price = 0
		max_price_items = None
		#loop thru
		for items in self.items:
			if items.price > max_price:
				max_price = items.price
				max_price_items= items
		return max_price_items	




# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		test_counta = count_a('Obiari')
		self.assertEqual(test_counta,1)
		#for i in str(sentence):
			#if i.lower == 'a':

		#print(f"Testing count_a('Obiari') should retun 1 and returns {count_a('Obiari')}")


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		wharehouse1 = Warehouse() #create a new object
		wharehouse1.add_item(self.item1)
		wharehouse1.add_item(self.item2)
		wharehouse1.add_item(self.item3)

		self.assertEqual(wharehouse1.items, [self.item1, self.item2, self.item3])

		wharehouse1.add_item(self.item4)

		self.assertEqual(wharehouse1.items, [self.item1, self.item2, self.item3, self.item4])

		#print(f"Testing add_item(self.item, self.item1) should retun ('Beer', 6, 20) and returns {add_item(self.item, self.item1)}")


	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		#self.item1 = Item("Beer", 6, 20)
		#self.item2 = Item("Cider", 5, 25)
		#self.item3 = Item("Water", 1, 100)
		#self.item4 = Item("Fanta", 2, 60)
		#self.item5 = Item("CocaCola", 3, 40)
		warehouse1 = Warehouse([self.item1, self.item2])
		max_item = warehouse1.get_max_stock()
		self.assertEqual(max_item, self.item2)

		warehouse1.add_item(self.item3)
		max_item = warehouse1.get_max_stock()

		self.assertEqual(max_item, self.item3)

		#print(f"Testing warehouse_max_stocks(,) should retun - and returns {warehouse_max_stocks()}")



	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		warehouse1 = Warehouse([self.item1, self.item2])
		max_item = warehouse1.get_max_price()
		self.assertEqual(max_item, self, self.item2)

		warehouse1.add_item(self.item3)
		max_item = warehouse1.get_max_price()

		self.assertEqual()

		#print(f"Testing warehouse_max_price(,) should retun - and returns {warehouse_max_stock()}")
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()