from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("google/gemma-4-E2B-it-assistant")
model = AutoModelForCausalLM.from_pretrained("google/gemma-4-E2B-it-assistant")