# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import time
from naoqi import ALProxy


NAO_IP = os.getenv("NAO_IP", "192.168.xxx.xxx")
NAO_PORT = int(os.getenv("NAO_PORT", "9559"))


def connect_to_nao():
    """Create the required NAOqi proxies."""
    tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
    motion = ALProxy("ALMotion", NAO_IP, NAO_PORT)
    posture = ALProxy("ALRobotPosture", NAO_IP, NAO_PORT)

    return tts, motion, posture


def reset_postura_neutral(motion):
    """Postura inicial: de pie, brazos abajo relajados."""
    names = [
        "LShoulderPitch",
        "RShoulderPitch",
        "LElbowRoll",
        "RElbowRoll",
        "LShoulderRoll",
        "RShoulderRoll",
    ]

    angles = [1.5, 1.5, -0.1, 0.1, 0.0, 0.0]
    times = [1.0] * len(names)

    motion.angleInterpolation(names, angles, times, True)
    time.sleep(1)


def gesto_superman_brazo_izquierdo(motion):
    """Alza el brazo izquierdo con la palma abierta hacia el frente como gesto simbólico."""
    names = [
        "LShoulderPitch",
        "LShoulderRoll",
        "LElbowRoll",
        "LElbowYaw",
        "LWristYaw",
        "RShoulderPitch",
        "RElbowRoll",
    ]

    angles = [
        -0.5,
        0.0,
        -0.1,
        -1.5,
        0.0,
        1.5,
        1.0,
    ]

    times = [3.5] * len(names)

    motion.angleInterpolation(names, angles, times, True)
    time.sleep(2)


def t_pose(motion):
    """Move both arms to a horizontal T-pose position."""
    names = [
        "LShoulderPitch",
        "RShoulderPitch",
        "LShoulderRoll",
        "RShoulderRoll",
        "LElbowRoll",
        "RElbowRoll",
    ]

    angles = [
        1.5,
        1.5,
        2.0,
        -2.0,
        -0.1,
        0.1,
    ]

    times = [2.0] * len(names)

    motion.angleInterpolation(names, angles, times, True)
    time.sleep(1)


def postura_preventiva_brazos(motion):
    """Postura preventiva con los brazos recogidos cerca del cuerpo."""
    names = [
        "LShoulderPitch",
        "RShoulderPitch",
        "LElbowRoll",
        "RElbowRoll",
    ]

    angles = [0.5, 0.5, -1.0, 1.0]
    times = [1.0] * len(names)

    motion.angleInterpolation(names, angles, times, True)
    time.sleep(1)


def gesto_movimiento_controlado(motion):
    """Movimiento simbólico de brazos usado como demostración educativa."""
    motion.setAngles(["RShoulderPitch", "RElbowRoll"], [0.1, 0.8], 0.3)
    time.sleep(0.8)

    motion.setAngles(["RShoulderPitch", "RElbowRoll"], [1.2, 1.0], 0.2)
    time.sleep(0.8)

    motion.setAngles(["LShoulderPitch", "LElbowRoll"], [0.1, -0.8], 0.3)
    time.sleep(0.8)

    motion.setAngles(["LShoulderPitch", "LElbowRoll"], [1.2, -1.0], 0.2)
    time.sleep(0.8)

    postura_preventiva_brazos(motion)


def gesture_emphasis(motion):
    """Small expressive gesture for speech emphasis."""
    names = ["LShoulderPitch", "RShoulderPitch"]
    angles = [1.0, 1.0]
    times = [0.6, 0.6]

    motion.angleInterpolation(names, angles, times, True)


def gesture_point_right(motion):
    """Pointing gesture with the right arm."""
    motion.setAngles(
        ["RShoulderPitch", "RElbowYaw", "RElbowRoll", "RWristYaw"],
        [0.3, 1.0, 0.5, 0.0],
        0.2,
    )


def gesture_open_arms(motion):
    """Open arms gesture for welcoming or emphasizing a message."""
    motion.setAngles(["LShoulderRoll", "RShoulderRoll"], [0.5, -0.5], 0.2)


def run_demo():
    """Run the complete Super NAO educational presentation."""
    print("Connecting to NAO at {}:{}...".format(NAO_IP, NAO_PORT))

    tts, motion, posture = connect_to_nao()

    motion.wakeUp()
    posture.goToPosture("StandInit", 0.5)

    reset_postura_neutral(motion)

    tts.say("Hola, soy Nao.")
    gesture_emphasis(motion)
    time.sleep(1.2)

    tts.say("Hoy quiero hablarte sobre una realidad que nos afecta a todos:")
    gesture_open_arms(motion)
    time.sleep(1.0)

    tts.say("la inseguridad social.")
    gesture_point_right(motion)
    time.sleep(1.0)

    tts.say("Aprender sobre autocuidado no se trata de pelear.")
    gesture_emphasis(motion)
    time.sleep(1.2)

    tts.say("Se trata de protegernos, cuidarnos y actuar con responsabilidad.")
    gesture_open_arms(motion)
    time.sleep(1.2)

    tts.say("La prevención comienza con la información, la preparación y la actitud.")
    gesture_emphasis(motion)
    time.sleep(1.2)

    tts.say("Ahora quiero mostrarte algunos movimientos simbólicos de prevención y autocuidado.")
    gesture_point_right(motion)
    time.sleep(1.2)

    tts.say("Primero, una postura preventiva con los brazos.")
    postura_preventiva_brazos(motion)

    tts.say("Luego, un movimiento controlado para representar atención y reacción.")
    gesto_movimiento_controlado(motion)

    tts.say("Y recuerda: la mejor defensa es la prevención.")
    postura_preventiva_brazos(motion)

    tts.say("Gracias por tu atención. Cuídate mucho. Soy Super Nao.")
    gesto_superman_brazo_izquierdo(motion)

    t_pose(motion)


if __name__ == "__main__":
    run_demo()