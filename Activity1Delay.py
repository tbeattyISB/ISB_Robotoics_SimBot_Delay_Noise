from Robot import MainRun
# Try changing the amount of DELAY to see  how it affects your controller's ability to function normally
# We will also work together to try "auto tuning" our PID controller
# https://en.wikipedia.org/wiki/Ziegler%E2%80%93Nichols_method#cite_note-1


def go(bot):
    bot.setDelay(0)  #Delay can be changed from 0 to 1

    desired = 300
    error = 0
    integral = 0
    bot.setPayload(10)

    kp = 0.3  # motor "gain"
    ki = 0
    kd = 0

    bot.wait(1000)  # Wait 1 seconds before starting

    while True:  # Always run the controller
        previous_error = error

        error = desired - bot.ultrasonic_sensor()  # Calculate error

        slope = error - previous_error

        if (integral*error < 0):
            integral = 0
        elif (abs(error) < 200):
            integral = integral + error

        bot.run(-(kp * error + ki * integral + kd * slope))  # Set the motor power

        bot.wait(20)

MainRun(go)


# In a comment below discuss how delay impacts a controller (a P-controller and a tuned PID-controller)
