class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        top=-1  #last element of the array always   
        for ops in operations:
            if ops=='+':
                stack.append(stack[top]+stack[top-1])

            elif ops=='D':
                stack.append(2*stack[top])
            
            elif ops=='C':
                stack.pop()

            else:
                stack.append(int(ops))

        return sum(stack)