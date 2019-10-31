#Respuesta Juan Munoz

#import numpy as np

#1. Use a list comprehension to create and print a list of consecutive integers starting with 1 and ending with 50.

#Primero el bucle tradicional
list11 = []
for i in range(1,51):
    list11.append(i)
print(list11)

#Respuesta en list comprehensions
list12 = [(i+1) for i in range(50)]
print(list12)

#2. Use a list comprehension to create and print a list of even numbers starting with 2 and ending with 200.

#Primero el bucle tradicional
list21 = []
for i in range(1,101):
    list21.append(i*2)
print(list21)

#Respuesta en list comprehensions
list22 = [(i*2) for i in range(101) if i != 0]
print(list22)


#3. Use a list comprehension to create and print a list containing all elements of the 10 x 4 Numpy array below.

a = ([[0.84062117, 0.48006452, 0.7876326 , 0.77109654],
       [0.44409793, 0.09014516, 0.81835917, 0.87645456],
       [0.7066597 , 0.09610873, 0.41247947, 0.57433389],
       [0.29960807, 0.42315023, 0.34452557, 0.4751035 ],
       [0.17003563, 0.46843998, 0.92796258, 0.69814654],
       [0.41290051, 0.19561071, 0.16284783, 0.97016248],
       [0.71725408, 0.87702738, 0.31244595, 0.76615487],
       [0.20754036, 0.57871812, 0.07214068, 0.40356048],
       [0.12149553, 0.53222417, 0.9976855 , 0.12536346],
       [0.80930099, 0.50962849, 0.94555126, 0.33364763]])

#Primero el bucle tradicional
list31 = []
for i in a:
    for j in i:
        list31.append(j)
print(list31)

#Respuesta en list comprehensions
list32 = [j for i in a for j in i]
print(list32)

#4. Add a condition to the list comprehension above so that only values greater than or equal to 0.5 are printed.

#Primero el bucle tradicional
list41 = []
for i in a:
    for j in i:
        if j >= 0.5:
            list41.append(j)
print(list41)

#Respuesta en list comprehensions
list42 = [j for i in a for j in i if j >= 0.5]
print(list42)


#5. Use a list comprehension to create and print a list containing all elements of the 5 x 2 x 3 Numpy array below.

b = ([[[0.55867166, 0.06210792, 0.08147297],
        [0.82579068, 0.91512478, 0.06833034]],

       [[0.05440634, 0.65857693, 0.30296619],
        [0.06769833, 0.96031863, 0.51293743]],

       [[0.09143215, 0.71893382, 0.45850679],
        [0.58256464, 0.59005654, 0.56266457]],

       [[0.71600294, 0.87392666, 0.11434044],
        [0.8694668 , 0.65669313, 0.10708681]],

       [[0.07529684, 0.46470767, 0.47984544],
        [0.65368638, 0.14901286, 0.23760688]]])

#Primero el bucle tradicional
list51 = []
for i in b:
    for j in i:
        for x in j:
            list51.append(x)
print(list51)

#Respuesta en list comprehensions
list52 = [x for i in b for j in i for x in j]
print(list52)


#5. Add a condition to the list comprehension above so that the last value in each subarray is printed, but only if it is less than or equal to 0.5.

#Primero el bucle tradicional
list61 = []
for i in b:
    for j in i:
        for x in j:
            if x <= 0.5:
                list61.append(x)
print(list61)

#Respuesta en list comprehensions
list62 = [x for i in b for j in i for x in j if x <= 0.5]
print(list62)



#6. Use a list comprehension to select and print the names of all CSV files in the /data directory.

# I do not have the csv files

#7. Use a list comprehension and the Pandas read_csv and concat methods to read all CSV files in the /data directory and combine them into a single data frame. Display the top 10 rows of the resulting data frame.

#8. Use a list comprehension to select and print the column numbers for columns from the data set whose median is less than 0.48.


#9. Use a list comprehension to add a new column (20) to the data frame whose values are the values in column 19 minus 0.1. Display the top 10 rows of the resulting data frame.


#10. Use a list comprehension to extract and print all values from the data set that are between 0.7 and 0.75.¶
