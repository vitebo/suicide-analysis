# Suicide Data Service
Um serviço com o objetivo de fornecer uma interface de alto nivel para efetuar buscas sobre suicidio no
[Data SUS](http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sim/cnv/obt10SP.def).

## Métodos
Lista dos métodos públicos do serviço

### Search
Efetua uma busca no **DATA SUS** de acordo com os filtros passados, e retorna a tabela separando as colunas por ``;``

#### Parâmetros
| params  | type | required |
|---------|------|----------|
| options | dict | false    |

##### options
Parâmetro opcional para adicionar filtros para a busca.
Options é um **dict**, e as sus possiveis **keys** para os filtros são:
- Linha
- Coluna
- Incremento
- Arquivos
- SMunicípio
- SRegião_de_Saúde_(CIR)
- SMacrorregião_de_Saúde
- SDivisão_administ_estadual
- SMicrorregião_IBGE
- SRegião_Metropolitana_-_RIDE
- SCapítulo_CID-10
- SGrupo_CID-10
- SCategoria_CID-10
- SCausa_-_CID-BR-10
- SCausa_mal_definidas
- SFaixa_Etária
- SFaixa_Etária_OPS
- SFaixa_Etária_det
- SFx.Etária_Menor_1A
- SSexo
- SCor/raça
- SEscolaridade
- SEstado_civil
- SLocal_ocorrência

###### Linha
Define oque será exibido na linha da tabela 
- 'Município' *(DEFAULT)*
- 'Região_de_Saúde_(CIR)'
- 'Região_de_Saúde/Município'
- 'Macrorregião_de_Saúde'
- 'Divisão_administ_estadual'
- 'Divisão_admin_estadual/Municíp'
- 'Microrregião_IBGE'
- 'Microrregião_IBGE/Município'
- 'Região_Metropolitana_-_RIDE'
- 'Capítulo_CID-10'
- 'Grupo_CID-10'
- 'Categoria_CID-10'
- 'Causa_-_CID-BR-10'
- 'Causa_mal_definidas'
- 'Ano_do_Óbito'
- 'Ano/mês_do_Óbito'
- 'Mês_do_Óbito'
- 'Faixa_Etária'
- 'Faixa_Etária_OPS'
- 'Faixa_Etária_det'
- 'Fx.Etária_Menor_1A'
- 'Sexo'
- 'Cor/raça'
- 'Escolaridade'
- 'Estado_civil'
- 'Local_ocorrência'

###### Coluna
Define oque será exibido na coluna da tabela 
- '--Não-Ativa--' *(DEFAULT)*
- 'Região_de_Saúde_(CIR)'
- 'Região_de_Saúde/Município'
- 'Macrorregião_de_Saúde'
- 'Divisão_administ_estadual'
- 'Divisão_admin_estadual/Municíp'
- 'Microrregião_IBGE'
- 'Microrregião_IBGE/Município'
- 'Região_Metropolitana_-_RIDE'
- 'Capítulo_CID-10'
- 'Grupo_CID-10'
- 'Categoria_CID-10'
- 'Causa_-_CID-BR-10'
- 'Causa_mal_definidas'
- 'Ano_do_Óbito'
- 'Ano/mês_do_Óbito'
- 'Mês_do_Óbito'
- 'Faixa_Etária'
- 'Faixa_Etária_OPS'
- 'Faixa_Etária_det'
- 'Fx.Etária_Menor_1A'
- 'Sexo'
- 'Cor/raça'
- 'Escolaridade'
- 'Estado_civil'
- 'Local_ocorrência'

###### Incremento
- 'Incremento'
- 'Óbitos_p/Ocorrênc'

###### Arquivos
Define o ano de onde sera tirado os dados
- 'obtsp16.dbf' *(DEFAULT)*
- 'obtsp15.dbf'
- 'obtsp14.dbf'
- 'obtsp13.dbf'
- 'obtsp12.dbf'
- 'obtsp11.dbf'
- 'obtsp10.dbf'
- 'obtsp09.dbf'
- 'obtsp08.dbf'
- 'obtsp07.dbf'
- 'obtsp06.dbf'
- 'obtsp05.dbf'
- 'obtsp04.dbf'
- 'obtsp03.dbf'
- 'obtsp02.dbf'
- 'obtsp01.dbf'
- 'obtsp00.dbf'
- 'obtsp99.dbf'
- 'obtsp98.dbf'
- 'obtsp97.dbf'
- 'obtsp96.dbf'

###### SMunicípio
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 499

###### SRegião_de_Saúde_(CIR)
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 64

###### SMacrorregião_de_Saúde
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 18

###### SDivisão_administ_estadual
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 18

###### SMicrorregião_IBGE
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 64

###### SRegião_Metropolitana_-_RIDE
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 13

###### SCapítulo_CID-10
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 22

###### SGrupo_CID-10
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 264

###### SCategoria_CID-10
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 2045

###### SCausa_-_CID-BR-10
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 144

###### SCausa_mal_definidas
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 4

###### SFaixa_Etária
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 13

###### SFaixa_Etária_OPS
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 11

###### SFaixa_Etária_det
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 22

###### SFx.Etária_Menor_1A
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 4

###### SSexo
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 3

###### SCor/raça
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 6

###### SEscolaridade
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 8

###### SEstado_civil
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 6

###### SLocal_ocorrência
- 'TODAS_AS_CATEGORIAS__' *(DEFAULT)*
- 1 ... 6

#### Exemplo de saída:
<pre>
"Município";"Óbitos p/Residênc"
"350010 Adamantina";1
"350070 Agudos";2
"350100 Altinópolis";2
"350115 Alumínio";1
"350130 Álvares Machado";1
</pre>





