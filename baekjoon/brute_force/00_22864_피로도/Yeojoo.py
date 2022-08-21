a, b, c, m = map(int, input().split())

day = 0

max_work = 0
tired = 0

if a > m :
  print(0)
else :
  while day != 24 :
    day += 1
    if tired + a <= m :
      max_work += b
      tired += a
    else :
      if tired - c >= 0 :
        tired -= c
      else :
        tired = 0

  print(max_work)