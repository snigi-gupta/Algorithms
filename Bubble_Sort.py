# https://www.geeksforgeeks.org/bubble-sort/
class BubbleSort:

    # O(n^2)
    """
    When i=1 then last element is in highest ordered.
    When i=2 then last two elements are in highest order. Hence loop count can be reduced to n-i-1
    """
    def sorting(self, A):
        for i in range(0, len(A)):
            swapped = False
            for j in range(0, len(A)-i-1):
                if A[j] > A[j+1]:
                    A[j], A[j+1] = A[j+1], A[j]
                    swapped = True
            if not swapped:
                break

        return A


if __name__ == "__main__":
    A = [38,27,43,3,9,82,10]
    # A = [1,20,6,4]
    obj = BubbleSort()
    print(obj.sorting(A))