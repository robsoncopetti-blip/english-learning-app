"""
Video Call Screen - Tela de Videochamada
========================================

Tela de videochamada para lições em dupla (pai + filho).
Integra com Google Meet para comunicação em tempo real.

Funcionalidades:
- Vídeo e áudio entre pai e filho
- Chat de texto
- Compartilhamento de tela
- Controles de microfone e câmera
"""

import flet as ft
from datetime import datetime
from lib.integrations.google.meet_integration import GoogleMeet


class VideoCallScreen:
    """
    Tela de videochamada para lições em dupla.
    """
    
    def __init__(self, page: ft.Page, parent_name: str, child_name: str, lesson_name: str, on_back, on_start_lesson):
        """
        Inicializa a tela de videochamada.
        
        Args:
            page: Objeto Page do Flet
            parent_name: Nome do pai
            child_name: Nome da criança
            lesson_name: Nome da lição
            on_back: Função callback para voltar
            on_start_lesson: Função callback para iniciar a lição após a chamada
        """
        self.page = page
        self.parent_name = parent_name
        self.child_name = child_name
        self.lesson_name = lesson_name
        self.on_back = on_back
        self.on_start_lesson = on_start_lesson
        
        # Estados de vídeo e áudio
        self.video_enabled = True
        self.audio_enabled = True
        
        # Google Meet (simulado por enquanto)
        self.meet_link = None
        self.google_meet = GoogleMeet({})
        
        # Inicia a sessão de vídeo
        self._init_video_session()
    
    def _init_video_session(self):
        """
        Inicia a sessão de vídeo chamada.
        """
        # Cria a sessão duo no Google Meet
        start_time = datetime.now()
        self.meet_link = self.google_meet.create_duo_session(
            child_name=self.child_name,
            parent_name=self.parent_name,
            start_time=start_time,
            duration_minutes=30
        )
        
        print(f"Sessão de vídeo iniciada: {self.meet_link}")
    
    def build(self):
        """
        Constrói e retorna a tela de videochamada.
        
        Returns:
            Componente Flet com a tela completa
        """
        # App bar
        app_bar = ft.AppBar(
            title=ft.Text(f"📹 Lição em Dupla: {self.lesson_name}", size=18, weight=ft.FontWeight.BOLD),
            bgcolor=ft.Colors.PURPLE,
            leading=ft.IconButton(
                ft.Icons.CLOSE,
                icon_color=ft.Colors.WHITE,
                on_click=self.handle_end_call
            )
        )
        
        # Placeholder de vídeo do pai
        parent_video = ft.Container(
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.PERSON, size=80, color=ft.Colors.GREY_400),
                    ft.Container(height=10),
                    ft.Text(
                        self.parent_name,
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.GREY_600
                    ),
                    ft.Text(
                        "Pai/Mãe",
                        size=12,
                        color=ft.Colors.GREY_500
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=200,
            height=150,
            bgcolor=ft.Colors.GREY_200,
            border_radius=15,
            alignment=ft.Alignment(-1, -1),
            border=ft.Border.all(3, ft.Colors.PURPLE)
        )
        
        # Placeholder de vídeo da criança
        child_video = ft.Container(
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.CHILD_CARE, size=80, color=ft.Colors.GREY_400),
                    ft.Container(height=10),
                    ft.Text(
                        self.child_name,
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.GREY_600
                    ),
                    ft.Text(
                        "Você",
                        size=12,
                        color=ft.Colors.GREY_500
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=200,
            height=150,
            bgcolor=ft.Colors.GREY_200,
            border_radius=15,
            alignment=ft.Alignment(-1, -1),
            border=ft.Border.all(3, ft.Colors.BLUE)
        )
        
        # Controles de vídeo e áudio
        toggle_video_btn = ft.IconButton(
            ft.Icons.VIDEOCAM,
            icon_color=ft.Colors.WHITE,
            bgcolor=ft.Colors.BLUE if self.video_enabled else ft.Colors.GREY,
            on_click=self.toggle_video
        )
        
        toggle_audio_btn = ft.IconButton(
            ft.Icons.MIC,
            icon_color=ft.Colors.WHITE,
            bgcolor=ft.Colors.BLUE if self.audio_enabled else ft.Colors.GREY,
            on_click=self.toggle_audio
        )
        
        # Botão para iniciar a lição
        start_lesson_btn = ft.FilledButton(
            "Iniciar Lição",
            icon=ft.Icons.PLAY_ARROW,
            bgcolor=ft.Colors.GREEN,
            on_click=self.handle_start_lesson
        )
        
        # Link do Google Meet
        meet_link_text = ft.Text(
            f"Link da chamada: {self.meet_link}",
            size=12,
            color=ft.Colors.GREY_600,
            max_lines=1,
            overflow=ft.TextOverflow.ELLIPSIS
        )
        
        # Container principal
        main_content = ft.Column(
            [
                ft.Container(height=20),
                ft.Text(
                    "👨‍👩‍👧 Sessão Duo: Pai + Filho",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE
                ),
                ft.Container(height=20),
                meet_link_text,
                ft.Container(height=20),
                ft.Row(
                    [parent_video, ft.Container(width=20), child_video],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Container(height=30),
                ft.Text(
                    "Controles",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.GREY_700
                ),
                ft.Container(height=15),
                ft.Row(
                    [toggle_video_btn, ft.Container(width=15), toggle_audio_btn],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Container(height=30),
                start_lesson_btn,
                ft.Container(height=10),
                ft.Text(
                    "Clique em 'Iniciar Lição' quando estiverem prontos",
                    size=12,
                    color=ft.Colors.GREY_600,
                    text_align=ft.TextAlign.CENTER
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
        return ft.Column(
            [
                app_bar,
                ft.Container(content=main_content, expand=True),
            ],
            expand=True
        )
    
    def toggle_video(self, e):
        """
        Liga/desliga o vídeo.
        
        Args:
            e: Evento de clique
        """
        self.video_enabled = not self.video_enabled
        print(f"Vídeo {'ativado' if self.video_enabled else 'desativado'}")
        self.page.update()
    
    def toggle_audio(self, e):
        """
        Liga/desliga o áudio.
        
        Args:
            e: Evento de clique
        """
        self.audio_enabled = not self.audio_enabled
        print(f"Áudio {'ativado' if self.audio_enabled else 'desativado'}")
        self.page.update()
    
    def handle_start_lesson(self, e):
        """
        Inicia a lição após a videochamada.
        
        Args:
            e: Evento de clique
        """
        print("Iniciando lição em modo dupla...")
        self.on_start_lesson()
    
    def handle_end_call(self, e):
        """
        Encerra a chamada de vídeo.
        
        Args:
            e: Evento de clique
        """
        print("Encerrando chamada de vídeo...")
        self.on_back()
