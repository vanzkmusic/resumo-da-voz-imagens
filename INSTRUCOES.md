# Resumo da Voz: rotina diária (@voz.brasilsemanal)

Carrossel do Instagram que resume, de segunda a sexta, a edição do dia do programa
**A Voz do Brasil**, com identidade visual fixa. Siga este roteiro na ordem.

## 0. Antes de começar
- **Data de hoje: rode `TZ=America/Sao_Paulo date +%F` e use EXATAMENTE essa saída.** Nunca use a data UTC do sistema: a tarefa roda à noite em Brasília, quando em UTC já é o dia seguinte. Confira também o dia da semana com `TZ=America/Sao_Paulo date +%A` e a hora com `TZ=America/Sao_Paulo date +%H:%M`. Pasta do dia: `<AAAA-MM-DD>/`.
- Faça `git pull` antes de tudo. Se a pasta do dia já tiver `postado.txt` ou `sem-edicao.txt`, o dia já foi resolvido: **pare** sem fazer nada.
- Não houve edição hoje? Pode ser feriado nacional ou o Rádio Gov não ter nada com a data de hoje. Nesse caso **não poste**. Registre `sem-edicao.txt` na pasta e pare.

## 0.1 Esperar votação? (a tarefa roda às 20h27, 21h27 e 22h27)
O programa vai ao ar das 19h às 20h. O normal é postar já na primeira rodada (20h27). A exceção é quando há votação importante acontecendo à noite.
1. Confira se há **sessão deliberativa do Plenário em andamento agora** no Senado ou na Câmara, com votação de matéria relevante (PEC, MP, projeto de grande impacto) ainda **não concluída**:
   - Senado: agenda do Plenário de hoje em https://www25.senado.leg.br/web/atividade/agenda e notícias da Agência Senado de hoje.
   - Câmara: https://www.camara.leg.br/agenda (Plenário) e notícias da Agência Câmara de hoje.
2. **Se houver votação relevante em andamento e a hora for antes de 22h27:** não poste. Grave `<AAAA-MM-DD>/aguardando-votacao.txt` com o horário e o que está em votação, faça commit e push e **pare**. A próxima rodada confere de novo.
3. **Se não houver, ou se já for a rodada de 22h27:** siga o roteiro normal e poste. Se alguma votação terminou depois das 20h, inclua o resultado (com fonte oficial) e apague `aguardando-votacao.txt`. Na rodada de 22h27, se a votação ainda não acabou, poste com o que já foi decidido e diga na legenda que a votação continua.
4. Em caso de dúvida (agenda fora do ar, sem informação clara), **não espere**: poste.

## 1. Pesquisa (só fontes oficiais como base)
1. Rádio Gov, bloco do Executivo: https://radiogov.ebc.com.br/programas/materias-da-voz. Abra cada matéria com a data de hoje.
2. Rádio Câmara: https://www.camara.leg.br/radio/164-a-voz-do-brasil/. Se o site bloquear, busque por "Câmara aprova" com a data de hoje e use a Agência Câmara ou a Agência Brasil.
3. Senado: busque "Senado aprova" com a data de hoje e use a Agência Senado (www12.senado.leg.br/noticias).
4. Para cada tema, aprofunde na página oficial (gov.br, Agência Brasil, Agência Senado/Câmara) e anote números exatos, nomes de projetos (PL/PEC/PLP), placares e próximos passos.
5. **Regra de ouro:** só entra no card o que estiver escrito numa fonte. Nada de número estimado ou inventado. Fato de fonte não oficial (imprensa comum) não entra no card. No máximo vai à legenda, e só se for relevante.
6. Escolha de 4 a 6 temas, priorizando o que mais afeta a vida das pessoas (trabalho, dinheiro, saúde, direitos).

## 2. Cards (pasta `<AAAA-MM-DD>/cards/`)
Crie de 5 a 9 arquivos HTML numerados (`01-capa.html` … `NN-fechamento.html`). A ordem alfabética é a ordem do carrossel. **Copie a estrutura de `modelo/exemplo/`** e troque só o conteúdo:

| Modelo | Use para |
|---|---|
| `01-capa.html` | Sempre o 1º. **Use o modelo de capa do dia da semana** (seção 2.1 abaixo), não o de `modelo/exemplo/`. |
| `02-senado-destaque-numeros.html` | Manchete principal com 2 números grandes. Fundo escuro. |
| `03-senado-linha-do-tempo.html` | "O que muda": antes, depois e prazos. |
| `04-camara-valores.html` | Valores lado a lado (antes, 2027, 2028) mais 2 pontos. |
| `05-executivo-numeros-e-lista.html` | Notícia com 2 números e 3 bullets. |
| `06-executivo-dois-blocos.html` | Dois assuntos relacionados no mesmo card. |
| `07-executivo-cards-com-icone.html` | Dois assuntos curtos com ícone. |
| `08-fechamento.html` | Sempre o último: CTA, "Siga @voz.brasilsemanal" e FONTES com a data. |

### 2.1 Capa: um modelo por dia da semana (aprovado pelo Vaner em 20/10/2026)
Pegue o dia com `TZ=America/Sao_Paulo date +%A`, copie `modelo/capas/<dia>.html` para `cards/01-capa.html` e troque só o conteúdo. Cada dia tem a sua cara, e é isso que deixa a grade do perfil variada. Não troque o modelo entre os dias.

| Dia | Arquivo | Fundo | Conteúdo |
|---|---|---|---|
| Segunda | `modelo/capas/segunda.html` | azul | "O que a Voz do Brasil falou hoje", data `SEG · DD OUT AAAA` e 4 chips de temas (borda amarela no principal). |
| Terça | `modelo/capas/terca.html` | areia | "O NÚMERO DO DIA": um número curto e marcante da notícia principal (ex.: `R$ 691`, `75 a 1`, `42h`), uma frase em h1 explicando e uma linha de contexto. Embaixo, 3 pílulas `+ tema`. O número deve caber numa linha (no máximo ~7 caracteres; se for maior, reduza a fonte). |
| Quarta | `modelo/capas/quarta.html` | amarelo | "A MANCHETE DE HOJE": a notícia principal como manchete (até ~45 caracteres), a onda de áudio e a faixa `+ N notícias no carrossel` com o número real de cards de notícia. |
| Quinta | `modelo/capas/quinta.html` | azul com círculos | "QUINTA" e a data dentro dos círculos, "NO AR" no topo, a manchete principal embaixo (até ~60 caracteres, com o dado-chave em amarelo) e a linha "E mais: …". |
| Sexta | `modelo/capas/sexta.html` | metade azul, metade areia | Uma pergunta direta ao público sobre o tema principal (até ~55 caracteres, palavra-chave em amarelo) e "A VOZ RESPONDE HOJE" com 3 itens numerados `01 02 03`. |

Data no selo: `TER · 20 OUT`, `QUA · 21 OUT`, `SEX · 23 OUT` (terça, quarta e sexta). Na quinta, `22 OUT 2026` vai abaixo de "QUINTA". Use `&nbsp;` entre "R$" e o número para não quebrar a linha. Confira na prévia se o texto não passa dos círculos (quinta) nem fica cortado.

Identidade (não mude):
- Cores: azul-marinho `#0F1E33`, areia `#F3EFE6`, amarelo `#F2C230`. Texto secundário `#B8C2D1` no escuro e `#2D3748` ou `#4A5568` no claro.
- Fontes: `Archivo` (títulos, 800/900) e `IBM Plex Sans` (texto). O `render.py` já carrega as duas.
- Topo de todo card: ícone de ondas e "RESUMO DA VOZ". **Sem contador de páginas** (nada de "01 / 08").
- Etiqueta do Poder: `PODER EXECUTIVO`, `CÂMARA DOS DEPUTADOS` ou `SENADO FEDERAL`. Alterne fundo escuro e claro entre os cards.
- Rodapé: `Fonte: <órgão> · DD.MM.AAAA` e a seta. O @ aparece na capa e no fechamento: **@voz.brasilsemanal**.
- Card de 1080×1350. Título com 80 a 112 px. Texto nunca abaixo de 24 px. Nada de emoji dentro dos cards.

## 3. Renderizar e conferir
```
python3 modelo/render.py <AAAA-MM-DD>
```
Abra `<AAAA-MM-DD>/_previa.png` e **olhe**. Se houver texto cortado, número quebrando de linha, sobreposição ou conteúdo saindo do card, corrija o HTML (diminua a fonte ou o texto) e renderize de novo. Não poste com defeito visual.

## 4. Publicar as imagens
Faça commit da pasta do dia (cards e JPGs) e push em `main`. Confira que
`https://raw.githubusercontent.com/vanzkmusic/resumo-da-voz-imagens/main/<AAAA-MM-DD>/01-capa.jpg` responde 200.

## 5. Legenda (até 2.200 caracteres)
```
<gancho de 1 linha sobre o tema principal, terminando com 👇>

<1 frase de contexto> Arrasta pro lado:

🗳️/💼/🩺/🎮/... TEMA: 1 a 2 frases com o número principal.
(uma linha por tema, na ordem dos cards)

💬 <pergunta concreta para o público responder nos comentários>

📌 Salve para consultar depois e mande para quem precisa saber.
🔔 Siga @voz.brasilsemanal para o resumo da Voz de segunda a sexta.

Fontes: <órgãos>. Resumo independente, sem vínculo com o governo.

#VozDoBrasil #ResumoDaVoz #NoticiasDoBrasil + 5 a 7 hashtags dos temas
```
Salve a legenda em `<AAAA-MM-DD>/legenda.txt`.

## 6. Postar
Ferramenta Windsor.ai `execute_action`: connector `instagram`, action `create_carousel_post`,
account **17841423025294375** (= @voz.brasilsemanal; **nunca** a 17841460178890973, que é @moctechinfo).
`image_urls` = URLs raw dos JPGs na ordem. `caption` = legenda.
Depois grave o media id em `<AAAA-MM-DD>/postado.txt`, faça commit e push.

## 7. Se algo falhar
Não tente caminhos alternativos para postar. Deixe os JPGs e a legenda no repositório e avise o Vaner do que falhou e de onde está o material, para ele postar à mão.
