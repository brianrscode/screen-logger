# Screen Logger

Este repositorio contiene un script Python que toma capturas de pantalla de la pantalla cada 5 segundos y las guarda en archivos PNG numerados secuencialmente.

## Requisitos

- Pillow
- pyscreenshot

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/brianrscode/screen-logger.git
```
2. Instala las dependencias con: 
```bash
pip install -r requirements.txt
```

## Uso

Ejecuta el script con el siguiente comando:
```bash
python main.py
```

El script se ejecutará indefinidamente hasta que se presione `Ctrl + C` para detenerlo. Las capturas de pantalla se guardarán en la misma carpeta que el script.

## Créditos

Este script utiliza la biblioteca [pyscreenshot](https://github.com/ponty/pyscreenshot) para tomar capturas de pantalla.
