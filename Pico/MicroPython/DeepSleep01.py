import machine

# put the device to sleep for 10 seconds
print("Going to Sleep")
machine.deepsleep(1000)
print("Waking Up")

# check if the device woke from a deep sleep
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')

# put the device to sleep for 10 seconds
print("Going to sleep")
machine.deepsleep(1000)

# check if the device woke from a deep sleep
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep x 2')