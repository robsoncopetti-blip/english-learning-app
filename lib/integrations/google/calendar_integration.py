"""
Google Calendar Integration - Integração com Google Agenda
=========================================================

Este módulo gerencia a integração com Google Calendar.

Funcionalidades:
- Criar eventos de estudo
- Listar eventos
- Atualizar eventos
- Sincronizar calendário
"""

from typing import List, Dict, Optional
from datetime import datetime, timedelta


class GoogleCalendar:
    """
    Cliente para Google Calendar API.
    """
    
    def __init__(self, credentials: Dict):
        """
        Inicializa o cliente Google Calendar.
        
        Args:
            credentials: Dicionário com access_token e refresh_token
        """
        self.credentials = credentials
        self.service = None
        self._init_service()
    
    def _init_service(self):
        """
        Inicializa o serviço Google Calendar.
        
        NOTA: Requer configuração de credenciais reais.
        """
        try:
            from googleapiclient.discovery import build
            from google.oauth2.credentials import Credentials
            
            creds = Credentials(
                token=self.credentials.get("access_token"),
                refresh_token=self.credentials.get("refresh_token"),
                token_uri="https://oauth2.googleapis.com/token",
                client_id="YOUR_CLIENT_ID",
                client_secret="YOUR_CLIENT_SECRET",
                scopes=["https://www.googleapis.com/auth/calendar"]
            )
            
            self.service = build("calendar", "v3", credentials=creds)
            
        except Exception as e:
            print(f"Erro ao inicializar Google Calendar: {e}")
            self.service = None
    
    def create_study_event(
        self,
        title: str,
        start_time: datetime,
        duration_minutes: int = 30,
        description: str = "",
        attendees: Optional[List[str]] = None
    ) -> bool:
        """
        Cria um evento de estudo no calendário.
        
        Args:
            title: Título do evento
            start_time: Data e hora de início
            duration_minutes: Duração em minutos
            description: Descrição do evento
            attendees: Lista de emails dos participantes
            
        Returns:
            True se criado com sucesso
        """
        if not self.service:
            # Modo simulação para demonstração
            print(f"[SIMULAÇÃO] Evento criado: {title}")
            print(f"  Início: {start_time}")
            print(f"  Duração: {duration_minutes} minutos")
            print(f"  Descrição: {description}")
            if attendees:
                print(f"  Participantes: {', '.join(attendees)}")
            return True
        
        try:
            end_time = start_time + timedelta(minutes=duration_minutes)
            
            event = {
                "summary": title,
                "description": description,
                "start": {
                    "dateTime": start_time.isoformat(),
                    "timeZone": "America/Sao_Paulo",
                },
                "end": {
                    "dateTime": end_time.isoformat(),
                    "timeZone": "America/Sao_Paulo",
                },
            }
            
            if attendees:
                event["attendees"] = [{"email": email} for email in attendees]
            
            self.service.events().insert(
                calendarId="primary",
                body=event
            ).execute()
            
            return True
            
        except Exception as e:
            print(f"Erro ao criar evento: {e}")
            return False
    
    def list_events(self, days_ahead: int = 7) -> List[Dict]:
        """
        Lista eventos dos próximos dias.
        
        Args:
            days_ahead: Número de dias à frente
            
        Returns:
            Lista de eventos
        """
        if not self.service:
            # Modo simulação
            return []
        
        try:
            now = datetime.utcnow().isoformat() + "Z"
            time_max = (datetime.utcnow() + timedelta(days=days_ahead)).isoformat() + "Z"
            
            events_result = self.service.events().list(
                calendarId="primary",
                timeMin=now,
                timeMax=time_max,
                singleEvents=True,
                orderBy="startTime"
            ).execute()
            
            events = events_result.get("items", [])
            return events
            
        except Exception as e:
            print(f"Erro ao listar eventos: {e}")
            return []
    
    def create_duo_meeting(
        self,
        child_name: str,
        parent_name: str,
        start_time: datetime,
        duration_minutes: int = 30
    ) -> Optional[str]:
        """
        Cria um evento de estudo pai-filho.
        
        Args:
            child_name: Nome da criança
            parent_name: Nome do pai
            start_time: Data e hora de início
            duration_minutes: Duração em minutos
            
        Returns:
            Link do Meet se criado com sucesso
        """
        title = f"Sessão de Estudo: {child_name} e {parent_name}"
        description = f"Sessão de estudo conjunto para aprender inglês."
        
        # Cria o evento
        success = self.create_study_event(
            title=title,
            start_time=start_time,
            duration_minutes=duration_minutes,
            description=description
        )
        
        if success:
            # Em produção, aqui integraria com Google Meet
            # Para simulação, retorna um link fictício
            meet_link = f"https://meet.google.com/simulated-{datetime.now().timestamp()}"
            return meet_link
        
        return None
