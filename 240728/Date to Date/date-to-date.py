from datetime import datetime, timedelta

m1, d1, m2, d2 = list(map(int,input().split()))
time1 = datetime(2011,m1,d1,0,0,0)
time2 = datetime(2011,m2,d2,0,0,0)

print((time2-time1).days+1)