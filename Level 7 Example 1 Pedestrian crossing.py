#Program name: Level 7 Example 1 Pedestrian crossing
#Program counts down seconds until light turns green

import time
print("Wait")
for seconds in range(10,0,-1):
    print (seconds, "seconds")
    time.sleep(1)
print ("Walk")
    
