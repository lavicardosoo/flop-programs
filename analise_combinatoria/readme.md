
# 🔐 Gerador de Senhas com Brute Force (Projeto Educacional)

Este é um projeto feito com fins **educacionais** para demonstrar como conceitos de **análise combinatória** podem ser aplicados na **programação**. Mais especificamente na geração e teste de senhas por meio de um **ataque de Brute Force**.

Eu estava resolvendo algumas questões do ENEM 2024, e acabei encontrando uma questão que falava sobre a criação de senhas e as combinações
possíveis, com determinados números e requisitos específicos. Decidi ver como seria gerar essas senhas com os meus próprios requisitos, e aplicá-las em uma página web feita localmente(obviamente por motivos de ética, e pelo fato da maioria das páginas possuirem medidas de segurança contra o Brute Force). 

O sistema simula um ataque à uma página, baseada na aparência da tela de login do Instagram, onde senhas são testadas automaticamente até que a correta seja encontrada.(Tudo feito localmente)

## 🚀 Tecnologias usadas

- **Python 3**
- **Selenium** (para automação do navegador)
- **HTML/CSS e Javascript** (para a página de login local)
- **Random** (para gerar letras aleatórias e fazer combinações) | Intertools também é uma ótima opção para tarefas como essa

## 🧠 Objetivo educacional

Demonstrar:
- Como a **análise combinatória** (permutação e combinação de caracteres) pode gerar todas as possíveis senhas dentro de certos critérios.
- A importância de criar **senhas fortes**, já que senhas curtas ou simples podem ser facilmente descobertas por força bruta.
- O uso de **automatização com Python** para testar senhas de forma iterativa.

## ⚠️ Aviso Legal

> Este projeto **não deve ser usado para invadir contas reais**. Ele foi feito apenas como uma simulação local, sem qualquer intenção de prejudicar sistemas ou violar políticas de segurança. O uso indevido pode ser ilegal.

## 💻 Como usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/lavicardosoo/analise_combinatoria.git
   ```

2. Instale as dependências:
   ```bash
   pip install selenium
   ```

3. Instale o webdriver referente ao navegador que você está utilizando. No caso desse projeto
está sendo utilizado o navegador chromium. Recomendo que seja utilizado esse navegador, caso contrário será necessário
mudar parte do código para ficar configurado para outro navegador.

5. Adicione nessa parte do código os caminhos referentes:
    ```bash 
    #define o caminho do executável do navegador(nesse caso o chromium pq o chrome n estava funcionando :( )
    options = ChromiumOptions()
    options.binary_location = 'aqui vc adiciona o caminho executável do chromium'

    #faz com que a janela continue aberta depois de rodar o script 
    options.add_experimental_option("detach",True)

    #define o caminho do webdriver que vai ser utilizado(depende do navegador que está sendo utilizado)
    servico = ChromiumService('aquir vc adiciona o caminho do webdriver do chromium')
    ```

6. Execute o script:
   ```bash
   python /analise_combinatoria/main.py
   ```

## 📈 Explicação combinatória

O número de combinações possíveis é calculado com base no tamanho do alfabeto e na quantidade de caracteres usados na senha. Por exemplo:
- Para senhas de 4 dígitos com caracteres de `a-z`, temos `26⁴ = 456.976` combinações possíveis.
- No caso desse projeto foram utilizadas somente as letras 'a','c','s' e 't', obtendo 4⁴ = 256 diferentes combinações(contando somente com a formatação minúsculas das letras).
- Esse conceito é parte essencial da **combinatória** em matemática.

## 🧠 Aprendizados

- Automatizar tarefas com Selenium
- Gerar combinações com random(também é há outras opções como Intertools)
- Aplicar matemática discreta em contextos computacionais
- Entender os riscos de senhas fracas

## ✨
Projeto feito como parte de um estudo sobre aplicações práticas de análise combinatória na computação.
