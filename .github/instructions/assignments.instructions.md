---
description: "Instruções para usar sempre que criar ou editar arquivos markdown de assignment, garantindo consistência e clareza para os alunos."
applyTo: "assignments/**/*.md"
---

# Diretrizes de Estrutura para Markdowns de Tarefas

Todos os arquivos markdown de tarefas devem seguir estas diretrizes:

## 1. Uso do Template

- Os arquivos markdown de tarefas devem seguir a estrutura em [`templates/assignment-template.md`](../../templates/assignment-template.md).
- A tarefa deve ser criada como um arquivo `README.md`
- Não remova ou pule seções obrigatórias do template.

## 2. Orientação das Seções

Os cabeçalhos devem reproduzir EXATAMENTE os textos do template, incluindo acentos e emojis. Use esta estrutura:

- `# 📘 Atividade: [Título da Atividade]` — Escolha um título curto e descritivo.
- `## 🎯 Objetivo` — Escreva 1-2 frases sobre o que o aluno aprenderá ou construirá.
- `## 📝 Tarefas` — Inclua uma ou mais tarefas, cada uma com a estrutura abaixo:
   - `### 🛠️ [Título da Tarefa]` — Use um título específico e orientado à ação.
   - `#### Descrição` — Explique claramente o que o aluno deve fazer.
   - `#### Requisitos` — Liste em bullet points os resultados ou funcionalidades esperados; seja específico e mensurável.

Inclua exemplos de entrada e saída em blocos de código quando forem úteis. Não remova nem pule seções obrigatórias e não adicione seções extras, a menos que solicitado explicitamente.
