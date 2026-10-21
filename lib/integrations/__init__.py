"""
Integrations - Módulo de Integrações
=====================================

Este módulo contém integrações com serviços externos:
- Google (OAuth, Calendar, Meet, Drive)
- Outros serviços podem ser adicionados no futuro
"""

from .google import GoogleOAuthHandler, GoogleCalendar, GoogleMeet, GoogleDrive

__all__ = [
    'GoogleOAuthHandler',
    'GoogleCalendar',
    'GoogleMeet',
    'GoogleDrive'
]
