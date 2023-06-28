def bubbleSort(my_list):
    number = len(my_list)
    swapped = False

    for i in range(number - 1):                      #vising the each element in the list

        for j in range(0, number - i - 1):           #placing the last element i in place 

            if my_list[j] > my_list[j + 1]:          #swap if its greater that next element in list
                swapped = True
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                
        if not swapped:
            return
    
my_list = [2, 4, 6, 33, 5, 12, 77, 35]              #declaring the sorting list
bubbleSort(my_list)

for i in range (len(my_list)):                        #loop through the element in my list
    print("% d" % my_list[i], end=" ")                #display element in sorted order with gap in it