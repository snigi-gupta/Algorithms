# Merge sort O(nlogn)

class MergeSort:
    def sort_list(self, left, right):
        sorted = []
        lstart = rstart = 0
        target_len = len(left) + len(right)
        if len(left) == 0:
            return right
        if len(right) == 0:
            return left
        while len(sorted) < target_len:
            if left <= right:
                sorted.append(left[lstart])
                lstart += 1
            else:
                sorted.append(right[rstart])
                rstart += 1

            if lstart == len(left):
                sorted.extend(right[rstart:])
                break
            if rstart == len(right):
                sorted.extend(left[lstart:])
                break
        return sorted

    def split_list(self, input):
        split_point = len(input)//2
        return input[:split_point], input[split_point:]
    def merge(self, input):
        if len(input) <= 1:
            return input
        left, right = self.split_list(input)
        left = self.merge(left)
        right = self.merge(right)
        merged_list = self.sort_list(left,right)
        return  merged_list

if __name__ == "__main__":
    unsorted = [38,27,43,3,9,82,10]
    obj = MergeSort()
    print(obj.merge(unsorted))