"""
Memory Game - Jogo da Memória
==============================

Jogo da memória para reforçar o vocabulário aprendido.
O jogador deve encontrar pares de cartas (palavra em inglês + tradução).

Features:
- Grid de cartas viradas para baixo
- Ao clicar, vira a carta
- Encontrar pares = acerto
- Sistema de pontuação
- Contador de movimentos
- Tempo decorrido
"""

import flet as ft
import random
from lib.core.gamification import GamificationSystem


class MemoryGame:
    """
    Jogo da memória interativo.
    
    Features:
    - Grid 4x4 de cartas
    - Pares de palavras (inglês + português)
    - Animações de virar cartas
    - Sistema de pontuação
    - Integração com gamificação
    """
    
    def __init__(self, page: ft.Page, on_back, user_id=None):
        """
        Inicializa o jogo da memória.
        
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
        
        # Pares de palavras para o jogo
        self.word_pairs = [
            {"english": "Red", "portuguese": "Vermelho", "color": ft.Colors.RED},
            {"english": "Blue", "portuguese": "Azul", "color": ft.Colors.BLUE},
            {"english": "Green", "portuguese": "Verde", "color": ft.Colors.GREEN},
            {"english": "Yellow", "portuguese": "Amarelo", "color": ft.Colors.YELLOW},
            {"english": "Cat", "portuguese": "Gato", "color": ft.Colors.PURPLE},
            {"english": "Dog", "portuguese": "Cachorro", "color": ft.Colors.ORANGE},
            {"english": "One", "portuguese": "Um", "color": ft.Colors.CYAN},
            {"english": "Two", "portuguese": "Dois", "color": ft.Colors.PINK},
        ]
        
        # Estado do jogo
        self.cards = []
        self.flipped_cards = []
        self.matched_pairs = 0
        self.moves = 0
        self.game_started = False
        self.game_completed = False
        
        # Prepara as cartas
        self._prepare_cards()
    
    def _prepare_cards(self):
        """
        Prepara as cartas para o jogo.
        Cria duas cartas para cada par (inglês e português).
        """
        self.cards = []
        for pair in self.word_pairs:
            # Carta em inglês
            self.cards.append({
                "text": pair["english"],
                "pair_id": pair["english"],
                "color": pair["color"],
                "flipped": False,
                "matched": False
            })
            # Carta em português
            self.cards.append({
                "text": pair["portuguese"],
                "pair_id": pair["english"],
                "color": pair["color"],
                "flipped": False,
                "matched": False
            })
        
        # Embaralha as cartas
        random.shuffle(self.cards)
    
    def build(self):
        """
        Constrói e retorna o componente do jogo.
        
        Returns:
            Componente Flet com o jogo completo
        """
        # AppBar
        app_bar = ft.AppBar(
            title=ft.Text("🧠 Jogo da Memória"),
            bgcolor=ft.Colors.PURPLE,
            color=ft.Colors.WHITE,
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK,
                on_click=lambda e: self.on_back()
            )
        )
        
        # Seção de estatísticas
        stats_row = ft.Row(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Movimentos", size=12, color=ft.Colors.GREY_600),
                            ft.Text(str(self.moves), size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=10,
                    bgcolor=ft.Colors.PURPLE_50,
                    border_radius=10,
                ),
                ft.Container(width=10),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Pares", size=12, color=ft.Colors.GREY_600),
                            ft.Text(f"{self.matched_pairs}/8", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=10,
                    bgcolor=ft.Colors.GREEN_50,
                    border_radius=10,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        
        # Grid de cartas
        cards_grid = self._build_cards_grid()
        
        # Botão de reiniciar
        restart_button = ft.FilledButton(
            "Reiniciar",
            icon=ft.Icons.REFRESH,
            width=200,
            height=50,
            on_click=lambda e: self.restart_game()
        )
        
        # Container principal
        main_content = ft.Column(
            [
                ft.Container(height=20),
                stats_row,
                ft.Container(height=20),
                cards_grid,
                ft.Container(height=20),
                restart_button,
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
    
    def _build_cards_grid(self):
        """
        Constrói o grid de cartas.
        
        Returns:
            Componente GridView com as cartas
        """
        card_buttons = []
        
        for i, card in enumerate(self.cards):
            if card["matched"]:
                # Carta já combinada - mostra verde
                card_btn = ft.Container(
                    content=ft.Column(
                        [
                            ft.Icon(ft.Icons.CHECK, color=ft.Colors.WHITE, size=30),
                            ft.Text(card["text"], size=14, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    width=80,
                    height=80,
                    bgcolor=ft.Colors.GREEN,
                    border_radius=10,
                    alignment=ft.Alignment(-1, -1)
                )
            elif card["flipped"]:
                # Carta virada - mostra o conteúdo
                card_btn = ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(card["text"], size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.center,
                    ),
                    width=80,
                    height=80,
                    bgcolor=card["color"],
                    border_radius=10,
                    alignment=ft.Alignment(-1, -1)
                )
            else:
                # Carta oculta - mostra verso
                card_btn = ft.Container(
                    content=ft.Icon(ft.Icons.HELP, color=ft.Colors.GREY_400, size=30),
                    width=80,
                    height=80,
                    bgcolor=ft.Colors.GREY_200,
                    border_radius=10,
                    alignment=ft.Alignment(-1, -1),
                    on_click=lambda e, idx=i: self.handle_card_click(idx)
                )
            
            card_buttons.append(card_btn)
        
        # Organiza em grid 4x4
        rows = []
        for i in range(0, len(card_buttons), 4):
            row = ft.Row(
                card_buttons[i:i+4],
                alignment=ft.MainAxisAlignment.CENTER
            )
            rows.append(row)
            rows.append(ft.Container(height=10))
        
        return ft.Column(rows, alignment=ft.MainAxisAlignment.CENTER)
    
    def handle_card_click(self, card_index):
        """
        Manipula o clique em uma carta.
        
        Args:
            card_index: Índice da carta clicada
        """
        if self.game_completed:
            return
        
        card = self.cards[card_index]
        
        # Se a carta já estiver virada ou combinada, ignora
        if card["flipped"] or card["matched"]:
            return
        
        # Se já tem 2 cartas viradas, ignora
        if len(self.flipped_cards) >= 2:
            return
        
        # Vira a carta
        card["flipped"] = True
        self.flipped_cards.append(card_index)
        
        # Se é o primeiro clique, inicia o jogo
        if not self.game_started:
            self.game_started = True
        
        # Se tem 2 cartas viradas, verifica se formam par
        if len(self.flipped_cards) == 2:
            self.moves += 1
            self._check_match()
        
        # Atualiza a interface
        self.page.clean()
        self.page.add(self.build())
        self.page.update()
    
    def _check_match(self):
        """
        Verifica se as duas cartas viradas formam um par.
        """
        card1 = self.cards[self.flipped_cards[0]]
        card2 = self.cards[self.flipped_cards[1]]
        
        if card1["pair_id"] == card2["pair_id"]:
            # Par encontrado!
            card1["matched"] = True
            card2["matched"] = True
            self.matched_pairs += 1
            self.flipped_cards = []
            
            # Verifica se o jogo terminou
            if self.matched_pairs == 8:
                self.game_completed = True
                self._show_completion()
        else:
            # Não é par - desvira após um delay
            # Por simplicidade, desvira imediatamente
            card1["flipped"] = False
            card2["flipped"] = False
            self.flipped_cards = []
    
    def _show_completion(self):
        """
        Mostra a tela de conclusão do jogo.
        """
        # Calcula pontos baseados nos movimentos
        # Menos movimentos = mais pontos
        base_points = 50
        bonus_points = max(0, 20 - self.moves) * 2
        total_points = base_points + bonus_points
        
        # Adiciona pontos ao usuário
        self.gamification.add_points(
            total_points,
            "game_completed",
            {"game": "memory", "moves": self.moves}
        )
        self.gamification.update_streak()
        
        # Obtém estatísticas
        stats = self.gamification.get_user_stats()
        
        # Mostra mensagem de conclusão
        message = f"Parabéns! Você completou em {self.moves} movimentos!"
        
        # Constrói tela de conclusão
        conclusion = ft.Container(
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.EMOJI_EVENTS, size=100, color=ft.Colors.YELLOW),
                    ft.Container(height=30),
                    ft.Text(
                        "Jogo Completo!",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_GREY_800,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=20),
                    ft.Text(
                        message,
                        size=18,
                        color=ft.Colors.GREY_600,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=20),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(
                                    f"+{total_points} pontos ganhos!",
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
                    ft.Container(height=30),
                    ft.FilledButton(
                        "Jogar Novamente",
                        icon=ft.Icons.REFRESH,
                        width=200,
                        height=50,
                        on_click=lambda e: self.restart_game()
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
        
        self.page.clean()
        self.page.add(conclusion)
        self.page.update()
    
    def restart_game(self):
        """
        Reinicia o jogo.
        """
        self.flipped_cards = []
        self.matched_pairs = 0
        self.moves = 0
        self.game_started = False
        self.game_completed = False
        self._prepare_cards()
        
        self.page.clean()
        self.page.add(self.build())
        self.page.update()
