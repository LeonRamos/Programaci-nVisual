# Ejercicios de Programación Selectiva y Repetitiva 

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Electrónica](https://img.shields.io/badge/Electrónica-Embebidos-green?logo=raspberry-pi)]
[![Versionado](https://img.shields.io/badge/Git-Versionado-red?logo=git)]
[![LowCode](https://img.shields.io/badge/LowCode-Soluciones-yellow?logo=appveyor)]
[![C](https://img.shields.io/badge/C-Compatible-lightgrey?logo=c)]

---

## Introducción

Problemas prácticos para aprender Python con estructuras selectivas (`if`, `if-else`) y repetitivas (`while`, `do while`, `for`), aplicados a casos reales en sistemas **electrónicos y embebidos**.

---

## Problema 1: Control de Temperatura en un Microcontrolador

**Caso:** 
Monitorea la temperatura de un sensor digital. Si la temperatura excede los 70 °C, activa un ventilador; si baja de 65 °C, apágalo. El monitoreo debe ser continuo.

- Usar `while` para el ciclo de monitoreo.
- Condiciones `if-else` para la lógica de encendido/apagado.
- Simular lectura de sensor con lista o valores aleatorios.

---

## Problema 2: Revisión de Voltaje de Baterías

**Caso:**
Una placa verifica el voltaje de 5 baterías en cada ciclo. Si alguna batería tiene menos de 3.3 V → "Baja"; si igual/mayor a 4.0 V → "Óptima"; entre 3.3 V y 4.0 V → "Advertencia".

- Usar bucle `for` para recorrer los voltajes.
- Condiciones `if-elif-else` para la clasificación.

---

## Problema 3: Contador de Señales Digitales Recibidas

**Caso:**
En un sistema de adquisición, contar cuántas señales altas (‘1’) y bajas (‘0’) se reciben en 20 ciclos. Si las señales altas superan las bajas al final, activa indicador "Alto flujo de datos"; si no, permanece apagado.

- Usar ciclo `do-while` simulado con `while True` y break.
- Comparar contadores con condición `if` al finalizar.

---

## Tecnologías Empleadas

- **Python**: Programación y simulación
- **Electronica y Embebidos**: Casos prácticos simulados.
- **LowCode**: Enfoque simplificado y educativo
- **Versionado con Git**: Para control de cambios y colaboración.
- **C (Compatible)**: Muchos conceptos son trasladables a C tradicional.

---

