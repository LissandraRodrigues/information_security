from threading import Thread
import time

def car(velocity, pilot):
    position = 0

    while position <= 100:
        time.sleep(.5)
        print(f"Piloto {pilot}: {position} km\n")
        position += velocity

threading_car1 = Thread(target=car, args=[10, "Jerry"])
threading_car2 = Thread(target=car, args=[20, "Mauro"])

threading_car1.start()
threading_car2.start()
