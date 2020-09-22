# https://www.geeksforgeeks.org/quick-sort/

class QuickSort:
    def partition(self, A, low, high):
        pivot = A[high]
        i = low - 1
        for j in range(low, high):
            if A[j] < pivot:
                i += 1
                A[i], A[j] = A[j], A[i]

        A[i+1], A[high] = A[high], A[i+1]
        return i+1

    def sorting(self, A,low, high):
        if low < high:
            pi = self.partition(A, low, high)
            self.sorting(A, low, pi-1)
            self.sorting(A, pi+1, high)
        return A


if __name__ == "__main__":
    A = [38,27,43,3,9,82,10]
    # A = [1,20,6,4]
    obj = QuickSort()
    print(obj.sorting(A,0,len(A)-1))
