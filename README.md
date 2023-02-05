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


Se após trocar os PATHs, identificar o erro:

**Traceback (most recent call last):**
  **File "/home/mateusdiasnunes/Downloads/baixar_IFS_40KM.py", line 88, in <module>
    client.retrieve( **
  **File "/home/mateusdiasnunes/anaconda3/envs/mconda/lib/python3.11/site-packages/ecmwf/opendata/client.py", line 68, in retrieve
    data_urls, target = self._get_urls( **
                        
Basta entrar no arquivo **client.py** e trocar a URL na linha que aparece:

```
self._url = "https://"
```

Para:

```
self._url = "https://data.ecmwf.int/forecasts/"
```

Deixei adicionado um gráfico gerado apartir dos dados gerados pelo pyNGL (porque não sou obrigado a usar biblioteca do matlab aliada ao atraso do cartopy) 

PS: Otimize esse código o quanto quiser. Desculpem a bagunça do código.
