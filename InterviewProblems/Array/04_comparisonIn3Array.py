
def do_comparison(arr1, arr2, arr3):
    
    p1 = p2 = p3 = 0

    while(p1<len(arr1) and p2<len(arr2) and p3<len(arr3)):

        if(arr1[p1]==arr2[p2]==arr3[p3]):
            return arr1[p1]

        if(arr1[p1]<=arr2[p2] and arr1[p1]<=arr3[p3]):
            p1 += 1
        
        elif(arr2[p2]<=arr1[p1] and arr2[p2]<=arr3[p3]):
            p2 += 1    
        
        elif(arr3[p3]<=arr1[p1] and arr3[p3]<=arr2[p2]):
            p3 += 1

    return "no match found"


print(do_comparison([5,6,7,20,30,54], [0,1,2,6,7,23,60,104], [3,4,6,20,25]))