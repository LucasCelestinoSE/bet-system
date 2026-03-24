🟢 Estudo 1: self.__init__ e o Ciclo de Vida

    O que focar: Entender a diferença entre o __new__ (quem cria o objeto) e o __init__ (quem configura o objeto).

    Desafio: Descobrir por que colocar objetos pesados (como conexões de banco de dados ou clientes de API) no __init__ pode ser um gargalo se você instanciar a classe milhares de vezes por segundo.

🟡 Estudo 2: Garbage Collector (GC) no Python

    O que focar: Como o Python usa Contagem de Referências. O objeto só morre quando o número de referências a ele chega a zero.

    Cenário Real: Se você guardar o GeminiService em uma lista global, o GC nunca vai matá-lo, o que pode causar um Memory Leak (vazamento de memória) se você não tomar cuidado.

🔴 Estudo 3: Injeção de Dependência com Depends (FastAPI)

    O que focar: Entender o parâmetro use_cache=True (que é o padrão do Depends).

    O "Pulo do Gato": O FastAPI consegue resolver a dependência uma única vez por request. Se três funções diferentes na mesma rota pedirem o GeminiService, o FastAPI é inteligente o suficiente para criar apenas um e repassar para as três, economizando memória.


📈 Atualização do Guia de Estudos: Foco em SeleniumBase (SB)
🕵️ Estudo 6: O Modo Undetected (UC) e Evasão de Fingerprint

    O que focar: Entender o que é o reconnect. Às vezes o Cloudflare te dá um "Soft Block" (aquela tela de espera). O uc_open_with_reconnect abre o site, espera o desafio carregar e tenta "fingir" um refresh humano para validar o cookie de acesso.

    O Desafio: Tente rodar o mesmo código, mas troque uc=True por uc=False. Você verá que o Cloudflare te barrará instantaneamente. Isso prova que o SB está manipulando o binário do navegador para esconder que é um bot.

    Links de Estudo: *  - A "bíblia" do bypass.

🖥️ Estudo 7: Headless vs. XVFB (Telas Virtuais)

    O que focar: No WSL ou Docker, não existe "monitor". O modo headless=True comum é facilmente detectado por sites pesados. O xvfb=True cria um monitor invisível na memória do Linux.

    O Desafio: Estude como o Cloudflare consegue detectar se um navegador está rodando sem interface gráfica (headless) através da resolução de tela e renderização de fontes.

    Dica de Sênior: O xvfb é o seu melhor amigo para rodar scrapers no Docker que precisam parecer 100% humanos.

🧱 Estudo 8: Seletores Estratégicos e Espera Implícita

    O que focar: No seu código, você usou sb.wait_for_element('table.stats_table'). Isso é Arquitetura de Resiliência.

    O Desafio: Aprenda a usar o sb.uc_click() em vez do .click() comum. O uc_click simula o movimento do mouse e o tempo de reação humano antes de apertar o botão.