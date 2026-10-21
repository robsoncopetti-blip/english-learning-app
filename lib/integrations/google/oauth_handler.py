"""
Google OAuth Handler - Autenticação Google
==========================================

Este módulo gerencia a autenticação com Google OAuth 2.0.

Para uso em produção:
1. Criar projeto em https://console.cloud.google.com
2. Habilitar Google OAuth
3. Configurar OAuth consent screen
4. Obter Client ID e Client Secret
5. Adicionar as credenciais abaixo

Scopes necessários:
- openid: Para login básico
- email: Para obter email do usuário
- profile: Para obter nome e foto
- https://www.googleapis.com/auth/calendar: Para Google Calendar
- https://www.googleapis.com/auth/meetings: Para Google Meet
- https://www.googleapis.com/auth/drive: Para Google Drive
"""

import flet as ft
from typing import Optional, Dict, Callable
import json


class GoogleOAuthHandler:
    """
    Handler para autenticação Google OAuth 2.0.
    
    Para produção, configure as credenciais reais do Google Cloud Console.
    """
    
    # CREDENCIAIS DO GOOGLE (Substituir pelas credenciais reais)
    CLIENT_ID = "YOUR_GOOGLE_CLIENT_ID.apps.googleusercontent.com"
    CLIENT_SECRET = "YOUR_GOOGLE_CLIENT_SECRET"
    REDIRECT_URI = "http://localhost:8501"  # Para Flet web
    
    # Scopes necessários
    SCOPES = [
        "openid",
        "email",
        "profile",
        "https://www.googleapis.com/auth/calendar",
        "https://www.googleapis.com/auth/drive",
    ]
    
    def __init__(self):
        """Inicializa o handler OAuth."""
        self.access_token = None
        self.refresh_token = None
        self.user_info = None
        self.authenticated = False
    
    def is_configured(self) -> bool:
        """
        Verifica se as credenciais Google estão configuradas.
        
        Returns:
            True se configurado, False caso contrário
        """
        return (
            self.CLIENT_ID != "YOUR_GOOGLE_CLIENT_ID.apps.googleusercontent.com"
            and self.CLIENT_SECRET != "YOUR_GOOGLE_CLIENT_SECRET"
        )
    
    def authenticate(self, on_success: Callable, on_error: Callable):
        """
        Inicia o fluxo de autenticação OAuth.
        
        Args:
            on_success: Callback quando autenticação for bem-sucedida
            on_error: Callback quando houver erro
        """
        if not self.is_configured():
            # Se não configurado, usa modo simulação para demonstração
            self._simulate_auth(on_success, on_error)
        else:
            # Usa OAuth real (requer implementação com webbrowser)
            self._real_auth(on_success, on_error)
    
    def _simulate_auth(self, on_success: Callable, on_error: Callable):
        """
        Simula autenticação para demonstração.
        
        Args:
            on_success: Callback quando autenticação for bem-sucedida
            on_error: Callback quando houver erro
        """
        # Dados simulados do usuário
        simulated_user = {
            "email": "usuario@gmail.com",
            "name": "Usuário de Teste",
            "given_name": "Usuário",
            "family_name": "de Teste",
            "picture": "https://lh3.googleusercontent.com/a/default-user",
            "locale": "pt-BR"
        }
        
        self.user_info = simulated_user
        self.authenticated = True
        self.access_token = "simulated_access_token"
        
        # Chama callback de sucesso
        on_success(simulated_user)
    
    def _real_auth(self, on_success: Callable, on_error: Callable):
        """
        Autenticação real com Google OAuth.
        
        NOTA: Requer implementação com webbrowser para abrir
        a URL de autorização do Google.
        
        Args:
            on_success: Callback quando autenticação for bem-sucedida
            on_error: Callback quando houver erro
        """
        try:
            import webbrowser
            from google_auth_oauthlib.flow import InstalledAppFlow
            
            # Cria o flow OAuth
            flow = InstalledAppFlow.from_client_config(
                {
                    "installed": {
                        "client_id": self.CLIENT_ID,
                        "client_secret": self.CLIENT_SECRET,
                        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                        "token_uri": "https://oauth2.googleapis.com/token",
                        "redirect_uris": [self.REDIRECT_URI]
                    }
                },
                scopes=self.SCOPES
            )
            
            # Abre o navegador para autenticação
            flow.run_local_server(port=8080, open_browser=True)
            
            # Obtém as credenciais
            credentials = flow.credentials
            
            self.access_token = credentials.token
            self.refresh_token = credentials.refresh_token
            self.authenticated = True
            
            # Obtém informações do usuário
            self.user_info = self._get_user_info(credentials.token)
            
            on_success(self.user_info)
            
        except Exception as e:
            on_error(str(e))
    
    def _get_user_info(self, access_token: str) -> Dict:
        """
        Obtém informações do usuário do Google.
        
        Args:
            access_token: Token de acesso
            
        Returns:
            Dicionário com informações do usuário
        """
        import requests
        
        url = "https://www.googleapis.com/oauth2/v3/userinfo"
        headers = {"Authorization": f"Bearer {access_token}"}
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        
        return {}
    
    def get_credentials(self):
        """
        Retorna as credenciais OAuth.
        
        Returns:
            Dicionário com access_token e refresh_token
        """
        return {
            "access_token": self.access_token,
            "refresh_token": self.refresh_token
        }
    
    def logout(self):
        """Faz logout do usuário."""
        self.access_token = None
        self.refresh_token = None
        self.user_info = None
        self.authenticated = False


def create_google_login_button(on_click: Callable) -> ft.FilledButton:
    """
    Cria um botão de login com estilo Google.
    
    Args:
        on_click: Callback quando clicado
        
    Returns:
        Componente ElevatedButton estilizado
    """
    return ft.FilledButton(
        content=ft.Row(
            [
                ft.Image(
                    src="https://www.google.com/favicon.ico",
                    width=20,
                    height=20,
                ),
                ft.Container(width=10),
                ft.Text("Entrar com Google"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        width=300,
        height=50,
        bgcolor=ft.Colors.WHITE,
        color=ft.Colors.BLACK,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=5),
            side=ft.BorderSide(1, ft.Colors.GREY_300),
        ),
        on_click=on_click
    )
