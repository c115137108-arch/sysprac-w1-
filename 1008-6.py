def power(v,i):
    return v*i
def adc_to_v(adc,vref=3.3):
    return round(adc / 4095 * vref, 2)
print(power(1.5,2.0))
print(adc_to_v(2048))
print(adc_to_v(2048,5))