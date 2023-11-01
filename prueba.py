import flet
from flet import IconButton, Page, Row, TextField, icons
import serial

# Configuración del puerto serie
ser = serial.Serial('COM3', 9600)  # Reemplaza 'COM3' con el nombre de tu puerto serie

def main(page: Page):
    page.title = "Monitor de Frecuencia Cardíaca"
    page.vertical_alignment = "center"

    heart_rate_value = TextField(value="0", text_align="right", width=100)

    def update_heart_rate():
        try:
            data = ser.readline().decode('utf-8').strip()
            heart_rate_value.value = data
            page.update()
        except Exception as e:
            print(f'Error al leer los datos del puerto serie: {str(e)}')

    def start_monitoring(e):
        # Iniciar la lectura de la frecuencia cardíaca desde el Arduino
        # Puedes implementar esta lógica según tu configuración específica

        def stop_monitoring(e):
            # Detener la lectura de la frecuencia cardíaca
            # Puedes implementar esta lógica según tu configuración específica

            page.add(
                Row(
                    [
                        IconButton(icons.PLAY, on_click=start_monitoring),
                        IconButton(icons.STOP, on_click=stop_monitoring),
                    ],
                    alignment="center",
                )
            )

            page.add(heart_rate_value)

            flet.set_interval(update_heart_rate, 1000)  # Actualizar la frecuencia cardíaca cada segundo

flet.app(target=main)
