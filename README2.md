A aplicação consiste em uma API que simula o saque de um banco. Foi feita na linguagem python usando a ferramenta do Visual Studio Code.
Para realizar o teste da aplicação usando o visual studio code faça os seguintes passos:
Abra o terminal (Ctrl+') e digite o seguinte comando: python api/saque.py.
Abra um novo terminal e digite o seguinte comando: $body = '{"valor":300}'
    >> $headers = @{
    >>     "Content-Type" = "application/json"
    >> }
    >>
    >> Invoke-WebRequest -Uri "http://localhost:5000/api/saque" -Method POST -Headers $headers -Body $body
    >> 
Subistituindo o o "valor" pela quantia que deseja sacar.

O programa faz a checagem se o valor é negativo, retornando um erro caso seja. Faz também a checagem se o valor é um inteiro, retornando outro erro.

Considerações: Meu conhecimento com a linguagem Python é limitado, precisei de ajuda para que pudesse transformar uma lógica simples em API. Meu contato mais próximo com API foi com JavaScript durante trabalhos da faculdade, ainda sim, bem básico considerando que estou no primeiro período. O arquivo "saqueBasico.py" foi a minha ideia do que seria esse desafio. Como ainda não tive contato com a linguagem diretamente na faculdade, somente a estudei por fora, tenho certeza de que há formas para otimizar o código. Mesmo que não resulte em nada, foi divertido ter a oportunidade de experimentar soluções novas em "solo desconhecido". Agradeço a equipe da morada.ia desde já.