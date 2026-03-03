
from core.filesystem import FileSystem
from cli.command_line import CLI

def main():
    fs = FileSystem()                 # создаём объект файловой системы
    if not fs.load():                  # пытаемся загрузить сохранённое состояние
        print("Сохранённое состояние не найдено. Создаю начальную конфигурацию...")
        fs._init_default_state()       # если нет — создаём admin и диск C:
        fs.save()                       # сразу сохраняем, чтобы файл появился
    cli = CLI(fs)                       # передаём файловую систему в CLI
    cli.run()                            # запускаем цикл команд

if __name__ == "__main__":
    main()

