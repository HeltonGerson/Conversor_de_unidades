# 🔄 Conversor de Unidades Gerais

Uma ferramenta de Interface de Linha de Comando projetada para realizar conversões métricas e monetárias de forma rápida e precisa.

---

## Funcionalidades Principais

### 1. Módulo Métrico
O conversor métrico oferece suporte para a grande maioria das unidades de medida mais comuns do dia a dia.
* **Fluxo de Operação:** Menu interativo baseado em entrada dupla ("de X para Y").
* **Flexibilidade:** Permite realizar múltiplas conversões consecutivas sem fechar o módulo.
* **Persistência:** O usuário permanece no menu de unidades até que decida explicitamente retornar ao menu principal.

### 2. Módulo Monetário
Conversão dinâmica de valores entre diferentes moedas globais.
* **Tempo Real:** Atualização automática das taxas de câmbio para garantir precisão financeira.
* **Praticidade:** Interface direta que solicita a moeda de origem, a moeda de destino e o valor.

---

## Experiência do Usuário & Aspectos Gerais

* **Interface CLI Intuitiva:** Design autodidata pensado para que o usuário saiba exatamente o que fazer, mesmo sem ler um manual.
* **Fluxo de Navegação Dinâmico:** Telas personalizadas e totalmente distintas para cada módulo.
* **Mensagem de Boas-Vindas:** Abertura estilizada que organiza visualmente o ecossistema do programa logo no primeiro contato.

---

## Aspectos Técnicos

* **Tratamento de Erros Robusto:** Sistema preparado para lidar com entradas inválidas ou falhas de conexão sem quebrar a execução.
* **Customização Segura:** Permite alterar variáveis do sistema de forma personalizada, com garantia de recuperação das configurações padrão de fábrica a qualquer momento.

---

## Fluxo de Navegação

```text
[ Início do Programa ]
       │
       └──> 🎨 Tela de Boas-Vindas
               │
               ├──> 🏢 [Opção 1] Unidades de Medida
               │       │
               │       ├──> Seleção da Unidade Base
               │       ├──> Entrada Dupla ("De" -> "Para")
               │       ├──> Inserção do Valor -> Resultado
               │       └──> Loop (Permanece até solicitar saída)
               │
               └──> 💵 [Opção 2] Financeiro
                       │
                       ├──> Moeda de Origem
                       ├──> Moeda de Destino
                       └──> Consulta & Conversão em Tempo Real
