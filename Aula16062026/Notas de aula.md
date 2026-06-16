A arquitetura básica (estrutura dos módulos) de um programa web será a seguinte:

Obs.: o ideal é que um modulo de para ver todo na tela e que cada função seja no máx 10/15 linhas, se não o ideal é quebrar.



* modulo/pacote es/InOut (aqui posso ter módulos de saída para tela, para http, impressora, etc.; e para entrada por teclado, por arquivo, por http, etc.)
* modulo(s) procedimento(s) que preciso para resolver o problema
* \_\_main\_\_.py



A gestão de rede é feita pelo protocolo (streamlit). Mas para isso preciso indicar, pois por padrão se uso print ele vai colocar a informação na tela; para mandar pela rede preciso usar outra função, socket, o que só funciona se tiver algum http instalado.



\*DAL: gestão de dados quando existem muiotos dados ou já se sabe que no futuro vai ficar muito grande. Se nao for grande, pode deixar a função que le dados no prórpio model. Difere do view também pq este cuida da conversa com o usuário, enquanto o dal serve para fornecer os dados para a conta, nao cuida da interface com o usuario; o write do dal escreve no banco de dados, no view é na tela/para o usuário.

\*MVC: View, Controller, Model - o controller principal será sempre o \_\_main\_\_; se for necessário fazer um controller para cada classe quando o código crescer muito, mas isso é bem raro, se não ficamos em um controller único, ainda que grande. Já o model é a conta específica que se está pedindo fazer, que precisa ter um conhecimento específico de do que o código está fazendo; e o view é a aparencia, que o streamlit vai ajudar, embora seja algo básico para funcionalidade e apresentação.



\*cd .. (para voltar uma pasta para trás)

\*se há um \_\_main\_\_ em uma pasta, para rodar basta usar "python nome\_da\_pasta"



