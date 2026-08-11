class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result: List[List[int]] = []
        # range is exclusive at the end
        for row in range(0,numRows):
            rowVal: List[int] = []
            if row == 0:
                rowVal.append(1)
            elif row == 1:
                rowVal.append(1)
                rowVal.append(1)
            else:
                for col in range(0,row+1):
                    if col == 0:
                        rowVal.append(1)
                    elif col==row:
                        rowVal.append(1)
                    else:
                        sum=result[row-1][col-1]+result[row-1][col]
                        rowVal.append(sum)
            result.append(rowVal)
        return result


                

