#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o Grub para reconhecer o `Windows` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o Grub para reconhecer o `Windows` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings to configure/install/use the Grub to recognize `Windows` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ## Grub
# 
# O GRUB (Grand Unified Bootloader) é um carregador de inicialização multissistema muito utilizado em sistemas operacionais baseados em Unix, como Linux e FreeBSD. Sua função principal é gerenciar o processo de boot do computador, permitindo que o usuário escolha entre diferentes sistemas operacionais instalados ou diferentes versões de um mesmo sistema. O GRUB se destaca por sua flexibilidade e capacidade de personalização, oferecendo suporte a diversos sistemas de arquivos e possuindo recursos como a detecção automática de outros sistemas operacionais e a capacidade de modificar parâmetros de inicialização em tempo real. Ele substituiu o LILO (Linux Loader) como o carregador de boot padrão em muitas distribuições Linux, devido à sua maior facilidade de configuração e robustez
# 
# ## Windows
# 
# 
# O Windows é um sistema operacional desenvolvido pela Microsoft, amplamente utilizado em computadores pessoais e em ambientes empresariais em todo o mundo. Conhecido por sua interface gráfica intuitiva e amigável, o Windows oferece um ambiente de computação completo, fornecendo suporte para uma ampla variedade de aplicativos, jogos e utilitários. Com uma história de evolução contínua ao longo das décadas, o Windows apresenta várias versões, como o Windows 10 e o Windows 11, cada uma com recursos aprimorados, segurança e desempenho. Ele é compatível com uma vasta gama de hardware e oferece uma plataforma flexível para usuários domésticos e profissionais, tornando-o um dos sistemas operacionais mais populares e influentes na história da computação pessoal.
# 

# ## 1. Configurar/Instalar/Usar o `Grub` para reconhecer o `Windows` no `Linux Ubuntu` [1]
# 
# **ATENÇÂO**: Tenha em mente que o `GRUB` deve ser instalado no primário da sequência de `boot`, logo, se ele for instalado em outro disco, este, por sua vez, deve ser alterado para ser o primeiro disco na inicialização do computador.
# 
# ### 1.1 Atualizar o Sistema Operacional (SO)
# 
# Se o Windows está instalado em uma unidade separada, seja a `/dev/sda/` ou outra, por exemplo: `/dev/sdb`, e você quer configurar o GRUB para reconhecê-lo, siga estes passos:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes APT. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo APT e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.5 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.6 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.7 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.8 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

# 3. **Atualize o GRUB:** Primeiro, atualize o GRUB para garantir que ele detecte automaticamente o Windows. Abra o terminal e digite: `sudo update-grub`
# 
#     Este comando procura por sistemas operacionais em todas as unidades conectadas. Se o Windows estiver instalado corretamente e a partição não estiver corrompida, o GRUB deve encontrá-lo e adicioná-lo ao menu de inicialização.
# 
# 4. **Verifique se o Windows foi Adicionado:** Após a execução do comando, verifique a saída no terminal. Geralmente, ele mostrará uma mensagem informando que encontrou o Windows Boot Manager em `/dev/sdb`, por exemplo.
# 
# 5. **Reinicie o Computador:** Reinicie o sistema e verifique se o Windows aparece no menu do GRUB.
# 
# 6. **Caso o Windows Não Apareça:** Se o Windows ainda não aparecer no menu do GRUB, você pode precisar adicionar uma entrada manualmente.
# 
#     6.1 **Usando o os-prober:**
# 
#     6.1.1 Para localizar a instalação do Windows a partir do terminal do Linux Ubuntu, você pode usar o comando `os-prober` ou verificar manualmente as partições. Aqui estão os passos para ambos os métodos:
# 
#     6.1.2 **Usando o `os-prober`:** Instale o `os-prober` (se ainda não estiver instalado): Abra o terminal e digite:
# 
#         ```
#         sudo apt update -y
#         sudo apt list --upgradable
#         sudo apt upgrade -y
#         sudo apt install os-prober
#         ```
# 
#     6.1.3 **Execute o `os-prober`:** Após a instalação, execute o comando: `sudo os-prober`
# 
#     Este comando irá listar os sistemas operacionais instalados. Se o Windows estiver instalado, ele deve aparecer na lista.
# 
#     6.2 **Verificando Manualmente as Partições:**
# 
#     6.2.1 **Liste as partições do disco:** Utilize o comando `lsblk` para listar as partições. Por exemplo:  `lsblk -f`
# 
#     Esse comando mostra as partições em todos os discos. As partições do Windows geralmente estão formatadas em `NTFS` ou `FAT32`.
# 
#     6.2.2 **Identifique a Partição do Windows:**
# 
#     Procure por partições com o tipo `NTFS` ou `FAT32`. O tamanho da partição também pode ajudar a identificar qual delas é a do Windows, especialmente se for uma partição grande, que provavelmente é a partição `C:` do Windows.
# 
#     6.3 **Monte a Partição (Opcional):**
# 
#     6.3.1 Se você deseja acessar os arquivos do Windows, pode montar a partição. Por exemplo: `sudo mount /dev/sdXN /mnt`
# 
#     Aqui, substitua /dev/sdXN pelo identificador correto da partição do Windows (por exemplo, /dev/sda2).
# 
#     Lembre-se de que alterar arquivos do Windows a partir do Linux pode ser arriscado, especialmente os arquivos de sistema. É sempre recomendado fazer backups antes de realizar tais operações.
# 
# 7. Abra um editor de texto com privilégios de administrador, como o `nano`, e edite o arquivo `/etc/grub.d/40_custom` executando o comando: `sudo nano /etc/grub.d/40_custom`
# 
# 7. Adicione a seguinte entrada no arquivo:
# 
#     ```
#     menuentry "Windows 7 Professional" {
#         set root='(hd1,1)'
#         chainloader +1
#     }
#     ```
# 
#     **Note que:** `(hd1,1)` refere-se a `/dev/sdb2`. Se o Windows estiver em uma partição diferente em `/dev/sdb`, ajuste conforme necessário. `hd1` representa o segundo disco (`sdb`), e `1` representa a primeira partição nesse disco.
# 
# 8. Salve e feche o arquivo (`Ctrl+O`, Enter, `Ctrl+X` para salvar e sair no nano).
# 
# 9. **Atualize o GRUB Novamente:** Após adicionar a entrada manual, atualize o GRUB novamente: `sudo update-grub`
# 
# 10. **Reinicie e Verifique:** Reinicie o sistema novamente e verifique se o Windows agora aparece no menu de inicialização do GRUB.
# 
# Essas etapas devem ajudá-lo a configurar o GRUB para reconhecer e listar o Windows no menu de inicialização, especialmente quando está instalado em um segundo disco (/dev/sdb).
# 

# ## 2. Código completo
# 
# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `GRUB` para reconhecer o `Windows` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÃO há.
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***GRUB: carregador de inicialização multifuncional.*** Disponível em: <https://chat.openai.com/c/4e8aa5fa-7954-4191-976a-7d81731aac10> (texto adaptado). Acessado em: 09/11/2023 16:38.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 16/11/2023 14:25.
# 
