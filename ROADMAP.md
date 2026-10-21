# Roadmap de Desenvolvimento - English Learning App

## ✅ Implementado (MVP Completo)

### 1. Sistema de Autenticação Básico
- ✅ Login universal (email/senha)
- ✅ Cadastro (pai ou criança)
- ✅ Navegação entre telas

### 2. Versão Criança
- ✅ Tela principal com design colorido
- ✅ 3 lições interativas (Cores, Números, Animais)
- ✅ 2 jogos interativos (Memória, Quiz)
- ✅ Sistema de gamificação (pontos, streak, níveis)
- ✅ Banner dedicado à Betina 💖

### 3. Versão Pai
- ✅ Dashboard com progresso da criança
- ✅ Histórico de atividades
- ✅ Sistema de conquistas
- ✅ Envio de desafios (placeholder)
- ✅ Banner dedicado à Betina 💖

### 4. Sistema de Gamificação
- ✅ Pontos por atividades
- ✅ Streak (dias consecutivos)
- ✅ Níveis baseados em pontos
- ✅ Conquistas/badges
- ✅ Banco de dados SQLite para persistência

## 🚧 Em Desenvolvimento / Planejado

### 1. Melhorias no Sistema de Cadastro (PRIORIDADE ALTA)

#### O que precisa ser implementado:
- [ ] **Apelido como login**: Usar apelido (ex: Rob, Betina) em vez de email
- [ ] **Senha numérica**: Senha de 6 dígitos (mais fácil para crianças)
- [ ] **Gênero**: Seleção de gênero (Menino/Menina/Outro)
  - Define tema de cores automaticamente
  - Menino: tema azul
  - Menina: tema rosa
  - Outro: tema verde
- [ ] **Foto do perfil**: Upload de foto
  - Usada pela IA para personalizar conteúdo
  - Salva localmente (pasta assets/photos/)
- [ ] **Personagem**: Escolha de avatar/personagem
- [ ] **3 cores favoritas**: Seleção de 3 cores preferidas
  - Personaliza lições e jogos
- [ ] **3 animais favoritos**: Seleção de 3 animais preferidos
  - Personaliza conteúdo e exemplos

#### Arquivos a modificar:
- `lib/models/user.py` ✅ (já criado)
- `lib/features/register_screen.py` (em progresso)
- `lib/features/login_screen.py` (mostrar usuários salvos)
- `main.py` (integrar novo sistema)

### 2. Sistema de Salvamento de Usuários (PRIORIDADE ALTA)

#### O que precisa ser implementado:
- [ ] Lista de usuários cadastrados na tela de login
- [ ] Login automático se usuário já existir
- [ ] Persistência de todos os dados do usuário
- [ ] Bibliotecas personalizadas por usuário
  - Lições favoritas
  - Jogos preferidos
  - Progresso individual

#### Arquivos a criar/modificar:
- `lib/features/login_screen.py` (adicionar lista de usuários)
- `lib/models/user.py` ✅ (já criado)
- `main.py` (integrar sistema)

### 3. Modo Dupla Pai-Filho (PRIORIDADE MÉDIA)

#### O que precisa ser implementado:
- [ ] Sistema de chat em tempo real
- [ ] Chamada de vídeo
- [ ] Atividades colaborativas
  - Quiz em dupla
  - Jogo da memória cooperativo
  - Lições conjuntas
- [ ] Pai pode ajudar durante perguntas/jogos
- [ ] Compartilhamento de tela

#### Tecnologias necessárias:
- WebRTC para vídeo
- WebSocket para chat em tempo real
- Servidor de sinalização

#### Arquivos a criar:
- `lib/features/duo_mode/`
  - `chat_screen.py`
  - `video_call_screen.py`
  - `collaborative_activities.py`

### 4. Integração Google (PRIORIDADE MÉDIA)

#### 4.1 Google Agenda
- [ ] Agendar sessões de estudo
- [ ] Lembretes automáticos
- [ ] Sincronizar com calendário da criança
- [ ] Definir horários de estudo pai-filho

#### 4.2 Google Meet
- [ ] Criar reuniões automáticas
- [ ] Link para vídeo chamada
- [ ] Integração com modo dupla

#### 4.3 Google Drive
- [ ] Salvar progresso e conquistas
- [ ] Armazenar fotos e áudios
- [ ] Backup de dados
- [ ] Compartilhar com pais

#### Tecnologias necessárias:
- Google Calendar API
- Google Meet API
- Google Drive API
- OAuth 2.0 para autenticação Google

#### Arquivos a criar:
- `lib/integrations/google/`
  - `calendar_integration.py`
  - `meet_integration.py`
  - `drive_integration.py`
  - `oauth_handler.py`

### 5. Melhorias na Gamificação (Estilo Duolingo) (PRIORIDADE BAIXA)

#### O que precisa ser implementado:
- [ ] Vidas (hearts)
- [ ] Gemas/coins
- [ ] Loja de recompensas
- [ ] Streak freeze (proteger streak)
- [ ] XP experience points
- [ ] Leagues (competição com outros)
- [ ] Leaderboards
- [ ] Avatar customizável com itens
- [ ] Daily goals
- [ ] Weekly challenges

#### Arquivos a criar:
- `lib/core/gamification.py` (expansão)
- `lib/features/shop/`
  - `shop_screen.py`
  - `avatar_customization.py`
- `lib/features/leaderboard/`
  - `leaderboard_screen.py`

### 6. Aulas Individuais para Criança (PRIORIDADE BAIXA)

#### O que precisa ser implementado:
- [ ] Sistema de temas
- [ ] Aulas baseadas em temas
  - Animais
  - Cores
  - Números
  - Família
  - Frutas
  - Escola
  - etc.
- [ ] Progresso independente
- [ ] Recomendações baseadas em preferências

#### Arquivos a criar:
- `lib/features/lessons/`
  - `themed_lessons.py`
  - `lesson_recommendations.py`

## 📋 Estrutura Sugerida para Continuação

### Fase 1: Sistema de Usuários Melhorado (1-2 dias)
1. Finalizar `register_screen.py` com todas as opções
2. Atualizar `login_screen.py` para mostrar usuários salvos
3. Testar fluxo completo cadastro -> login -> personalização

### Fase 2: Personalização (1 dia)
1. Implementar temas baseados em gênero
2. Personalizar conteúdo com cores/animais favoritos
3. Testar personalização

### Fase 3: Modo Dupla (2-3 dias)
1. Implementar chat básico
2. Implementar vídeo chamada
3. Criar atividades colaborativas
4. Testar modo dupla

### Fase 4: Integração Google (2-3 dias)
1. Configurar OAuth 2.0
2. Implementar Google Agenda
3. Implementar Google Meet
4. Implementar Google Drive
5. Testar integrações

### Fase 5: Gamificação Avançada (2-3 dias)
1. Implementar sistema de vidas
2. Implementar loja
3. Implementar leaderboards
4. Implementar desafios diários/semanais

## 🔧 Tecnologias Adicionais Necessárias

### Para Modo Dupla:
- WebRTC (vídeo)
- WebSocket (chat em tempo real)
- Servidor de sinalização (Socket.io ou similar)

### Para Integração Google:
- google-api-python-client
- google-auth-oauthlib
- google-auth-httplib2

### Para IA:
- OpenAI API (para gerar conteúdo personalizado)
- Base64 para encoding de imagens

## 📝 Notas Importantes

### Sobre Fotos e IA:
- Fotos precisam ser salvas localmente ou no Google Drive
- Enviar para API de IA para gerar contextos personalizados
- Usar a foto para:
  - Personalizar avatares
  - Gerar exemplos com o nome da criança
  - Criar histórias personalizadas

### Sobre Senha Numérica:
- Mais fácil para crianças de 5-7 anos
- Validação: deve ser exatamente 6 dígitos
- Exemplo: 123456

### Sobre Apelido:
- Usado como login único
- Exemplos: Rob, Betina
- Deve ser único no sistema
- Usado para identificar usuário no banco de dados

### Sobre Gênero e Temas:
- Define cores da interface
- Define tipo de personagens
- Pode ser alterado depois nas configurações

## 🎯 Próximos Passos Imediatos

1. ✅ Modelo de usuário criado (`lib/models/user.py`)
2. 🔄 Atualizar tela de cadastro com novas opções
3. ⏳ Atualizar tela de login para mostrar usuários salvos
4. ⏳ Implementar temas baseados em gênero
5. ⏳ Testar fluxo completo

---

**Status Atual**: MVP funcional completo, pronto para expansão
**Próxima Prioridade**: Sistema de usuários melhorado com personalização
