#Concatenate two lists index-wise

list_1 = ['rashed:', 'Dir:']
list_2 = ['rion', 'khan']
list_3 = [i + j  for i, j  in zip(list_1, list_2)]

print(list_3)