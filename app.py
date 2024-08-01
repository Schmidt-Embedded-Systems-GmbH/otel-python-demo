from random import randint
from flask import Flask, request
import logging
from opentelemetry import trace
from opentelemetry import metrics

import sys
import signal
def handler(signal, frame):
  print('CTRL-C pressed!')
  sys.exit(0)
signal.signal(signal.SIGINT, handler)

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
tracer = trace.get_tracer("diceroller.tracer")
meter = metrics.get_meter("diceroller.meter")


roll_counter = meter.create_counter(
    "dice.rolls",
    description="The number of rolls by roll value",
)

@app.route("/rolldice")
def roll_dice():
    player = request.args.get('player', default=None, type=str)
    result = str(roll())
    if player:
        logger.warning("%s is rolling the dice: %s", player, result)
    else:
        logger.warning("Anonymous player is rolling the dice: %s", result)
    return result

def roll():
    with tracer.start_as_current_span("roll") as rollspan:
        res = randint(1, 6)
        roll_counter.add(1, {"roll.value": str(res)})
        rollspan.set_attribute("roll.value", res)
        return res
        


