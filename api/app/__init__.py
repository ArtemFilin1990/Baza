"""
API приложение для справочника подшипников.
FastAPI приложение для работы с базой данных подшипников.
"""

from __future__ import annotations

from .api import app

APP_NAME = "Bearing API"
APP_DESCRIPTION = "API для работы с базой данных подшипников"
APP_VERSION = "1.0.0"

__version__ = APP_VERSION
__author__ = "ArtemFilin1990"

__all__ = ['app', "APP_DESCRIPTION", "APP_NAME", "APP_VERSION", "__author__", "__version__"]
