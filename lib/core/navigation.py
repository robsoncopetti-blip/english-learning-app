"""
Navigation - Sistema de Navegação
===================================

Este módulo gerencia a navegação entre as telas do aplicativo.
Usa um sistema de rotas para alternar entre:
- Tela de Login
- Tela de Cadastro
- Tela Principal (Criança)
- Tela Principal (Pai)
- Outras telas do app
"""

import flet as ft


class Navigation:
    """
    Classe responsável por gerenciar a navegação do aplicativo.
    
    Permite alternar entre diferentes telas de forma organizada.
    """
    
    def __init__(self, page: ft.Page):
        """
        Inicializa o sistema de navegação.
        
        Args:
            page: Objeto Page do Flet
        """
        self.page = page
        self.current_route = "/"
        
    def navigate_to(self, route: str, content: ft.Control):
        """
        Navega para uma rota específica com o conteúdo fornecido.
        
        Args:
            route: String identificando a rota (ex: "/login", "/home")
            content: Componente Flet a ser exibido
        """
        self.current_route = route
        self.page.clean()  # Limpa o conteúdo atual
        self.page.add(content)  # Adiciona o novo conteúdo
        self.page.update()  # Atualiza a página
        
    def go_back(self):
        """
        Volta para a tela anterior.
        (Implementação futura com histórico de navegação)
        """
        pass  # Será implementado com histórico de rotas
