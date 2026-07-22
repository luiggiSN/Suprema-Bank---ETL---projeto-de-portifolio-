<div align="center">

[![header](https://capsule-render.vercel.app/api?type=waving&color=1E90FF&height=120&section=header)](https://github.com/luiggiSN)

# 🏦 Suprema Bank — Pipeline ETL

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=22&pause=1000&color=1E90FF&center=true&width=500&lines=Dados+brutos+entram.+Insights+saem.;Do+SQL+ao+CSV%2C+sem+enrolac%CC%A7a%CC%83o.;ETL+de+verdade%2C+na+pra%CC%81tica.)](https://git.io/typing-svg)

</div>

---

## 💡 O que é isso?

Um pipeline ETL construído do zero com dados de um banco fictício — o **Suprema Bank**. A ideia foi simples: pegar uma base relacional bruta, limpar, transformar e extrair insights que fazem sentido de verdade.

Sem dado arrumado pra analisar. Sem tutorial seguido à risca. Só o banco de dados e código.

---

## 📂 Estrutura do projeto

```
📦 suprema-bank-etl
├── 📂 dados/
│   └── base_fonte.sql          # fonte original — banco MySQL
├── 📂 notebooks/
│   └── pipeline_etl.ipynb      # onde a mágica acontece
├── 📂 output/
│   └── relatorio_final.csv     # resultado do pipeline
└── README.md
```

---

## ⚙️ Stack utilizada

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

</div>

---

## 🔄 O pipeline

```
[ MySQL ]  →  [ Python + Pandas ]  →  [ CSV / Relatório ]
    E                  T                        L
Extração          Transformação               Carga
```

**Extração** — dados brutos do Suprema Bank: 500 clientes, 600 contas, 20 agências em 10 cidades.

**Transformação** — limpeza, padronização de tipos, métricas por agência e regional, ranking de saldos.

**Carga** — relatório exportado em CSV, pronto pra consumo.

---

## 📊 Análises geradas

- 📍 Distribuição de clientes por status (Ativo / Inativo / Bloqueado)
- 💰 Saldo médio por tipo de conta e agência
- 🏆 Ranking de agências por volume de contas abertas
- 🔒 Clientes bloqueados por regional
- 📈 Crescimento de contas abertas por ano

---

## ⚡ Por que esse projeto?

Porque aprender engenharia de dados sem colocar a mão na massa é perda de tempo. Esse projeto faz parte da minha jornada pra área — do zero até um pipeline funcional, sem atalho.

Encaro projeto como oficina: desmonta, entende, monta melhor. 🔧

---

<div align="center">

⭐ Se curtiu, deixa uma star. Se quiser trocar ideia sobre dados ou dev, só chamar!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/brunoluiggisn/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/luiggiSN)

[![footer](https://capsule-render.vercel.app/api?type=waving&color=1E90FF&height=80&section=footer)](https://github.com/luiggiSN)

</div>
