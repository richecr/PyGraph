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

O comando acima irá preparar todos os arquivos modificados para serem commitados(você deve estar dentro da pasta do projeto para usar o comando). Agora é só commitar as alterações:

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

Depois de ter realizado o fork e o clone do projeto, escolhido seu editor de texto favorito, nós amamos o VSCode, mas fique a vontade para escolher o seu. Então é hora da codificação.

Mas calma ai, antes de qualquer coisa, você deve escolher uma issue que pretender trabalhar. Se a issue que trata sobre a funcionalidade não existir, você deve criar e dizer que esta trabalhando nela, caso ela exista você deve dizer lá(caso não já tenha alguém) que pretende trabalhar na issue. E após feito isso, agora sim você está pronto para codificação.

### Entendendo as pastas:

O projeto se encontra na pasta `py_graph_t`, estamos aceitando dicas de nomes para biblioteca também :blush: .

- Na pasta `edges` : Encontra-se todos os arquivos sobre arestas de um grafo, todas as implementações de uma aresta irão estar nessa pasta. Por exemplo, quando existir um grafo com arestas que possuem pesos, essa aresta será criada dentro dessa pasta, herdando da classe base de aresta(`SimpleEdge`).

- Na pasta `vertex` : Encontra-se todos os arquivos sobre vértices de um grafo, todas as implementações de um vértice irão estar nessa pasta. Por exemplo, quando existir um grafo com vértices que possuem um dado a ser salvo, esse vértice será criado dentro dessa pasta, herdando da classe base de vértice(`SimpleVertex`).

### Realizando uma Pull Request - PR

Na página do seu fork irá aparecer uma mensagem em amarelo solicitando que você faça uma Pull Request para o repositório original. Ao clicar irá abrir uma página para você preencher as informações sobre sua PR.

- Referencie a issue em que você está trabalhando usando `#<numero_da_issue>`

- Descreva suas modificações

- Espere pela avaliação da sua PR, e pode ocorrer de pedimos algumas alterações a seres feitas
