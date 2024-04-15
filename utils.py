# utils.py

import tkinter as tk
import threading


def run_gui(api_com_port: str = None, machine_com_port: str = None):
    root = tk.Tk()
    # Убираем стандартный заголовок окна и кнопки управления
    root.overrideredirect(True)
    root.title("Найденные Виртуальные COM Порты")

    # Установка размера окна
    window_width = 600
    window_height = 340
    root.geometry(f"{window_width}x{window_height}")

    # Получение размеров экрана и центрирование окна
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f"+{center_x}+{center_y}")

    # Установка цвета фона и шрифта
    root.configure(bg='lightblue')
    font_settings = ("Helvetica", 20)

    if api_com_port and machine_com_port:
        message = (
            f"Настройки Станка\n\n"
            f"Номер последовательного порта: {machine_com_port}\n"
            f"Скорость передачи: 9600\n"
            f"Биты данных: 8\n"
            f"Контрольный бит: None\n"
            f"Стоповый бит: 1"
        )
    else:
        message = "\nCOM порты не найдены!\n\n Обратитесь к программистам!\n"

    label = tk.Label(root, text=message, padx=10, pady=10, bg='lightblue', font=font_settings)
    label.pack()

    close_button = tk.Button(root, text="Закрыть", command=root.destroy, font=font_settings)
    close_button.pack(pady=20)

    root.mainloop()


def show_message(api_com_port: str = None, machine_com_port: str = None):
    gui_thread = threading.Thread(target=run_gui, args=(api_com_port, machine_com_port))
    gui_thread.daemon = True  # Устанавливаем поток как демон, чтобы он завершился с основной программой
    gui_thread.start()


if __name__ == "__main__":
    show_message("СCOM", "СCOM")
