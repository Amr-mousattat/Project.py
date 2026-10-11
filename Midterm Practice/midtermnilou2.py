#Question 1 - mixing a solution

def final_concentration(volume, concentration, water):
    vt = volume + water
    pureSubstance = volume * concentration/100
    return (pureSubstance/vt)*100

#Question 2 - Movie Ticket Price

def calculate_ticket(age, weekend):
    price = 0
    if(age <= 5): price += 0
    elif(age <= 17): price += 8
    elif(age <= 60): price += 10

    if(weekend and age >= 5):
        price += 3

#Question 3 - Electricity Consumption

def calculate_electricity_costs():
    totalconsumption = 0
    totalCosts = 0
    count = 0
    for days in range(7):
        dailyEnergyConsumption = float(input(f"enter energy consumption for day {days+1}:"))
        totalconsumption += dailyEnergyConsumption

        if(dailyEnergyConsumption >= 20):
            totalCosts += (dailyEnergyConsumption*0.15)
            count += 1
        else: totalCosts += (dailyEnergyConsumption*0.10)
        days +=1
    return f"total consumption: {totalconsumption} kWh \nDays above 20 khw: {count} \nTotal Costs: {totalCosts} $"
    
    
# print(calculate_electricity_costs())

#Question 4 - zero one pattern

def pattern(integer):
    result = ""
    for i in range(integer):
        for j in range(integer):
            if(i%2 ==0):
                result += "0 "
            else: result += "1 "
        result += "\n"
        i+=1
    return result

print(pattern(int(input("enter integer:"))))