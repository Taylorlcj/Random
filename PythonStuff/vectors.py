import math
import os

def getMode():
    print("SELECT MODE")
    print("1: Polar to Cartisan")
    print("2: Cartisan to Polar")
    print("3: Vector addition")
    return int(input("MODE:"))

def ptc(mag,dir):
    if dir < 90 and dir >= 0:
        x = math.cos(math.radians(dir))*mag
        y = math.sin(math.radians(dir))*mag
    elif dir < 360 and dir >= 270:
        x = math.cos(math.radians(dir))*mag
        y = math.sin(math.radians(dir))*mag
    elif dir < 180 and dir >= 90:
        x = math.cos(math.radians(dir))*mag
        y = math.sin(math.radians(dir))*mag
    elif dir < 270 and dir >= 180:
        x = math.cos(math.radians(dir))*mag
        y = math.sin(math.radians(dir))*mag
    else:
        print("error")
    #print(f"\nx= {round(x,2)}")
    #print(f"y= {round(y,2)}")
    return round(x,4),round(y,4)
    
def ctp(x,y):
    mag = math.sqrt(x * x + y * y)
    if x > 0 and y > 0:
        dir = math.degrees(math.atan2(math.radians(y),math.radians(x)))
    elif x < 0 and y > 0:
        dir = math.degrees(math.atan2(math.radians(y),math.radians(x)))
    elif x < 0 and y < 0:
        dir = math.degrees(math.atan2(math.radians(y),math.radians(x)))+360
    elif x > 0 and y < 0:
        dir = math.degrees(math.atan2(math.radians(y),math.radians(x)))+360
    else:
        print("error")
    return(mag,dir)

another = True
magnitude = 0
direction = 0
magnitude2 = 0
direction2 = 0
x = 0
y = 0
x2 = 0
y2 = 0

while another == True:
    os.system('cls')
    mode = getMode()
    os.system('cls')
    if mode == 1:
        magnitude = float(input("Enter Magnitude:"))
        direction = float(input("Enter direction ccw from +x:"))
        x,y = ptc(magnitude,direction)
        print(f"\nx= {round(x,2)}")
        print(f"y= {round(y,2)}")
    elif mode == 2:
        x = float(input("Enter x:"))
        y = float(input("Enter y:"))
        magnitude,direction = ctp(x,y)
        print(f"\nmagnitude= {round(magnitude,2)}")
        print(f"direction ccw from +x = {round(direction,2)}")
    elif mode == 3:
        print("Vetor 1\n1:Polar\n2:Cartisan")
        v1type = int(input("Type:"))
        os.system('cls')
        if v1type == 1:
            magnitude = float(input("Enter Magnitude:"))
            direction = float(input("Enter direction ccw from +x:"))
            x,y = ptc(magnitude,direction)
        if v1type == 2:
            x = float(input("Enter x:"))
            y = float(input("Enter y:"))
        os.system('cls')
        
        print("Vetor 2\n1:Polar\n2:Cartisan")
        v2type = int(input("Type:"))
        os.system('cls')
        if v2type == 1:
            magnitude2 = float(input("Enter Magnitude:"))
            direction2 = float(input("Enter direction ccw from +x:"))
            x2,y2 = ptc(magnitude2,direction2)
        if v2type == 2:
            x2 = float(input("Enter x:"))
            y2 = float(input("Enter y:"))
        os.system('cls')
        x = x + x2
        y = y + y2
        magnitude,direction = ctp(x,y)
        print("Vector Result")
        print(f"\nx= {round(x,2)}")
        print(f"y= {round(y,2)}")
        print(f"\nmagnitude= {round(magnitude,2)}")
        print(f"direction ccw from +x = {round(direction,2)}")
    else:
        print("error")
    another = False
    if input("\nDo another?:").casefold() == "yes" or "y":
        another = True
    else:
        another = False