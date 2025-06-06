#Program name: Level 5 Example 4 average bookings

booking = [ [1, 2, 3, 4],   #total 10 for site 0 (Cambridge)
            [10,20,30,40],  #total 100 for site 1 (Newcastle)
            [ 2, 3, 4, 5] ] #total 14 for site 2 (Manchester)
siteName = ["Cambridge", " Newcastle", " Manchester"]

#define empty lists
totalSiteBookings = [0]*3
averageBookings = [0]*3
totalBookings = 0

#find total and average of each row
for site in range(3):
    for month in range(4):
        totalSiteBookings[site] = totalSiteBookings[site] + booking[site][month]
    totalBookings = totalBookings + totalSiteBookings[site]

    averageBookings[site] = totalSiteBookings[site] / 4

#print average bookings for each site over 4-month period
for site in range(3):
    print("Average booking in", siteName[site], "=", \
          round(averageBookings[site],1))    

#print total overall bookings for season
print("\nTotal bookings at all sites: " ,totalBookings)
