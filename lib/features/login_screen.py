"""
Login Screen - Tela de Login Universal
========================================

Esta tela permite que usuários façam login no aplicativo.
Funciona tanto para pais quanto para crianças.
Após login, o sistema detecta o tipo de usuário e redireciona.

NOVO: Inclui login com Google OAuth
"""

import flet as ft
from lib.integrations.google import GoogleOAuthHandler


class LoginScreen:
    """
    Tela de login do aplicativo.
    
    Features:
    - Campo de email
    - Campo de senha
    - Botão de entrar
    - Link para cadastro de novo usuário
    - Design amigável e intuitivo
    """
    
    def __init__(self, page: ft.Page, on_login, on_register):
        """
        Inicializa a tela de login.
        
        Args:
            page: Objeto Page do Flet
            on_login: Função callback quando login for bem-sucedido
            on_register: Função callback para ir para tela de cadastro
        """
        self.page = page
        self.on_login = on_login
        self.on_register = on_register
        
        # Handler Google OAuth
        self.google_oauth = GoogleOAuthHandler()
        
        # Campo de email
        self.email_field = ft.TextField(
            label="Email",
            hint_text="seu@email.com",
            width=300,
            border_radius=10,
            prefix_icon=ft.Icons.EMAIL
        )
        
        # Campo de senha
        self.password_field = ft.TextField(
            label="Senha",
            hint_text="••••••••",
            width=300,
            password=True,  # Oculta a senha
            can_reveal_password=True,  # Botão para mostrar senha
            border_radius=10,
            prefix_icon=ft.Icons.LOCK
        )
        
        # Mensagem de erro (inicialmente oculta)
        self.error_message = ft.Text(
            "",
            color=ft.Colors.RED,
            size=12,
            visible=False
        )
        
    def build(self):
        """
        Constrói e retorna o componente da tela de login.
        
        Returns:
            Componente Flet com a tela de login completa
        """
        # Logo/Título
        title = ft.Text(
            "English Learning App",
            size=32,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE
        )
        
        subtitle = ft.Text(
            "Aprenda inglês brincando!",
            size=16,
            color=ft.Colors.GREY_600
        )
        
        # Mensagem especial dedicada à Betina
        dedication = ft.Container(
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
        
        # Botão de login
        login_button = ft.FilledButton(
            "Entrar",
            icon=ft.Icons.LOGIN,
            width=300,
            height=50,
            on_click=self.handle_login
        )
        
        # Botão de login com Google
        google_login_button = ft.OutlinedButton(
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.PUBLIC, color=ft.Colors.RED_700),
                    ft.Container(width=10),
                    ft.Text("Entrar com Google"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            width=300,
            height=50,
            on_click=self.handle_google_login
        )
        
        # Botão de login com Google (temporariamente desativado)
        # google_login_button = ft.OutlinedButton(
        #     content=ft.Row(
        #         [
        #             ft.Icon(ft.Icons.PUBLIC, color=ft.Colors.RED_700),
        #             ft.Container(width=10),
        #             ft.Text("Entrar com Google"),
        #         ],
        #         alignment=ft.MainAxisAlignment.CENTER,
        #     ),
        #     width=300,
        #     height=50,
        #     on_click=self.handle_google_login
        # )
        
        # Link para cadastro
        register_link = ft.TextButton(
            "Não tem conta? Cadastre-se",
            on_click=self.handle_register
        )
        
        # Container principal
        return ft.Container(
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.SCHOOL, size=80, color=ft.Colors.BLUE),
                    ft.Container(height=20),
                    title,
                    subtitle,
                    ft.Container(height=20),
                    dedication,
                    ft.Container(height=20),
                    google_login_button,
                    ft.Container(height=15),
                    ft.Text("ou", size=14, color=ft.Colors.GREY_600),
                    ft.Container(height=15),
                    self.email_field,
                    ft.Container(height=10),
                    self.password_field,
                    ft.Container(height=10),
                    self.error_message,
                    ft.Container(height=20),
                    login_button,
                    ft.Container(height=10),
                    register_link,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=30,
        )
    
    def handle_login(self, e):
        """
        Manipula o evento de clique no botão de login.
        
        Valida os campos e chama o callback de login.
        
        Args:
            e: Evento de clique
        """
        email = self.email_field.value
        password = self.password_field.value
        
        # Validação básica
        if not email or not password:
            self.error_message.value = "Por favor, preencha todos os campos"
            self.error_message.visible = True
            self.page.update()
            return
        
        # Validação de email simples
        if "@" not in email or "." not in email:
            self.error_message.value = "Email inválido"
            self.error_message.visible = True
            self.page.update()
            return
        
        # Validação de senha
        if len(password) < 6:
            self.error_message.value = "A senha deve ter pelo menos 6 caracteres"
            self.error_message.visible = True
            self.page.update()
            return
        
        # Se tudo estiver ok, chama o callback de login
        # (Futuramente aqui verificará no banco de dados)
        self.on_login(email, password)
    
    def handle_google_login(self, e):
        """
        Manipula o login com Google OAuth.
        
        Args:
            e: Evento de clique
        """
        def on_google_success(user_info):
            """
            Callback quando login Google for bem-sucedido.
            
            Args:
                user_info: Informações do usuário do Google
            """
            # Usa email e nome do Google
            email = user_info.get("email")
            name = user_info.get("name")
            
            # Chama o callback de login com dados do Google
            self.on_login(email, "google_auth", name=name, google_user_info=user_info)
        
        def on_google_error(error):
            """
            Callback quando houver erro no login Google.
            
            Args:
                error: Mensagem de erro
            """
            self.error_message.value = f"Erro no login Google: {error}"
            self.error_message.visible = True
            self.page.update()
        
        # Inicia autenticação Google
        self.google_oauth.authenticate(on_google_success, on_google_error)
    
    def handle_register(self, e):
        """
        Manipula o clique no link de cadastro.
        
        Navega para a tela de cadastro.
        
        Args:
            e: Evento de clique
        """
        self.on_register()
