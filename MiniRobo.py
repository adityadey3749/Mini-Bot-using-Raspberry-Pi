from gpiozero import Motor

motors=[Motor (14, 15), 
        Motor(17, 18),
        Motor(27, 22),
        Motor(23, 24),
        Motor(9, 10),
        Motor(25, 8)]

def stop_all():
  for m in motors:
    m.stop()

stop_all()

while True:
  d=input("Give direction (Clockwise (C)/ Anticlockwise (A)/ Forward (F)/ Backward (B)/ Right (R)/ Left(L)/ Stop(s))? ")

  if d=="C":

    speed = float(input("Speed? (1 to 10)")) 
    m=int(input("Motor? (1-6)"))
    motors [m-1].forward(speed)

  elif d=="A":

    speed= float(input("Speed? (1 to 10)")) 
    m=int(input("Motor?(1-6)"))
    motors [m-1].backward(speed)

  elif d=="R":

    speed = float(input("Speed? (1 to 10)"))
    motors[0].forward(speed)
    motors[2].forward(speed)
    motors[4].forward(speed)
    motors[1].backward(speed)
    motors[3].backward(speed)
    motors[5].backward(speed)

  elif d=="L":
    speed = float(input("Speed? (1 to 10)")) 
    motors[1].forward(speed)
    motors[3].forward(speed)
    motors[5].forward(speed)
    motors[0].backward(speed)
    motors[2].backward(speed)
    motors[4].backward(speed)
    
  elif d=="F":
    speed = float(input("Speed? (1 to 10)"))
    motors[0].forward(speed)
    motors[1].forward(speed)
    motors[2].forward(speed)
    motors[3].forward(speed)
    motors[4].forward(speed)
    motors[5].forward(speed)
    
  elif d=="B":
    speed = float(input("Speed? (1 to 10)"))
    motors[0].backward(speed)
    motors[1].backward(speed)
    motors[2].backward(speed)
    motors[3].backward(speed)
    motors[4].backward(speed)
    motors[5].backward(speed)

  elif d=="S":
    stop_all()
