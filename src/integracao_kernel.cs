using Microsoft.SemanticKernel;

var kernel = Kernel.Builder.Build();

var azureAIConfig = new AzureOpenAIConfig("<sua-instancia>", "<seu-deployment>", "<chave_api>");
kernel.Config.AddAzureTextCompletionService("davinci", azureAIConfig);

var prompt = "Explique o conceito de inteligência artificial.";
var result = await kernel.RunAsync(prompt);

Console.WriteLine(result);
