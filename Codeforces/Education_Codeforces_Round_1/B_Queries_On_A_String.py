
s = input()

for _ in range(int(input())):
  left, right, k = [int(x) for x in input().split()]
  
  left -= 1
  right -= 1
  k = k % (right - left + 1)

  # Before part
  before = s[:left]  
   
  # After part
  after = s[right+1:]
  
  # Rotate in-between part
  middle = s[right - k + 1: right + 1] + s[left: right - k + 1]
 
  s = before + middle + after

# Print final result.
print(s)
