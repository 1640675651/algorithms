# For every element i in a list (height), find the first element that is less than element i to its left and right in O(n).
from collections import deque
heights = list(map(int, input().split()))
firstlowerleft = [-1] * len(heights)
firstlowerright = [len(heights)] * len(heights)
stack = deque()
stack.append(0)
# use a stack to keep track of an increasing sequence. 
# for height[i], pop all stack element that have higher height than column i and make i the top of the stack. 
# We want to compute the column that is lower than column i with the greatest index (firstlowerleft), all the columns that are higher than column i and to the left of column i can be ignored (popped out from the stack) since column i will be a better candidate than them.
# In worst case, each i can be pushed into stack and popped from stack once. The time complexity is O(n).
for i in range(1, len(heights), 1):
    top = stack.pop()
    while heights[top] >= heights[i]:
        if len(stack) == 0:
            top = -1
            break
        top = stack.pop()
    firstlowerleft[i] = top
    if top != -1: # if some column on the left is lower than column i, it should remain in the stack
        stack.append(top)
    stack.append(i)

stack = deque()
stack.append(len(heights) - 1)
for i in range(len(heights)-2, -1, -1):
    top = stack.pop()
    while heights[top] >= heights[i]:
        if len(stack) == 0:
            top = len(heights)
            break
        top = stack.pop()
    firstlowerright[i] = top
    if top != len(heights):
        stack.append(top)
    stack.append(i)

print(firstlowerleft)
print(firstlowerright)
