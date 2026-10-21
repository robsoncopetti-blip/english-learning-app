"""
Colors Lesson - Lição de Cores
===============================

Esta lição ensina as cores básicas em inglês para crianças de 5-7 anos.

Estrutura da lição:
1. Introdução: Apresentar as cores com visual
2. Aprendizado: Mostrar cor + nome em inglês + nome em português
3. Quiz: Testar conhecimento com múltipla escolha
4. Conclusão: Mostrar pontuação e oferecer replay

Cores ensinadas:
- Red (Vermelho)
- Blue (Azul)
- Green (Verde)
- Yellow (Amarelo)
- Orange (Laranja)
- Purple (Roxo)
- Pink (Rosa)
- Black (Preto)
- White (Branco)
"""

import flet as ft
from lib.core.gamification import GamificationSystem


class ColorsLesson:
    """
    Lição interativa de cores.
    
    Features:
    - Visual colorido e atraente
    - Navegação por etapas
    - Quiz interativo
    - Feedback visual imediato
    - Pontuação ao final
    """
    
    def __init__(self, page: ft.Page, on_back, user_id=None):
        """
        Inicializa a lição de cores.
        
        Args:
            page: Objeto Page do Flet
            on_back: Função callback para voltar à tela anterior
            user_id: ID do usuário para sistema de gamificação
        """
        self.page = page
        self.on_back = on_back
        self.user_id = user_id or "default_user"
        
        # Sistema de gamificação
        self.gamification = GamificationSystem(self.user_id)
        
        # Dados das cores (inglês, português, código hex)
        self.colors = [
            {"english": "Red", "portuguese": "Vermelho", "color": ft.Colors.RED},
            {"english": "Blue", "portuguese": "Azul", "color": ft.Colors.BLUE},
            {"english": "Green", "portuguese": "Verde", "color": ft.Colors.GREEN},
            {"english": "Yellow", "portuguese": "Amarelo", "color": ft.Colors.YELLOW},
            {"english": "Orange", "portuguese": "Laranja", "color": ft.Colors.ORANGE},
            {"english": "Purple", "portuguese": "Roxo", "color": ft.Colors.PURPLE},
            {"english": "Pink", "portuguese": "Rosa", "color": ft.Colors.PINK},
            {"english": "Black", "portuguese": "Preto", "color": ft.Colors.BLACK},
            {"english": "White", "portuguese": "Branco", "color": ft.Colors.WHITE},
        ]
        
        # Estado da lição
        self.current_step = 0  # 0: intro, 1-9: learning, 10: quiz, 11: conclusion
        self.quiz_score = 0
        self.current_quiz_question = 0
        
    def build(self):
        """
        Constrói e retorna o componente da lição.
        
        Returns:
            Componente Flet com a lição completa
        """
        # AppBar com botão de voltar
        app_bar = ft.AppBar(
            title=ft.Text("🎨 Lição: Cores"),
            bgcolor=ft.Colors.RED,
            color=ft.Colors.WHITE,
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                on_click=lambda e: self.on_back()
            )
        )
        
        # Conteúdo principal baseado no passo atual
        content = self.get_content_for_step()
        
        return ft.Column(
            [
                app_bar,
                ft.Container(content=content, expand=True),
            ],
            expand=True
        )
    
    def get_content_for_step(self):
        """
        Retorna o conteúdo baseado no passo atual da lição.
        
        Returns:
            Componente Flet com o conteúdo do passo atual
        """
        if self.current_step == 0:
            return self.build_intro()
        elif 1 <= self.current_step <= len(self.colors):
            return self.build_learning_step(self.current_step - 1)
        elif self.current_step == len(self.colors) + 1:
            return self.build_quiz_intro()
        elif self.current_step == len(self.colors) + 2:
            return self.build_quiz_question()
        elif self.current_step == len(self.colors) + 3:
            return self.build_conclusion()
        else:
            return self.build_intro()
    
    def build_intro(self):
        """
        Constrói a tela de introdução da lição.
        
        Returns:
            Componente Container com a introdução
        """
        return ft.Container(
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.PALETTE, size=100, color=ft.Colors.RED),
                    ft.Container(height=30),
                    ft.Text(
                        "Vamos aprender as cores!",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_GREY_800,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=20),
                    ft.Text(
                        "Nesta lição você vai aprender 9 cores em inglês.",
                        size=16,
                        color=ft.Colors.GREY_600,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=40),
                    ft.FilledButton(
                        "Começar!",
                        icon=ft.Icons.PLAY_ARROW,
                        width=200,
                        height=50,
                        on_click=lambda e: self.next_step()
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=30,
            alignment=ft.Alignment(-1, -1)
        )
    
    def build_learning_step(self, color_index):
        """
        Constrói uma etapa de aprendizado de uma cor específica.
        
        Args:
            color_index: Índice da cor a ser ensinada
            
        Returns:
            Componente Container com a etapa de aprendizado
        """
        color_data = self.colors[color_index]
        
        # Card da cor
        color_card = ft.Container(
            width=200,
            height=200,
            bgcolor=color_data["color"],
            border_radius=20,
            border=ft.Border.all(3, ft.Colors.GREY_300),
            shadow=ft.BoxShadow(
                blur_radius=20,
                spread_radius=5,
                color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                offset=ft.Offset(0, 5)
            )
        )
        
        # Nome da cor em inglês
        english_name = ft.Text(
            color_data["english"],
            size=48,
            weight=ft.FontWeight.BOLD,
            color=color_data["color"]
        )
        
        # Nome da cor em português
        portuguese_name = ft.Text(
            color_data["portuguese"],
            size=24,
            color=ft.Colors.GREY_600
        )
        
        # Texto explicativo
        explanation = ft.Text(
            f"Esta cor é {color_data['english']} em inglês!",
            size=18,
            color=ft.Colors.BLUE_GREY_700,
            text_align=ft.TextAlign.CENTER
        )
        
        # Botão de próximo
        next_button = ft.FilledButton(
            "Próximo",
            icon=ft.Icons.ARROW_FORWARD,
            width=200,
            height=50,
            on_click=lambda e: self.next_step()
        )
        
        return ft.Container(
            content=ft.Column(
                [
                    color_card,
                    ft.Container(height=30),
                    english_name,
                    ft.Container(height=10),
                    portuguese_name,
                    ft.Container(height=30),
                    explanation,
                    ft.Container(height=40),
                    next_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=30,
            alignment=ft.Alignment(-1, -1)
        )
    
    def build_quiz_intro(self):
        """
        Constrói a tela de introdução do quiz.
        
        Returns:
            Componente Container com a introdução do quiz
        """
        return ft.Container(
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.QUIZ, size=100, color=ft.Colors.PURPLE),
                    ft.Container(height=30),
                    ft.Text(
                        "Hora do Quiz!",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_GREY_800,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=20),
                    ft.Text(
                        "Vamos testar o que você aprendeu.",
                        size=16,
                        color=ft.Colors.GREY_600,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=40),
                    ft.FilledButton(
                        "Começar Quiz",
                        icon=ft.Icons.PLAY_ARROW,
                        width=200,
                        height=50,
                        on_click=lambda e: self.next_step()
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=30,
            alignment=ft.Alignment(-1, -1)
        )
    
    def build_quiz_question(self):
        """
        Constrói uma pergunta do quiz.
        
        Returns:
            Componente Container com a pergunta do quiz
        """
        # Seleciona uma cor aleatória para perguntar
        import random
        target_color = random.choice(self.colors)
        
        # Cria opções de resposta (correta + 3 erradas)
        options = [target_color]
        while len(options) < 4:
            option = random.choice(self.colors)
            if option not in options:
                options.append(option)
        
        random.shuffle(options)
        
        # Pergunta
        question = ft.Text(
            f"Qual é {target_color['english']} em português?",
            size=22,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_GREY_800,
            text_align=ft.TextAlign.CENTER
        )
        
        # Opções de resposta
        option_buttons = []
        for option in options:
            btn = ft.FilledButton(
                option["portuguese"],
                width=250,
                height=50,
                on_click=lambda e, opt=option: self.handle_quiz_answer(opt, target_color)
            )
            option_buttons.append(btn)
        
        return ft.Container(
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.HELP, size=80, color=ft.Colors.PURPLE),
                    ft.Container(height=20),
                    question,
                    ft.Container(height=30),
                    *option_buttons,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=30,
            alignment=ft.Alignment(-1, -1)
        )
    
    def handle_quiz_answer(self, selected_option, correct_option):
        """
        Manipula a resposta do quiz.
        
        Args:
            selected_option: Opção selecionada pelo usuário
            correct_option: Opção correta
        """
        if selected_option["english"] == correct_option["english"]:
            self.quiz_score += 1
            # Mostra feedback positivo
            self.show_feedback(True)
        else:
            # Mostra feedback negativo
            self.show_feedback(False)
    
    def show_feedback(self, is_correct):
        """
        Mostra feedback visual sobre a resposta.
        
        Args:
            is_correct: Se a resposta estava correta
        """
        if is_correct:
            message = "Correto! 🎉"
            color = ft.Colors.GREEN
            icon = ft.Icons.CHECK_CIRCLE
        else:
            message = "Tente novamente! 😊"
            color = ft.Colors.RED
            icon = ft.Icons.CANCEL
        
        # Mostra snack bar com feedback
        snack_bar = ft.SnackBar(
            content=ft.Text(message, color=ft.Colors.WHITE),
            bgcolor=color,
            duration=2000,
        )
        self.page.snack_bar = snack_bar
        self.page.update()
        
        # Avança para conclusão após delay
        self.next_step()
    
    def build_conclusion(self):
        """
        Constrói a tela de conclusão da lição.
        
        Returns:
            Componente Container com a conclusão
        """
        # Adiciona pontos ao usuário
        points_earned = 10 + (self.quiz_score * 5)  # 10 pontos pela lição + 5 por acerto
        self.gamification.add_points(
            points_earned,
            "lesson_completed",
            {"lesson": "colors", "quiz_score": self.quiz_score}
        )
        self.gamification.update_streak()
        
        # Obtém estatísticas atualizadas
        stats = self.gamification.get_user_stats()
        
        # Mensagem baseada na pontuação
        if self.quiz_score >= 3:
            message = "Excelente! Você aprendeu muito! 🌟"
            icon = ft.Icons.STAR
            icon_color = ft.Colors.YELLOW
        else:
            message = "Bom trabalho! Continue praticando! 💪"
            icon = ft.Icons.THUMB_UP
            icon_color = ft.Colors.BLUE
        
        return ft.Container(
            content=ft.Column(
                [
                    ft.Icon(icon, size=100, color=icon_color),
                    ft.Container(height=30),
                    ft.Text(
                        "Lição Completa!",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_GREY_800,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=20),
                    ft.Text(
                        f"Sua pontuação: {self.quiz_score}/4",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PURPLE,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=20),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(
                                    f"+{points_earned} pontos ganhos!",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.GREEN,
                                    text_align=ft.TextAlign.CENTER
                                ),
                                ft.Text(
                                    f"Total: {stats['points']} pontos",
                                    size=16,
                                    color=ft.Colors.GREY_600,
                                    text_align=ft.TextAlign.CENTER
                                ),
                                ft.Text(
                                    f"Streak: {stats['streak']} dias 🔥",
                                    size=16,
                                    color=ft.Colors.ORANGE,
                                    text_align=ft.TextAlign.CENTER
                                ),
                                ft.Text(
                                    f"Nível: {stats['level']} ⭐",
                                    size=16,
                                    color=ft.Colors.YELLOW,
                                    text_align=ft.TextAlign.CENTER
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=15,
                        bgcolor=ft.Colors.GREEN_50,
                        border_radius=10,
                    ),
                    ft.Container(height=20),
                    ft.Text(
                        message,
                        size=18,
                        color=ft.Colors.GREY_600,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=40),
                    ft.FilledButton(
                        "Voltar",
                        icon=ft.Icons.HOME,
                        width=200,
                        height=50,
                        on_click=lambda e: self.on_back()
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=30,
            alignment=ft.Alignment(-1, -1)
        )
    
    def next_step(self):
        """
        Avança para o próximo passo da lição.
        """
        self.current_step += 1
        self.page.clean()
        self.page.add(self.build())
        self.page.update()
