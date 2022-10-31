def sum_to(num):
  total = 0

  for i in range(num + 1):
    total += i

  return total

def largest(lst):
  largest = -99999999

  for num in lst:
    if num > largest:
      largest = num

  return largest
