# **Desafio Azure OpenAI com Integração Semantic Kernel**

Este repositório contém a implementação de um projeto que explora o uso do **Azure OpenAI** para chamadas de API, aliado à integração com o **Semantic Kernel**. O objetivo é demonstrar a criação de aplicações práticas utilizando inteligência artificial e integrar capacidades avançadas por meio dessas tecnologias.

## **Descrição do Projeto**

O projeto inclui:
- Uma **chamada de API** ao Azure OpenAI Service para execução de tarefas como conclusão de texto.
- Uma **integração prática** com o Semantic Kernel para demonstrar como organizar prompts e utilizar modelos avançados.

## **Estrutura do Repositório**

```
/desafio-azure-openai
├── /src
│   ├── chamada_api.py          # Código para chamada de API em Python
│   └── integracao_kernel.cs    # Código de integração com Semantic Kernel em C#
├── README.md                   # Documentação do projeto
└── slides_referencia.pptx      # Material de apoio opcional
```

## **Pré-requisitos**

Certifique-se de que o seguinte está configurado:
1. Uma conta no **Azure** com o **Azure OpenAI Service** habilitado.
2. Ferramentas instaladas:
   - **Python 3.7+** (para a chamada de API)
   - **.NET Core SDK** (para a integração com Semantic Kernel)
   - **Git** para versionamento.

## **Como Rodar o Projeto**

### **Parte 1: Chamada de API com Python**

1. Navegue até a pasta `/src`.
2. Instale as dependências necessárias:
   ```bash
   pip install requests
   ```
3. Configure o código no arquivo `chamada_api.py`:
   - Atualize os campos `api_url` e `api_key` com suas credenciais do Azure.
4. Execute o script:
   ```bash
   python chamada_api.py
   ```

### **Parte 2: Integração com Semantic Kernel**

1. Navegue até a pasta `/src`.
2. Adicione o pacote **Semantic Kernel** ao projeto .NET:
   ```bash
   dotnet add package Microsoft.SemanticKernel
   ```
3. Configure o arquivo `integracao_kernel.cs`:
   - Substitua as credenciais pelo nome da sua instância, deployment e chave de API.
4. Compile e execute o projeto:
   ```bash
   dotnet run
   ```

## **Materiais de Apoio**

- **Slides**: *Aplicação de Chats e Configurações API - API e Semantic Kernel.pptx*
- **Documentações Importantes**:
  - [Azure OpenAI Service REST API Reference](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)
  - [Semantic Kernel Overview](https://learn.microsoft.com/en-us/semantic-kernel/overview)

## **Contribuição**

Sinta-se à vontade para abrir issues ou enviar pull requests com sugestões de melhoria para este projeto. 😊

## **Licença**

Este repositório segue a [MIT License](https://opensource.org/licenses/MIT).

---

