"""
Lesson Types - Tipos de Lições
================================

Gerencia os diferentes tipos de lições disponíveis:
- Casa: Sozinho ou com ajuda de familiar físico
- Aula: Dupla Pai/Mãe e filho (com videochamada via Google Meet)

Cada tipo tem características diferentes de conteúdo e interação.
"""

from typing import Dict, List, Optional
from enum import Enum


class LessonType(Enum):
    """
    Enumera os tipos de lições disponíveis.
    """
    HOME = "home"  # Casa - sozinho ou com ajuda física
    CLASS = "class"  # Aula - dupla pai/filho com videochamada


class LessonContent:
    """
    Gerencia o conteúdo das lições com suporte multilíngue.
    """
    
    def __init__(self, age_group: str):
        """
        Inicializa o gerenciador de conteúdo.
        
        Args:
            age_group: Faixa etária ('4-5', '5-6', '6-7')
        """
        self.age_group = age_group
        self.content_data = self._load_content_by_age()
    
    def _load_content_by_age(self) -> Dict:
        """
        Carrega o conteúdo baseado na faixa etária.
        
        Returns:
            Dicionário com conteúdo apropriado para a idade
        """
        content = {
            "4-5": {
                "colors": {
                    "words": ["red", "blue", "green", "yellow", "pink", "black", "white"],
                    "portuguese_words": ["vermelho", "azul", "verde", "amarelo", "rosa", "preto", "branco"],
                    "pronunciation": ["/red/", "/bluː/", "/griːn/", "/ˈjɛloʊ/", "/pɪŋk/", "/blæk/", "/waɪt/"],
                    "has_reading": False,  # Foco visual, sem leitura
                    "visual_heavy": True
                },
                "numbers": {
                    "words": ["one", "two", "three", "four", "five", "six", "seven"],
                    "portuguese_words": ["um", "dois", "três", "quatro", "cinco", "seis", "sete"],
                    "pronunciation": ["/wʌn/", "/tuː/", "/θriː/", "/fɔːr/", "/faɪv/", "/sɪks/", "/ˈsɛvən/"],
                    "has_reading": False,
                    "visual_heavy": True
                },
                "animals": {
                    "words": ["dog", "cat", "bird", "fish", "rabbit"],
                    "portuguese_words": ["cachorro", "gato", "pássaro", "peixe", "coelho"],
                    "pronunciation": ["/dɔɡ/", "/kæt/", "/bɜːrd/", "/fɪʃ/", "/ˈræbɪt/"],
                    "has_reading": False,
                    "visual_heavy": True
                }
            },
            "5-6": {
                "colors": {
                    "words": ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "grey"],
                    "portuguese_words": ["vermelho", "azul", "verde", "amarelo", "laranja", "roxo", "rosa", "marrom", "cinza"],
                    "pronunciation": ["/red/", "/bluː/", "/griːn/", "/ˈjɛloʊ/", "/ˈɔrɪndʒ/", "/ˈpɜːrpəl/", "/pɪŋk/", "/braʊn/", "/ɡreɪ/"],
                    "has_reading": True,  # Introdução à leitura
                    "visual_heavy": True
                },
                "numbers": {
                    "words": ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"],
                    "portuguese_words": ["um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze"],
                    "pronunciation": ["/wʌn/", "/tuː/", "/θriː/", "/fɔːr/", "/faɪv/", "/sɪks/", "/ˈsɛvən/", "/eɪt/", "/naɪn/", "/tɛn/", "/ɪˈlɛvən/", "/twɛlv/"],
                    "has_reading": True,
                    "visual_heavy": True
                },
                "animals": {
                    "words": ["dog", "cat", "bird", "fish", "rabbit", "lion", "elephant", "monkey", "horse", "cow"],
                    "portuguese_words": ["cachorro", "gato", "pássaro", "peixe", "coelho", "leão", "elefante", "macaco", "cavalo", "vaca"],
                    "pronunciation": ["/dɔɡ/", "/kæt/", "/bɜːrd/", "/fɪʃ/", "/ˈræbɪt/", "/ˈlaɪən/", "/ˈɛlɪfənt/", "/ˈmʌŋki/", "/hɔːrs/", "/kaʊ/"],
                    "has_reading": True,
                    "visual_heavy": True
                },
                "fruits": {
                    "words": ["apple", "banana", "orange", "grape", "strawberry"],
                    "portuguese_words": ["maçã", "banana", "laranja", "uva", "morango"],
                    "pronunciation": ["/ˈæpəl/", "/bəˈnænə/", "/ˈɔrɪndʒ/", "/ɡreɪp/", "/ˈstrɔːbɛri/"],
                    "has_reading": True,
                    "visual_heavy": True
                }
            },
            "6-7": {
                "colors": {
                    "words": ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "white", "brown", "grey", "gold", "silver"],
                    "portuguese_words": ["vermelho", "azul", "verde", "amarelo", "laranja", "roxo", "rosa", "preto", "branco", "marrom", "cinza", "dourado", "prata"],
                    "pronunciation": ["/red/", "/bluː/", "/griːn/", "/ˈjɛloʊ/", "/ˈɔrɪndʒ/", "/ˈpɜːrpəl/", "/pɪŋk/", "/blæk/", "/waɪt/", "/braʊn/", "/ɡreɪ/", "/ɡoʊld/", "/ˈsɪlvər/"],
                    "has_reading": True,  # Leitura completa
                    "visual_heavy": False,
                    "portuguese_reading": True  # Apoio leitura em português
                },
                "numbers": {
                    "words": ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "twenty"],
                    "portuguese_words": ["um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "vinte"],
                    "pronunciation": ["/wʌn/", "/tuː/", "/θriː/", "/fɔːr/", "/faɪv/", "/sɪks/", "/ˈsɛvən/", "/eɪt/", "/naɪn/", "/tɛn/", "/ɪˈlɛvən/", "/twɛlv/", "/θɜːˈtiːn/", "/fɔːrˈtiːn/", "/fɪfˈtiːn/", "/ˈtwɛnti/"],
                    "has_reading": True,
                    "visual_heavy": False,
                    "portuguese_reading": True
                },
                "animals": {
                    "words": ["dog", "cat", "bird", "fish", "rabbit", "lion", "elephant", "monkey", "horse", "cow", "pig", "sheep", "duck", "chicken"],
                    "portuguese_words": ["cachorro", "gato", "pássaro", "peixe", "coelho", "leão", "elefante", "macaco", "cavalo", "vaca", "porco", "ovelha", "pato", "galinha"],
                    "pronunciation": ["/dɔɡ/", "/kæt/", "/bɜːrd/", "/fɪʃ/", "/ˈræbɪt/", "/ˈlaɪən/", "/ˈɛlɪfənt/", "/ˈmʌŋki/", "/hɔːrs/", "/kaʊ/", "/pɪɡ/", "/ʃiːp/", "/dʌk/", "/ˈtʃɪkən/"],
                    "has_reading": True,
                    "visual_heavy": False,
                    "portuguese_reading": True
                },
                "fruits": {
                    "words": ["apple", "banana", "orange", "grape", "strawberry", "watermelon", "pineapple", "peach", "pear"],
                    "portuguese_words": ["maçã", "banana", "laranja", "uva", "morango", "melancia", "abacaxi", "pêssego", "pera"],
                    "pronunciation": ["/ˈæpəl/", "/bəˈnænə/", "/ˈɔrɪndʒ/", "/ɡreɪp/", "/ˈstrɔːbɛri/", "/ˈwɔːtərmɛlən/", "/ˈpaɪnæpəl/", "/piːtʃ/", "/pɪr/"],
                    "has_reading": True,
                    "visual_heavy": False,
                    "portuguese_reading": True
                },
                "family": {
                    "words": ["mother", "father", "sister", "brother", "grandmother", "grandfather", "aunt", "uncle"],
                    "portuguese_words": ["mãe", "pai", "irmã", "irmão", "avó", "avô", "tia", "tio"],
                    "pronunciation": ["/ˈmʌðər/", "/ˈfɑːðər/", "/ˈsɪstər/", "/ˈbrʌðər/", "/ˈɡrændmʌðər/", "/ˈɡrændfɑːðər/", "/ænt/", "/ˈʌŋkəl/"],
                    "has_reading": True,
                    "visual_heavy": False,
                    "portuguese_reading": True
                },
                "body": {
                    "words": ["head", "eyes", "nose", "mouth", "ears", "hands", "feet", "hair"],
                    "portuguese_words": ["cabeça", "olhos", "nariz", "boca", "orelhas", "mãos", "pés", "cabelo"],
                    "pronunciation": ["/hɛd/", "/aɪz/", "/noʊz/", "/maʊθ/", "/ɪrz/", "/hændz/", "/fiːt/", "/hɛər/"],
                    "has_reading": True,
                    "visual_heavy": False,
                    "portuguese_reading": True
                }
            }
        }
        
        return content.get(self.age_group, {})
    
    def get_lesson(self, lesson_name: str) -> Optional[Dict]:
        """
        Retorna o conteúdo de uma lição específica.
        
        Args:
            lesson_name: Nome da lição (ex: 'colors', 'numbers')
            
        Returns:
            Dicionário com conteúdo da lição ou None
        """
        return self.content_data.get(lesson_name)
    
    def get_available_lessons(self) -> List[str]:
        """
        Retorna a lista de lições disponíveis para a faixa etária.
        
        Returns:
            Lista de nomes de lições
        """
        return list(self.content_data.keys())
    
    def supports_portuguese_reading(self, lesson_name: str) -> bool:
        """
        Verifica se a lição suporta leitura em português.
        
        Args:
            lesson_name: Nome da lição
            
        Returns:
            True se suporta leitura em português
        """
        lesson = self.get_lesson(lesson_name)
        return lesson.get("portuguese_reading", False) if lesson else False
    
    def has_pronunciation_guide(self, lesson_name: str) -> bool:
        """
        Verifica se a lição tem guia de pronúncia.
        
        Args:
            lesson_name: Nome da lição
            
        Returns:
            True se tem guia de pronúncia
        """
        lesson = self.get_lesson(lesson_name)
        return "pronunciation" in lesson if lesson else False


class LessonTypeManager:
    """
    Gerencia os tipos de lições (Casa vs Aula).
    """
    
    def __init__(self):
        """
        Inicializa o gerenciador de tipos de lições.
        """
        self.active_sessions = {}  # Sessões ativas de aula (pai + filho)
    
    def get_lesson_type_config(self, lesson_type: LessonType) -> Dict:
        """
        Retorna a configuração para um tipo de lição.
        
        Args:
            lesson_type: Tipo de lição (HOME ou CLASS)
            
        Returns:
            Dicionário com configuração do tipo de lição
        """
        configs = {
            LessonType.HOME: {
                "name": "Casa",
                "description": "Estude sozinho ou com ajuda de familiar físico",
                "supports_video": False,
                "supports_chat": False,
                "parent_participation": "optional",  # Pai pode ajudar fisicamente
                "difficulty_adjustment": "adaptive",  # Adapta dificuldade se criança pedir ajuda
                "requires_google_meet": False
            },
            LessonType.CLASS: {
                "name": "Aula",
                "description": "Aula em dupla com Pai/Mãe via videochamada",
                "supports_video": True,
                "supports_chat": True,
                "parent_participation": "required",  # Pai participa ativamente
                "difficulty_adjustment": "collaborative",  # Pai e filho colaboram
                "requires_google_meet": True,
                "requires_google_calendar": True  # Agendar sessão
            }
        }
        
        return configs.get(lesson_type, {})
    
    def start_class_session(self, parent_id: str, child_id: str) -> str:
        """
        Inicia uma sessão de aula (pai + filho).
        
        Args:
            parent_id: ID do pai
            child_id: ID da criança
            
        Returns:
            ID da sessão criada
        """
        import uuid
        session_id = str(uuid.uuid4())
        
        self.active_sessions[session_id] = {
            "parent_id": parent_id,
            "child_id": child_id,
            "started_at": None,
            "google_meet_link": None,
            "status": "pending"
        }
        
        return session_id
    
    def end_class_session(self, session_id: str) -> bool:
        """
        Encerra uma sessão de aula.
        
        Args:
            session_id: ID da sessão
            
        Returns:
            True se encerrada com sucesso
        """
        if session_id in self.active_sessions:
            del self.active_sessions[session_id]
            return True
        return False
    
    def get_active_session(self, session_id: str) -> Optional[Dict]:
        """
        Retorna informações de uma sessão ativa.
        
        Args:
            session_id: ID da sessão
            
        Returns:
            Dicionário com informações da sessão ou None
        """
        return self.active_sessions.get(session_id)
