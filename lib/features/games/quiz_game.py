"""
Quiz Game - Quiz Rápido
========================

Quiz rápido para testar o vocabulário aprendido.
Perguntas de múltipla escolha com tempo limite.

Features:
- Perguntas aleatórias sobre cores, números e animais
- 4 opções de resposta
- Tempo limite por pergunta
- Sistema de pontuação
- Feedback visual imediato
"""

import flet as ft
import random
from lib.core.gamification import GamificationSystem


class QuizGame:
    """
    Quiz rápido interativo.
    
    Features:
    - Perguntas de múltipla escolha
    - Tema variado (cores, números, animais)
    - Contador de tempo
    - Sistema de pontuação
    - Integração com gamificação
    """
    
    def __init__(self, page: ft.Page, on_back, user_id=None):
        """
        Inicializa o quiz.
        
        Args:
            page: Objeto Page do Flet
            on_back: Função callback para voltar
            user_id: ID do usuário para gamificação
        """
        self.page = page
        self.on_back = on_back
        self.user_id = user_id or "default_user"
        
        # Sistema de gamificação
        self.gamification = GamificationSystem(self.user_id)
        
        # Banco de perguntas
        self.questions = [
            # Cores
            {"question": "What color is RED?", "correct": "Vermelho", "options": ["Azul", "Verde", "Vermelho", "Amarelo"]},
            {"question": "What color is BLUE?", "correct": "Azul", "options": ["Vermelho", "Azul", "Roxo", "Laranja"]},
            {"question": "What color is GREEN?", "correct": "Verde", "options": ["Amarelo", "Verde", "Preto", "Branco"]},
            {"question": "What color is YELLOW?", "correct": "Amarelo", "options": ["Rosa", "Amarelo", "Cinza", "Marrom"]},
            # Números
            {"question": "What is ONE in Portuguese?", "correct": "Um", "options": ["Dois", "Três", "Um", "Quatro"]},
            {"question": "What is FIVE in Portuguese?", "correct": "Cinco", "options": ["Seis", "Sete", "Cinco", "Oito"]},
            {"question": "What is TEN in Portuguese?", "correct": "Dez", "options": ["Nove", "Dez", "Oito", "Sete"]},
            # Animais
            {"question": "What is DOG in Portuguese?", "correct": "Cachorro", "options": ["Gato", "Pássaro", "Cachorro", "Peixe"]},
            {"question": "What is CAT in Portuguese?", "correct": "Gato", "options": ["Cachorro", "Gato", "Coelho", "Leão"]},
            {"question": "What is BIRD in Portuguese?", "correct": "Pássaro", "options": ["Peixe", "Pássaro", "Macaco", "Elefante"]},
        ]
        
        # Estado do jogo
        self.current_question_index = 0
        self.score = 0
        self.total_questions = 5
        self.selected_questions = []
        self.game_completed = False
        
        # Seleciona perguntas aleatórias
        self._select_questions()
    
    def _select_questions(self):
        """
        Seleciona perguntas aleatórias para o quiz.
        """
        self.selected_questions = random.sample(self.questions, min(self.total_questions, len(self.questions)))
    
    def build(self):
        """
        Constrói e retorna o componente do quiz.
        
        Returns:
            Componente Flet com o quiz completo
        """
        # AppBar
        app_bar = ft.AppBar(
            title=ft.Text("❓ Quiz Rápido"),
            bgcolor=ft.Colors.BLUE,
            color=ft.Colors.WHITE,
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                on_click=lambda e: self.on_back()
            )
        )
        
        if self.game_completed:
            return self._build_completion()
        
        # Se o quiz ainda não terminou
        return ft.Column(
            [
                app_bar,
                ft.Container(content=self._build_question(), expand=True),
            ],
            expand=True
        )
    
    def _build_question(self):
        """
        Constrói a tela da pergunta atual.
        
        Returns:
            Componente Container com a pergunta
        """
        if self.current_question_index >= len(self.selected_questions):
            self.game_completed = True
            return self._build_completion()
        
        question = self.selected_questions[self.current_question_index]
        
        # Barra de progresso
        progress_bar = ft.ProgressBar(
            value=(self.current_question_index + 1) / len(self.selected_questions),
            bgcolor=ft.Colors.GREY_200,
            color=ft.Colors.BLUE,
        )
        
        # Texto de progresso
        progress_text = ft.Text(
            f"Pergunta {self.current_question_index + 1} de {len(self.selected_questions)}",
            size=14,
            color=ft.Colors.GREY_600
        )
        
        # Pontuação atual
        score_text = ft.Text(
            f"Pontuação: {self.score}",
            size=18,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE
        )
        
        # Pergunta
        question_text = ft.Text(
            question["question"],
            size=22,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_GREY_800,
            text_align=ft.TextAlign.CENTER
        )
        
        # Opções de resposta
        option_buttons = []
        for option in question["options"]:
            btn = ft.FilledButton(
                option,
                width=250,
                height=50,
                on_click=lambda e, opt=option: self.handle_answer(opt, question["correct"])
            )
            option_buttons.append(btn)
        
        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(height=20),
                    progress_text,
                    ft.Container(height=5),
                    progress_bar,
                    ft.Container(height=10),
                    score_text,
                    ft.Container(height=30),
                    ft.Icon(ft.Icons.HELP, size=60, color=ft.Colors.BLUE),
                    ft.Container(height=20),
                    question_text,
                    ft.Container(height=30),
                    *option_buttons,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=30,
        )
    
    def handle_answer(self, selected_option, correct_option):
        """
        Manipula a resposta do usuário.
        
        Args:
            selected_option: Opção selecionada
            correct_option: Opção correta
        """
        if selected_option == correct_option:
            self.score += 1
            # Mostra feedback positivo
            self._show_feedback(True)
        else:
            # Mostra feedback negativo
            self._show_feedback(False)
        
        # Avança para a próxima pergunta
        self.current_question_index += 1
        
        # Atualiza a interface
        self.page.clean()
        self.page.add(self.build())
        self.page.update()
    
    def _show_feedback(self, is_correct):
        """
        Mostra feedback visual sobre a resposta.
        
        Args:
            is_correct: Se a resposta estava correta
        """
        if is_correct:
            message = "Correto! 🎉"
            color = ft.Colors.GREEN
        else:
            message = "Incorreto! 😅"
            color = ft.Colors.RED
        
        snack_bar = ft.SnackBar(
            content=ft.Text(message, color=ft.Colors.WHITE),
            bgcolor=color,
            duration=1000,
        )
        self.page.snack_bar = snack_bar
    
    def _build_completion(self):
        """
        Constrói a tela de conclusão do quiz.
        
        Returns:
            Componente Container com a conclusão
        """
        # Calcula pontos
        points_earned = self.score * 10  # 10 pontos por acerto
        
        # Adiciona pontos ao usuário
        self.gamification.add_points(
            points_earned,
            "quiz_completed",
            {"score": self.score, "total": self.total_questions}
        )
        self.gamification.update_streak()
        
        # Obtém estatísticas
        stats = self.gamification.get_user_stats()
        
        # Mensagem baseada na pontuação
        if self.score == self.total_questions:
            message = "Perfeito! Você é incrível! 🌟"
            icon = ft.Icons.STAR
            icon_color = ft.Colors.YELLOW
        elif self.score >= self.total_questions * 0.7:
            message = "Muito bem! Excelente trabalho! 👏"
            icon = ft.Icons.THUMB_UP
            icon_color = ft.Colors.BLUE
        else:
            message = "Bom esforço! Continue praticando! 💪"
            icon = ft.Icons.SCHOOL
            icon_color = ft.Colors.GREEN
        
        # AppBar
        app_bar = ft.AppBar(
            title=ft.Text("❓ Quiz Rápido"),
            bgcolor=ft.Colors.BLUE,
            color=ft.Colors.WHITE,
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                on_click=lambda e: self.on_back()
            )
        )
        
        # Conteúdo de conclusão
        conclusion = ft.Container(
            content=ft.Column(
                [
                    ft.Icon(icon, size=100, color=icon_color),
                    ft.Container(height=30),
                    ft.Text(
                        "Quiz Completo!",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_GREY_800,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=20),
                    ft.Text(
                        f"Sua pontuação: {self.score}/{self.total_questions}",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE,
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
                    ft.Container(height=30),
                    ft.FilledButton(
                        "Jogar Novamente",
                        icon=ft.Icons.REFRESH,
                        width=200,
                        height=50,
                        on_click=lambda e: self.restart_quiz()
                    ),
                    ft.Container(height=10),
                    ft.OutlinedButton(
                        "Voltar",
                        icon=ft.Icons.HOME,
                        width=200,
                        height=50,
                        on_click=lambda e: self.on_back()
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.center,
            ),
            padding=30,
        )
        
        return ft.Column(
            [
                app_bar,
                ft.Container(content=conclusion, expand=True),
            ],
            expand=True
        )
    
    def restart_quiz(self):
        """
        Reinicia o quiz.
        """
        self.current_question_index = 0
        self.score = 0
        self.game_completed = False
        self._select_questions()
        
        self.page.clean()
        self.page.add(self.build())
        self.page.update()
