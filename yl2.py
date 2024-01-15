import math
while True:

    radius = float(input('sisesta raadiuse arvu: '))

    square = radius * radius * math.pi

    perimeter = math.pi * radius * 2

    print("Ringi pindala on" , square,"\nümbermõõt on", perimeter)