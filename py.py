def fazer_big_mac(nome):
    print(f"sanduiche bm {nome}")

def fazer_batata(tamanho):
    print(f"batata {tamanho}")

def refrigerante(tipo, tamanho):
    print(f"refrigerante {tipo} {tamanho}")

fazer_big_mac("Carlos")
fazer_batata("grande")
refrigerante("Coca", "media")

def combo_bm(nome,tamanho_batata,tamanho_refri,tipo_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    refrigerante(tamanho_refri, tipo_refri)



#usa o terminal com: python nomedoarquivo.py