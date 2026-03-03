from enum import Enum
from typing import Optional
from dataclasses import dataclass


@dataclass
class FormatProperties:
    """Минимальные свойства формата: расширение и категория."""
    extension: str
    category: str


class FileFormat(Enum):
    """Форматы файлов для файловой системы (только необходимые)."""

    TXT = FormatProperties("txt", "text")
    PDF = FormatProperties("pdf", "document")
    JPG = FormatProperties("jpg", "image")
    ZIP = FormatProperties("zip", "archive")
    PY = FormatProperties("py", "code")
    JSON = FormatProperties("json", "data")
    EXE = FormatProperties("exe", "executable")

    @property
    def extension(self) -> str:
        return self.value.extension

    @property
    def category(self) -> str:
        return self.value.category

    @classmethod
    def from_file(cls, filename: str) -> Optional["FileFormat"]:
        """Определяет формат по имени файла."""
        if '.' in filename:
            ext = filename.split('.')[-1].lower()
            for fmt in cls:
                if fmt.extension == ext:
                    return fmt
        return None

    def get_folder_name_for_category(self) -> str:
        """Возвращает имя папки для организации файлов этой категории."""
        folders = {
            "text": "Текстовые файлы",
            "document": "Документы",
            "image": "Изображения",
            "archive": "Архивы",
            "code": "Исходный код",
            "data": "Данные",
            "executable": "Исполняемые файлы"
        }
        return folders.get(self.category, "Другие")