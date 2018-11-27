# Mortality Data Service
Um serviço com o objetivo de fornecer uma interface de alto nivel para efetuar buscas sobre **mortalidade - 1996 a 2016, pela CID-10** utilizando o site do
**[Data SUS](http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sim/cnv/obt10SP.def)**.

## Métodos
Lista dos métodos públicos do serviço

### Search
Efetua uma busca no **DATA SUS** de acordo com os filtros passados, e retorna o resultado em um arquivo *csv*

#### Parâmetros
| params  | type | required | return      |
|---------|------|----------|-------------|
| options | dict | false    | StringIO    |

##### options
Parâmetro opcional para adicionar filtros para a busca.
Options é um **dict**, e as sus possiveis **keys** para os filtros são:

| keys                         | type     | default                 |
|------------------------------|----------|-------------------------|
| Linha                        | str      | 'Município'             |
| Coluna                       | str      | '--Não-Ativa--'         |
| Incremento                   | str/list | 'Óbitos_p/Residênc'     |
| Arquivos                     | str/list | 'obtsp16.dbf'           |
| SMunicípio                   | str/list | 'TODAS_AS_CATEGORIAS__' |
| SRegião_de_Saúde_(CIR)       | str/list | 'TODAS_AS_CATEGORIAS__' |
| SMacrorregião_de_Saúde       | str/list | 'TODAS_AS_CATEGORIAS__' |
| SDivisão_administ_estadual   | str/list | 'TODAS_AS_CATEGORIAS__' |
| SMicrorregião_IBGE           | str/list | 'TODAS_AS_CATEGORIAS__' |
| SRegião_Metropolitana_-_RIDE | str/list | 'TODAS_AS_CATEGORIAS__' |
| SCapítulo_CID-10             | str/list | 'TODAS_AS_CATEGORIAS__' |
| SGrupo_CID-10                | str/list | 'TODAS_AS_CATEGORIAS__' |
| SCategoria_CID-10            | str/list | 'TODAS_AS_CATEGORIAS__' |
| SCausa_-_CID-BR-10           | str/list | 'TODAS_AS_CATEGORIAS__' |
| SCausa_mal_definidas         | str/list | 'TODAS_AS_CATEGORIAS__' |
| SFaixa_Etária                | str/list | 'TODAS_AS_CATEGORIAS__' |
| SFaixa_Etária_OPS            | str/list | 'TODAS_AS_CATEGORIAS__' |
| SFaixa_Etária_det            | str/list | 'TODAS_AS_CATEGORIAS__' |
| SFx.Etária_Menor_1A          | str/list | 'TODAS_AS_CATEGORIAS__' |
| SSexo                        | str/list | 'TODAS_AS_CATEGORIAS__' |
| SCor/raça                    | str/list | 'TODAS_AS_CATEGORIAS__' |
| SEscolaridade                | str/list | 'TODAS_AS_CATEGORIAS__' |
| SEstado_civil                | str/list | 'TODAS_AS_CATEGORIAS__' |
| SLocal_ocorrência            | str/list | 'TODAS_AS_CATEGORIAS__' |

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
- 'Macrorregião_de_Saúde'
- 'Divisão_administ_estadual'
- 'Microrregião_IBGE'
- 'Região_Metropolitana_-_RIDE'
- 'Capítulo_CID-10'
- 'Causa_mal_definidas'
- 'Ano_do_Óbito'
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
- 'Óbitos_p/Residênc'
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





