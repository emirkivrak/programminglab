import random
def olustur(m:int,n:int):
    my_list=[]
    for i in range(m):
        my_list.append([])
        for j in range(n):
            #s = random.randint(0,10)
            s = -1
            my_list[i].append(s)
    return my_list

def my_function_convert(my_list):
    my_dict={}
    m= len(my_list)
    n= len(my_list[0])

    for i in range(m):
        for j in range(n):
            my_dict[(i,j)] = my_list[i][j]
    return my_dict

def my_function_print_hash(myHashList):
    print("  ")
    for key in myHashList:
        print(myHashList[key],end=" ")

print(my_function_print_hash(my_function_convert(olustur(5,5))))

## hash yapısı ile gösterilen matrislere ait toplama çıkarma çarpma işlemlerini yapan fonk yazının
