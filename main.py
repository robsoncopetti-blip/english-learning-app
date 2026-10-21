"""
English Learning App - Aplicativo de Aprendizado de Inglês
===========================================================

Este é o arquivo principal do aplicativo.
Ele inicializa o app Flet e gerencia a navegação entre as telas.

Tecnologia: Flet (Python + Flutter)
Plataformas: Android, iOS, Windows, Web

Estrutura do app:
- Tela de Login Universal (para pais e crianças)
- Tela de Cadastro (com opção de pai ou criança)
- Tela Principal Criança (lições, jogos, gamificação)
- Tela Principal Pai (dashboard, progresso, desafios)
- Modo Dupla (atividades colaborativas)

Escopo inicial: Crianças de 5-7 anos
"""

import flet as ft
from lib.core.navigation import Navigation
from lib.features.login_screen import LoginScreen
from lib.features.register_screen import RegisterScreen
from lib.features.child_home_screen import ChildHomeScreen
from lib.features.parent_home_screen import ParentHomeScreen


class EnglishLearningApp:
    """
    Classe principal do aplicativo.
    
    Gerencia toda a navegação e estado do aplicativo.
    """
    
    def __init__(self, page: ft.Page):
        """
        Inicializa o aplicativo.
        
        Args:
            page: Objeto Page do Flet
        """
        self.page = page
        self.navigation = Navigation(page)
        
        # Estado do usuário (simulado por enquanto)
        self.current_user = None
        self.user_type = None  # "child" ou "parent"
        
        # Configurações da página
        self.setup_page()
        
        # Inicia na tela de login
        self.show_login()
    
    def setup_page(self):
        """
        Configura as propriedades da página principal.
        """
        self.page.title = "English Learning App"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.window_width = 400
        self.page.window_height = 700
        self.page.window_min_width = 350
        self.page.window_min_height = 600
        
        # Tema personalizado
        self.page.theme = ft.Theme(
            color_scheme=ft.ColorScheme(
                primary=ft.Colors.BLUE,
                secondary=ft.Colors.ORANGE,
                surface=ft.Colors.WHITE,
            )
        )
    
    def show_login(self):
        """
        Exibe a tela de login.
        """
        login_screen = LoginScreen(
            page=self.page,
            on_login=self.handle_login,
            on_register=self.show_register
        )
        self.navigation.navigate_to("/login", login_screen.build())
    
    def show_register(self):
        """
        Exibe a tela de cadastro.
        """
        register_screen = RegisterScreen(
            page=self.page,
            on_register=self.handle_register,
            on_back=self.show_login
        )
        self.navigation.navigate_to("/register", register_screen.build())
    
    def handle_login(self, email, password, name=None, google_user_info=None):
        """
        Manipula o login do usuário.
        
        NOTA: Por enquanto, aceita qualquer login válido.
        Futuramente, verificará no banco de dados.
        
        Args:
            email: Email do usuário
            password: Senha do usuário
            name: Nome do usuário (opcional, do Google)
            google_user_info: Informações completas do Google (opcional)
        """
        # Se for login do Google, usa o nome do Google
        if google_user_info:
            self.current_user = google_user_info.get("given_name", name or email.split("@")[0])
            self.user_full_name = google_user_info.get("name", name)
            self.user_photo = google_user_info.get("picture", None)
            self.google_authenticated = True
        else:
            self.current_user = name or email.split("@")[0]
            self.user_full_name = name
            self.user_photo = None
            self.google_authenticated = False
        
        self.user_id = email  # Usa email como ID único
        self.user_type = "child"  # Simulado - deve vir do banco
        
        # Redireciona para a tela apropriada
        if self.user_type == "child":
            self.show_child_home()
        else:
            self.show_parent_home()
    
    def handle_register(self, name, email, password, user_type, birth_date):
        """
        Manipula o cadastro de novo usuário.
        
        NOTA: Por enquanto, apenas simula o cadastro.
        Futuramente, salvará no banco de dados.
        
        Args:
            name: Nome do usuário
            email: Email do usuário
            password: Senha do usuário
            user_type: Tipo de usuário ("child" ou "parent")
            birth_date: Data de nascimento (YYYY-MM-DD)
        """
        # Simulação de cadastro
        self.current_user = name
        self.user_type = user_type
        self.user_birth_date = birth_date
        
        # Calcula faixa etária (simulado)
        from lib.models.user import User
        user_model = User(email)
        age = user_model._calculate_age(birth_date)
        age_group = user_model._get_age_group(age)
        
        print(f"Usuário cadastrado: {name}, Tipo: {user_type}, Idade: {age}, Faixa: {age_group}")
        
        # Redireciona para a tela apropriada
        if self.user_type == "child":
            self.show_child_home(age_group)
        else:
            self.show_parent_home()
    
    def show_child_home(self, age_group=None):
        """
        Exibe a tela principal da criança.
        
        Args:
            age_group: Faixa etária da criança ('4-5', '5-6', '6-7')
        """
        child_home = ChildHomeScreen(
            page=self.page,
            user_name=self.current_user,
            on_logout=self.handle_logout,
            user_id=self.user_id,
            age_group=age_group
        )
        self.navigation.navigate_to("/child_home", child_home.build())
    
    def show_parent_home(self):
        """
        Exibe a tela principal do pai.
        """
        parent_home = ParentHomeScreen(
            page=self.page,
            user_name=self.current_user,
            on_logout=self.handle_logout,
            child_user_id=self.user_id  # Usa o mesmo ID para demonstração
        )
        self.navigation.navigate_to("/parent_home", parent_home.build())
    
    def handle_logout(self):
        """
        Manipula o logout do usuário.
        """
        self.current_user = None
        self.user_type = None
        self.show_login()


def main(page: ft.Page):
    """
    Função principal que inicializa o aplicativo Flet.
    
    Args:
        page: Objeto Page do Flet que representa a janela do aplicativo
    """
    app = EnglishLearningApp(page)


# Ponto de entrada do aplicativo
if __name__ == "__main__":
    ft.run(main)
