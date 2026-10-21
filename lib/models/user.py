"""
User Model - Modelo de Usuário
================================

Modelo de dados completo para usuários do aplicativo.
Inclui todas as informações necessárias para personalização e IA.

Atributos:
- Informações básicas (nome, apelido, senha)
- Gênero (para personalização de cores/temas)
- Idade (para faixa etária e progressão de conteúdo)
- Fotos (para IA gerar contextos)
- Preferências (cores, animais, personagem)
- Tipo (pai ou criança)
- Vínculo pai-filho

Faixas Etárias:
- 4-5 anos: Conteúdo básico, visual, pouca leitura
- 5-6 anos: Conteúdo intermediário, introdução à leitura
- 6-7 anos: Conteúdo avançado, leitura completa, mais desafios
"""

import sqlite3
from typing import Optional, List, Dict
from datetime import datetime, date


class User:
    """
    Modelo de usuário do aplicativo.
    """
    
    def __init__(self, user_id: str):
        """
        Inicializa o modelo de usuário.
        
        Args:
            user_id: ID único do usuário (apelido)
        """
        self.user_id = user_id
        self.db_path = "users.db"
        self._init_database()
    
    def _init_database(self):
        """
        Inicializa o banco de dados de usuários.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Tabela de usuários
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                full_name TEXT,
                nickname TEXT,
                password TEXT,
                user_type TEXT,  -- 'child' ou 'parent'
                gender TEXT,  -- 'male', 'female', 'other'
                birth_date TEXT,  -- Data de nascimento (YYYY-MM-DD)
                age INTEGER,  -- Idade calculada
                age_group TEXT,  -- Faixa etária: '4-5', '5-6', '6-7'
                photo_path TEXT,
                character_type TEXT,  -- tipo de personagem escolhido
                favorite_colors TEXT,  -- JSON com 3 cores
                favorite_animals TEXT,  -- JSON com 3 animais
                theme_preference TEXT,  -- tema baseado no gênero
                parent_id TEXT,  -- ID do pai (se for criança)
                child_id TEXT,  -- ID da criança (se for pai)
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                last_login TEXT,
                FOREIGN KEY (parent_id) REFERENCES users (user_id),
                FOREIGN KEY (child_id) REFERENCES users (user_id)
            )
        """)
        
        conn.commit()
        conn.close()
    
    def create_user(
        self,
        full_name: str,
        nickname: str,
        password: str,
        user_type: str,
        gender: str,
        birth_date: Optional[str] = None,  # YYYY-MM-DD
        photo_path: Optional[str] = None,
        character_type: Optional[str] = None,
        favorite_colors: Optional[List[str]] = None,
        favorite_animals: Optional[List[str]] = None,
        parent_id: Optional[str] = None,
        child_id: Optional[str] = None
    ) -> bool:
        """
        Cria um novo usuário.
        
        Args:
            full_name: Nome completo
            nickname: Apelido (usado como login)
            password: Senha numérica de 6 dígitos
            user_type: 'child' ou 'parent'
            gender: 'male', 'female' ou 'other'
            birth_date: Data de nascimento (YYYY-MM-DD)
            photo_path: Caminho da foto (opcional)
            character_type: Tipo de personagem (opcional)
            favorite_colors: Lista de 3 cores favoritas (opcional)
            favorite_animals: Lista de 3 animais favoritos (opcional)
            parent_id: ID do pai (se for criança)
            child_id: ID da criança (se for pai)
            
        Returns:
            True se criado com sucesso, False caso contrário
        """
        import json
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            # Calcula idade e faixa etária
            age = self._calculate_age(birth_date) if birth_date else None
            age_group = self._get_age_group(age) if age else None
            
            # Define tema baseado no gênero
            theme_preference = self._get_theme_by_gender(gender)
            
            cursor.execute(
                """INSERT INTO users 
                   (user_id, full_name, nickname, password, user_type, gender, 
                    birth_date, age, age_group, photo_path, character_type, 
                    favorite_colors, favorite_animals, theme_preference, 
                    parent_id, child_id, last_login)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    nickname,  # user_id = nickname
                    full_name,
                    nickname,
                    password,
                    user_type,
                    gender,
                    birth_date,
                    age,
                    age_group,
                    photo_path,
                    character_type,
                    json.dumps(favorite_colors) if favorite_colors else None,
                    json.dumps(favorite_animals) if favorite_animals else None,
                    theme_preference,
                    parent_id,
                    child_id,
                    str(datetime.now())
                )
            )
            
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            # Usuário já existe
            return False
        finally:
            conn.close()
    
    def get_user(self, user_id: str) -> Optional[dict]:
        """
        Busca um usuário pelo ID.
        
        Args:
            user_id: ID do usuário (nickname)
            
        Returns:
            Dicionário com dados do usuário ou None
        """
        import json
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        
        conn.close()
        
        if result:
            columns = [
                "user_id", "full_name", "nickname", "password", "user_type",
                "gender", "birth_date", "age", "age_group", "photo_path", 
                "character_type", "favorite_colors", "favorite_animals", 
                "theme_preference", "parent_id", "child_id", "created_at", "last_login"
            ]
            
            user_dict = dict(zip(columns, result))
            
            # Converte JSON strings para listas
            if user_dict["favorite_colors"]:
                user_dict["favorite_colors"] = json.loads(user_dict["favorite_colors"])
            if user_dict["favorite_animals"]:
                user_dict["favorite_animals"] = json.loads(user_dict["favorite_animals"])
            
            return user_dict
        
        return None
    
    def verify_login(self, nickname: str, password: str) -> Optional[dict]:
        """
        Verifica login do usuário.
        
        Args:
            nickname: Apelido do usuário
            password: Senha numérica
            
        Returns:
            Dicionário com dados do usuário se login válido, None caso contrário
        """
        user = self.get_user(nickname)
        
        if user and user["password"] == password:
            # Atualiza último login
            self._update_last_login(nickname)
            return user
        
        return None
    
    def _update_last_login(self, user_id: str):
        """
        Atualiza o último login do usuário.
        
        Args:
            user_id: ID do usuário
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            "UPDATE users SET last_login = ? WHERE user_id = ?",
            (str(datetime.now()), user_id)
        )
        
        conn.commit()
        conn.close()
    
    def link_parent_child(self, parent_id: str, child_id: str) -> bool:
        """
        Vincula pai e filho.
        
        Args:
            parent_id: ID do pai
            child_id: ID da criança
            
        Returns:
            True se vinculado com sucesso
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "UPDATE users SET child_id = ? WHERE user_id = ?",
                (child_id, parent_id)
            )
            cursor.execute(
                "UPDATE users SET parent_id = ? WHERE user_id = ?",
                (parent_id, child_id)
            )
            
            conn.commit()
            return True
        except:
            return False
        finally:
            conn.close()
    
    def _calculate_age(self, birth_date: str) -> Optional[int]:
        """
        Calcula a idade baseada na data de nascimento.
        
        Args:
            birth_date: Data de nascimento (YYYY-MM-DD)
            
        Returns:
            Idade em anos ou None se não for possível calcular
        """
        try:
            birth = datetime.strptime(birth_date, "%Y-%m-%d").date()
            today = date.today()
            age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
            return age
        except:
            return None
    
    def _get_age_group(self, age: Optional[int]) -> Optional[str]:
        """
        Retorna a faixa etária baseada na idade.
        
        Faixas:
        - 4-5 anos: Conteúdo básico, visual
        - 5-6 anos: Conteúdo intermediário
        - 6-7 anos: Conteúdo avançado
        
        Args:
            age: Idade em anos
            
        Returns:
            String da faixa etária ou None
        """
        if age is None:
            return None
        
        if 4 <= age < 5:
            return "4-5"
        elif 5 <= age < 6:
            return "5-6"
        elif 6 <= age <= 7:
            return "6-7"
        else:
            return None  # Fora da faixa 4-7
    
    def get_content_for_age_group(self, age_group: str) -> Dict[str, List[str]]:
        """
        Retorna o conteúdo disponível para cada faixa etária.
        
        Args:
            age_group: Faixa etária ('4-5', '5-6', '6-7')
            
        Returns:
            Dicionário com lições e jogos disponíveis
        """
        content_map = {
            "4-5": {
                "lessons": ["colors", "numbers"],
                "games": ["memory_easy"],
                "features": ["visual_only", "audio_guide"]
            },
            "5-6": {
                "lessons": ["colors", "numbers", "animals"],
                "games": ["memory_easy", "quiz_easy"],
                "features": ["reading_intro", "pronunciation_guide"]
            },
            "6-7": {
                "lessons": ["colors", "numbers", "animals", "fruits", "family"],
                "games": ["memory_easy", "quiz_easy", "quiz_advanced"],
                "features": ["full_reading", "portuguese_reading", "pronunciation_advanced"]
            }
        }
        
        return content_map.get(age_group, {})
    
    def _get_theme_by_gender(self, gender: str) -> str:
        """
        Retorna o tema preferido baseado no gênero.
        
        Args:
            gender: 'male', 'female' ou 'other'
            
        Returns:
            Nome do tema
        """
        themes = {
            "male": "blue_theme",
            "female": "pink_theme",
            "other": "green_theme"
        }
        return themes.get(gender, "blue_theme")
    
    def get_all_users(self) -> List[dict]:
        """
        Retorna todos os usuários cadastrados.
        
        Returns:
            Lista de dicionários com dados dos usuários
        """
        import json
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        
        conn.close()
        
        columns = [
            "user_id", "full_name", "nickname", "password", "user_type",
            "gender", "birth_date", "age", "age_group", "photo_path", 
            "character_type", "favorite_colors", "favorite_animals", 
            "theme_preference", "parent_id", "child_id", "created_at", "last_login"
        ]
        
        users = []
        for result in results:
            user_dict = dict(zip(columns, result))
            
            if user_dict["favorite_colors"]:
                user_dict["favorite_colors"] = json.loads(user_dict["favorite_colors"])
            if user_dict["favorite_animals"]:
                user_dict["favorite_animals"] = json.loads(user_dict["favorite_animals"])
            
            users.append(user_dict)
        
        return users
