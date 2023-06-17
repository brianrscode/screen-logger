import pyscreenshot
import time


def main():
    i: int = 1

    while True:
        time.sleep(5)

        image = pyscreenshot.grab()  # Captura la pantalla
        # image.show()  # Muestra la captura de pantalla
        image.save(f"./foto{str(i)}.png")  # Salva la screenshot

        i += 1


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
