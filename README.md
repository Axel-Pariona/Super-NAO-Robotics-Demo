# Super NAO Robotics Demo

Super NAO Robotics Demo es un proyecto académico de robótica educativa desarrollado con el robot humanoide **NAO**. El proyecto utiliza movimientos corporales, posturas simbólicas y mensajes hablados para presentar una demostración sobre prevención, autocuidado y seguridad personal.

La demostración fue implementada en Python mediante el SDK **NAOqi**, sincronizando gestos del robot con frases educativas.

## Objetivo

Programar al robot NAO para ejecutar una presentación educativa breve, combinando voz, gestos y posturas corporales con el fin de promover mensajes de prevención y autocuidado en un entorno académico.

## Descripción del proyecto

El robot NAO realiza una secuencia de acciones como:

- Presentación inicial mediante voz.
- Gestos expresivos sincronizados con el discurso.
- Postura preventiva con los brazos.
- Movimiento simbólico y controlado de brazos.
- Gesto final tipo superhéroe.
- Postura final en forma de T.

El proyecto no busca enseñar técnicas de combate, sino demostrar el uso de robótica humanoide como recurso educativo para comunicar mensajes de seguridad personal.

## Tecnologías utilizadas

- Python 2.7
- NAOqi SDK
- Robot NAO V5
- Choregraphe
- Visual Studio Code

## Estructura del proyecto

```txt
Super-NAO-Robotics-Demo/
  src/
    super_nao_demo.py

  docs/
    script.md

  media/
    README.md

  .gitignore
  README.md
  requirements.txt
```

## Archivos principales

### `src/super_nao_demo.py`

Contiene el programa principal. Se encarga de:

- Conectarse al robot NAO mediante NAOqi.
- Inicializar los módulos de voz, movimiento y postura.
- Ejecutar la secuencia de gestos.
- Sincronizar movimientos con frases habladas.

### `docs/script.md`

Contiene el guion hablado por NAO durante la demostración.

### `media/README.md`

Contiene el enlace al video de demostración y recomendaciones para recursos multimedia.

## Configuración

El proyecto requiere tener instalado el SDK de NAOqi y acceso a un robot NAO físico o simulador compatible.

Configurar la IP y el puerto mediante variables de entorno.

En Linux o macOS:

```bash
export NAO_IP="192.168.xxx.xxx"
export NAO_PORT="9559"
```

En Windows PowerShell:

```powershell
$env:NAO_IP="192.168.xxx.xxx"
$env:NAO_PORT="9559"
```

También se puede editar directamente el archivo `src/super_nao_demo.py` en caso de pruebas locales.

## Ejecución

Ejecutar el programa principal:

```bash
python src/super_nao_demo.py
```

El proyecto fue desarrollado para un entorno con **Python 2.7** y **NAOqi SDK**.

## Video de demostración

La siguiente demostración muestra al robot NAO ejecutando la secuencia de voz, gestos y posturas programadas para el proyecto.

[![Ver demostración en YouTube](https://img.youtube.com/vi/zzAa6k6IlxM/maxresdefault.jpg)](https://youtu.be/zzAa6k6IlxM)

Enlace directo: https://youtu.be/zzAa6k6IlxM

## Funciones principales

El programa está organizado en funciones que representan gestos o acciones del robot:

- `reset_postura_neutral()`: coloca al robot en una postura neutral.
- `postura_preventiva_brazos()`: ejecuta una postura preventiva simbólica.
- `gesto_movimiento_controlado()`: realiza un movimiento controlado de brazos.
- `gesto_superman_brazo_izquierdo()`: ejecuta un gesto final tipo superhéroe.
- `t_pose()`: coloca al robot en una postura final en forma de T.
- `gesture_emphasis()`: gesto de énfasis durante el discurso.
- `gesture_point_right()`: gesto de señalamiento.
- `gesture_open_arms()`: gesto de apertura de brazos.

## Alcance del proyecto

Este proyecto corresponde a una demostración académica de robótica educativa.

Incluye:

- Conexión con NAO mediante NAOqi.
- Control básico de articulaciones.
- Uso de texto a voz.
- Secuencia de gestos sincronizados.
- Presentación educativa guiada.

## Limitaciones

- Requiere robot NAO físico o simulador compatible.
- Requiere SDK NAOqi.
- Fue desarrollado para Python 2.7.
- No incluye interfaz gráfica.
- No implementa visión por computadora ni reconocimiento de voz.
- Los movimientos son simbólicos y controlados.

## Posibles mejoras

- Agregar interacción mediante reconocimiento de voz.
- Integrar sensores táctiles del robot.
- Implementar una secuencia configurable desde archivo externo.
- Agregar más gestos expresivos.
- Crear una versión compatible con Python 3 si el entorno lo permite.
- Documentar capturas o fotografías del proceso de prueba.

## Estado del proyecto

Proyecto académico funcional desarrollado como demostración de robótica educativa con NAO.

## Autor

Desarrollado por Axel Pariona como proyecto académico de Inteligencia Artificial y robótica educativa.
