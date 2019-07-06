sec = int(input())
res = []
for unit in [3600, 60, 1]:
  count = int(sec / unit)
  res.append(str(count))
  if count > 0:
    sec = sec % unit
print(':'.join(res))