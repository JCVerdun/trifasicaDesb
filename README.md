# trifasicaDesbalanceada

# Cálculo de Corriente en una Carga Trifásica Conectada en Estrella

Este proyecto es una aplicación Python que calcula la corriente en cada una de las fases de una carga trifásica conectada en estrella. La aplicación es útil para ingenieros eléctricos y estudiantes que necesitan entender cómo calcular las corrientes en un sistema trifásico desequilibrado y poder calcular fácilmente el voltaje de desplazamiento del neutro.

## Descripción

La aplicación toma como entradas los siguientes parámetros:
- **Impedancias de fase**: Las impedancias de cada fase que pueden ser cargadas de manera polar o binomica.
Los valores de las impedancias son requeridos durante la ejecución del programa.


- **Voltaje de fase**: El módulo del voltaje entre cada una de las fases y el conductor de neutro.
- **Secuencia de lineas**: Se puede modificar la secuencia de lineas del generador (Secuencia posititva y negativa).
- **Angulo inicial del voltaje de fase**: El argumento del voltaje de fase que se considera inicial, en el caso de una secuencia positiva el valor que se cargue le será asignado al voltaje URN.
Estos parametros son modificados previo a la ejecucion del programa desde el archivo **voltajes.config**

## Requisitos

- Python 3.x
- Bibliotecas: `math` (para cálculos trigonométricos), `matplotlib` (para el ploteo de los gráficos que posteriormente se muetsran en el archivo reporte), `reportlab` (para la creacion del archivo PDF para el reporte), `PIL`(para el guardado y posterior ploteo de imagenes) y `configparser` (para obtener los datos del archivo de configuracion)


## Instalación

1. Clona este repositorio o descarga los archivos en tu máquina local.
2. Asegúrate de tener Python instalado. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
3. Descargar e Instalar las bibliotecas de matplotlib, pillow (PIL), reportlab y configparser. Todas ellas pueden obtenerse mediante pip install por linea de comandos.
```bash
pip install matplotlib
pip install pillow
pip install reportlab
pip install configparser   
```
## Uso

1. Descarga o clona el repositorio.
2. Abre una terminal y navega a la carpeta donde se encuentra el archivo `desbalanceada.py`.
3. Ejecuta el siguiente comando para ejecutar el script:

```bash
python estrellaDesbalanceada.py
```

## Ejecutar online

👉 Podés ejecutar este proyecto directamente en Binder:

[![Abrir en Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JCVerdun/trifasicaDesb/HEAD?filepath=estrellaDesbalanceada.py)

