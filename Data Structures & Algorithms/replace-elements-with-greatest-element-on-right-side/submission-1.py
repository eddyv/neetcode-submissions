class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # iterate through the array and keep track of the max number seen. 
        # use a pointer to keep track of the index where this max has started.
        # once a max is found we want to replace all the indexes up until the max # was reached.
        # 1 <= arr.length <= 10,000
        # 1 <= arr[i] <= 100,000
        array_size = len(arr);

        curr_max = arr[array_size-1];
        curr_index = array_size-1;
        arr[array_size-1]=-1
        
        while curr_index > 0:
            curr_index-=1
            new_max = -1
            if curr_max < arr[curr_index]:
                new_max = arr[curr_index]
            else:
                new_max = curr_max
            arr[curr_index] = curr_max
            curr_max = new_max
        
        return arr;
        