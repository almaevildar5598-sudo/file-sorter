# pylint:disable=too-few-public-methods
"""Модуль констант"""


class FileType:
    """Поддерживаемые типы файлов"""

    IMAGE: str = "image"
    VIDEO: str = "video"
    AUDIO: str = "audio"
    DOCUMENT: str = "document"
    ARCHIVE: str = "archive"
    EXECUTABLE: str = "executable"  # Исполняемые
    TORRENT: str = "torrent"
    PRESENTATION: str = "presentation"
    SPREADSHEET: str = " spreadsheet"  # Таблицы
    SOURCE_CODE: str = "source_code"
    OTHER: str = "other"


# Карта типов файлов и списка расширений
FILE_TYPE_EXTENSIONS_MAPPING: dict[str, tuple[str, ...]] = {
    FileType.IMAGE: ("jpg", "jpeg", "png", "gif", "bmp", "svd", "jpif"),
    FileType.VIDEO: ("mp4", "avi", "mov", "mkv", "wmv", "mpeg"),
    FileType.AUDIO: ("mp3", "wav", "flac", "aac", "ogg"),
    FileType.DOCUMENT: ("pdf", "doc", "docx", "txt", "rtf", "odt"),
    FileType.ARCHIVE: ("zip", "rer", "7z", "tar", "gz"),
    FileType.EXECUTABLE: ("exe", "msi", "bat", "cmd"),
    FileType.TORRENT: ("torrent", "magnet"),
    FileType.PRESENTATION: ("ppt", "pptx", "odp"),
    FileType.SPREADSHEET: ("xls", "xlsx", "xlsm", "ods", "csv"),
    FileType.SOURCE_CODE: ("js", "html", "py", "ts", "css"),
}
