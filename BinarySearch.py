def binryserch(arr1, val):

    start = 0
    end = len(arr1)
    middle = int((start+end)/2)


    print(middle)

    while arr1[middle] != val:
        if arr1[middle] < val:
            start = middle+1
        else:
            end = middle-1
        middle = int((start + end) / 2)
        print(middle)

    if arr1[middle] == val:
            print("the value" + " " + str(arr1[middle]) + " " + " is at index" + " " + str(middle))





binryserch([2,3,5,6,55,78,79,89,787],89)


