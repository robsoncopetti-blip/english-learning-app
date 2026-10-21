# English Learning App 🎮📚

Aplicativo de aprendizado de inglês gamificado para crianças, com envolvimento dos pais.

**Dedicado à Betina - a filha mais linda do mundo 💖**

## 🎯 Objetivo

Criar um aplicativo interativo tipo Duolingo para ensinar inglês a crianças de 4-7 anos, com:
- **Versão Criança**: Lições interativas, jogos, gamificação, conteúdo por faixa etária
- **Versão Pai**: Dashboard para acompanhar progresso, enviar desafios
- **Modo Dupla**: Atividades colaborativas entre pai e filho (implementado base)
- **Integração Google**: Agenda, Meet, Drive (estrutura criada)
- **Bilinguismo**: Apoio em português e pronúncia

## ✅ MVP Completo - Funcionalidades Implementadas

### 1. Sistema de Autenticação
- ✅ Login universal (email/senha)
- ✅ Cadastro com data de nascimento
- ✅ Cálculo automático de faixa etária
- ✅ Navegação fluida entre telas
- ✅ Google OAuth (simulado, estrutura pronta)

### 2. Sistema de Faixa Etária (NOVO!)
- ✅ **4-5 anos**: Conteúdo básico, visual, sem leitura
- ✅ **5-6 anos**: Conteúdo intermediário, introdução à leitura
- ✅ **6-7 anos**: Conteúdo avançado, leitura completa, português
- ✅ Conteúdo adaptado automaticamente por idade
- ✅ Lições diferentes por faixa etária

### 3. Tipos de Lições (NOVO!)
- ✅ **Casa**: Sozinho ou com ajuda de familiar físico
- ✅ **Aula**: Dupla Pai/Mãe e filho (estrutura pronta)
- ✅ Suporte a videochamada (estrutura criada)
- ✅ Suporte a chat (estrutura criada)

### 4. Conteúdo Multilíngue (NOVO!)
- ✅ Palavras em inglês
- ✅ Tradução em português
- ✅ Guia de pronúncia (IPA)
- ✅ Leitura em português para faixa 6-7 anos
- ✅ Suporte progressivo de leitura por idade

### 5. Versão Criança
- ✅ Tela principal com design colorido
- ✅ Banner dedicado à Betina 💖
- ✅ Sistema de gamificação (pontos, streak, níveis)
- ✅ Lições interativas por faixa etária:
  - 🎨 Cores (4-9 cores dependendo da idade)
  - 🔢 Números (5-10 números)
  - 🐾 Animais (4-8 animais)
  - 🍎 Frutas (apenas 6-7 anos)
  - 👨‍👩‍👧 Família (apenas 6-7 anos)
- ✅ 2 jogos interativos:
  - 🧠 Jogo da Memória
  - ❓ Quiz Rápido
- ✅ Quiz ao final de cada lição
- ✅ Feedback visual imediato

### 6. Versão Pai
- ✅ Dashboard completo
- ✅ Banner dedicado à Betina 💖
- ✅ Progresso em tempo real (pontos, streak, nível)
- ✅ Histórico de atividades detalhado
- ✅ Sistema de conquistas
- ✅ Envio de desafios (placeholder)
- ✅ Botão Modo Dupla (placeholder)

### 7. Sistema de Gamificação
- ✅ Pontos por lições e jogos
- ✅ Streak (dias consecutivos de estudo)
- ✅ Níveis (1-5 baseados em pontos)
- ✅ Conquistas/badges:
  - Primeira lição
  - Streak de 3/7 dias
  - Níveis 2 e 3
  - Marcos de pontos (100, 500)
- ✅ Banco de dados SQLite para persistência
- ✅ Histórico de atividades

### 8. Integrações Google (Estrutura Criada)
- ✅ Google OAuth Handler (simulado)
- ✅ Google Calendar (agendar sessões)
- ✅ Google Meet (videochamadas)
- ✅ Google Drive (salvar progresso)
- ⏳ Configuração com credenciais reais pendente

## 🚧 Funcionalidades Planejadas (Roadmap)

### 1. Sistema de Usuários Melhorado
- [ ] Apelido como login (ex: Rob, Betina)
- [ ] Senha numérica de 6 dígitos
- [ ] Gênero (define tema de cores)
- [ ] Foto do perfil (para IA)
- [ ] Personagem customizável
- [ ] 3 cores favoritas
- [ ] 3 animais favoritos
- [ ] Salvamento automático de usuários

### 2. Modo Dupla Pai-Filho
- [ ] Chat em tempo real
- [ ] Chamada de vídeo (Google Meet)
- [ ] Atividades colaborativas
- [ ] Pai ajuda durante perguntas/jogos
- [ ] Compartilhamento de tela

### 3. Integração Google Funcional
- [ ] Configurar OAuth 2.0 real
- [ ] Google Agenda (agendar sessões)
- [ ] Google Meet (vídeo chamadas)
- [ ] Google Drive (backup e compartilhamento)

### 4. Gamificação Avançada (Estilo Duolingo)
- [ ] Vidas (hearts)
- [ ] Gemas/coins
- [ ] Loja de recompensas
- [ ] Leaderboards
- [ ] Competições
- [ ] Desafios diários/semanais

### 5. Mais Jogos
- [ ] Jogo de arrastar e soltar
- [ ] Jogo de complete a palavra
- [ ] Jogo de pronúncia
- [ ] Jogo de escutar e identificar

**Veja o roadmap completo em [ROADMAP.md](ROADMAP.md)**

## 🛠️ Stack Tecnológica

- **Framework**: Flet 1.0.4 (Python + Flutter)
- **Linguagem**: Python 3.14
- **Plataformas**: Android, iOS, Windows, Web
- **Banco de Dados**: SQLite (local)
- **Google APIs**: OAuth, Calendar, Meet, Drive (estrutura criada)

## 📁 Estrutura do Projeto

```
english-learning-app/
├── main.py                          # App principal
├── requirements.txt                 # Dependências
├── README.md                       # Este arquivo
├── ROADMAP.md                      # Roadmap de desenvolvimento
├── .gitignore                      # Git ignore
├── lib/
│   ├── core/
│   │   ├── navigation.py          # Sistema de navegação
│   │   ├── gamification.py        # Sistema de gamificação
│   │   └── lesson_types.py        # Tipos de lições e faixa etária (NOVO)
│   ├── models/
│   │   └── user.py                # Modelo de usuário com faixa etária
│   ├── integrations/
│   │   └── google/                # Integrações Google
│   │       ├── oauth_handler.py   # Google OAuth
│   │       ├── calendar_integration.py  # Google Calendar
│   │       ├── meet_integration.py      # Google Meet
│   │       └── drive_integration.py    # Google Drive
│   └── features/
│       ├── login_screen.py        # Tela de login (com Google)
│       ├── register_screen.py     # Tela de cadastro (com data nasc)
│       ├── child_home_screen.py   # Tela criança (por faixa etária)
│       ├── parent_home_screen.py  # Tela pai
│       ├── lessons/
│       │   ├── colors_lesson.py   # Lição de cores
│       │   ├── numbers_lesson.py  # Lição de números
│       │   └── animals_lesson.py  # Lição de animais
│       └── games/
│           ├── memory_game.py     # Jogo da memória
│           └── quiz_game.py       # Quiz rápido
├── assets/                        # Imagens, áudios, fontes
├── gamification.db                # Banco de dados gamification
└── users.db                       # Banco de dados usuários
```

## 🚀 Como Executar

### Instalação

1. Instale Python 3.8 ou superior
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executar em modo desktop (Windows)

```bash
python main.py
```

### Executar em modo web

```bash
python main.py --web
```

## 🎨 Design

- Cores vibrantes e amigáveis para crianças
- Ícones grandes e intuitivos
- Animações suaves
- Feedback visual imediato
- Fontes legíveis (sans-serif)
- Temas baseados em gênero (planejado)
- Conteúdo adaptado por faixa etária

## 📊 Sistema de Pontuação

- **Lições**: 10 pontos por lição + 5 por acerto no quiz
- **Jogos**: 50-70 pontos baseados no desempenho
- **Quiz**: 10 pontos por acerto
- **Níveis**:
  - Nível 1: 0-99 pontos
  - Nível 2: 100-299 pontos
  - Nível 3: 300-599 pontos
  - Nível 4: 600-999 pontos
  - Nível 5: 1000+ pontos

## 👶 Faixas Etárias

### 4-5 Anos
- Conteúdo visual
- Sem leitura
- 4 cores básicas
- 5 números
- Foco em imagens e sons

### 5-6 Anos
- Introdução à leitura
- 6 cores
- 10 números
- 4 animais
- Pronúncia guia

### 6-7 Anos
- Leitura completa
- 9 cores
- 10 números
- 8 animais
- Frutas e família
- Apoio em português
- Pronúncia avançada

## 🔒 Privacidade

- Dados de crianças protegidos
- Controle parental
- Sem anúndios
- Offline-first
- Dados salvos localmente
- Consentimento parental para fotos (planejado)

## 📝 Como Contribuir

Este projeto está em desenvolvimento. Código bem comentado em português para facilitar o entendimento.

## 📄 Licença

Projeto educacional em desenvolvimento.

---

**Status**: MVP funcional completo com faixa etária ✅
**Próxima Prioridade**: Aumentar quantidade de jogos gradualmente
**Dedicado a**: Betina 💖
