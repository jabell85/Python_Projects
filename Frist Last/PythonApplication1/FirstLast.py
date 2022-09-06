
def first_last_same(numberlist):
        print("Given List:", numberlist)

        first_num = numberlist[0]
        last_num = numberlist[-1]

        if first_num == last_num:
          return True;
        else:
          return False;

numbers_x = [5, 10 , 25, 20, 10 ]
print("result is", first_last_same(numbers_x))

numbers_y = [30, 60, 70, 80, 35]
print("result is", first_last_same(numbers_y))

