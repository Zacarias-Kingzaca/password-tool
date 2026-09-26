import random
import string

def verificar_forca(senha):
    pontos = 0
    feedback = []

    if len(senha) >= 8:
        pontos += 1
    else:
        feedback.append("- Use pelo menos 8 caracteres")

    if any(c.isupper() for c in senha):
        pontos += 1
    else:
        feedback.append("- Adicione letras MAIÚSCULAS")

    if any(c.islower() for c in senha):
        pontos += 1
    else:
        feedback.append("- Adicione letras minúsculas")

    if any(c.isdigit() for c in senha):
        pontos += 1
    else:
        feedback.append("- Adicione NÚMEROS")

    if any(c in string.punctuation for c in senha):
        pontos += 1
    else:
        feedback.append("- Adicione SÍMBOLOS (!@#$%)")

    if pontos <= 2:
        forca = "FRACA ❌"
    elif pontos <= 4:
        forca = "MÉDIA ⚠️"
    else:
        forca = "FORTE ✅"

    return forca, feedback

def gerar_senha_forte(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# --- PROGRAMA PRINCIPAL ---
print("=== PASSWORD SECURITY TOOL ===")
senha_user = input("Digite uma senha para verificar: ")

forca, dicas = verificar_forca(senha_user)
print(f"\nForça da senha: {forca}")

if dicas:
    print("Como melhorar:")
    for dica in dicas:
        print(dica)

print("\n--- Gerador de senha forte ---")
print(f"Sugestão de senha segura: {gerar_senha_forte(12)}")
print(f"Sugestão extra forte: {gerar_senha_forte(16)}")

