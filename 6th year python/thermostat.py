def thermostatModel(actual, target):
    if actual < target:
        return True
    else:
        return False
tempToggle = thermostatModel(18,20)
print(tempToggle)