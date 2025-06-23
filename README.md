# Super NAO - Defensa Personal con robótica educativa

Este proyecto utiliza al robot humanoide **NAO** como herramienta educativa para enseñar movimientos básicos de defensa personal a niños y jóvenes. A través de una combinación de gestos físicos y mensajes hablados, NAO busca concientizar sobre la importancia del autocuidado y la preparación ante situaciones de riesgo, en respuesta al contexto de creciente inseguridad en Lima.

## 🎯 Objetivo

Programar al robot NAO para ejecutar una presentación interactiva con movimientos y discurso educativo que promueva la prevención y la autodefensa en entornos escolares y sociales.

## 🤖 Descripción del Proyecto

El robot ha sido programado para:

- Realizar gestos simbólicos como postura de defensa, ataques controlados, postura tipo superhéroe y postura en T.
- Sincronizar los movimientos con frases pregrabadas que refuerzan el mensaje educativo.
- Simular una pequeña clase de defensa personal a través de un guion dinámico y visual.

## 🛠️ Tecnologías y herramientas utilizadas

- **Lenguaje:** Python 2.7
- **SDK:** NAOqi SDK
- **Entorno de desarrollo:** Visual Studio Code
- **Simulación previa:** Choregraphe
- **Robot físico:** NAO V5 (SoftBank Robotics)

## 📁 Estructura del código

El programa está dividido en funciones que encapsulan cada gesto o postura. Algunas de ellas son:

- `defensa_personal_brazos()`: postura defensiva.
- `gesto_ambos_brazos_ataque()`: golpes simulados con ambos brazos.
- `gesto_superman_brazo_izquierdo()`: postura inspiradora estilo superhéroe.
- `t_pose()`: postura final en forma de "T".
- `gesture_emphasis()`, `gesture_point_right()`, `gesture_open_arms()`: gestos expresivos sincronizados con el discurso.

## ▶️ Ejecución del programa

1. Asegúrate de tener instalado el SDK NAOqi en tu entorno con Python 2.7.
2. Conecta tu PC a la misma red que el robot NAO o usa el simulador.
3. Establece la IP del robot en el archivo Python:
   NAO_IP = "192.168.xxx.xxx"
   PORT = 9559

## 📹 Video de la ejecución del programa

- Mira la [demostración en video](https://youtu.be/zzAa6k6IlxM) para ver a NAO en acción.
