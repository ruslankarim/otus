from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, T5Tokenizer, RobertaTokenizer
# C:/Users/Руслан/.cache/huggingface/hub/models--sberbank-ai--ruT5-large/snapshots/b3321d48aefe45ffd70ea2f649570b91441e0055/spiece.model
tokenizer = AutoTokenizer.from_pretrained("sberbank-ai/ruT5-large")

with open("C:/Users/Руслан/.cache/huggingface/hub/models--sberbank-ai--ruT5-large/snapshots/b3321d48aefe45ffd70ea2f649570b91441e0055/spiece.model", "rb") as file:
    b = file.read()
    print("")