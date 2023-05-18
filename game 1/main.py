import time

import model
import view
import controller

while True:
    time.sleep(0.01)
    model.oblako_letit()
    view.ion()
    controller.eve()
