# Analisador de Currículos

Este é um projeto de análise de currículos que utiliza a API do Ollama para resumir e pontuar currículos com base na descrição de uma vaga específica. O projeto é desenvolvido em Python, com o Streamlit como front-end para a interface do usuário.

## Funcionalidades

- **Upload de Currículos em Lote**: Carregue vários currículos de uma vez para análise.
- **Análise de Currículos**: Avalie currículos com base em diferentes seções, atribuindo uma pontuação conforme a relevância para a vaga.
- **Comparação de Currículos**: Compare currículos lado a lado para uma avaliação mais detalhada.
- **Análise Crítica Descritiva**: Geração de uma análise crítica e descritiva sobre o currículo em relação à vaga.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal utilizada no projeto.
- **Streamlit**: Framework utilizado para criar a interface web de maneira rápida e interativa.
- **Groq API (Llama 3.1)**: API utilizada para resumir os currículos e gerar a pontuação.
- **Pip**: Ferramenta de gerenciamento de pacotes em Python para instalar as dependências do projeto.

## Instalação e Execução

Para executar este projeto localmente, siga as etapas abaixo:

### Pré-requisitos

- Python 3.10 ou superior
- Pip instalado globalmente

### Passos para instalação

1. Clone este repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/PauloVictoSantos/cv-analyzer.git
   cd cv-analyser
   ```

2. Instale as dependências do projeto utilizando o Poetry:
   ```bash
   pip install
   ```

3. Execute o projeto com o Streamlit:
   ```bash
   streamlit run analyze/app.py
   ```

4. Acesse o projeto no seu navegador através do endereço:
   ```
   http://localhost:8502
   ```

## Documentação do Sistema de Pontuação

O sistema de pontuação foi projetado para avaliar currículos com base em uma vaga específica. As seções avaliadas incluem:

- **Experiência (Peso: 30%)**
- **Habilidades Técnicas (Peso: 25%)**
- **Educação (Peso: 10%)**
- **Idiomas (Peso: 10%)**
- **Pontos Fortes (Peso: 15%)**
- **Pontos Fracos (Desconto de até 10%)**

Cada seção recebe uma pontuação de 0 a 10, com justificativas para as notas atribuídas. A pontuação final é uma média ponderada das avaliações, refletindo a adequação do candidato à vaga.

## Melhorias Futuras

- Melhoria na Visualização dos Gráficos e no Front-end
Aperfeiçoar a interface gráfica com gráficos interativos e visualizações modernas, tornando os dados mais acessíveis e compreensíveis.

- Menu para Cadastro de Vagas e Currículos
Implementar um menu intuitivo para facilitar o cadastro de novas vagas e a adição de currículos diretamente pela interface.

- Exportação de Relatórios
Adicionar uma funcionalidade que permita a exportação de relatórios detalhados em formatos como PDF ou Excel para documentação e análise externa.

- Histórico de Vagas e Análises
Criar uma seção dedicada ao histórico de vagas e análises realizadas, com filtros para datas, cargos ou status.

- Personalização do Painel
Permitir que usuários personalizem o painel de visualização, escolhendo métricas, gráficos e informações relevantes.

- Análise Comparativa entre Candidatos
Desenvolver um recurso que possibilite a comparação direta de candidatos, destacando diferenças em habilidades, experiências e adequação à vaga.

- Personalizar o Sistema de Pontuação
Oferecer a opção de personalizar o sistema de pontuação de acordo com os critérios de cada empresa ou vaga específica, permitindo ajustes nos pesos e nas seções avaliadas. Isso possibilitará uma avaliação ainda mais precisa e alinhada com as necessidades de cada recrutador.
