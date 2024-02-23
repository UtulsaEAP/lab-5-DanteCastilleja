def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
   return (dollars_per_gallon / (miles_per_gallon / miles_driven))

if __name__ == '__main__':
   miles_per_gallon = float(input())
   dollars_per_gallon = float(input())
   for miles_driven in [10, 50, 400] :
      if miles_driven == 10 :
         print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):.2f}')
      elif miles_driven == 50 :
         print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):.2f}')
      elif miles_driven == 400 :
         print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):.2f}')
         break
    #print your costs here like example below
    #print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}')
   