import flet as ft
from pynput import keyboard

key_logs = []


def on_press(key, log_text, page):
    try:
        key_logs.append(key.char)
    except AttributeError:
        key_logs.append(str(key))
    update_logs(log_text, page)


def on_release(key):
    if key == keyboard.Key.esc:
        return False


def update_logs(log_text, page):
    # Обновляем содержимое логов
    log_text.value = '\n'.join([str(log) for log in key_logs])
    page.update()
7

def main(page: ft.Page):
    # Настройки окна
    page.title = 'keylogger'
    page.window.width = 400
    page.window.height = 400
    page.window.resizable = False

    # Создаем компонент для текста
    log_text = ft.Text(value='', expand=True, style='bodyMedium')

    # Создаем контейнер для текста с прокруткой
    scrollable_column = ft.Column([log_text], expand=True, scroll=ft.ScrollMode.AUTO)
    container = ft.Container(content=scrollable_column, width=300, height=300, padding=10)

    # Добавление контейнера на страницу
    page.add(container)

    # Запускаем считыватель клавиатуры в отдельном потоке
    listener = keyboard.Listener(
        on_press=lambda key: on_press(key, log_text, page),
        on_release=on_release
    )
    listener.start()


if __name__ == '__main__':
    ft.app(target=main)