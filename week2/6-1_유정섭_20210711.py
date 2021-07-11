from collections import deque

card_stack = deque(range(1, int(input()) + 1))

step = 0
while len(card_stack) != 1:
  last = card_stack.popleft()
  if step % 2 == 1:
    card_stack.append(last)
  step += 1
print(card_stack[0])

# card_stack = list(range(1, int(input()) + 1))

# step = 0
# while len(card_stack) != 1:
#   last = card_stack.pop(0)
#   if step % 2 == 1:
#     card_stack.append(last)
#   step += 1
# print(card_stack[0])