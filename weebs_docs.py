"""
Weebs Docs - Gerador de Documentos em PDF
-------------------------------------------
App desktop pra gerar Contrato, Orçamento, Recibo, Proposta Comercial,
Ordem de Serviço e Termo de Confidencialidade em PDF, na hora.

Como rodar:
    pip install fpdf2
    python app.py

Feito por Enzo / WEEBS 💜
"""

import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime
from fpdf import FPDF
import base64
import io

# ------------------------------------------------------------
# ÍCONE DO APP (PNG codificado em base64 pra continuar num arquivo só)
# ------------------------------------------------------------

ICONE_BASE64 = (
    "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"
)


def definir_icone(janela):
    """Aplica o ícone roxo da Weebs na janela (título + barra de tarefas)."""
    try:
        dados_png = base64.b64decode(ICONE_BASE64)
        imagem_icone = tk.PhotoImage(data=dados_png)
        janela.iconphoto(True, imagem_icone)
        janela._icone_ref = imagem_icone  # evita o Python coletar a imagem no lixo
    except Exception:
        pass  # se der ruim (ex: SO sem suporte), o app segue liso sem ícone

# ------------------------------------------------------------
# CONFIGS VISUAIS (tudo global, sem classe, do jeito que o Enzo curte)
# ------------------------------------------------------------

COR_FUNDO = "#15151f"
COR_TOPO = "#1a1a26"
COR_CARD = "#20202e"
COR_CARD_HOVER = "#2b2b40"
COR_INPUT = "#282838"
COR_ACCENT = "#7C5CFF"
COR_ACCENT_HOVER = "#9376ff"
COR_TEXTO = "#f2f2f7"
COR_TEXTO_FRACO = "#8b8ba7"
COR_VOLTAR = "#2a2a3a"
COR_VOLTAR_HOVER = "#38384c"

FONTE_LOGO = ("Segoe UI", 22, "bold")
FONTE_TAGLINE = ("Segoe UI", 10)
FONTE_TITULO_TELA = ("Segoe UI", 16, "bold")
FONTE_CARD_ICONE = ("Segoe UI", 26)
FONTE_CARD_TITULO = ("Segoe UI", 12, "bold")
FONTE_CARD_SUB = ("Segoe UI", 9)
FONTE_LABEL = ("Segoe UI", 10, "bold")
FONTE_INPUT = ("Segoe UI", 10)
FONTE_BOTAO = ("Segoe UI", 11, "bold")

# ------------------------------------------------------------
# CATÁLOGO DE DOCUMENTOS
# Cada campo é (chave, rótulo, multilinha?)
# ------------------------------------------------------------

DOCUMENTOS = {
    "Contrato": {
        "icone": "📑",
        "subtitulo": "Prestação de serviços",
        "titulo_pdf": "CONTRATO DE PRESTAÇÃO DE SERVIÇOS",
        "campos": [
            ("cliente", "Nome do Cliente / Empresa", False),
            ("descricao", "Descrição do Serviço", True),
            ("valor", "Valor (R$)", False),
            ("data", "Data", False),
            ("pagamento", "Forma de Pagamento", False),
            ("prazo", "Prazo de Entrega", False),
        ],
        "obrigatorios": ["cliente", "valor"],
        "assinatura": True,
    },
    "Orçamento": {
        "icone": "💰",
        "subtitulo": "Proposta de valores",
        "titulo_pdf": "ORÇAMENTO",
        "campos": [
            ("cliente", "Nome do Cliente", False),
            ("descricao", "Descrição do Serviço", True),
            ("valor", "Valor (R$)", False),
            ("data", "Data", False),
            ("validade", "Validade da Proposta", False),
        ],
        "obrigatorios": ["cliente", "valor"],
        "assinatura": False,
    },
    "Recibo": {
        "icone": "🧾",
        "subtitulo": "Comprovante de pagamento",
        "titulo_pdf": "RECIBO DE PAGAMENTO",
        "campos": [
            ("cliente", "Nome do Cliente", False),
            ("descricao", "Referente a", True),
            ("valor", "Valor (R$)", False),
            ("data", "Data", False),
            ("pagamento", "Forma de Pagamento", False),
        ],
        "obrigatorios": ["cliente", "valor"],
        "assinatura": True,
    },
    "Proposta Comercial": {
        "icone": "📈",
        "subtitulo": "Apresentação de projeto",
        "titulo_pdf": "PROPOSTA COMERCIAL",
        "campos": [
            ("cliente", "Nome do Cliente", False),
            ("descricao", "Escopo do Projeto", True),
            ("valor", "Investimento (R$)", False),
            ("data", "Data", False),
            ("validade", "Validade da Proposta", False),
            ("pagamento", "Condições de Pagamento", False),
        ],
        "obrigatorios": ["cliente", "valor"],
        "assinatura": False,
    },
    "Ordem de Serviço": {
        "icone": "🛠️",
        "subtitulo": "Registro de execução",
        "titulo_pdf": "ORDEM DE SERVIÇO",
        "campos": [
            ("cliente", "Cliente", False),
            ("descricao", "Serviço a Realizar", True),
            ("responsavel", "Responsável Técnico", False),
            ("data", "Data", False),
            ("prioridade", "Prioridade (Baixa / Média / Alta)", False),
        ],
        "obrigatorios": ["cliente", "descricao"],
        "assinatura": True,
    },
    "Termo de Confidencialidade": {
        "icone": "🔒",
        "subtitulo": "Acordo de sigilo (NDA)",
        "titulo_pdf": "TERMO DE CONFIDENCIALIDADE",
        "campos": [
            ("parte_a", "Parte Contratante", False),
            ("parte_b", "Parte Contratada", False),
            ("objeto", "Objeto do Sigilo", True),
            ("data", "Data", False),
            ("vigencia", "Prazo de Vigência", False),
        ],
        "obrigatorios": ["parte_a", "parte_b"],
        "assinatura": True,
    },
}

# Variáveis globais de estado
root = None
entries = {}
tipo_atual = None


# ------------------------------------------------------------
# HELPERS DE UI
# ------------------------------------------------------------

def limpar_tela():
    for widget in root.winfo_children():
        widget.destroy()


def aplicar_bg_recursivo(widget, cor):
    try:
        widget.config(bg=cor)
    except tk.TclError:
        pass
    for filho in widget.winfo_children():
        aplicar_bg_recursivo(filho, cor)


def bind_recursivo(widget, evento, comando):
    widget.bind(evento, comando)
    for filho in widget.winfo_children():
        bind_recursivo(filho, evento, comando)


def tornar_clicavel(widget, comando):
    bind_recursivo(widget, "<Button-1>", lambda e: comando())


def tornar_hover(widget, cor_normal, cor_hover):
    bind_recursivo(widget, "<Enter>", lambda e: aplicar_bg_recursivo(widget, cor_hover))
    bind_recursivo(widget, "<Leave>", lambda e: aplicar_bg_recursivo(widget, cor_normal))


def criar_botao(pai, texto, comando, cor=COR_ACCENT, cor_hover=COR_ACCENT_HOVER, largura=20):
    btn = tk.Button(
        pai, text=texto, command=comando, font=FONTE_BOTAO,
        bg=cor, fg="white", activebackground=cor_hover, activeforeground="white",
        bd=0, relief="flat", width=largura, height=2, cursor="hand2",
    )
    btn.bind("<Enter>", lambda e: btn.config(bg=cor_hover))
    btn.bind("<Leave>", lambda e: btn.config(bg=cor))
    return btn


def cabecalho(pai, titulo_tela=None):
    topo = tk.Frame(pai, bg=COR_TOPO)
    topo.pack(fill="x")

    faixa = tk.Frame(topo, bg=COR_ACCENT, height=3)
    faixa.pack(fill="x", side="bottom")

    conteudo = tk.Frame(topo, bg=COR_TOPO)
    conteudo.pack(fill="x", padx=25, pady=(18, 14))

    logo = tk.Frame(conteudo, bg=COR_TOPO)
    logo.pack(side="left")
    tk.Label(logo, text="Weebs", font=FONTE_LOGO, bg=COR_TOPO, fg=COR_TEXTO).pack(side="left")
    tk.Label(logo, text="Docs", font=FONTE_LOGO, bg=COR_TOPO, fg=COR_ACCENT).pack(side="left")

    if titulo_tela:
        tk.Label(
            conteudo, text=titulo_tela, font=FONTE_TAGLINE, bg=COR_TOPO, fg=COR_TEXTO_FRACO
        ).pack(side="right", pady=(10, 0))


# ------------------------------------------------------------
# TELAS
# ------------------------------------------------------------

def tela_principal():
    limpar_tela()
    global entries, tipo_atual
    entries = {}
    tipo_atual = None

    cabecalho(root)

    corpo = tk.Frame(root, bg=COR_FUNDO)
    corpo.pack(expand=True, fill="both", padx=25, pady=20)

    tk.Label(
        corpo, text="Qual documento você quer gerar hoje?",
        font=FONTE_TITULO_TELA, bg=COR_FUNDO, fg=COR_TEXTO
    ).pack(anchor="w", pady=(0, 4))
    tk.Label(
        corpo, text="Escolhe um modelo e preenche os dados. Simples assim.",
        font=FONTE_TAGLINE, bg=COR_FUNDO, fg=COR_TEXTO_FRACO
    ).pack(anchor="w", pady=(0, 18))

    grid = tk.Frame(corpo, bg=COR_FUNDO)
    grid.pack(fill="both", expand=True)
    grid.columnconfigure(0, weight=1)
    grid.columnconfigure(1, weight=1)

    tipos = list(DOCUMENTOS.keys())
    for indice, tipo in enumerate(tipos):
        linha, coluna = divmod(indice, 2)
        criar_card_documento(grid, tipo).grid(
            row=linha, column=coluna, padx=8, pady=8, sticky="nsew"
        )

    tk.Label(
        corpo, text="feito com 💜 por WEEBS", font=("Segoe UI", 8),
        bg=COR_FUNDO, fg=COR_TEXTO_FRACO
    ).pack(side="bottom", pady=(18, 0))


def criar_card_documento(pai, tipo):
    info = DOCUMENTOS[tipo]

    card = tk.Frame(pai, bg=COR_CARD, cursor="hand2", padx=16, pady=16)

    tk.Label(card, text=info["icone"], font=FONTE_CARD_ICONE, bg=COR_CARD, fg=COR_ACCENT).pack(anchor="w")
    tk.Label(card, text=tipo, font=FONTE_CARD_TITULO, bg=COR_CARD, fg=COR_TEXTO, anchor="w",
             wraplength=220, justify="left").pack(anchor="w", pady=(8, 2))
    tk.Label(card, text=info["subtitulo"], font=FONTE_CARD_SUB, bg=COR_CARD, fg=COR_TEXTO_FRACO,
             anchor="w", wraplength=220, justify="left").pack(anchor="w")

    comando = lambda t=tipo: tela_formulario(t)
    tornar_clicavel(card, comando)
    tornar_hover(card, COR_CARD, COR_CARD_HOVER)

    return card


def tela_formulario(tipo):
    limpar_tela()
    global entries, tipo_atual
    entries = {}
    tipo_atual = tipo
    info = DOCUMENTOS[tipo]

    cabecalho(root, titulo_tela=f"Novo documento · {tipo}")

    corpo = tk.Frame(root, bg=COR_FUNDO)
    corpo.pack(expand=True, fill="both", padx=25, pady=20)

    tk.Label(
        corpo, text=f"{info['icone']}  {tipo}", font=FONTE_TITULO_TELA,
        bg=COR_FUNDO, fg=COR_TEXTO
    ).pack(anchor="w", pady=(0, 2))
    tk.Label(
        corpo, text="Preenche os campos abaixo (os com * são obrigatórios):",
        font=FONTE_TAGLINE, bg=COR_FUNDO, fg=COR_TEXTO_FRACO
    ).pack(anchor="w", pady=(0, 16))

    card = tk.Frame(corpo, bg=COR_CARD, padx=22, pady=20)
    card.pack(fill="both", expand=True)

    for chave, rotulo, multilinha in info["campos"]:
        linha = tk.Frame(card, bg=COR_CARD)
        linha.pack(fill="x", pady=7)

        marcador = " *" if chave in info["obrigatorios"] else ""
        tk.Label(
            linha, text=rotulo + marcador, font=FONTE_LABEL,
            bg=COR_CARD, fg=COR_TEXTO, anchor="w"
        ).pack(anchor="w")

        if multilinha:
            widget = tk.Text(
                linha, font=FONTE_INPUT, bg=COR_INPUT, fg=COR_TEXTO,
                insertbackground=COR_TEXTO, relief="flat", height=3, wrap="word",
                highlightthickness=1, highlightbackground=COR_INPUT, highlightcolor=COR_ACCENT,
            )
            widget.pack(fill="x", pady=(4, 0), ipady=4)
        else:
            widget = tk.Entry(
                linha, font=FONTE_INPUT, bg=COR_INPUT, fg=COR_TEXTO,
                insertbackground=COR_TEXTO, relief="flat",
                highlightthickness=1, highlightbackground=COR_INPUT, highlightcolor=COR_ACCENT,
            )
            widget.pack(fill="x", pady=(4, 0), ipady=6)
            if chave == "data":
                widget.insert(0, datetime.now().strftime("%d/%m/%Y"))

        entries[chave] = widget

    botoes = tk.Frame(corpo, bg=COR_FUNDO)
    botoes.pack(fill="x", pady=(18, 0))

    criar_botao(botoes, "⬅ Voltar", tela_principal, cor=COR_VOLTAR, cor_hover=COR_VOLTAR_HOVER, largura=10).pack(
        side="left"
    )
    criar_botao(botoes, "Gerar PDF ✅", lambda: processar_geracao(tipo), largura=16).pack(
        side="right"
    )


# ------------------------------------------------------------
# LÓGICA / GERAÇÃO DO PDF
# ------------------------------------------------------------

def obter_valor(widget):
    if isinstance(widget, tk.Text):
        return widget.get("1.0", "end").strip()
    return widget.get().strip()


def processar_geracao(tipo):
    info = DOCUMENTOS[tipo]
    dados = {chave: obter_valor(widget) for chave, widget in entries.items()}

    faltando = [chave for chave in info["obrigatorios"] if not dados.get(chave)]
    if faltando:
        messagebox.showwarning(
            "Opa, falta coisa!",
            "Preenche pelo menos os campos marcados com * antes de gerar, parça 🙏"
        )
        return

    referencia = dados.get("cliente") or dados.get("parte_a") or "documento"
    nome_sugerido = f"{tipo}_{referencia}.pdf".replace(" ", "_")
    caminho = filedialog.asksaveasfilename(
        title="Salvar documento como...",
        defaultextension=".pdf",
        filetypes=[("Arquivo PDF", "*.pdf")],
        initialfile=nome_sugerido,
    )
    if not caminho:
        return

    try:
        gerar_pdf(tipo, dados, caminho)
        messagebox.showinfo("Show de bola! 🎉", f"PDF gerado com sucesso em:\n{caminho}")
        tela_principal()
    except Exception as erro:
        messagebox.showerror("Deu ruim 😬", f"Não rolou gerar o PDF:\n{erro}")


def gerar_pdf(tipo, dados, caminho):
    info = DOCUMENTOS[tipo]

    pdf = FPDF()
    pdf.add_page()

    # Cabeçalho / título
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(21, 21, 31)
    pdf.cell(0, 12, info["titulo_pdf"], ln=True, align="C")

    pdf.set_draw_color(124, 92, 255)
    pdf.set_line_width(0.8)
    pdf.line(10, pdf.get_y() + 2, 200, pdf.get_y() + 2)
    pdf.ln(12)

    # Corpo com os dados preenchidos, na ordem definida no catálogo
    pdf.set_text_color(20, 20, 20)
    for chave, rotulo, _multilinha in info["campos"]:
        valor = dados.get(chave)
        if not valor:
            continue
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(60, 10, f"{rotulo}:", ln=False)
        pdf.set_font("Helvetica", "", 12)
        pdf.multi_cell(0, 10, valor)
        pdf.ln(1)

    # Espaço pra assinatura, quando o tipo de documento pede
    if info["assinatura"]:
        pdf.ln(18)
        pdf.set_font("Helvetica", "", 11)
        pdf.cell(90, 8, "_" * 30, ln=False)
        pdf.cell(0, 8, "_" * 30, ln=True)
        nome_esquerda = dados.get("cliente") or dados.get("parte_a") or "Contratante"
        pdf.cell(90, 6, nome_esquerda[:35], ln=False, align="C")
        pdf.cell(0, 6, "WEEBS", ln=True, align="C")

    # Rodapé
    pdf.set_y(-25)
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(120, 120, 120)
    agora = datetime.now().strftime("%d/%m/%Y às %H:%M")
    pdf.cell(0, 10, f"Documento gerado em {agora} - Weebs Docs", align="C")

    pdf.output(caminho)


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Weebs Docs")
    root.geometry("680x760")
    root.configure(bg=COR_FUNDO)
    root.minsize(560, 640)
    definir_icone(root)

    tela_principal()
    root.mainloop()