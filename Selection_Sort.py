class Selection:
    def sorting(self, A):
        # O(n^2)
        for i in range(0, len(A)):
            min_val = min(A[i:])
            min_index = A.index(min_val)
            A[min_index] = A[i]
            A[i] = min_val
        return A


if __name__ == "__main__":
    A = [38,27,43,3,9,82,10]

    obj = Selection()
    print(obj.sorting(A))