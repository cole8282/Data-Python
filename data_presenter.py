from array import array


open_file = open("CupcakeInvoices.csv")


total_for_all = 0
total_for_strawberry = 0
total_for_chocolate = 0
total_for_vanilla = 0

# Loop through all the data and print each row.
# Loop through all the data and print the type of cupcakes purchased
# Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).
for line in open_file:
  print(line)
  array_line = line.split(',')
  typeof = array_line[2]
  print(typeof)
  individual_total = float(array_line[3]) * float(array_line[4])
  # See if you can implement one of them to display the total income of chocolate cupcakes vs vanilla cupcakes vs strawberry cupcakes.
  if typeof == 'Strawberry':
    total_for_strawberry += individual_total
  elif typeof == 'Chocolate':
    total_for_chocolate += individual_total
  elif typeof == 'Vanilla':
    total_for_vanilla += individual_total
  print(individual_total)
  total_for_all += individual_total
# Loop through all the data, and print out the total for all invoices combined.
print(total_for_all)
print('Strawberry Cupcake total income: ' + str(total_for_strawberry))
print('Chocolate Cupcake total income: ' + str(total_for_chocolate))
print('Vanilla Cupcake total income: ' + str(total_for_vanilla))

open_file.close











