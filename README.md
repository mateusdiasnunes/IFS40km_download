# IFS40km_download


## Script para baixar dados diários de previsão de precipitação do modelo **IFS** - Integrated Forecast System | ECMWF

Aqui é possível baixar gratuitamente os dados do modelo IFS **selecionando apenas a variável desejada**.

Não esqueça de instalar as bibliotecas necessárias, bem como realizar o cadastro no sistema do ECMWF. Registered access (recommended)
No link abaixo é apresentada a explicação para o cadastro (mesmo cadastro válido para o CDSAPI do ERA-5)

https://github.com/ecmwf/ecmwf-api-client

Your $HOME/.ecmwfapirc (Unix/Linux) or %USERPROFILE%\.ecmwfapirc (Windows) should look something like this:

{
    "url"   : "https://api.ecmwf.int/v1",
    "key"   : "XXXXXXXXXXXXXXXXXXXXXX",
    "email" : "john.smith@example.com"
}

Não esqueça de trocar o PATH e inserir seu login e senha do cadastro no ONS.
