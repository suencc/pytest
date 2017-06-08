# from math import *
#
# # input Lat_A 纬度A
# # input Lng_A 经度A
# # input Lat_B 纬度B
# # input Lng_B 经度B
# # output distance 距离(km)
# def calcDistance(Lat_A, Lng_A, Lat_B, Lng_B):
#     ra = 6378.140  # 赤道半径 (km)
#     rb = 6356.755  # 极半径 (km)
#     flatten = (ra - rb) / ra  # 地球扁率
#     rad_lat_A = radians(Lat_A)
#     rad_lng_A = radians(Lng_A)
#     rad_lat_B = radians(Lat_B)
#     rad_lng_B = radians(Lng_B)
#     pA = atan(rb / ra * tan(rad_lat_A))
#     pB = atan(rb / ra * tan(rad_lat_B))
#     xx = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(rad_lng_A - rad_lng_B))
#     c1 = (sin(xx) - xx) * (sin(pA) + sin(pB)) ** 2 / cos(xx / 2) ** 2
#     c2 = (sin(xx) + xx) * (sin(pA) - sin(pB)) ** 2 / sin(xx / 2) ** 2
#     dr = flatten / 8 * (c1 - c2)
#     distance = ra * (xx + dr)
#     return distance
#
# Lat_A=32.060255; Lng_A=118.796877 # 南京
# Lat_B=39.904211; Lng_B=116.407395 # 北京
# distance=calcDistance(Lat_A,Lng_A,Lat_B,Lng_B)
# print('(Lat_A, Lng_A)=({0:10.3f},{1:10.3f})'.format(Lat_A,Lng_A))
# print('(Lat_B, Lng_B)=({0:10.3f},{1:10.3f})'.format(Lat_B,Lng_B))
# print('Distance={0:10.3f} km'.format(distance))

lng1 = 106.70170678755728
lat1 = 26.57594987828108

lng2 = 106.6333188789358
lat2 = 26.604155944932327

lng3 = 106.71367507445606
lat3 = 26.579208769951844
lng4 = 106.72905345303576
lat4 = 26.608584478410346

lng5 = 106.62994951013857
lat5 = 26.636322823902727

lnd =  0.008774687519
lad =  0.00374531687912

# lngs = [106.70170678755728, 106.6333188789358, 106.71367507445606, 106.72905345303576, 106.62994951013857]
# lats = [26.57594987828108,]


print((lng1 + lnd), (lat1 + lnd))
print((lng2 +lnd), (lat2 +lnd))
print((lng3 +lnd), (lat3 +lnd))
print((lng4 +lnd), (lat4 +lnd))
print((lng5 +lnd), (lat5 +lnd))