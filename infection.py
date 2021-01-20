#Members: Thomas J Rowe, Jixi He, Eyasu Woldu, & Wayne Zheng
#Software Design: Ice Breaker
#input: n
#output: total infected number, the % of infected, total amount of refunds
condition=True
temple_pop = 39740

def infection_calculator(n):
    initial_infection=7
    reproduction_rate=1.2
    total_infected=0
    for i in range(n):
        new_infection=reproduction_rate*initial_infection
        initial_infection=new_infection
        total_infected+=new_infection
    percentage_total=total_infected/temple_pop*100
    return total_infected, percentage_total

while condition:
    days=int(input("Enter n (enter 0 to exit): "))
    if(days==0):
        break
    total_infected, per_infected=infection_calculator(days)
    total_infected=round(total_infected)
    total_refund=total_infected*9972
    print("Total infected people: "+str(total_infected))
    print("Percentage of infected: %"+str(per_infected))
    print("Temple will lose $"+str(total_refund)+'\n')


