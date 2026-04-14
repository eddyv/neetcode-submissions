class Solution:

    # integer: record a new score
    # +: Record a new score that is the sum of the previous two scores.
    # D: Record a new score that is the double of the previous score.
    # C: Invalidate the previous score, removing it from the record.
    # Return the sum of all the scores on the record after applying all the operations.
    def calPoints(self, operations: List[str]) -> int:
        # ["1","2","+","C","5","D"]
        records = []
        result = 0
        for operation in operations:
            if operation == '+':
                records.append(records[-1] + records[-2])
            elif operation == 'D':
                records.append(records[-1] * 2)
            elif operation == 'C':
                records.pop()
            else:
                print(f"adding digit: {operation}")
                records.append(int(operation))
        print(records)
        result = sum(records)
        return result
                
        