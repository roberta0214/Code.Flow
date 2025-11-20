from flask import Flask, render_template_string

app = Flask(__name__)

html_template = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Code.Flow - Engenharia de Software Avançada</title>
    <style>
        body {
            background-color: #121212; /* Preto escuro */
            color: #A9A9A9; /* Cinza claro */
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #556B2F; /* Verde musgo */
            padding: 20px;
            text-align: center;
            font-size: 2em;
            color: white;
            font-weight: bold;
        }
        nav {
            background-color: #333333; /* Cinza escuro */
            padding: 10px;
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
        }
        nav a {
            color: #A9A9A9; /* Cinza claro */
            text-decoration: none;
            font-weight: bold;
            padding: 5px 10px;
            border-radius: 4px;
        }
        nav a:hover {
            color: #FFFFFF;
            background-color: #556B2F;
        }
        section {
            padding: 20px;
            max-width: 900px;
            margin: 0 auto;
        }
        h2 {
            color: #8F9779; /* Verde musgo claro */
            border-bottom: 2px solid #556B2F;
            padding-bottom: 5px;
        }
        article {
            margin-bottom: 40px;
            background-color: #1E1E1E;
            padding: 20px;
            border-radius: 6px;
            box-shadow: 0 0 5px #556B2F;
        }
        .content-section {
            margin-top: 15px;
            padding-left: 15px;
            border-left: 3px solid #8F9779;
        }
        .content-section h3 {
            color: #A2B28F;
        }
        .content-section p {
            margin-top: 5px;
            line-height: 1.5;
        }
    </style>
</head>
<body>
    <header>Code.Flow - Engenharia de Software Avançada</header>
    <nav>
        <a href="#engenharia">Engenharia de Software</a>
        <a href="#computacao">Ciência da Computação</a>
        <a href="#analise">Análise e Desenvolvimento</a>
        <a href="#engenharia_computacao">Engenharia da Computação</a>
        <a href="#manutencao">Manutenção</a>
        <a href="#pericia">Perícia Computacional</a>
    </nav>
    <section>
        <article id="engenharia">
            <h2>Engenharia de Software</h2>
            <div class="content-section">
                <h3>Conteúdo Básico</h3>
                <p>A engenharia de software é a área da T.I que se dedica ao desenvolvimento de sistemas de software complexos, usando metodologias, processos e ferramentas para garantir qualidade, eficiência e manutenção dos programas.</p>
                <p>Básicos incluem entendimento do ciclo de vida do software, modelagem de requisitos, design, codificação, testes e manutenção.</p>
            </div>
            <div class="content-section">
                <h3>Conteúdo Avançado</h3>
                <p>Topics avançados envolvem arquiteturas de software (microsserviços, SOA), metodologias ágeis aplicadas extensivamente, DevOps e CI/CD, testes automatizados, integração contínua, análise de performance e escalabilidade, além de padrões de design avançados.</p>
            </div>
        </article>

        <article id="computacao">
            <h2>Ciência da Computação</h2>
            <div class="content-section">
                <h3>Conteúdo Básico</h3>
                <p>Ciência da computação estuda os fundamentos teóricos da informação e computação, como algoritmos, estruturas de dados, lógica computacional e arquitetura de computadores.</p>
                <p>É a base para todas as áreas de T.I, fornecendo o conhecimento para desenvolver novas tecnologias.</p>
            </div>
            <div class="content-section">
                <h3>Conteúdo Avançado</h3>
                <p>Conteúdos avançados incluem técnicas complexas em algoritmos paralelos e distribuídos, teoria da computação e autômatos, aprendizado de máquina, inteligência artificial, complexidade computacional, criptografia avançada e sistemas distribuídos.</p>
            </div>
        </article>

        <article id="analise">
            <h2>Análise e Desenvolvimento de Sistemas</h2>
            <div class="content-section">
                <h3>Conteúdo Básico</h3>
                <p>Focado em entender problemas do negócio para projetar e desenvolver sistemas que atendam suas necessidades.</p>
                <p>Inclui levantamento de requisitos, modelagem, programação e implantação de soluções.</p>
            </div>
            <div class="content-section">
                <h3>Conteúdo Avançado</h3>
                <p>Avançado envolve modelagem UML complexa, análise orientada a objetos, arquitetura empresarial, integração de sistemas, APIs RESTful, segurança de sistemas e metodologias ágeis avançadas como SAFe e LeSS.</p>
            </div>
        </article>

        <article id="engenharia_computacao">
            <h2>Engenharia da Computação</h2>
            <div class="content-section">
                <h3>Conteúdo Básico</h3>
                <p>Área que integra conhecimentos de engenharia elétrica e ciência da computação para projetar hardware e software.</p>
                <p>Envolve desenvolvimento de circuitos, microcontroladores, sistemas embarcados e programação de baixo nível.</p>
            </div>
            <div class="content-section">
                <h3>Conteúdo Avançado</h3>
                <p>Inclui design de sistemas embarcados complexos, desenvolvimento FPGA, síntese lógica, sistemas ciber-físicos, arquiteturas paralelas, sistemas em tempo real e integração de hardware/software em larga escala.</p>
            </div>
        </article>

        <article id="manutencao">
            <h2>Manutenção de Computadores e Celulares</h2>
            <div class="content-section">
                <h3>Conteúdo Básico</h3>
                <p>Trabalha com diagnóstico, reparo e prevenção de falhas em dispositivos eletrônicos e sistemas operacionais.</p>
                <p>Inclui troca de peças, formatação, remoção de vírus e otimização de performance.</p>
            </div>
            <div class="content-section">
                <h3>Conteúdo Avançado</h3>
                <p>Aborda técnicas avançadas de diagnósticos eletrônicos, soldagem SMD, recuperação de dados, análise e recuperação de sistemas operacionais corrompidos, forense digital aplicada a dispositivos móveis e automação de manutenção preventiva.</p>
            </div>
        </article>

        <article id="pericia">
            <h2>Perícia Computacional</h2>
            <div class="content-section">
                <h3>Conteúdo Básico</h3>
                <p>Especialidade que investiga crimes digitais por meio de análise de sistemas, arquivos e redes para coletar evidências.</p>
                <p>É utilizada em investigações judiciais para provar fraudes, invasões e outros delitos cibernéticos.</p>
            </div>
            <div class="content-section">
                <h3>Conteúdo Avançado</h3>
                <p>Inclui análise profunda de logs, técnicas de recuperação e análise de mídias digitais, criptografia aplicada à perícia, análise de malware, investigação de ataques cibernéticos sofisticados, e uso de ferramentas forenses especializadas.</p>
            </div>
        </article>

    </section>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)