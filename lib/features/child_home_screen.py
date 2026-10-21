"""
Child Home Screen - Tela Principal para Crianças
=================================================

Esta é a tela principal que a criança vê após fazer login.
Design colorido, divertido e interativo com:
- Avatar/personagem
- Pontuação e streak
- Acesso a Dashboard de Lições
- Acesso a Dashboard de Jogos
- Elementos visuais atraentes

Faixas Etárias (Foco: 4-7 anos):
- 4-5 anos: Conteúdo básico, visual
- 5-6 anos: Conteúdo intermediário
- 6-7 anos: Conteúdo avançado com leitura em português
"""

import flet as ft
from lib.features.lessons.colors_lesson import ColorsLesson
from lib.features.lessons.numbers_lesson import NumbersLesson
from lib.features.lessons.animals_lesson import AnimalsLesson
from lib.features.games.memory_game import MemoryGame
from lib.features.games.quiz_game import QuizGame
from lib.core.gamification import GamificationSystem
from lib.core.lesson_types import LessonContent


class ChildHomeScreen:
    """
    Tela principal da versão criança.
    
    Features:
    - Avatar animado
- Display de pontos e streak
- Lista de lições/missões
- Acesso a mini-jogos
- Design colorido e divertido
    """
    
    def __init__(self, page: ft.Page, user_name, on_logout, user_id=None, age_group=None):
        """
        Inicializa a tela principal da criança.
        
        Args:
            page: Objeto Page do Flet
            user_name: Nome da criança
            on_logout: Função callback para fazer logout
            user_id: ID do usuário para sistema de gamificação
            age_group: Faixa etária ('4-5', '5-6', '6-7')
        """
        self.page = page
        self.user_name = user_name
        self.on_logout = on_logout
        self.user_id = user_id or user_name  # Usa o nome como ID se não fornecido
        self.age_group = age_group or "5-6"  # Padrão para teste
        
        # Sistema de conteúdo baseado na faixa etária
        self.lesson_content = LessonContent(self.age_group)
        
        # Sistema de gamificação
        self.gamification = GamificationSystem(self.user_id)
        
        # Obtém estatísticas do usuário
        stats = self.gamification.get_user_stats()
        self.points = stats["points"]
        self.streak = stats["streak"]
        self.level = stats["level"]
        
    def build(self):
        """
        Constrói e retorna o componente da tela principal da criança.
        
        Returns:
            Componente Flet com a tela principal completa
        """
        # AppBar personalizada
        app_bar = ft.AppBar(
            title=ft.Text(f"Olá, {self.user_name}! 👋"),
            bgcolor=ft.Colors.BLUE,
            color=ft.Colors.WHITE,
            actions=[
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
                        "💖 For BETINA - The most beautiful daughter in the world 💖",
                        size=13,
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Text(
                        "Para BETINA - A filha mais linda do mundo",
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
        
        # Card de pontuação
        points_card = ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.STAR, color=ft.Colors.YELLOW, size=20),
                            ft.Text(
                                f"{self.points}",
                                size=22,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.YELLOW
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Text("Pontos", size=10, color=ft.Colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=90,
            height=70,
            bgcolor=ft.Colors.BLUE_700,
            border_radius=10,
            padding=8,
        )
        
        # Card de streak
        streak_card = ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.LOCAL_FIRE_DEPARTMENT, color=ft.Colors.ORANGE, size=20),
                            ft.Text(
                                f"{self.streak}",
                                size=22,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.ORANGE
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Text("Dias", size=10, color=ft.Colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=90,
            height=70,
            bgcolor=ft.Colors.ORANGE_700,
            border_radius=10,
            padding=8,
        )
        
        # Card de nível
        level_card = ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.EMOJI_EVENTS, color=ft.Colors.PURPLE, size=20),
                            ft.Text(
                                f"{self.level}",
                                size=22,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.PURPLE
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Text("Nível", size=10, color=ft.Colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=90,
            height=70,
            bgcolor=ft.Colors.PURPLE_700,
            border_radius=10,
            padding=8,
        )
        
        # Bloco Central - Ramificação de Faixas Etárias
        age_4_7_card = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "4-7",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE
                    ),
                    ft.Text(
                        "Anos",
                        size=11,
                        color=ft.Colors.WHITE_70
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=85,
            height=85,
            bgcolor=ft.Colors.BLUE,
            border_radius=42,
            padding=10,
            alignment=ft.Alignment(-1, -1),
            on_click=self.show_age_modules
        )
        
        age_7_10_card = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "7-10",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.GREY_400
                    ),
                    ft.Text(
                        "Anos",
                        size=11,
                        color=ft.Colors.GREY_500
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=85,
            height=85,
            bgcolor=ft.Colors.GREY_200,
            border_radius=42,
            padding=10,
            alignment=ft.Alignment(-1, -1),
        )
        
        age_10_13_card = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "10-13",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.GREY_400
                    ),
                    ft.Text(
                        "Anos",
                        size=11,
                        color=ft.Colors.GREY_500
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=85,
            height=85,
            bgcolor=ft.Colors.GREY_200,
            border_radius=42,
            padding=10,
            alignment=ft.Alignment(-1, -1),
        )
        
        # Card Lições Dupla (Pai + Filho)
        duo_lessons_card = ft.Container(
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.PEOPLE, size=35, color=ft.Colors.WHITE),
                    ft.Container(height=5),
                    ft.Text(
                        "👨‍👩‍👧",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE
                    ),
                    ft.Text(
                        "Pai + Filho",
                        size=12,
                        color=ft.Colors.WHITE_70
                    ),
                    ft.Text(
                        "Videochamada",
                        size=10,
                        color=ft.Colors.WHITE_24
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=140,
            height=120,
            bgcolor=ft.Colors.PURPLE,
            border_radius=15,
            padding=10,
            alignment=ft.Alignment(-1, -1),
            on_click=self.open_lessons_dashboard
        )
        
        # Card Lições Casa (Revisão)
        home_lessons_card = ft.Container(
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.HOME, size=35, color=ft.Colors.WHITE),
                    ft.Container(height=5),
                    ft.Text(
                        "🏠",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE
                    ),
                    ft.Text(
                        "Tema de Casa",
                        size=12,
                        color=ft.Colors.WHITE_70
                    ),
                    ft.Text(
                        "Revisão",
                        size=10,
                        color=ft.Colors.WHITE_24
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=140,
            height=120,
            bgcolor=ft.Colors.GREEN,
            border_radius=15,
            padding=10,
            alignment=ft.Alignment(-1, -1),
            on_click=self.open_home_lessons_dashboard
        )
        
        # Card Jogos de Aprendizado
        games_card = ft.Container(
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.SPORTS_ESPORTS, size=35, color=ft.Colors.WHITE),
                    ft.Container(height=5),
                    ft.Text(
                        "🎮",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE
                    ),
                    ft.Text(
                        "Jogos",
                        size=12,
                        color=ft.Colors.WHITE_70
                    ),
                    ft.Text(
                        "Aprendizado",
                        size=10,
                        color=ft.Colors.WHITE_24
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=140,
            height=120,
            bgcolor=ft.Colors.ORANGE,
            border_radius=15,
            padding=10,
            alignment=ft.Alignment(-1, -1),
            on_click=self.open_games_dashboard
        )
        
        # Container principal com scroll - Estilo Mapa Mental
        main_content = ft.Column(
            [
                dedication_banner,
                ft.Container(height=15),
                ft.Row(
                    [points_card, ft.Container(width=15), streak_card, ft.Container(width=15), level_card],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Container(height=25),
                ft.Text(
                    "🗺️ Mapa de Aprendizado - Escolha sua Faixa Etária",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.GREY_700
                ),
                ft.Container(height=20),
                # Linha de faixas etárias
                ft.Row(
                    [age_4_7_card, ft.Container(width=15), age_7_10_card, ft.Container(width=15), age_10_13_card],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Container(height=25),
                # Container para módulos (mostra apenas quando selecionado)
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                f"📍 Faixa {self.age_group} Anos - Módulos Disponíveis",
                                size=14,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLUE
                            ),
                            ft.Container(height=15),
                            # Linha superior: Lições Dupla
                            ft.Row(
                                [duo_lessons_card],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Container(height=15),
                            # Linha inferior: Lições Casa e Jogos
                            ft.Row(
                                [home_lessons_card, ft.Container(width=15), games_card],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    padding=15,
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=12,
                    visible=True
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
    
    def create_lesson_card(self, title, description, color, icon):
        """
        Cria um card de lição com design atraente.
        
        Args:
            title: Título da lição
            description: Descrição da lição
            color: Cor do card
            icon: Ícone do card
            
        Returns:
            Componente Container com o card da lição
        """
        # Determina qual lição abrir baseado no título
        def open_lesson(e):
            if title == "Cores":
                lesson = ColorsLesson(self.page, self.return_to_home, self.user_id)
            elif title == "Números":
                lesson = NumbersLesson(self.page, self.return_to_home, self.user_id)
            elif title == "Animais":
                lesson = AnimalsLesson(self.page, self.return_to_home, self.user_id)
            else:
                return
            
            self.page.clean()
            self.page.add(lesson.build())
            self.page.update()
        
        return ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Icon(icon, size=40, color=ft.Colors.WHITE),
                        width=60,
                        height=60,
                        bgcolor=color,
                        border_radius=10,
                    ),
                    ft.Container(width=15),
                    ft.Column(
                        [
                            ft.Text(
                                title,
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLUE_GREY_800
                            ),
                            ft.Text(
                                description,
                                size=14,
                                color=ft.Colors.GREY_600
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        expand=True
                    ),
                    ft.IconButton(
                        ft.Icons.ARROW_FORWARD,
                        icon_color=color,
                        on_click=open_lesson
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=15,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            width=350,
            shadow=ft.BoxShadow(
                blur_radius=10,
                spread_radius=2,
                color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                offset=ft.Offset(0, 2)
            )
        )
    
    def return_to_home(self):
        """
        Retorna à tela principal da criança.
        Recarrega as estatísticas do usuário.
        """
        # Recarrega estatísticas
        stats = self.gamification.get_user_stats()
        self.points = stats["points"]
        self.streak = stats["streak"]
        self.level = stats["level"]
        
        self.page.clean()
        self.page.add(self.build())
        self.page.update()
    
    def handle_logout(self, e):
        """
        Manipula o logout do usuário.
        
        Args:
            e: Evento de clique
        """
        self.on_logout()
    
    def open_lessons_dashboard(self, e):
        """
        Abre o dashboard de lições separado.
        
        Args:
            e: Evento de clique
        """
        lessons_dashboard = LessonsDashboard(
            page=self.page,
            age_group=self.age_group,
            on_back=self.return_to_home,
            user_id=self.user_id
        )
        self.page.clean()
        self.page.add(lessons_dashboard.build())
        self.page.update()
    
    def open_games_dashboard(self, e):
        """
        Abre o dashboard de jogos separado.
        
        Args:
            e: Evento de clique
        """
        games_dashboard = GamesDashboard(
            page=self.page,
            age_group=self.age_group,
            on_back=self.return_to_home,
            user_id=self.user_id
        )
        self.page.clean()
        self.page.add(games_dashboard.build())
        self.page.update()
    
    def open_home_lessons_dashboard(self, e):
        """
        Abre o dashboard de lições de casa (apenas lições normais, sem dupla).
        
        Args:
            e: Evento de clique
        """
        home_lessons_dashboard = HomeLessonsDashboard(
            page=self.page,
            age_group=self.age_group,
            on_back=self.return_to_home,
            user_id=self.user_id
        )
        self.page.clean()
        self.page.add(home_lessons_dashboard.build())
        self.page.update()
    
    def show_age_modules(self, e):
        """
        Mostra os módulos para a faixa 4-7 anos (já ativo por padrão).
        
        Args:
            e: Evento de clique
        """
        print("Mostrando módulos para faixa 4-7 anos")
        # Por enquanto, já está visível no layout


class HomeLessonsDashboard:
    """
    Dashboard separado para lições de casa (tema de casa/revisão).
    Mostra apenas lições normais, sem modo dupla.
    """
    
    def __init__(self, page: ft.Page, age_group: str, on_back, user_id: str):
        """
        Inicializa o dashboard de lições de casa.
        
        Args:
            page: Objeto Page do Flet
            age_group: Faixa etária ('4-5', '5-6', '6-7')
            on_back: Função callback para voltar
            user_id: ID do usuário
        """
        self.page = page
        self.age_group = age_group
        self.on_back = on_back
        self.user_id = user_id
        
        # Sistema de conteúdo
        self.lesson_content = LessonContent(age_group)
        
        # Sistema de gamificação
        self.gamification = GamificationSystem(user_id)
    
    def build(self):
        """
        Constrói e retorna o dashboard de lições de casa.
        
        Returns:
            Componente Flet com o dashboard completo
        """
        # App bar com botão voltar
        app_bar = ft.AppBar(
            title=ft.Text("🏠 Lições de Casa", size=20, weight=ft.FontWeight.BOLD),
            bgcolor=ft.Colors.GREEN,
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                icon_color=ft.Colors.WHITE,
                on_click=lambda e: self.on_back()
            )
        )
        
        # Banner dedicado à Betina
        dedication_banner = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "💖 Made for the most beautiful daughter in the world - BETINA 💖",
                        size=12,
                        color=ft.Colors.PINK,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Text(
                        "Feito para a filha mais linda do mundo - BETINA",
                        size=11,
                        color=ft.Colors.PINK_400,
                        text_align=ft.TextAlign.CENTER
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=10,
            bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.PINK),
            border_radius=10,
        )
        
        # Lições disponíveis
        available_lessons = self.lesson_content.get_available_lessons()
        lesson_cards = []
        
        lesson_configs = {
            "colors": ("Cores", "Aprenda as cores em inglês", ft.Colors.RED, ft.Icons.PALETTE, ColorsLesson),
            "numbers": ("Números", "Conte de 1 a 10", ft.Colors.GREEN, ft.Icons.LOOKS_ONE, NumbersLesson),
            "animals": ("Animais", "Conheça os animais", ft.Colors.PURPLE, ft.Icons.PETS, AnimalsLesson),
            "fruits": ("Frutas", "Nome das frutas", ft.Colors.ORANGE, ft.Icons.LOCAL_DRINK, None),
            "family": ("Família", "Membros da família", ft.Colors.PINK, ft.Icons.PEOPLE, None)
        }
        
        for lesson in available_lessons:
            if lesson in lesson_configs:
                title, desc, color, icon, lesson_class = lesson_configs[lesson]
                lesson_cards.append(self.create_lesson_card(title, desc, color, icon, lesson_class))
                lesson_cards.append(ft.Container(height=15))
        
        # Container principal
        main_content = ft.Column(
            [
                dedication_banner,
                ft.Container(height=20),
                ft.Text(
                    f"Lições de Casa - Faixa {self.age_group} anos (4-7)",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.GREEN
                ),
                ft.Container(height=20),
                ft.Text(
                    "📝 Estude sozinho ou com ajuda de familiar físico",
                    size=14,
                    color=ft.Colors.GREY_600
                ),
                ft.Container(height=20),
            ] + lesson_cards,
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
    
    def create_lesson_card(self, title, description, color, icon, lesson_class):
        """
        Cria um card de lição.
        
        Args:
            title: Título da lição
            description: Descrição
            color: Cor do card
            icon: Ícone
            lesson_class: Classe da lição
            
        Returns:
            Componente Container com o card
        """
        def open_lesson(e):
            """Abre a lição selecionada."""
            if lesson_class:
                lesson = lesson_class(
                    page=self.page,
                    on_back=self.on_back,
                    user_id=self.user_id
                )
                self.page.clean()
                self.page.add(lesson.build())
                self.page.update()
        
        return ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Icon(icon, size=40, color=color),
                        width=60,
                        height=60,
                        bgcolor=ft.Colors.with_opacity(0.1, color),
                        border_radius=10,
                        alignment=ft.Alignment(-1, -1)
                    ),
                    ft.Container(width=15),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(
                                    title,
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.GREY_800
                                ),
                                ft.Text(
                                    description,
                                    size=14,
                                    color=ft.Colors.GREY_600
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=5
                        ),
                        expand=True
                    ),
                    ft.IconButton(
                        ft.Icons.ARROW_FORWARD,
                        icon_color=color,
                        on_click=open_lesson
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=15,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            width=350,
            shadow=ft.BoxShadow(
                blur_radius=10,
                spread_radius=2,
                color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                offset=ft.Offset(0, 2)
            )
        )


class LessonsDashboard:
    """
    Dashboard separado para lições.
    Mostra todas as lições disponíveis para a faixa etária.
    """
    
    def __init__(self, page: ft.Page, age_group: str, on_back, user_id: str):
        """
        Inicializa o dashboard de lições.
        
        Args:
            page: Objeto Page do Flet
            age_group: Faixa etária ('4-5', '5-6', '6-7')
            on_back: Função callback para voltar
            user_id: ID do usuário
        """
        self.page = page
        self.age_group = age_group
        self.on_back = on_back
        self.user_id = user_id
        
        # Sistema de conteúdo
        self.lesson_content = LessonContent(age_group)
        
        # Sistema de gamificação
        self.gamification = GamificationSystem(user_id)
    
    def build(self):
        """
        Constrói e retorna o dashboard de lições.
        
        Returns:
            Componente Flet com o dashboard completo
        """
        # App bar com botão voltar
        app_bar = ft.AppBar(
            title=ft.Text("📚 Lições", size=20, weight=ft.FontWeight.BOLD),
            bgcolor=ft.Colors.BLUE,
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                icon_color=ft.Colors.WHITE,
                on_click=lambda e: self.on_back()
            )
        )
        
        # Banner dedicado à Betina
        dedication_banner = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "💖 Made for the most beautiful daughter in the world - BETINA 💖",
                        size=12,
                        color=ft.Colors.PINK,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Text(
                        "Feito para a filha mais linda do mundo - BETINA",
                        size=11,
                        color=ft.Colors.PINK_400,
                        text_align=ft.TextAlign.CENTER
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=10,
            bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.PINK),
            border_radius=10,
        )
        
        # Lições disponíveis
        available_lessons = self.lesson_content.get_available_lessons()
        
        lesson_configs = {
            "colors": ("Cores", "Aprenda as cores em inglês", ft.Colors.RED, ft.Icons.PALETTE, ColorsLesson),
            "numbers": ("Números", "Conte de 1 a 10", ft.Colors.GREEN, ft.Icons.LOOKS_ONE, NumbersLesson),
            "animals": ("Animais", "Conheça os animais", ft.Colors.PURPLE, ft.Icons.PETS, AnimalsLesson),
            "fruits": ("Frutas", "Nome das frutas", ft.Colors.ORANGE, ft.Icons.LOCAL_DRINK, None),
            "family": ("Família", "Membros da família", ft.Colors.PINK, ft.Icons.PEOPLE, None)
        }
        
        # Lições em Dupla (pai + filho via videochamada)
        duo_lesson_cards = []
        for lesson in available_lessons:
            if lesson in lesson_configs:
                title, desc, color, icon, lesson_class = lesson_configs[lesson]
                duo_lesson_cards.append(self.create_duo_lesson_card(title, desc, color, icon, lesson_class))
                duo_lesson_cards.append(ft.Container(height=15))
        
        # Container principal
        main_content = ft.Column(
            [
                dedication_banner,
                ft.Container(height=20),
                ft.Text(
                    f"Lições em Dupla - Faixa {self.age_group} anos (4-7)",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE
                ),
                ft.Container(height=20),
                ft.Text(
                    "� Aula com Pai/Mãe via videochamada",
                    size=14,
                    color=ft.Colors.GREY_600
                ),
                ft.Container(height=20),
            ] + duo_lesson_cards,
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
    
    def create_lesson_card(self, title, description, color, icon, lesson_class):
        """
        Cria um card de lição para estudo em casa.
        
        Args:
            title: Título da lição
            description: Descrição
            color: Cor do card
            icon: Ícone
            lesson_class: Classe da lição
            
        Returns:
            Componente Container com o card
        """
        def open_lesson(e):
            """Abre a lição selecionada."""
            if lesson_class:
                lesson = lesson_class(
                    page=self.page,
                    on_back=self.on_back,
                    user_id=self.user_id
                )
                self.page.clean()
                self.page.add(lesson.build())
                self.page.update()
        
        return ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Icon(icon, size=40, color=color),
                        width=60,
                        height=60,
                        bgcolor=ft.Colors.with_opacity(0.1, color),
                        border_radius=10,
                        alignment=ft.Alignment(-1, -1)
                    ),
                    ft.Container(width=15),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(
                                    title,
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.GREY_800
                                ),
                                ft.Text(
                                    description,
                                    size=14,
                                    color=ft.Colors.GREY_600
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=5
                        ),
                        expand=True
                    ),
                    ft.IconButton(
                        ft.Icons.ARROW_FORWARD,
                        icon_color=color,
                        on_click=open_lesson
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=15,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            width=350,
            shadow=ft.BoxShadow(
                blur_radius=10,
                spread_radius=2,
                color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                offset=ft.Offset(0, 2)
            )
        )
    
    def create_duo_lesson_card(self, title, description, color, icon, lesson_class):
        """
        Cria um card de lição para estudo em dupla (pai + filho).
        
        Args:
            title: Título da lição
            description: Descrição
            color: Cor do card
            icon: Ícone
            lesson_class: Classe da lição
            
        Returns:
            Componente Container com o card
        """
        # Captura lesson_class no closure
        captured_lesson_class = lesson_class
        
        def open_lesson(e):
            """Abre a lição em modo dupla com videochamada."""
            from lib.features.video_call_screen import VideoCallScreen
            
            # Abre a tela de videochamada
            video_call = VideoCallScreen(
                page=self.page,
                parent_name="Pai/Mãe",  # TODO: Buscar nome real do pai
                child_name=self.user_name,
                lesson_name=title,
                on_back=self.on_back,
                on_start_lesson=lambda: self._open_lesson_after_call(captured_lesson_class)
            )
            self.page.clean()
            self.page.add(video_call.build())
            self.page.update()
        
        return ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Icon(icon, size=40, color=color),
                        width=60,
                        height=60,
                        bgcolor=ft.Colors.with_opacity(0.1, color),
                        border_radius=10,
                        alignment=ft.Alignment(-1, -1)
                    ),
                    ft.Container(width=15),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(
                                    title,
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.GREY_800
                                ),
                                ft.Text(
                                    description,
                                    size=14,
                                    color=ft.Colors.GREY_600
                                ),
                                ft.Text(
                                    "📹 Com Pai/Mãe via videochamada",
                                    size=11,
                                    color=ft.Colors.PURPLE,
                                    weight=ft.FontWeight.BOLD
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=3
                        ),
                        expand=True
                    ),
                    ft.IconButton(
                        ft.Icons.VIDEO_CALL,
                        icon_color=ft.Colors.PURPLE,
                        on_click=open_lesson
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=15,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            width=350,
            shadow=ft.BoxShadow(
                blur_radius=10,
                spread_radius=2,
                color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                offset=ft.Offset(0, 2)
            )
        )
    
    def _open_lesson_after_call(self, lesson_class):
        """
        Abre a lição após a videochamada (modo dupla).
        
        Args:
            lesson_class: Classe da lição (normalmente não usado em duo)
        """
        from lib.features.lessons.duo_lesson import DuoLesson
        
        # Mapeia o nome da lição para a DuoLesson
        lesson_name_map = {
            ColorsLesson: "Cores",
            NumbersLesson: "Números",
            AnimalsLesson: "Animais"
        }
        
        lesson_name = lesson_name_map.get(lesson_class, "Cores")
        
        # Abre a lição em modo dupla
        duo_lesson = DuoLesson(
            page=self.page,
            lesson_name=lesson_name,
            on_back=self.on_back,
            user_id=self.user_name,
            parent_name="Pai/Mãe"  # TODO: Buscar nome real do pai
        )
        self.page.clean()
        self.page.add(duo_lesson.build())
        self.page.update()


class GamesDashboard:
    """
    Dashboard separado para jogos.
    Mostra todos os jogos disponíveis para a faixa etária.
    """
    
    def __init__(self, page: ft.Page, age_group: str, on_back, user_id: str):
        """
        Inicializa o dashboard de jogos.
        
        Args:
            page: Objeto Page do Flet
            age_group: Faixa etária ('4-5', '5-6', '6-7')
            on_back: Função callback para voltar
            user_id: ID do usuário
        """
        self.page = page
        self.age_group = age_group
        self.on_back = on_back
        self.user_id = user_id
        
        # Sistema de gamificação
        self.gamification = GamificationSystem(user_id)
    
    def build(self):
        """
        Constrói e retorna o dashboard de jogos.
        
        Returns:
            Componente Flet com o dashboard completo
        """
        # App bar com botão voltar
        app_bar = ft.AppBar(
            title=ft.Text("🎮 Jogos", size=20, weight=ft.FontWeight.BOLD),
            bgcolor=ft.Colors.ORANGE,
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                icon_color=ft.Colors.WHITE,
                on_click=lambda e: self.on_back()
            )
        )
        
        # Banner dedicado à Betina
        dedication_banner = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "💖 Made for the most beautiful daughter in the world - BETINA 💖",
                        size=12,
                        color=ft.Colors.PINK,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Text(
                        "Feito para a filha mais linda do mundo - BETINA",
                        size=11,
                        color=ft.Colors.PINK_400,
                        text_align=ft.TextAlign.CENTER
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=10,
            bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.PINK),
            border_radius=10,
        )
        
        # Jogos disponíveis (baseados na faixa etária)
        game_cards = []
        
        # Jogos disponíveis para todas as faixas
        game_cards.append(self.create_game_card(
            "Quiz Rápido",
            "Teste seu conhecimento",
            ft.Colors.PINK,
            ft.Icons.QUIZ,
            QuizGame
        ))
        game_cards.append(ft.Container(height=15))
        
        game_cards.append(self.create_game_card(
            "Memória",
            "Encontre os pares",
            ft.Colors.CYAN,
            ft.Icons.GRID_VIEW,
            MemoryGame
        ))
        game_cards.append(ft.Container(height=15))
        
        # Jogos adicionais para faixas mais avançadas
        if self.age_group in ["5-6", "6-7"]:
            game_cards.append(self.create_game_card(
                "Complete a Palavra",
                "Preencha as letras",
                ft.Colors.PURPLE,
                ft.Icons.EDIT,
                None  # Placeholder
            ))
            game_cards.append(ft.Container(height=15))
        
        if self.age_group == "6-7":
            game_cards.append(self.create_game_card(
                "Pronúncia",
                "Pratique a fala",
                ft.Colors.GREEN,
                ft.Icons.MIC,
                None  # Placeholder
            ))
            game_cards.append(ft.Container(height=15))
        
        # Container principal
        main_content = ft.Column(
            [
                dedication_banner,
                ft.Container(height=20),
                ft.Text(
                    f"Jogos para faixa {self.age_group} anos (4-7)",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.ORANGE
                ),
                ft.Container(height=20),
            ] + game_cards,
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
    
    def create_game_card(self, title, description, color, icon, game_class):
        """
        Cria um card de jogo.
        
        Args:
            title: Título do jogo
            description: Descrição
            color: Cor do card
            icon: Ícone
            game_class: Classe do jogo
            
        Returns:
            Componente Container com o card
        """
        def open_game(e):
            """Abre o jogo selecionado."""
            if game_class:
                game = game_class(
                    page=self.page,
                    on_back=self.on_back,
                    user_id=self.user_id
                )
                self.page.clean()
                self.page.add(game.build())
                self.page.update()
        
        return ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Icon(icon, size=40, color=color),
                        width=60,
                        height=60,
                        bgcolor=ft.Colors.with_opacity(0.1, color),
                        border_radius=10,
                        alignment=ft.Alignment(-1, -1)
                    ),
                    ft.Container(width=15),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(
                                    title,
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.GREY_800
                                ),
                                ft.Text(
                                    description,
                                    size=14,
                                    color=ft.Colors.GREY_600
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=5
                        ),
                        expand=True
                    ),
                    ft.IconButton(
                        ft.Icons.ARROW_FORWARD,
                        icon_color=color,
                        on_click=open_game
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=15,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            width=350,
            shadow=ft.BoxShadow(
                blur_radius=10,
                spread_radius=2,
                color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                offset=ft.Offset(0, 2)
            )
        )
    
    def create_game_card(self, title, description, color, icon=None, game_class=None):
        """
        Cria um card de jogo com design atraente.
        
        Args:
            title: Título do jogo
            description: Descrição do jogo
            color: Cor do card
            icon: Ícone do jogo
            game_class: Classe do jogo
            
        Returns:
            Componente Container com o card do jogo
        """
        # Determina qual jogo abrir baseado no título ou game_class
        def open_game(e):
            if game_class:
                game = game_class(self.page, self.return_to_home, self.user_id)
            elif title == "Memória":
                game = MemoryGame(self.page, self.return_to_home, self.user_id)
            elif title == "Quiz Rápido":
                game = QuizGame(self.page, self.return_to_home, self.user_id)
            else:
                return
            
            self.page.clean()
            self.page.add(game.build())
            self.page.update()
        
        # Usa o ícone fornecido ou padrão
        game_icon = icon if icon else ft.Icons.SPORTS_ESPORTS
        
        return ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Icon(game_icon, size=40, color=ft.Colors.WHITE),
                        width=60,
                        height=60,
                        bgcolor=color,
                        border_radius=10,
                    ),
                    ft.Container(width=15),
                    ft.Column(
                        [
                            ft.Text(
                                title,
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLUE_GREY_800
                            ),
                            ft.Text(
                                description,
                                size=14,
                                color=ft.Colors.GREY_600
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        expand=True
                    ),
                    ft.IconButton(
                        ft.Icons.PLAY_ARROW,
                        icon_color=color,
                        on_click=open_game
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=15,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            width=350,
            shadow=ft.BoxShadow(
                blur_radius=10,
                spread_radius=2,
                color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                offset=ft.Offset(0, 2)
            )
        )
    
    def handle_logout(self, e):
        """
        Manipula o clique no botão de logout.
        
        Args:
            e: Evento de clique
        """
        self.on_logout()
