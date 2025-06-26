from pydantic_ai.direct import model_request_sync
from pydantic_ai.messages import ModelRequest
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

provider = OpenAIProvider(base_url="http://localhost:4891/v1")
model = OpenAIModel(model_name="Llama 3 8B Instruct", provider=provider)

model_response = model_request_sync(
    model,
    [ModelRequest.user_text_prompt('Write 20 random words')]
)

print(model_response.parts[0].content)
print(model_response.usage)