# Youtube-Data-Analysis
Sistema para Análise de Indicadores de Comentários de Vídeos do YouTube

 ---

 ## Build e Teste da API localmente

Configurar variáveis de ambiente:

- Criar arquivo chamado "local.env" no diretório raiz do projeto com as informações:
  - youtubeApiKey: Api Key do Youtuve Api Service do GCP

Fazer o build da imagem para usar no docker:
`docker build --file Dockerfile.local -t youtube-data-analysis .`

Rodar container docker com aplicação:
`docker run -p 8000:8000 youtube-data-analysis:latest uvicorn --host 0.0.0.0 run:create_app`
