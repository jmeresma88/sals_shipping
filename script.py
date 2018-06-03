#This function calculates the cost of ground shipping based on the weight.

def ground_shipping(weight):
  if weight <= 2.0:
    cost = (weight*1.50)+20
    return cost
  elif weight <= 6.0:
    cost = (weight*3.0)+20
    return cost
  elif weight <= 10.0:
    cost = (weight*4.0)+20
    return cost  
  else:
    cost = (weight*4.75)+20
    return cost

 

#This is testing the above function. Desired output = 53.6
print("${:.2f}".format(ground_shipping(8.4)))

#This variable represents the cost of premium ground shipping
premium_ground = 125

#This function calculates the cost of drone shipping based on the weight.
def drone_shipping(weight):
  if weight <= 2.0:
    cost = (weight*4.50)
    return cost
  elif weight <= 6.0:
    cost = (weight*9.0)
    return cost
  elif weight <= 10.0:
    cost = (weight*12.0)
    return cost
  else:
    cost = (weight*14.25)
    return cost
  
#This is testing the above function. Desired output = 6.75
print("${:.2f}".format(drone_shipping(1.5)))

#This function calculates the cheapest shipping cost based on the weight.
def cheapest_shipping(weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_ground:
    return "Your cheapest option is ground shipping. This will cost "+str("${:.2f}".format(ground_shipping(weight)))+" to ship."
  elif drone_shipping(weight) < premium_ground:
    return "Your cheapest option is drone shipping. This will cost "+str("${:.2f}".format(drone_shipping(weight)))+" to ship."
  else:
    return "Your cheapest option is premium ground shipping. This will cost "+str("${:.2f}".format(premium_ground))+" to ship."

#This is testing the above function. Desired output = 34.40
print(cheapest_shipping(4.8))
#This is testing the above function. Desired output = 125
print(cheapest_shipping(41.5))
    