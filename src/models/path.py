"""Модуль модели для работы с путем каталога"""
from pathlib import Path
from typing import Any, Generator


class PathModel:
    """
    Модель пути каталога

    Attributes:
        _path (Path): объект Path с путем каталога

    """
    def __init__(self, path: Path, skip_check: bool = False) -> None:
        """
        Инициализация модели пути каталога

        Args:
            path: (Path): объект Path с путем каталога
            skip_check (bool): флаг пропуска проверки на существование. По-умолчание: False
        """
        self._path: Path = path

        if not skip_check:
            self._check_exists()

    @property
    def files_count(self) -> int:
        """
        Количество файлов в каталоге

        Returns:
            (int): количество файлов в self._path

        Examples:
            >>> # Количество файлов в "C:/Users/admin/Downloads"
            >>> PathModel(Path("C:/Users/admin/Downloads")).files_count
        """
        file_count: int = 0

        for item in self._path.iterdir():
            if item.is_file():
                file_count += 1

        return file_count

    @property
    def files(self) -> Generator[Path, Any, None]:
        """
        Генератор списка файлов в каталоге

        Returns:
            (Generator[Path, Any, None]): генератор списка файлов в self._path
        """
        for item in self._path.iterdir():
            if item.is_file():
                yield item

    def create(self) -> None:
        """
        Создание каталога

        Notes:

            * Создаст полную структуру
            * Допускает существование

        Examples:
            >>> # Создаст все несуществующие папки до 3
            >>> PathModel(Path("C:/1/2/3")).create()

        """
        self._path.mkdir(parents=True, exist_ok=True)

    def _check_exists(self) -> None:
        """
        Проверяет существование каталога

        Raises:
            FileNotFoundError: если папка не существует
            NotADirectoryError: если переданный путь не является каталогом
        """
        if not self._path.exists():
            raise FileNotFoundError(f"Папка {self._path} не существует")

        if not self._path.is_dir():
            raise NotADirectoryError(f"Путь {self._path} не папка")
