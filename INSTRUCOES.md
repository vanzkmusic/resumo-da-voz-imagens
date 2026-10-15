# Resumo da Voz: rotina diária (@voz.brasilsemanal)

Carrossel do Instagram que resume, de segunda a sexta, a edição do dia do programa
**A Voz do Brasil**, com identidade visual fixa. Siga este roteiro na ordem.

## 0. Antes de começar
- Data de hoje em America/Sao_Paulo → `AAAA-MM-DD`. Pasta do dia: `<AAAA-MM-DD>/`.
- Se essa pasta já tiver JPGs e `postado.txt`, o dia já foi postado: **pare**.
- Não houve edição hoje? Pode ser feriado nacional ou o Rádio Gov não ter nada com a data de hoje. Nesse caso **não poste**. Registre `sem-edicao.txt` na pasta e pare.

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
| `01-capa.html` | Sempre o 1º. Data (ex.: `QUI · 15 OUT 2026`) e 4 chips com os temas. O chip do tema principal leva a borda amarela. |
| `02-senado-destaque-numeros.html` | Manchete principal com 2 números grandes. Fundo escuro. |
| `03-senado-linha-do-tempo.html` | "O que muda": antes, depois e prazos. |
| `04-camara-valores.html` | Valores lado a lado (antes, 2027, 2028) mais 2 pontos. |
| `05-executivo-numeros-e-lista.html` | Notícia com 2 números e 3 bullets. |
| `06-executivo-dois-blocos.html` | Dois assuntos relacionados no mesmo card. |
| `07-executivo-cards-com-icone.html` | Dois assuntos curtos com ícone. |
| `08-fechamento.html` | Sempre o último: CTA, "Siga @voz.brasilsemanal" e FONTES com a data. |

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
