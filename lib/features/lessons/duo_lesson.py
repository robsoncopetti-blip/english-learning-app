"""
Duo Lesson - Lição Colaborativa Pai + Filho
=============================================

Lições especiais para estudo em dupla (pai + filho) com videochamada.
Conteúdo estruturado para 30-50 minutos de aprendizado colaborativo.

Estrutura:
- Fase 1: Introdução (5 minutos)
- Fase 2: Aprendizado conjunto (15-25 minutos)
- Fase 3: Atividade colaborativa (10-15 minutos)
- Fase 4: Revisão e feedback (5 minutos)
"""

import flet as ft
from datetime import datetime, timedelta
from lib.core.gamification import GamificationSystem


class DuoLesson:
    """
    Lição colaborativa para pai e filho.
    """
    
    def __init__(self, page: ft.Page, lesson_name: str, on_back, user_id: str, parent_name: str = "Pai/Mãe"):
        """
        Inicializa a lição em dupla.
        
        Args:
            page: Objeto Page do Flet
            lesson_name: Nome da lição
            on_back: Função callback para voltar
            user_id: ID do usuário
            parent_name: Nome do pai
        """
        self.page = page
        self.lesson_name = lesson_name
        self.on_back = on_back
        self.user_id = user_id
        self.parent_name = parent_name
        
        # Sistema de gamificação
        self.gamification = GamificationSystem(user_id)
        
        # Fases da lição
        self.current_phase = 0
        self.phases = self._get_lesson_phases()
        
        # Timer
        self.start_time = datetime.now()
        self.total_duration = 45  # 45 minutos padrão
        
        # Pontuação colaborativa
        self.duo_score = 0
    
    def _get_lesson_phases(self):
        """
        Retorna as fases da lição baseadas no tipo.
        
        Returns:
            Lista de dicionários com as fases
        """
        lesson_content = {
            "Cores": {
                "phases": [
                    {
                        "title": "🎨 Fase 1: Introdução às Cores",
                        "duration": 5,
                        "content": """
                        <h3>Olá, {child} e {parent}!</h3>
                        <p>Hoje vamos aprender sobre cores juntos!</p>
                        <p><strong>Papel do Pai:</strong> Mostre objetos coloridos ao redor da casa.</p>
                        <p><strong>Papel da Criança:</strong> Diga o nome da cor em inglês.</p>
                        <p>Exemplo: "Look! This is RED!"</p>
                        """,
                        "activity": "Mostrar 3 objetos coloridos e nomear em inglês"
                    },
                    {
                        "title": "🎨 Fase 2: Aprendizado Juntos",
                        "duration": 20,
                        "content": """
                        <h3>Aprendendo Cores em Inglês</h3>
                        <p><strong>Red - Vermelho</strong> /red/</p>
                        <p><strong>Blue - Azul</strong> /bluː/</p>
                        <p><strong>Green - Verde</strong> /griːn/</p>
                        <p><strong>Yellow - Amarelo</strong> /ˈjɛloʊ/</p>
                        
                        <p><strong>Atividade:</strong></p>
                        <ul>
                        <li>Pai: "What color is this?" (apontando para objeto)</li>
                        <li>Criança: "It's [cor]!"</li>
                        <li>Troquem de papéis após 5 minutos</li>
                        </ul>
                        """,
                        "activity": "Praticar pronúncia e identificar cores"
                    },
                    {
                        "title": "🎨 Fase 3: Caça às Cores",
                        "duration": 15,
                        "content": """
                        <h3>Caça às Cores em Casa!</h3>
                        <p><strong>Regras:</strong></p>
                        <ol>
                        <li>Pai pede: "Find something RED!"</li>
                        <li>Criança corre e traz algo vermelho</li>
                        <li>Troquem: Criança pede, Pai busca</li>
                        <li>Pontos: +10 por objeto correto</li>
                        </ol>
                        
                        <p><strong>Bônus:</strong> Façam 3 objetos de cada cor!</p>
                        """,
                        "activity": "Caça às cores pela casa"
                    },
                    {
                        "title": "🎨 Fase 4: Revisão e Celebração",
                        "duration": 5,
                        "content": """
                        <h3>Revisão Final</h3>
                        <p>Responder juntos:</p>
                        <ul>
                        <li>Qual é sua cor favorita?</li>
                        <li>Mostre algo RED!</li>
                        <li>Diga "I love [cor]!"</li>
                        </ul>
                        
                        <p><strong>Parabéns!</strong> Vocês completaram a lição!</p>
                        <p><strong>Pontos ganhos:</strong> {score}</p>
                        """,
                        "activity": "Revisão e celebração"
                    }
                ]
            },
            "Números": {
                "phases": [
                    {
                        "title": "🔢 Fase 1: Contando Juntos",
                        "duration": 5,
                        "content": """
                        <h3>Olá, {child} e {parent}!</h3>
                        <p>Hoje vamos aprender a contar juntos!</p>
                        <p><strong>Papel do Pai:</strong> Conte objetos em voz alta.</p>
                        <p><strong>Papel da Criança:</strong> Repita em inglês.</p>
                        <p>Exemplo: "One, two, three... fingers!"</p>
                        """,
                        "activity": "Contar dedos juntos"
                    },
                    {
                        "title": "🔢 Fase 2: Números 1-10",
                        "duration": 20,
                        "content": """
                        <h3>Aprendendo Números</h3>
                        <p><strong>One - Um</strong> /wʌn/</p>
                        <p><strong>Two - Dois</strong> /tuː/</p>
                        <p><strong>Three - Três</strong> /θriː/</p>
                        <p><strong>Four - Quatro</strong> /fɔːr/</p>
                        <p><strong>Five - Cinco</strong> /faɪv/</p>
                        
                        <p><strong>Atividade:</strong></p>
                        <ul>
                        <li>Pai mostra X dedos: "How many?"</li>
                        <li>Criança responde: "It's [número]!"</li>
                        <li>Pratiquem até 10</li>
                        </ul>
                        """,
                        "activity": "Praticar contagem até 10"
                    },
                    {
                        "title": "🔢 Fase 3: Contando Objetos",
                        "duration": 15,
                        "content": """
                        <h3>Contando Objetos em Casa</h3>
                        <p><strong>Regras:</strong></p>
                        <ol>
                        <li>Pai traz objetos: "How many?"</li>
                        <li>Criança conta em inglês</li>
                        <li>Troquem de papéis</li>
                        <li>Pontos: +5 por contagem correta</li>
                        </ol>
                        
                        <p><strong>Desafio:</strong> Contem até 20!</p>
                        """,
                        "activity": "Contar objetos da casa"
                    },
                    {
                        "title": "🔢 Fase 4: Desafio Final",
                        "duration": 5,
                        "content": """
                        <h3>Desafio Final</h3>
                        <p><strong>Perguntas rápidas:</strong></p>
                        <ul>
                        <li>Conte até 5!</li>
                        <li>Mostre 7 dedos!</li>
                        <li>Diga: "I can count to 10!"</li>
                        </ul>
                        
                        <p><strong>Excelente trabalho!</strong></p>
                        <p><strong>Pontos ganhos:</strong> {score}</p>
                        """,
                        "activity": "Desafio rápido"
                    }
                ]
            },
            "Animais": {
                "phases": [
                    {
                        "title": "🐾 Fase 1: Conhecendo Animais",
                        "duration": 5,
                        "content": """
                        <h3>Olá, {child} e {parent}!</h3>
                        <p>Hoje vamos aprender nomes de animais!</p>
                        <p><strong>Papel do Pai:</strong> Mostre fotos ou brinquedos.</p>
                        <p><strong>Papel da Criança:</strong> Diga o nome em inglês.</p>
                        <p>Exemplo: "This is a DOG!"</p>
                        """,
                        "activity": "Mostrar fotos de animais"
                    },
                    {
                        "title": "🐾 Fase 2: Nomes de Animais",
                        "duration": 20,
                        "content": """
                        <h3>Aprendendo Animais</h3>
                        <p><strong>Dog - Cachorro</strong> /dɔɡ/</p>
                        <p><strong>Cat - Gato</strong> /kæt/</p>
                        <p><strong>Bird - Pássaro</strong> /bɜːrd/</p>
                        <p><strong>Fish - Peixe</strong> /fɪʃ/</p>
                        
                        <p><strong>Atividade:</strong></p>
                        <ul>
                        <li>Pai imita animal: "What animal is this?"</li>
                        <li>Criança adivinha em inglês</li>
                        <li>Troquem de papéis</li>
                        </ul>
                        """,
                        "activity": "Adivinhar animais"
                    },
                    {
                        "title": "🐾 Fase 3: Sons dos Animais",
                        "duration": 15,
                        "content": """
                        <h3>Sons dos Animais em Inglês</h3>
                        <p><strong>Dog says: Woof woof!</strong></p>
                        <p><strong>Cat says: Meow meow!</strong></p>
                        <p><strong>Bird says: Tweet tweet!</strong></p>
                        <p><strong>Fish says: Blub blub!</strong></p>
                        
                        <p><strong>Atividade:</strong></p>
                        <ul>
                        <li>Pai faz som: "What animal?"</li>
                        <li>Criança responde em inglês</li>
                        <li>Pontos: +10 por acerto</li>
                        </ul>
                        """,
                        "activity": "Adivinhar pelo som"
                    },
                    {
                        "title": "🐾 Fase 4: Show de Talentos",
                        "duration": 5,
                        "content": """
                        <h3>Show de Talentos!</h3>
                        <p><strong>Atividade final:</strong></p>
                        <ul>
                        <li>Criança imita um animal</li>
                        <li>Pai adivinha em inglês</li>
                        <li>Troquem e façam de novo</li>
                        </ul>
                        
                        <p><strong>Muito bem!</strong></p>
                        <p><strong>Pontos ganhos:</strong> {score}</p>
                        """,
                        "activity": "Show de talentos"
                    }
                ]
            }
        }
        
        return lesson_content.get(self.lesson_name, {}).get("phases", [])
    
    def build(self):
        """
        Constrói e retorna a tela da lição em dupla.
        
        Returns:
            Componente Flet com a lição completa
        """
        if self.current_phase >= len(self.phases):
            return self.build_completion()
        
        current_phase_data = self.phases[self.current_phase]
        
        # App bar
        app_bar = ft.AppBar(
            title=ft.Text(f"📹 {self.lesson_name} - Dupla", size=18, weight=ft.FontWeight.BOLD),
            bgcolor=ft.Colors.PURPLE,
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                icon_color=ft.Colors.WHITE,
                on_click=lambda e: self.on_back()
            )
        )
        
        # Timer
        elapsed = (datetime.now() - self.start_time).total_seconds() / 60
        timer_text = ft.Text(
            f"⏱️ Tempo: {int(elapsed)} min | Fase {self.current_phase + 1}/{len(self.phases)}",
            size=14,
            color=ft.Colors.GREY_600
        )
        
        # Container do conteúdo
        content_container = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        current_phase_data["title"],
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PURPLE
                    ),
                    ft.Container(height=10),
                    ft.Text(
                        f"⏱️ Duração estimada: {current_phase_data['duration']} minutos",
                        size=14,
                        color=ft.Colors.GREY_600
                    ),
                    ft.Container(height=20),
                    ft.Text(
                        current_phase_data["content"].format(
                            child=self.user_name,
                            parent=self.parent_name,
                            score=self.duo_score
                        ),
                        size=14,
                        color=ft.Colors.GREY_800
                    ),
                    ft.Container(height=20),
                    ft.Container(
                        content=ft.Text(
                            f"📌 Atividade: {current_phase_data['activity']}",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE
                        ),
                        padding=15,
                        bgcolor=ft.Colors.BLUE_50,
                        border_radius=10
                    ),
                ],
                scroll=ft.ScrollMode.AUTO,
            ),
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            expand=True
        )
        
        # Botão próxima fase
        next_button = ft.FilledButton(
            "Próxima Fase ➡️",
            icon=ft.Icons.ARROW_FORWARD,
            bgcolor=ft.Colors.PURPLE,
            on_click=self.next_phase
        )
        
        # Container principal
        main_content = ft.Column(
            [
                timer_text,
                ft.Container(height=20),
                content_container,
                ft.Container(height=20),
                next_button,
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
    
    def next_phase(self, e):
        """
        Avança para a próxima fase da lição.
        
        Args:
            e: Evento de clique
        """
        # Adiciona pontos por completar fase
        self.duo_score += 10
        
        self.current_phase += 1
        self.page.clean()
        self.page.add(self.build())
        self.page.update()
    
    def build_completion(self):
        """
        Constrói a tela de conclusão da lição em dupla.
        
        Returns:
            Componente Flet com a tela de conclusão
        """
        # Calcula tempo total
        total_time = (datetime.now() - self.start_time).total_seconds() / 60
        
        # Atualiza gamificação
        self.gamification.add_points(self.duo_score)
        self.gamification.increment_streak()
        
        # App bar
        app_bar = ft.AppBar(
            title=ft.Text("🎉 Lição Concluída!", size=18, weight=ft.FontWeight.BOLD),
            bgcolor=ft.Colors.GREEN,
            leading=ft.IconButton(
                ft.Icons.CHECK,
                icon_color=ft.Colors.WHITE,
                on_click=lambda e: self.on_back()
            )
        )
        
        # Container principal
        main_content = ft.Column(
            [
                ft.Icon(ft.Icons.EMOJI_EVENTS, size=100, color=ft.Colors.GOLD),
                ft.Container(height=20),
                ft.Text(
                    "Parabéns!",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.GREEN
                ),
                ft.Text(
                    f"{self.parent_name} e {self.user_name}",
                    size=20,
                    color=ft.Colors.GREY_600
                ),
                ft.Container(height=30),
                ft.Text(
                    f"⏱️ Tempo total: {int(total_time)} minutos",
                    size=18,
                    color=ft.Colors.GREY_700
                ),
                ft.Container(height=15),
                ft.Text(
                    f"⭐ Pontos ganhos: {self.duo_score}",
                    size=18,
                    color=ft.Colors.GREY_700
                ),
                ft.Container(height=30),
                ft.FilledButton(
                    "Voltar ao Dashboard",
                    icon=ft.Icons.HOME,
                    bgcolor=ft.Colors.BLUE,
                    on_click=lambda e: self.on_back()
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
        return ft.Column(
            [
                app_bar,
                ft.Container(content=main_content, expand=True),
            ],
            expand=True
        )
