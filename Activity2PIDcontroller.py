from Robot import MainRun

# In this problem you will need too create a PROPORTIONAL CONTROLLER for your robot.
# Steps:  - Create a PID controller
#         - Your power formula should then be  error * kp + integral * ki - slope * kd
#         - Make sure that your integral resets after it crosses the desired position
#         - Try creating a range in which integral is added (abs(error) < 100)

def go(bot):

    while True:
        ...

MainRun(go)


# Discuss the challenge of tuning a PID controller:
# Answer below (as comment):