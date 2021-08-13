'''
01 – Escreva um programa em Python que faça o seguinte:
- Pergunte ao jogador/jogadora qual o encantamento para abrir um portal.
- Teste se o encantamento informado é “DESTRAVIUM LAPARADA”
- Se for esse o encantamento informado, mostre uma mensagem dizendo que o portal foi aberto.
- Ao final, sempre mostre uma mensagem se despedindo do jogador/jogadora.
'''

encantamento_portal_pergunta = input (str("Qual é o encantamento para abrir o portal?\n"))

if encantamento_portal_pergunta == "Destravium Laparada" or "DESTRAVIUM LAPARADA" or "destravium laparada":
    print(f"O portal foi aberto após dizer!{encantamento_portal_pergunta}")

