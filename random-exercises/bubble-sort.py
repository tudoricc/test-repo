



def sort(array=[12,4,5,6,7,3,1,15]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[len(array)-1]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        less_sorted = sort(less)
        greater_sorted = sort(greater)
        return less_sorted + equal + greater_sorted
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array
def mergeSort(alist=[5 ,4,1,3,2,1]):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            print i
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

def mergesort(array=[5,4,1,3,2,1]):
    #Merging halves over and over again
    if len(array) > 1:
        mid_point = len(array) /2
        first_half = array[:mid_point]
        second_half = array[mid_point:]
        k = 0
        while i < len(first_half) and  j < len(second_half):
            if first_half[i] > second_half[j] :
                array[k] = first_half[i]
                i = i+1
            else:
                array[k] = second_half[j]
                j = j +1
            k = k + 1
        # while i < len(first_half):
        #     array[k] = first_half[i]
        #     k = k + 1
        # while j < len(first_half):
        #     array[k] = first_half[j]
        #     k = k + 1
def main():
    # my code here
    input_list = raw_input(" PLease enter your input list: ")

    input_string = input_list.split(" ")
    list_to_be_sorted = []
    for member in input_string:
        list_to_be_sorted.append(int(member))
    list_to_be_sorted_quick_sort = list_to_be_sorted
    passnumb = 0
    for passnumb in range(len(list_to_be_sorted)-1,0,-1):
        for i in range(passnumb):
            if list_to_be_sorted[i] > list_to_be_sorted[i+1]:
                temporary_value = list_to_be_sorted[i]
                list_to_be_sorted[i] = list_to_be_sorted[i+1]
                list_to_be_sorted[i+1] = temporary_value


    print("The list sorted by Bubble is {}".format(list_to_be_sorted))

    array = sort()
    mergeSort()
    print array

if __name__ == "__main__":
    main()
