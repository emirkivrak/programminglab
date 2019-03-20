class item(object):
    def __init__(self,name,value,weight,v_W):
        self.name = name
        self.value = value
        self.weight = weight
        self.v_w = v_W

def get_items():
    items = []
    items.append(item('clock', 175, 10, 17.5))
    items.append(item('painting', 90, 9, 10))
    items.append(item('radio', 20, 4, 5))
    items.append(item('vase', 50, 2, 25))
    items.append(item('book', 10, 1, 10))
    items.append(item('computer', 200, 20, 10))
    return items

def print_items():
    for item in items:
        print(item.name,item.value)
        #################
def sort_my_items(items):
    return sorted(items, key = lambda item:item.name ,reverse = True)

def test():
    items = get_items()
    print_items()
    print("------------Sorted items---------")
    items = sort_my_items(items)
    print(items)

def steal(items,max__weight):
    result=[]
    totalweight,totalvalue = 0,0
    for i in range(len(items)):
        if(items[i].weight + totalweight<=max__weight):
            result.append(items[i])
            totalweight = totalweight+item[i].weight
            totalvalue = totalvalue + items[i].value
    return (result, totalvalue)

item_1 = get_items()
item_2 = steal(item_1,20)


