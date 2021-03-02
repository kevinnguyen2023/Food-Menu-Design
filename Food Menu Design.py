data = []
result = None

menuList = ['Category', 'Item', 'Serving Size', 'Calories', 'Calories from fat', 'Total Fats', 'Cholesterol', 'Sodium', 'Carbohydrates', 'Protein', 'Quit']

def printMenu():
  for count in range(len(menuList)):
    print(count+1, '\t', menuList[count])
    
  
  choice = input('Enter the value between 1 and 11:')

  while type(choice) == str:
    try:
      choice = int(choice)
      if choice < 1 or choice > 11:
        print('ERROR: You did not enter a number between 1 and 11')
        return printMenu()
      elif choice == 11:
        exit()
      else:
        return choice
    except ValueError:
      print('ERROR: You did not enter a number')
      return printMenu()


def processInput(passedVal):
  print(value, ":", menuList[value-1])
  sortData = sorted(data, key = lambda r:(int(r[passedVal])), reverse = True)
  print('Top 5 Items based on', menuList[value-1])
  count = 0
  for count in range (0,5):
    print('     {}| {}  {}'. format(count+1, sortData[count][1], sortData[count][passedVal]))
  input('Hit the Enter key to continue')


fh = open('Mac_menu.csv.txt', 'r')
fh.readline()

for line in fh:
  line = line.rstrip('\n')
  line = line.replace('"', '', 6)
  line = line.rsplit(',')
  result = tuple(line)
  data.append(result)

# The file Mac_Menu.csv must be uploaded to the same folder in order to open the file

fh.close()

print(data)


value = printMenu()
print('The user entered:', value)
Function = processInput(value) 
