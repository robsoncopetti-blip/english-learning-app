"""
Gamification - Sistema de Gamificação
=======================================

Este módulo gerencia o sistema de pontos, streak, níveis e conquistas.

Features:
- Sistema de pontos ganhos ao completar lições
- Sistema de streak (dias consecutivos de estudo)
- Níveis baseados em pontos
- Conquistas/badges por metas alcançadas
- Persistência local de dados
"""

import sqlite3
import json
from datetime import datetime, date
from typing import Dict, List, Optional
import os


class GamificationSystem:
    """
    Sistema de gamificação do aplicativo.
    
    Gerencia pontos, streak, níveis e conquistas do usuário.
    """
    
    def __init__(self, user_id: str):
        """
        Inicializa o sistema de gamificação para um usuário.
        
        Args:
            user_id: ID único do usuário
        """
        self.user_id = user_id
        self.db_path = "gamification.db"
        self._init_database()
        self._ensure_user_exists()
    
    def _init_database(self):
        """
        Inicializa o banco de dados SQLite.
        Cria as tabelas necessárias se não existirem.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Tabela de usuários
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                points INTEGER DEFAULT 0,
                streak INTEGER DEFAULT 0,
                level INTEGER DEFAULT 1,
                last_active_date TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Tabela de conquistas
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS achievements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                achievement_id TEXT,
                achieved_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        """)
        
        # Tabela de histórico de atividades
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS activity_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                activity_type TEXT,
                activity_data TEXT,
                points_earned INTEGER,
                timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        """)
        
        conn.commit()
        conn.close()
    
    def _ensure_user_exists(self):
        """
        Garante que o usuário existe no banco de dados.
        Cria o usuário se não existir.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (self.user_id,))
        if not cursor.fetchone():
            cursor.execute(
                "INSERT INTO users (user_id, points, streak, level) VALUES (?, 0, 0, 1)",
                (self.user_id,)
            )
        
        conn.commit()
        conn.close()
    
    def get_user_stats(self) -> Dict:
        """
        Retorna as estatísticas do usuário.
        
        Returns:
            Dicionário com pontos, streak, nível, etc.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT points, streak, level, last_active_date FROM users WHERE user_id = ?",
            (self.user_id,)
        )
        result = cursor.fetchone()
        
        conn.close()
        
        if result:
            return {
                "points": result[0],
                "streak": result[1],
                "level": result[2],
                "last_active_date": result[3]
            }
        return {"points": 0, "streak": 0, "level": 1, "last_active_date": None}
    
    def add_points(self, points: int, activity_type: str, activity_data: Dict = None):
        """
        Adiciona pontos ao usuário.
        
        Args:
            points: Quantidade de pontos a adicionar
            activity_type: Tipo de atividade (ex: "lesson_completed", "quiz_passed")
            activity_data: Dados adicionais sobre a atividade
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Adiciona pontos
        cursor.execute(
            "UPDATE users SET points = points + ? WHERE user_id = ?",
            (points, self.user_id)
        )
        
        # Atualiza nível
        current_points = cursor.execute(
            "SELECT points FROM users WHERE user_id = ?",
            (self.user_id,)
        ).fetchone()[0]
        
        new_level = self._calculate_level(current_points)
        cursor.execute(
            "UPDATE users SET level = ? WHERE user_id = ?",
            (new_level, self.user_id)
        )
        
        # Registra atividade
        cursor.execute(
            """INSERT INTO activity_history 
               (user_id, activity_type, activity_data, points_earned) 
               VALUES (?, ?, ?, ?)""",
            (self.user_id, activity_type, json.dumps(activity_data) if activity_data else None, points)
        )
        
        conn.commit()
        conn.close()
        
        # Verifica conquistas
        self._check_achievements()
    
    def update_streak(self):
        """
        Atualiza o streak do usuário.
        Incrementa se o usuário estudou hoje, reseta se perdeu dias.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Obtém a última data ativa
        cursor.execute(
            "SELECT last_active_date, streak FROM users WHERE user_id = ?",
            (self.user_id,)
        )
        result = cursor.fetchone()
        
        if result:
            last_date_str, current_streak = result
            today = date.today()
            
            if last_date_str:
                last_date = datetime.strptime(last_date_str, "%Y-%m-%d").date()
                days_diff = (today - last_date).days
                
                if days_diff == 0:
                    # Já estudou hoje, não faz nada
                    pass
                elif days_diff == 1:
                    # Estudou ontem, incrementa streak
                    cursor.execute(
                        "UPDATE users SET streak = streak + 1, last_active_date = ? WHERE user_id = ?",
                        (str(today), self.user_id)
                    )
                else:
                    # Perdeu o streak, reseta
                    cursor.execute(
                        "UPDATE users SET streak = 1, last_active_date = ? WHERE user_id = ?",
                        (str(today), self.user_id)
                    )
            else:
                # Primeira vez
                cursor.execute(
                    "UPDATE users SET streak = 1, last_active_date = ? WHERE user_id = ?",
                    (str(today), self.user_id)
                )
        
        conn.commit()
        conn.close()
    
    def _calculate_level(self, points: int) -> int:
        """
        Calcula o nível baseado nos pontos.
        
        Regras:
        - Nível 1: 0-99 pontos
        - Nível 2: 100-299 pontos
        - Nível 3: 300-599 pontos
        - Nível 4: 600-999 pontos
        - Nível 5: 1000+ pontos
        
        Args:
            points: Pontos atuais do usuário
            
        Returns:
            Nível calculado
        """
        if points < 100:
            return 1
        elif points < 300:
            return 2
        elif points < 600:
            return 3
        elif points < 1000:
            return 4
        else:
            return 5
    
    def _check_achievements(self):
        """
        Verifica e desbloqueia conquistas.
        """
        stats = self.get_user_stats()
        achievements = self._get_available_achievements()
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        for achievement in achievements:
            # Verifica se já conquistou
            cursor.execute(
                "SELECT id FROM achievements WHERE user_id = ? AND achievement_id = ?",
                (self.user_id, achievement["id"])
            )
            if cursor.fetchone():
                continue  # Já conquistou
            
            # Verifica se atingiu os requisitos
            if achievement["condition"](stats):
                cursor.execute(
                    "INSERT INTO achievements (user_id, achievement_id) VALUES (?, ?)",
                    (self.user_id, achievement["id"])
                )
        
        conn.commit()
        conn.close()
    
    def _get_available_achievements(self) -> List[Dict]:
        """
        Retorna a lista de conquistas disponíveis.
        
        Returns:
            Lista de conquistas com condições
        """
        return [
            {
                "id": "first_lesson",
                "name": "Primeira Lição",
                "description": "Complete sua primeira lição",
                "icon": "🎯",
                "condition": lambda stats: stats["points"] >= 10
            },
            {
                "id": "streak_3",
                "name": "Streak de 3 Dias",
                "description": "Estude 3 dias consecutivos",
                "icon": "🔥",
                "condition": lambda stats: stats["streak"] >= 3
            },
            {
                "id": "streak_7",
                "name": "Streak de 7 Dias",
                "description": "Estude 7 dias consecutivos",
                "icon": "⚡",
                "condition": lambda stats: stats["streak"] >= 7
            },
            {
                "id": "level_2",
                "name": "Alcançou Nível 2",
                "description": "Chegue ao nível 2",
                "icon": "⭐",
                "condition": lambda stats: stats["level"] >= 2
            },
            {
                "id": "level_3",
                "name": "Alcançou Nível 3",
                "description": "Chegue ao nível 3",
                "icon": "🌟",
                "condition": lambda stats: stats["level"] >= 3
            },
            {
                "id": "points_100",
                "name": "100 Pontos",
                "description": "Acumule 100 pontos",
                "icon": "💯",
                "condition": lambda stats: stats["points"] >= 100
            },
            {
                "id": "points_500",
                "name": "500 Pontos",
                "description": "Acumule 500 pontos",
                "icon": "🏆",
                "condition": lambda stats: stats["points"] >= 500
            },
        ]
    
    def get_user_achievements(self) -> List[Dict]:
        """
        Retorna as conquistas do usuário.
        
        Returns:
            Lista de conquistas conquistadas
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT achievement_id, achieved_at FROM achievements WHERE user_id = ?",
            (self.user_id,)
        )
        results = cursor.fetchall()
        
        conn.close()
        
        all_achievements = self._get_available_achievements()
        user_achievements = []
        
        for achievement in all_achievements:
            achieved = any(result[0] == achievement["id"] for result in results)
            user_achievements.append({
                **achievement,
                "achieved": achieved,
                "achieved_at": next((result[1] for result in results if result[0] == achievement["id"]), None)
            })
        
        return user_achievements
    
    def get_activity_history(self, limit: int = 10) -> List[Dict]:
        """
        Retorna o histórico de atividades do usuário.
        
        Args:
            limit: Número máximo de atividades a retornar
            
        Returns:
            Lista de atividades recentes
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            """SELECT activity_type, activity_data, points_earned, timestamp 
               FROM activity_history 
               WHERE user_id = ? 
               ORDER BY timestamp DESC 
               LIMIT ?""",
            (self.user_id, limit)
        )
        results = cursor.fetchall()
        
        conn.close()
        
        activities = []
        for result in results:
            activities.append({
                "type": result[0],
                "data": json.loads(result[1]) if result[1] else None,
                "points": result[2],
                "timestamp": result[3]
            })
        
        return activities
