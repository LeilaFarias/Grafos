[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Fcga1yCj)
# Lab 01 - 2023.1

O objetivo desta atividade em Laboratório é construir as funções designadas usando o pacote NetworkX.

Este repositório está organizado da seguinte forma:
* O folder **src** contém os arquivos onde as funções solicitadas neste exercício devem ser implementadas;
* o folder **test** contém testes automáticos para cada uma das funções a serem implementadas. Estes testes são automaticamente executados durante a submissão (*push*) de cada *commit* do repositório. Para executar estes testes no VSCode, use o seguinte comando no terminal, a partir do folder principal (como exemplo, considere a questão Q01):

  python -m unittest test/test_Q01.py

* No folder principal, os trechos de código main_<questão>.py apresentam um ambiente para teste manual de cada função;
* **gtufcg** é um submódulo público da disciplina. 



**Observações Gerais**:

*  Use estritamente a estrutura já disponível, não altere nomes de arquivos ou sua localização e não altere o nome das funções, porque isto poderá inviabilizar a execução automática de testes durante o push do repositório;

* O folder **gtufcg** é um submódulo do git. Ao clonar este repositório, o conteúdo de gtufcg poderá não ser copiado. Assim, para carregar o seu conteúdo, execute os seguintes comandos no terminal, a partir do diretório raiz deste repositório:

    git submodule init

    git submodule update

* Para concluir a realização do exercício, o repositório deve ser submetido (push) pelo menos uma vez. 
