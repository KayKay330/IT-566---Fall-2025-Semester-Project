

"""Implements behavior common to all application classes."""

from abc import ABC, abstractmethod
from employee_training.logging import LoggingService
from employee_training.settings import Settings


class ApplicationBase(ABC):
    """Implements ApplicationBase class."""

    def __init__(self, subclass_name: str, logfile_prefix_name: str) -> None:
        """Instantiate instance."""
        # Load app settings file automatically
        self._settings = Settings().read_settings_file_from_location()

        # Create a logger for any subclass that inherits from this base
        self._logger = LoggingService(subclass_name, logfile_prefix_name)
