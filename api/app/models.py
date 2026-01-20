"""
Модели данных (Pydantic schemas).

Определяет структуры данных для:
- Подшипников
- Аналогов
- Стандартов
- Производителей
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# Placeholder для кода из bearing-api/app/models.py

class BearingBase(BaseModel):
    """Базовая модель подшипника"""
    designation: str = Field(..., description="Обозначение подшипника")
    bearing_type: Optional[str] = Field(None, description="Тип подшипника")
    inner_diameter: Optional[float] = Field(None, description="Внутренний диаметр (d), мм")
    outer_diameter: Optional[float] = Field(None, description="Наружный диаметр (D), мм")
    width: Optional[float] = Field(None, description="Ширина (B), мм")

class Bearing(BearingBase):
    """Полная модель подшипника"""
    id: int
    manufacturer: Optional[str] = None
    standard: Optional[str] = None
    dynamic_capacity: Optional[float] = None
    static_capacity: Optional[float] = None
    created_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class BearingCreate(BearingBase):
    """Модель для создания подшипника"""
    pass

class Analog(BaseModel):
    """Модель аналога подшипника"""
    original_designation: str
    analog_designation: str
    manufacturer: Optional[str] = None
    standard: Optional[str] = None
    compatibility: Optional[float] = Field(None, description="Степень совместимости (0-1)")

class SearchParams(BaseModel):
    """Параметры поиска подшипников"""
    designation: Optional[str] = None
    bearing_type: Optional[str] = None
    min_inner_diameter: Optional[float] = None
    max_inner_diameter: Optional[float] = None
    min_outer_diameter: Optional[float] = None
    max_outer_diameter: Optional[float] = None
    manufacturer: Optional[str] = None
    standard: Optional[str] = None
    limit: int = Field(100, ge=1, le=1000)
    offset: int = Field(0, ge=0)
