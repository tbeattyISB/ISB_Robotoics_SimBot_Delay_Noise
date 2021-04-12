from Robot import MainRun
# In this assignement you will crerate an proportional - derivative controller:
# 1. Create three variables previous "kd = 1", "error = 0", "prevError = 0" and "slope = 0"
# 2. In the loop, set the old error to prevError, then measure the slope as the change in the error.
# 3. Update the robots run power
# 4. Add a wait command so that there is 50 ms between each calculation.


def go(bot):
    while True:
        ...

MainRun(go)


# 1. Discuss how an derivative controller works

# 2. What happens if the derivative controller is too low or too high?

# 3. Why would an integral controller be valuable if the derivative controller is too strong?
