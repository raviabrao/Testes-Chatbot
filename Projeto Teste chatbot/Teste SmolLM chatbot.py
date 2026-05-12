from transformers import pipeline

pipe = pipeline("text-generation", model="HuggingFaceTB/SmolLM-135M-Instruct")

messages = [
    {"role": "user", "content": "What's your name?"},
]
pipe(messages)

print(pipe(messages))