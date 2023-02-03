# IFS40km_download


## Script para baixar dados diários de previsão de precipitação do modelo **IFS** - Integrated Forecast System | ECMWF

Aqui é possível baixar gratuitamente os dados do modelo IFS **selecionando apenas a variável desejada**. Dminuindo o tempo e espaço.
Isso se faz necessário pois ao utilizarmos o caminho https://data.ecmwf.int/forecasts/ só é possível variar por datas e baixar os 720 Gb por rodada.


Não esqueça de instalar as bibliotecas necessárias, bem como realizar o cadastro no sistema do ECMWF. Registered access (recommended)
No link abaixo é apresentada a explicação para o cadastro (mesmo cadastro válido para o CDSAPI do ERA-5)

https://github.com/ecmwf/ecmwf-api-client

Crie no seu $HOME o arquivo oculto .ecmwfapirc (Unix/Linux) ou %USERPROFILE%\.ecmwfapirc (Windows), copiando e colando os dados do seu cadastro no ECMWF. 

```python

{
    "url"   : "https://api.ecmwf.int/v1",
    "key"   : "XXXXXXXXXXXXXXXXXXXXXX",
    "email" : "john.smith@example.com"
}
```

Não esqueça de trocar o PATH no código.

Deixei adicionado um gráfico gerado apartir dos dados gerados (pyNGL). 

PS: Otimize esse código o quanto quiser. Não programo em python, não gosto de python.
