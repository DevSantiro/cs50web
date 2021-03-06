Procurar
Crie um front-end para a Pesquisa do Google, a Pesquisa de imagens do Google e a Pesquisa avançada do Google.

fundo
Lembre-se da palestra de que podemos criar um formulário HTML usando uma <form>tag e podemos adicionar <input>tags para criar campos de entrada para esse formulário. Mais adiante, veremos como escrever aplicativos da Web que podem aceitar dados de formulário como entrada. Para este projeto, escreveremos formulários que enviam dados para um servidor da Web existente: neste caso, o Google.

Quando você realiza uma pesquisa no Google, digitando uma consulta na página inicial do Google e clicando no botão 
Pesquisa
do
Google, como essa consulta funciona? Vamos tentar descobrir.

Navegue para https://www.google.com/, digite uma consulta como Harvard no campo de pesquisa e clique no botão Pesquisa
do
Google.

Como você provavelmente esperava, você verá os resultados de pesquisa do Google para Harvard. Mas agora, dê uma olhada no URL. Deve começar com https://www.google.com/searcha rota no site do Google que permite a pesquisa. Mas seguir a rota é um ?, seguido por algumas informações adicionais.

Essas informações adicionais no URL são conhecidas como uma string de consulta. A string de consulta consiste em uma sequência de parâmetros GET, em que cada parâmetro tem um nome e um valor. As cadeias de consulta geralmente são formatadas como

field1=value1&field2=value2&field3=value3...
onde um =separa o nome do parâmetro de seu valor e o &símbolo separa os parâmetros um do outro. Esses parâmetros são uma maneira de os formulários enviarem informações para um servidor Web, codificando os dados do formulário no URL.

Dê uma olhada no URL da sua página de resultados de pesquisa do Google. Parece que existem alguns parâmetros que o Google está usando. Examine o URL (pode ser útil copiá-lo / colá-lo em um editor de texto) e veja se você encontra alguma menção a Harvard, nossa consulta.

Se você procurar na URL, verá que um dos parâmetros GET na URL é q=Harvard. Isso sugere que o nome do parâmetro correspondente a uma pesquisa no Google é q(provavelmente abreviação de query).

Acontece que, enquanto os outros parâmetros fornecem dados úteis ao Google, apenas o qparâmetro é necessário para realizar uma pesquisa. Você pode testar isso por si mesmo visitando https://www.google.com/search?q=Harvard, excluindo todos os outros parâmetros. Você deve ver os mesmos resultados do Google!

Usando essas informações, podemos realmente reimplementar um front end para a página inicial do Google. Cole o abaixo em um arquivo HTML chamado index.htmle abra-o em um navegador.

<!DOCTYPE html>
<html lang=en>
    <head>
        <title>Search</title>
    </head>
    <body>
        <form action=https://google.com/search>
            <input type=text name=q>
            <input type=submit value=Google
Search>
        </form>
    </body>
</html>
Ao abrir esta página em um navegador, você verá um formulário HTML (muito simples). Digite uma consulta de pesquisa como Harvard e clique em Pesquisa
do
Google, e você será direcionado para a página de resultados de pesquisa do Google!

Como isso funcionou? Nesse caso, o actionatributo no forminformou ao navegador que, quando o formulário for enviado, os dados deverão ser enviados para https://google.com/search. E adicionando um inputcampo ao formulário cujo nameatributo era q, o que quer que o usuário digite nesse campo de entrada é incluído como um parâmetro GET na URL.

Sua tarefa neste projeto é expandir este site, criando seu próprio front end para a Pesquisa do Google, explorando a interface do Google para identificar quais parâmetros GET esperam e adicionando o HTML e CSS necessários ao seu site.

Começando
Faça o download do código de distribuição em https://cdn.cs50.net/web/2020/spring/projects/0/search.zip e descompacte-o.
Especificação
Seu site deve atender aos seguintes requisitos.

Páginas . Seu site deve ter pelo menos três páginas: uma para a Pesquisa do Google, uma para a Pesquisa de imagens do Google e uma para a Pesquisa avançada do Google.
Na página Pesquisa do Google, deve haver links no canto superior direito da página para acessar a Pesquisa de imagens ou a Pesquisa avançada. Em cada uma das outras duas páginas, deve haver um link no canto superior direito para voltar à Pesquisa do Google.
Texto de consulta . Na página de Pesquisa do Google, o usuário deve poder digitar uma consulta, clicar em Pesquisa
do
Google e ser levado aos resultados de pesquisa do Google para essa página.
Como o próprio Google, sua barra de pesquisa deve estar centralizada com cantos arredondados. O botão de pesquisa também deve estar centralizado e deve estar abaixo da barra de pesquisa.
Imagens de consulta . Na página Pesquisa de imagens do Google, o usuário poderá digitar uma consulta, clicar em um botão de pesquisa e ser direcionado aos resultados da pesquisa de imagens do Google para essa página.
Consulta avançada . Na página Pesquisa avançada do Google, o usuário deve fornecer informações para os quatro campos a seguir (extraídos das próprias opções de pesquisa avançada do Google )
Encontre páginas com… todas
estas
palavras:
Encontre páginas com ... essa
palavra
ou
frase
exata:
Encontre páginas com… qualquer
uma
destas
palavras:
Encontre páginas com… nenhuma
destas
palavras:
Aparência . Como a própria página de Pesquisa avançada do Google, as quatro opções devem ser empilhadas verticalmente e todos os campos de texto devem ser alinhados.
Consistente com o CSS do Google, o botão Pesquisa
avançada deve ficar azul com texto em branco. Quando o botão Pesquisa
avançada é clicado, o usuário deve ser levado para a página de resultados da pesquisa para a consulta em questão.
Sorte . Adicione um botão Estou
com
sorte à página principal da Pesquisa do Google. Consistente com o próprio comportamento do Google, clicar neste link deve levar os usuários diretamente ao primeiro resultado de pesquisa do Google para a consulta, ignorando a página de resultados normal.
Estética . O CSS que você escreve deve corresponder da melhor forma possível à estética do Google.
Dicas
Para determinar quais devem ser os nomes dos parâmetros, experimente fazer pesquisas no Google e consultar o URL resultante. Também pode ser útil abrir o inspetor Rede (acessível no Google Chrome, escolhendo Exibir -> Desenvolvedor -> Ferramentas do desenvolvedor) para exibir detalhes sobre as solicitações feitas pelo navegador ao Google.
Qualquer <input>elemento (se o seu typeé text, submit, number, ou algo completamente diferente) pode ter namee valueatributos que se tornarão parâmetros GET quando um formulário é submetido.
Você também pode achar útil consultar o próprio HTML do Google para responder a essas perguntas. Na maioria dos navegadores, você pode clicar com o botão direito do mouse ou clicar com o botão direito do mouse em uma página e escolher Exibir
código-fonte
da
página para exibir o HTML subjacente da página.
Para incluir um campo de entrada em um formulário que os usuários não possam ver ou modificar, você pode usar um campo de entrada oculto .
Como enviar
Aguente! Se você já enviou e recebeu uma nota de aprovação na versão anterior do Projeto 0 (página inicial), pare aqui. Você já recebeu um crédito de equivalência para este projeto e não deve enviar esta tarefa, pois ela não terá impacto no seu progresso no curso e, portanto, apenas atrasará nossos alunos!

Visite este link , faça login com sua conta do GitHub e clique em Autorizar cs50 . Em seguida, marque a caixa indicando que deseja conceder à equipe do curso acesso aos seus envios e clique em Ingressar no curso .
Instale o Git e, opcionalmente, instalesubmit50 .
Quando você envia seu projeto, o conteúdo da sua web50/projects/2020/x/searchramificação deve corresponder à estrutura do arquivo do código de distribuição descompactado como recebido originalmente. Ou seja, seus arquivos não devem ser aninhados dentro de outros diretórios de sua própria criação ( searchou project0, por exemplo). Sua ramificação também não deve conter nenhum código de outros projetos, apenas este. O não cumprimento desta estrutura de arquivo provavelmente resultará na rejeição do seu envio.

A título de exemplo, para este projeto, isso significa que, se a equipe de classificação visitar https://github.com/me50/USERNAME/blob/web50/projects/2020/x/search/index.html(onde USERNAMEestá seu próprio nome de usuário no GitHub, conforme fornecido no formulário abaixo), seu envio para este projeto deve ser o que aparece. Caso contrário, reorganize seu repositório conforme necessário para corresponder a esse paradigma.

Se você instalou submit50, execute
submit50 web50/projects/2020/x/search
Caso contrário, usando o Git, envie seu trabalho para https://github.com/me50/USERNAME.git, onde USERNAMEestá seu nome de usuário do GitHub, em uma ramificação chamada web50/projects/2020/x/search.

Grave um screencast com no máximo 5 minutos de duração, no qual você demonstra a funcionalidade do seu projeto. Certifique-se de que todos os elementos da especificação acima sejam demonstrados em seu vídeo. Não há necessidade de mostrar seu código neste vídeo, apenas seu aplicativo em ação; revisaremos seu código no GitHub. Carregue esse vídeo no YouTube (como não listado ou público, mas não privado) ou em outro lugar. Na descrição do seu vídeo, você deve registrar o registro de data e hora em que seu vídeo demonstra cada um dos sete (7) elementos da especificação. Isso não é opcional , vídeos sem registro de data e hora na descrição serão automaticamente rejeitados.
Envie este formulário .
Estaremos no meio da transição da versão antiga do CS50W para a nova versão nas primeiras semanas de julho. Durante esse período, os dados do seu boletim de notas podem mostrar apenas suas pontuações anteriores a 30 de junho de 2020, podem estar parcialmente incompletos ou mostrar diferentemente do que você espera. Esperamos ter feito a transição completa do boletim de notas até 17 de julho de 2020.

Você pode então acessar https://cs50.me/cs50w para ver seu progresso atual!
