# Contributing
> Pode contribuir a vontade, você será sempre bem-vindo(a). Mas temos algumas regras para serem seguidas.

## Adicionar/Atualizar funcionalidades

Você olhou a aplicação e pensou em alguma funcionalidade que deveria ser adicionada no projeto ? :open_mouth:

***Então, você tem duas opções:***

- [Abrir uma issue detalhando sua ideia](#criando-uma-issue)
- [Você mesmo implementar a funcionalidade](#contribuir-com-implementação)

## Criando uma issue

Na página do [projeto](https://github.com/Rickecr/PyGraph), você pode clicar no botão `Issues` e na página irá aparecer um botão `new issue`, então é só selecionar e seguir os seguintes passos:

- Selecione o tipo da sua issue: `Bug ou Feature`.
- Dê um bom nome a sua issue.
- Detalhe bem sobre qual objetivo da issue.
- Imagens caso possível.
- Selecione labels para sua issue.
- Por fim, clique em `Submit new issue`.

## Clonar o repositório

Na página inicial do [repositório](https://github.com/Rickecr/PyGraph) tem um botão `Fork`. Ao clicar é só esperar concluir o fork. E então ele irá criar o repositório na sua conta. E agora é só clonar em sua máquina, assim:

```sh
git clone https://github.com/<nome_de_usuario>/PyGraph
```

Ao concluir, você terá o repositório em seu computador e então é só abrir em seu editor preferido e fazer suas modificações.

Ao terminar suas modificações, você deve commitar suas alterações, mas primeiro:

```sh
git add .
```

O comando acima irá preparar todos os arquivos modificados para serem commitados, passando por todas as alterações que foram feitas por você onde decedirá se a alteração será adicionada (você deve estar dentro da pasta do projeto para usar o comando). Agora é só commitar as alterações:

```sh
git commit -m "<Sua_Mensagem>"
```

E por fim, você irá enviar as alterações para o repositório remoto:

```sh
git push origin master
```

Mas isso só irá alterar no seu fork, o repositório oficial não vai ter suas alterações e agora ? :confused:

Calma, agora que entra o `Pull Request` ou `PR`

## Contribuir com implementação:

Depois de ter realizado o fork e o clone do projeto, escolhido seu editor de texto favorito, nós amamos o VSCode, mas fique a vontade para escolher o seu. Então é hora de codar.

Mas calma ai, antes de qualquer coisa, você deve **escolher uma issue** que pretender trabalhar. Se a issue que trata sobre a funcionalidade não existir, você deve criar e dizer que esta trabalhando nela, caso ela exista você deve dizer lá(caso não já tenha alguém) que pretende trabalhar na issue. E após feito isso, agora sim você está pronto para **codar**.

### Entendendo as pastas:

O projeto se encontra na pasta `py_graph_t`, estamos aceitando dicas de nomes para biblioteca também :blush: .

- Na pasta `edges` : Encontra-se todos os arquivos sobre arestas de um grafo, todas as implementações de uma aresta irão estar nessa pasta. Por exemplo, quando existir um grafo com arestas que possuem pesos, essa aresta será criada dentro dessa pasta, herdando da classe base de aresta(`SimpleEdge`).

- Na pasta `vertex` : Encontra-se todos os arquivos sobre vértices de um grafo, todas as implementações de um vértice irão estar nessa pasta. Por exemplo, quando existir um grafo com vértices que possuem um dado a ser salvo, esse vértice será criado dentro dessa pasta, herdando da classe base de vértice(`SimpleVertex`).

### Como executar a aplicação:

Nós usamos o poetry para gerenciar os pacotes. Portanto, antes de tudo precisamos instalá-lo.

- Instalar o poetry:

    ~~~bash
    $ pip install --user poetry
    ~~~

- Para entrar em um shell dentro do seu ambiente virtual:

    ~~~bash
    $ poetry shell
    ~~~

- Instalar as dependências usadas no projeto:

    ~~~bash
    $ poetry install
    ~~~

Para mais detalhes do [poetry](https://python-poetry.org/docs/)

**OBS:** Executar o comando acima dentro da pasta do projeto.

- Agora você esta pronto para implementar sua funcionalidade/correção.

### Depois de implementar sua correção/funcionalidade:

Muito bem. Agora só falta uma coisinha para abrir sua PR e ela ser aceita, **Testes**. Muita gente não gosta, nós sabemos, mas são eles que garantem que todo nosso código esteja funcionando. Assim facilitando muito a vida dos desenvolvedores.

#### Testes:

Para os testes nós optamos por usar o `pytest`, visto que é bem aceito pela comunidade Python e bastante fácil de usar.

- Primeiro você precisa instalar o poetry:

    ~~~bash
    $ pip install --user poetry
    ~~~

- Para entrar em um shell dentro do seu ambiente virtual:

    ~~~bash
    $ poetry shell
    ~~~

- Para instalar as dependências usadas no projeto:

    ~~~bash
    $ poetry install
    ~~~

**OBS:** Os dois comandos acima só são necesśarios, caso ainda não tenha feito.

- Para testar se tudo funcionou bem, digite no terminal:

    ~~~bash
    $ poetry run pytest --version
    ~~~

- Se a saída for a mesma que abaixo(podendo mudar a versão) esta tudo correto:

    ~~~bash
    $ This is pytest version 5.2.0, imported from /home/rickecr/.local/lib/python3.6/site-packages/pytest.py
    ~~~

- Para execução da suite de testes basta executar:
   
    ~~~bash
    $ poetry run pytest
    ~~~
   
- Para a execução dos testes no modo watch:

    ~~~bash
    $ poetry run ptw
    ~~~
  

E agora é só criar sua classe de teste, caso ela não exista para a classe que você fez a funcionalidade.
Você deve criar os testes para a(s) sua(s) funcionalidade(s), tentando pegar todos os casos extremos, sabemos que é dificil também.

E suas alterações devem garantir que os outros testes continuem funcionando, a não ser que você tenha achado um problema no código, algo que não deveria acontecer.

E após realizar os testes, você está pronto para realizar sua [PR](https://github.com/Rickecr/PyGraph/blob/master/CONTRIBUTING.md#realizando-uma-pull-request---pr) e ser feliz com o mundo OpenSource.


### Entrando nos padrões:

Nós optamos por seguir o padrão da [PEP 8](https://www.python.org/dev/peps/pep-0008/). Portanto, seu código não deve violar nenhuma regra da mesma. Para verificar isso, usamos o `pycodestyle`.

#### Pycodestyle:

Nós usamos o poetry para gerenciar nossas dependências.

- Primeiro você precisa instalar o pipenv:

    ~~~bash
    $ pip install --user poetry
    ~~~
    
- Para instalar as dependências usadas no projeto:

    ~~~bash
    $ poetry install
    ~~~

**OBS:** Os dois comandos acima só são necesśarios, caso ainda não tenha feito.

- Para executar o pycodestyle:
    
    ~~~bash
    poetry run pycodestyle .
    ~~~

## Realizando uma Pull Request - PR

Na página do seu fork irá aparecer uma mensagem em amarelo solicitando que você faça uma Pull Request para o repositório original. Ao clicar irá abrir uma página para você preencher as informações sobre sua PR.

- Referencie a issue em que você está trabalhando usando `#<numero_da_issue>`

- Descreva suas modificações

- Espere pela avaliação da sua PR, e pode ocorrer de pedimos algumas alterações a seres feitas
