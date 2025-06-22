from naoqi import ALProxy
import time

# NAO_IP = "127.0.0.1"
# PORT = 53323

NAO_IP = "192.168.108.36"
PORT = 9559

tts = ALProxy("ALTextToSpeech", NAO_IP, PORT)
motion = ALProxy("ALMotion", NAO_IP, PORT)
posture = ALProxy("ALRobotPosture", NAO_IP, PORT)

motion.wakeUp()
posture.goToPosture("StandInit", 0.5)

def gesto_superman_brazo_izquierdo():
    """Alza el brazo izquierdo con la palma abierta hacia el frente como Superman."""
    names = ["LShoulderPitch", "LShoulderRoll", "LElbowRoll", "LElbowYaw", "LWristYaw",
             "RShoulderPitch", "RElbowRoll"]  # brazo derecho relajado

    angles = [-0.5, 0.0, -0.1, -1.5, 0.0,   # brazo izquierdo estirado al frente-arriba
              1.5, 1.0]                    # brazo derecho abajo y relajado

    times = [3.5] * len(names)

    motion.angleInterpolation(names, angles, times, True)
    time.sleep(2)  # mantener el gesto

def t_pose():
    """Move both arms to a horizontal T-pose position."""
    names = ["LShoulderPitch", "RShoulderPitch",
             "LShoulderRoll", "RShoulderRoll",
             "LElbowRoll", "RElbowRoll"]

    angles = [1.5, 1.5,     # Arms level with shoulders
              2.0, -2.0,    # ShoulderRoll to extend arms outward (left/right)
              -0.1, 0.1]    # Elbows slightly relaxed

    times = [2.0] * len(names)

    motion.angleInterpolation(names, angles, times, True)
    time.sleep(1)

def reset_postura_neutral():
    """Postura inicial: de pie, brazos abajo relajados."""
    names = ["LShoulderPitch", "RShoulderPitch", "LElbowRoll", "RElbowRoll",
             "LShoulderRoll", "RShoulderRoll"]
    angles = [1.5, 1.5, -0.1, 0.1, 0.0, 0.0]
    times = [1.0] * len(names)
    motion.angleInterpolation(names, angles, times, True)
    time.sleep(1)

def defensa_personal_brazos():
    """Postura defensiva (brazos recogidos, no estirados)."""
    names = ["LShoulderPitch", "RShoulderPitch", "LElbowRoll", "RElbowRoll"]
    angles = [0.5, 0.5, -1.0, 1.0]  # Brazos flexionados cerca del cuerpo
    times = [1.0] * len(names)
    motion.angleInterpolation(names, angles, times, True)
    time.sleep(1)

def gesto_ambos_brazos_ataque():
    """Simula golpes alternos con ambos brazos, luego vuelve a defensa."""
    # Golpe derecho
    motion.setAngles(["RShoulderPitch", "RElbowRoll"], [0.1, 0.8], 0.3)
    time.sleep(0.8)
    # Volver a neutral derecho
    motion.setAngles(["RShoulderPitch", "RElbowRoll"], [1.2, 1.0], 0.2)
    time.sleep(0.8)

    # Golpe izquierdo
    motion.setAngles(["LShoulderPitch", "LElbowRoll"], [0.1, -0.8], 0.3)
    time.sleep(0.8)
    # Volver a neutral izquierdo
    motion.setAngles(["LShoulderPitch", "LElbowRoll"], [1.2, -1.0], 0.2)
    time.sleep(0.8)

    # Volver a defensa completa
    defensa_personal_brazos()

def gesture_emphasis():
    names = ["LShoulderPitch", "RShoulderPitch"]
    angles = [1.0, 1.0]
    times = [0.6, 0.6]
    motion.angleInterpolation(names, angles, times, True)

def gesture_point_right():
    motion.setAngles(["RShoulderPitch", "RElbowYaw", "RElbowRoll", "RWristYaw"], [0.3, 1.0, 0.5, 0.0], 0.2)

def gesture_open_arms():
    motion.setAngles(["LShoulderRoll", "RShoulderRoll"], [0.5, -0.5], 0.2)

# INICIO

reset_postura_neutral()

tts.say("Hola, soy Nao.")
gesture_emphasis()
time.sleep(1.2)

tts.say("Hoy quiero hablarte sobre una realidad que nos afecta a todos:")
gesture_open_arms()
time.sleep(1.0)

tts.say("la inseguridad social.")
gesture_point_right()
time.sleep(1.0)

tts.say("Aprender defensa personal no se trata de pelear,")
gesture_emphasis()
time.sleep(1.2)

tts.say("sino de protegernos, cuidarnos y ganar confianza.")
gesture_open_arms()
time.sleep(1.2)

tts.say("La prevención comienza con la información, la preparación y la actitud.")
gesture_emphasis()
time.sleep(1.2)

tts.say("Por eso, ahora quiero mostrarte algunos movimientos básicos de defensa personal.")
gesture_point_right()
time.sleep(1.2)

# DEFENSA SOLO BRAZOS
tts.say("Primero, una postura defensiva con los brazos.")
defensa_personal_brazos()

# ATAQUE CON AMBOS BRAZOS Y DEFENSA FINAL
tts.say("Ataque con confianza, pero siempre con precaución.")
gesto_ambos_brazos_ataque()

tts.say("Y recuerda: la mejor defensa es estar preparado.")
# Final en postura defensiva
defensa_personal_brazos()

# Despedida final
tts.say("Gracias por tu atención. ¡Cuídate mucho!. Soy Super Nao.")
gesto_superman_brazo_izquierdo()

t_pose()

