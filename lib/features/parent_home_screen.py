"""
Parent Home Screen - Tela Principal para Pais
==============================================

Esta é a tela principal que o pai vê após fazer login.
Dashboard para acompanhar o progresso da criança com:
- Resumo do progresso
- Estatísticas
- Enviar desafios
- Configurações
- Link para a versão criança (modo dupla)
"""

import flet as ft
from lib.core.gamification import GamificationSystem


class ParentHomeScreen:
    """
    Tela principal da versão pai.
    
    Features:
    - Dashboard de progresso da criança
    - Estatísticas de aprendizado
    - Opção de enviar desafios
    - Configurações do perfil
    - Acesso ao modo dupla
    """
    
    def __init__(self, page: ft.Page, user_name, on_logout, child_user_id=None):
        """
        Inicializa a tela principal do pai.
        
        Args:
            page: Objeto Page do Flet
            user_name: Nome do pai
            on_logout: Função callback para fazer logout
            child_user_id: ID da criança para buscar dados do gamification
        """
        self.page = page
        self.user_name = user_name
        self.on_logout = on_logout
        self.child_user_id = child_user_id or "default_child"
        
        # Sistema de gamificação da criança
        self.gamification = GamificationSystem(self.child_user_id)
        
        # Obtém estatísticas da criança
        self.child_stats = self.gamification.get_user_stats()
        self.child_achievements = self.gamification.get_user_achievements()
        self.child_history = self.gamification.get_activity_history(limit=5)
        
    def build(self):
        """
        Constrói e retorna o componente da tela principal do pai.
        
        Returns:
            Componente Flet com a tela principal completa
        """
        # AppBar personalizada
        app_bar = ft.AppBar(
            title=ft.Text(f"Painel do Pai - {self.user_name}"),
            bgcolor=ft.Colors.ORANGE,
            color=ft.Colors.WHITE,
            actions=[
                ft.IconButton(
                    ft.Icons.SETTINGS,
                    tooltip="Configurações",
                    on_click=lambda e: print("Configurações")
                ),
                ft.IconButton(
                    ft.Icons.LOGOUT,
                    tooltip="Sair",
                    on_click=self.handle_logout
                )
            ]
        )
        
        # Mensagem especial dedicada à Betina
        dedication_banner = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "💖 Made with love for BETINA - The most beautiful daughter 💖",
                        size=13,
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Text(
                        "Feito com amor para BETINA - A filha mais linda",
                        size=12,
                        color=ft.Colors.WHITE_70,
                        text_align=ft.TextAlign.CENTER
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=15,
            bgcolor=ft.Colors.PINK,
            width=400,
        )
        
        # Card de resumo do progresso
        progress_card = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "📊 Progresso da Criança",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE
                    ),
                    ft.Container(height=15),
                    ft.Row(
                        [
                            self.create_stat_item("Pontos", str(self.child_stats["points"]), ft.Colors.YELLOW),
                            ft.Container(width=20),
                            self.create_stat_item("Streak", f"{self.child_stats['streak']} dias", ft.Colors.ORANGE),
                            ft.Container(width=20),
                            self.create_stat_item("Nível", str(self.child_stats["level"]), ft.Colors.PURPLE),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=20,
            bgcolor=ft.Colors.BLUE_700,
            border_radius=20,
        )
        
        # Seção de desafios
        challenges_section = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "🎯 Enviar Desafio",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE
                    ),
                    ft.Container(height=15),
                    ft.TextField(
                        label="Título do desafio",
                        hint_text="Ex: Aprender 5 palavras novas",
                        border_radius=10,
                    ),
                    ft.Container(height=10),
                    ft.TextField(
                        label="Descrição",
                        hint_text="Detalhes do desafio",
                        border_radius=10,
                        multiline=True,
                        min_lines=2,
                    ),
                    ft.Container(height=15),
                    ft.FilledButton(
                        "Enviar Desafio",
                        icon=ft.Icons.SEND,
                        width=200,
                        on_click=lambda e: print("Desafio enviado!")
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            padding=20,
            bgcolor=ft.Colors.BLUE_50,
            border_radius=20,
        )
        
        # Seção de histórico
        history_section = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "📜 Histórico de Atividades",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.ORANGE
                    ),
                    ft.Container(height=15),
                    self._build_history_list(),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            padding=20,
            bgcolor=ft.Colors.ORANGE_50,
            border_radius=20,
        )
        
        # Botão para modo dupla
        duo_mode_button = ft.Container(
            content=ft.FilledButton(
                "👨‍👧 Modo Dupla",
                icon=ft.Icons.PEOPLE,
                width=300,
                height=50,
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.PURPLE,
                    color=ft.Colors.WHITE,
                ),
                on_click=lambda e: print("Iniciando modo dupla...")
            ),
            padding=20,
        )
        
        # Seção de conquistas
        achievements_section = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "🏆 Conquistas",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PURPLE
                    ),
                    ft.Container(height=15),
                    self._build_achievements_list(),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            padding=20,
            bgcolor=ft.Colors.PURPLE_50,
            border_radius=20,
        )
        
        # Container principal com scroll
        main_content = ft.Column(
            [
                dedication_banner,
                ft.Container(height=20),
                progress_card,
                ft.Container(height=20),
                challenges_section,
                ft.Container(height=20),
                history_section,
                ft.Container(height=20),
                achievements_section,
                ft.Container(height=20),
                duo_mode_button,
            ],
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.center,
        )
        
        return ft.Column(
            [
                app_bar,
                ft.Container(content=main_content, expand=True),
            ],
            expand=True
        )
    
    def create_stat_item(self, label, value, color):
        """
        Cria um item de estatística.
        
        Args:
            label: Texto descritivo
            value: Valor da estatística
            color: Cor do ícone
            
        Returns:
            Componente Container com o item de estatística
        """
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        value,
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE
                    ),
                    ft.Text(
                        label,
                        size=12,
                        color=ft.Colors.WHITE70
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=100,
            padding=10,
            bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.WHITE),
            border_radius=10,
        )
    
    def _build_history_list(self):
        """
        Constrói a lista de histórico de atividades baseada nos dados reais.
        
        Returns:
            Lista de componentes com o histórico
        """
        if not self.child_history:
            return ft.Text(
                "Nenhuma atividade registrada ainda.",
                size=14,
                color=ft.Colors.GREY_600,
                text_align=ft.TextAlign.CENTER
            )
        
        history_items = []
        for activity in self.child_history:
            # Formata o tipo de atividade
            activity_type = activity["type"]
            if activity_type == "lesson_completed":
                title = f"Lição: {activity['data'].get('lesson', 'Desconhecida')}"
                status = f"+{activity['points']} pontos"
            elif activity_type == "quiz_completed":
                title = "Quiz Rápido"
                score = activity["data"].get("score", 0)
                total = activity["data"].get("total", 5)
                status = f"{score}/{total} acertos"
            elif activity_type == "game_completed":
                game_name = activity["data"].get("game", "Jogo")
                title = f"Jogo: {game_name}"
                status = f"+{activity['points']} pontos"
            else:
                title = activity_type
                status = f"+{activity['points']} pontos"
            
            # Formata a data
            timestamp = activity["timestamp"]
            date_str = timestamp.split(" ")[0] if " " in timestamp else timestamp
            
            # Cria o item
            item = self.create_history_item(title, status, date_str, ft.Colors.GREEN)
            history_items.append(item)
            history_items.append(ft.Container(height=10))
        
        return ft.Column(history_items)
    
    def _build_achievements_list(self):
        """
        Constrói a lista de conquistas da criança.
        
        Returns:
            Lista de componentes com as conquistas
        """
        if not self.child_achievements:
            return ft.Text(
                "Nenhuma conquista ainda. Continue estudando!",
                size=14,
                color=ft.Colors.GREY_600,
                text_align=ft.TextAlign.CENTER
            )
        
        achievement_items = []
        for achievement in self.child_achievements:
            # Cria o item da conquista
            if achievement["achieved"]:
                # Conquista desbloqueada
                item = ft.Container(
                    content=ft.Row(
                        [
                            ft.Text(
                                achievement["icon"],
                                size=30,
                            ),
                            ft.Container(width=15),
                            ft.Column(
                                [
                                    ft.Text(
                                        achievement["name"],
                                        size=16,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.BLUE_GREY_800
                                    ),
                                    ft.Text(
                                        achievement["description"],
                                        size=12,
                                        color=ft.Colors.GREY_600
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                expand=True
                            ),
                            ft.Icon(
                                ft.Icons.CHECK_CIRCLE,
                                color=ft.Colors.GREEN,
                                size=20
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    padding=15,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    width=350,
                )
            else:
                # Conquista bloqueada
                item = ft.Container(
                    content=ft.Row(
                        [
                            ft.Text(
                                "🔒",
                                size=30,
                            ),
                            ft.Container(width=15),
                            ft.Column(
                                [
                                    ft.Text(
                                        achievement["name"],
                                        size=16,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.GREY_400
                                    ),
                                    ft.Text(
                                        achievement["description"],
                                        size=12,
                                        color=ft.Colors.GREY_400
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                expand=True
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    padding=15,
                    bgcolor=ft.Colors.GREY_100,
                    border_radius=10,
                    width=350,
                )
            
            achievement_items.append(item)
            achievement_items.append(ft.Container(height=10))
        
        return ft.Column(achievement_items)
    
    def create_history_item(self, title, status, date, color):
        """
        Cria um item de histórico.
        
        Args:
            title: Título da atividade
            status: Status da atividade
            date: Data da atividade
            color: Cor do status
            
        Returns:
            Componente Container com o item de histórico
        """
        return ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Icon(ft.Icons.CHECK_CIRCLE, size=30, color=color),
                        width=50,
                        alignment=ft.Alignment(-1, -1)
                    ),
                    ft.Container(width=15),
                    ft.Column(
                        [
                            ft.Text(
                                title,
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLUE_GREY_800
                            ),
                            ft.Text(
                                f"{status} • {date}",
                                size=14,
                                color=ft.Colors.GREY_600
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        expand=True
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=15,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            width=350,
        )
    
    def handle_logout(self, e):
        """
        Manipula o clique no botão de logout.
        
        Args:
            e: Evento de clique
        """
        self.on_logout()
