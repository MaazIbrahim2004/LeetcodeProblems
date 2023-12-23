class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]] # res is every  row, with 1st row being 1

        for i in range(numRows - 1): # -1 as added bc already
            temp = [0] + res[-1] + [0] #builds new temp array w/2p
            row = [] # next row
            for j in range(len(res[-1]) + 1): # r2, this is 2
                # this loops builds next row
                # length of this row is length of previous row + 1
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res