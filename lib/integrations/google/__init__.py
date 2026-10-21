"""
Google Integrations - Integrações com Serviços Google
====================================================

Este módulo contém todas as integrações com serviços Google:
- Google OAuth (autenticação)
- Google Calendar (agenda)
- Google Meet (vídeo chamadas)
- Google Drive (armazenamento)
"""

from .oauth_handler import GoogleOAuthHandler
from .calendar_integration import GoogleCalendar
from .meet_integration import GoogleMeet
from .drive_integration import GoogleDrive

__all__ = [
    'GoogleOAuthHandler',
    'GoogleCalendar',
    'GoogleMeet',
    'GoogleDrive'
]
