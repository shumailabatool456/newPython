
import math
def paint_calc(height, width, cover):
   area = height * width
   number_of_cans = math.ceil(area/cover)
   print(f"You will need {number_of_cans} number of cans.")
  
test_h = int(input("Enter height of the wall: "))
test_w = int(input("Enter width of the wall: "))
coverage = 5
paint_calc(height= test_h, width = test_w, cover = coverage )
