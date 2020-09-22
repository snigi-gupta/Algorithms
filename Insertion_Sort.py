# https://www.geeksforgeeks.org/insertion-sort/

class InsertionSort:

    # O(n^2)
    def sorting(self, A):
        for i in range(1, len(A)):
            unsorted_element = A[i]
            # print("A[{}] = {}".format(i,unsorted_element))
            j = i-1
            # print("j = {}".format(j))
            while unsorted_element < A[j] and j >= 0:
                A[j+1] = A[j]
                # print("A[{}] = A[{}]: {}".format(j+1, j, A))
                j -= 1
            A[j+1] = unsorted_element
            # print("A[{}] = {}".format(j+1, unsorted_element))
            # print("A", A)
        return A

if __name__ == "__main__":
    A = [38,27,43,3,9,82,10]
    obj = InsertionSort()
    print("Sorted", obj.sorting(A))