rtn_text = []
val1, val2, val3 = 39.48719569273062, -76.53854508092664, None
print(type(val1))

if type(val1) is not float and type(val1) is not int:
    rtn_text.append('X value is out of range -90 to 90')

if val3 is None or \
        (type(val3) is not float
         and type(val3) is not int) \
        or (0 > val3) \
        or (val3 > 264000):
    rtn_text.append('Z value is out of range 0 to 264000')

print(rtn_text)
