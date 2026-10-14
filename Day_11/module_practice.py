

import math as m #Using an aliases for the module

try:
    import cclarke

except ModuleNotFoundError as e:
    print("This module is don't exist")


print(m.sin(30))
print(m.pi)