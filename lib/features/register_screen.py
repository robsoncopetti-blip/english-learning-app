"""
Register Screen - Tela de Cadastro
====================================

Esta tela permite que novos usuários se cadastrem no aplicativo.
O usuário escolhe se é pai ou criança e preenche os dados básicos.
"""

import flet as ft


class RegisterScreen:
    """
    Tela de cadastro do aplicativo.
    
    Features:
    - Seleção de tipo de usuário (Pai ou Criança)
    - Campo de nome
    - Campo de email
    - Campo de senha
    - Upload de foto (placeholder por enquanto)
    - Botão de cadastrar
    - Link para voltar ao login
    """
    
    def __init__(self, page: ft.Page, on_register, on_back):
        """
        Inicializa a tela de cadastro.
        
        Args:
            page: Objeto Page do Flet
            on_register: Função callback quando cadastro for bem-sucedido
            on_back: Função callback para voltar ao login
        """
        self.page = page
        self.on_register = on_register
        self.on_back = on_back
        
        # Radio buttons para escolher tipo de usuário
        self.user_type = ft.RadioGroup(
            content=ft.Column(
                [
                    ft.Radio(value="child", label="Sou Criança"),
                    ft.Radio(value="parent", label="Sou Pai/Mãe"),
                ]
            ),
            value="child"  # Valor padrão
        )
        
        # Campo de nome
        self.name_field = ft.TextField(
            label="Nome",
            hint_text="Seu nome",
            width=300,
            border_radius=10,
            prefix_icon=ft.Icons.PERSON
        )
        
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
            password=True,
            can_reveal_password=True,
            border_radius=10,
            prefix_icon=ft.Icons.LOCK
        )
        
        # Campo de confirmar senha
        self.confirm_password_field = ft.TextField(
            label="Confirmar Senha",
            hint_text="••••••••",
            width=300,
            password=True,
            can_reveal_password=True,
            border_radius=10,
            prefix_icon=ft.Icons.LOCK
        )
        
        # Campo de data de nascimento (para calcular faixa etária)
        self.birth_date_field = ft.TextField(
            label="Data de Nascimento",
            hint_text="DD/MM/AAAA",
            width=300,
            border_radius=10,
            prefix_icon=ft.Icons.CALENDAR_MONTH
        )
        
        # Placeholder para foto do perfil
        self.photo_placeholder = ft.Container(
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.PERSON, size=50, color=ft.Colors.GREY_400),
                    ft.Text("Adicionar foto", size=12, color=ft.Colors.GREY_600),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=100,
            height=100,
            border=ft.Border.all(2, ft.Colors.GREY_300),
            border_radius=50,
            alignment=ft.Alignment(-1, -1)
        )
        
        # Mensagem de erro
        self.error_message = ft.Text(
            "",
            color=ft.Colors.RED,
            size=12,
            visible=False
        )
        
    def build(self):
        """
        Constrói e retorna o componente da tela de cadastro.
        
        Returns:
            Componente Flet com a tela de cadastro completa
        """
        # Título
        title = ft.Text(
            "Criar Conta",
            size=32,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE
        )
        
        # Botão de cadastrar
        register_button = ft.FilledButton(
            "Cadastrar",
            icon=ft.Icons.PERSON_ADD,
            width=300,
            height=50,
            on_click=self.handle_register
        )
        
        # Link para voltar
        back_link = ft.TextButton(
            "Já tem conta? Fazer login",
            on_click=self.handle_back
        )
        
        # Container principal
        return ft.Container(
            content=ft.Column(
                [
                    title,
                    ft.Container(height=20),
                    self.photo_placeholder,
                    ft.Container(height=20),
                    ft.Text("Tipo de conta:", size=14, weight=ft.FontWeight.BOLD),
                    self.user_type,
                    ft.Container(height=10),
                    self.name_field,
                    ft.Container(height=10),
                    self.email_field,
                    ft.Container(height=10),
                    self.password_field,
                    ft.Container(height=10),
                    self.confirm_password_field,
                    ft.Container(height=10),
                    self.birth_date_field,
                    ft.Container(height=10),
                    self.error_message,
                    ft.Container(height=20),
                    register_button,
                    ft.Container(height=10),
                    back_link,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=30,
        )
    
    def handle_register(self, e):
        """
        Manipula o clique no botão de cadastrar.
        
        Valida os campos e chama o callback de cadastro.
        
        Args:
            e: Evento de clique
        """
        name = self.name_field.value
        email = self.email_field.value
        password = self.password_field.value
        confirm_password = self.confirm_password_field.value
        user_type = self.user_type.value
        birth_date = self.birth_date_field.value
        
        # Validação básica
        if not all([name, email, password, confirm_password, birth_date]):
            self.error_message.value = "Por favor, preencha todos os campos"
            self.error_message.visible = True
            self.page.update()
            return
        
        # Validação de email
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
        
        # Validação de data de nascimento (formato DD/MM/AAAA)
        try:
            # Converte DD/MM/AAAA para YYYY-MM-DD
            parts = birth_date.split("/")
            if len(parts) != 3:
                raise ValueError("Formato inválido")
            day, month, year = parts
            birth_date_formatted = f"{year}-{month}-{day}"
        except:
            self.error_message.value = "Data de nascimento inválida (use DD/MM/AAAA)"
            self.error_message.visible = True
            self.page.update()
            return
        
        # Validação de confirmação de senha
        if password != confirm_password:
            self.error_message.value = "As senhas não coincidem"
            self.error_message.visible = True
            self.page.update()
            return
        
        # Se tudo estiver ok, chama o callback de cadastro
        self.on_register(name, email, password, user_type, birth_date_formatted)
    
    def handle_back(self, e):
        """
        Manipula o clique no link de voltar.
        
        Navega de volta para a tela de login.
        
        Args:
            e: Evento de clique
        """
        self.on_back()
