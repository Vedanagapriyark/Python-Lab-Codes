import numpy as np

data = np.array(list(map(float, input("Enter numbers: ").split())))
index = int(input("Enter index to access: "))

if 0 <= index < len(data):
    print("Element at index", index, ":", data[index])
else:
    print("Invalid index!")

print("Sorted:", np.sort(data))

OUTPUT:
Enter numbers: 56 43 89 6
Enter index to access: 2
Element at index 2 : 89.0
Sorted: [ 6. 43. 56. 89.]
