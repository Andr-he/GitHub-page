/*
PROJETO PRONTO PARA DEPLOY - GITHUB PAGES

1. Criar projeto:
npm create vite@latest portfolio

2. Entrar na pasta:
cd portfolio

3. Instalar dependências:
npm install

4. Instalar Tailwind:
npm install tailwindcss @tailwindcss/vite

5. Instalar deploy GitHub Pages:
npm install gh-pages --save-dev

6. package.json:

Adicione:

"homepage": "https://SEU-USUARIO.github.io/portfolio"

Scripts:

"scripts": {
  "dev": "vite",
  "build": "vite build",
  "preview": "vite preview",
  "predeploy": "npm run build",
  "deploy": "gh-pages -d dist"
}

7. vite.config.js:

import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  base: '/portfolio/'
})

8. src/index.css:

@import "tailwindcss";

9. Deploy:

npm run deploy

*/

export default function PortfolioTemplate() {
  const projetos = [
    {
      titulo: "Sistema de Academia",
      descricao: "Projeto de banco de dados com modelagem DER, requisitos funcionais e integração SQL.",
      tecnologias: ["MySQL", "SQL", "Modelagem de Dados"]
    },
    {
      titulo: "Sistema de Loja",
      descricao: "Mini ERP desenvolvido para estudo de análise e desenvolvimento de sistemas.",
      tecnologias: ["Python", "Tkinter", "SQLite"]
    },
    {
      titulo: "Dashboard de Estudos",
      descricao: "Painel para organização de tarefas e progresso acadêmico.",
      tecnologias: ["React", "JavaScript", "CSS"]
    }
  ];

  return (
    <div className="min-h-screen bg-zinc-950 text-zinc-100 font-sans">
      {/* Header */}
      <header className="border-b border-zinc-800 backdrop-blur-sm sticky top-0 bg-zinc-950/80 z-50">
        <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
          <h1 className="text-2xl font-bold tracking-wide">André.dev</h1>

          <nav className="hidden md:flex gap-6 text-sm text-zinc-300">
            <a href="#sobre" className="hover:text-white transition">Sobre</a>
            <a href="#projetos" className="hover:text-white transition">Projetos</a>
            <a href="#habilidades" className="hover:text-white transition">Habilidades</a>
            <a href="#contato" className="hover:text-white transition">Contato</a>
          </nav>
        </div>
      </header>

      {/* Hero */}
      <section className="max-w-6xl mx-auto px-6 py-24 grid md:grid-cols-2 gap-12 items-center">
        <div>
          <p className="text-zinc-400 uppercase tracking-[0.2em] text-sm mb-4">
            Portfólio Acadêmico
          </p>

          <h2 className="text-5xl md:text-6xl font-extrabold leading-tight mb-6">
            Desenvolvedor em formação focado em projetos reais.
          </h2>

          <p className="text-zinc-400 text-lg leading-relaxed mb-8">
            Estudante de Análise e Desenvolvimento de Sistemas, construindo projetos práticos com foco em banco de dados, desenvolvimento web e lógica de programação.
          </p>

          <div className="flex gap-4 flex-wrap">
            <a
              href="#projetos"
              className="bg-white text-black px-6 py-3 rounded-2xl font-semibold hover:scale-105 transition"
            >
              Ver Projetos
            </a>

            <a
              href="#contato"
              className="border border-zinc-700 px-6 py-3 rounded-2xl hover:bg-zinc-900 transition"
            >
              Contato
            </a>
          </div>
        </div>

        <div className="flex justify-center">
          <div className="w-72 h-72 rounded-3xl bg-gradient-to-br from-zinc-800 to-zinc-900 border border-zinc-700 shadow-2xl flex items-center justify-center text-7xl font-bold">
            A
          </div>
        </div>
      </section>

      {/* Sobre */}
      <section id="sobre" className="max-w-6xl mx-auto px-6 py-20">
        <div className="bg-zinc-900 border border-zinc-800 rounded-3xl p-8 md:p-12 shadow-xl">
          <h3 className="text-3xl font-bold mb-6">Sobre Mim</h3>

          <p className="text-zinc-400 leading-relaxed text-lg">
            Atualmente cursando o primeiro semestre de Análise e Desenvolvimento de Sistemas. Tenho interesse em desenvolvimento backend, modelagem de banco de dados e criação de sistemas voltados para resolução de problemas reais.
          </p>
        </div>
      </section>

      {/* Projetos */}
      <section id="projetos" className="max-w-6xl mx-auto px-6 py-20">
        <div className="flex items-center justify-between mb-10">
          <h3 className="text-3xl font-bold">Projetos</h3>
          <span className="text-zinc-500 text-sm">Projetos acadêmicos e pessoais</span>
        </div>

        <div className="grid md:grid-cols-3 gap-6">
          {projetos.map((projeto, index) => (
            <div
              key={index}
              className="bg-zinc-900 border border-zinc-800 rounded-3xl p-6 hover:-translate-y-2 transition duration-300 shadow-lg"
            >
              <div className="w-full h-40 bg-zinc-800 rounded-2xl mb-6" />

              <h4 className="text-xl font-semibold mb-3">{projeto.titulo}</h4>

              <p className="text-zinc-400 mb-5 leading-relaxed">
                {projeto.descricao}
              </p>

              <div className="flex gap-2 flex-wrap">
                {projeto.tecnologias.map((tech, i) => (
                  <span
                    key={i}
                    className="px-3 py-1 text-sm rounded-full bg-zinc-800 border border-zinc-700"
                  >
                    {tech}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Habilidades */}
      <section id="habilidades" className="max-w-6xl mx-auto px-6 py-20">
        <h3 className="text-3xl font-bold mb-10">Habilidades</h3>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {[
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Python",
            "SQL",
            "GitHub",
            "Modelagem de Dados"
          ].map((skill, index) => (
            <div
              key={index}
              className="bg-zinc-900 border border-zinc-800 rounded-2xl p-5 text-center font-medium hover:bg-zinc-800 transition"
            >
              {skill}
            </div>
          ))}
        </div>
      </section>

      {/* Contato */}
      <section id="contato" className="max-w-6xl mx-auto px-6 py-20">
        <div className="bg-gradient-to-br from-zinc-900 to-zinc-950 border border-zinc-800 rounded-3xl p-10 text-center">
          <h3 className="text-3xl font-bold mb-4">Contato</h3>

          <p className="text-zinc-400 mb-8">
            Você pode adicionar aqui seus links profissionais.
          </p>

          <div className="flex justify-center gap-4 flex-wrap">
            <a
              href="#"
              className="px-6 py-3 rounded-2xl bg-white text-black font-semibold hover:scale-105 transition"
            >
              GitHub
            </a>

            <a
              href="#"
              className="px-6 py-3 rounded-2xl border border-zinc-700 hover:bg-zinc-900 transition"
            >
              LinkedIn
            </a>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-zinc-800 py-8 mt-10">
        <div className="max-w-6xl mx-auto px-6 text-zinc-500 text-sm flex flex-col md:flex-row justify-between gap-4">
          <span>© 2026 André.dev</span>
          <span>Desenvolvido com React + Tailwind</span>
        </div>
      </footer>
    </div>
  );
}
