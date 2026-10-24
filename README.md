Self-Balancing Robot with PID Control
Simulation-only project. No physical hardware was built, bought, or measured. Every result in this repository comes from numerical simulation (plots, tables, metrics). All physical parameters are assumptions based on a virtual bill of materials and are labeled as such. Real hardware will differ (see Simulation vs. real hardware).

Overview
The goal is to design, tune, and validate a PID-controlled self-balancing robot (a wheeled inverted pendulum) entirely in simulation, with firmware-quality C++ code that could be flashed to real hardware later.

This is a portfolio and learning project in embedded systems and mechatronics. It is built in layers, so that each layer can be checked against the previous one:

1. A plant model in Python (wheeled inverted pendulum + DC motor).
2. Control design in Python (PD/PID on tilt, then a cascade with an outer velocity/position loop).
3. Embedded firmware in C++ with a hardware abstraction layer (HAL), compiled both natively (unit tests) and for the ESP32.
4. Software-in-the-loop (SIL): the real firmware code is called from the Python plant.
5. A FreeRTOS architecture and timing analysis.
6. (Stretch) The ESP32 firmware running in Wokwi, connected to the Python plant in lockstep.

Modeling assumptions (current)

These apply to the first version of the plant model. Details are in docs/plant_model.md.

1. Motion in a vertical plane only; the robot balances and moves in a straight line.
2. The two wheels act as one equivalent wheel.
3. The wheel rolls without slipping on flat ground and never leaves it.
4. Body and wheel are rigid; everything above the axle (chassis, battery, electronics, motors) is one body.
5. No friction and no air drag.
6. The motor is an ideal torque source (to be replaced by a DC motor model).
7. Gravity is constant.

Friction, motor dynamics, deadzone, sensor effects, and delays are added in later layers.