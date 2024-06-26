from llama_cpp import Llama
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

SYSTEM_PROMPT = "Always make only a summary of the given text. Always answer in russian language."
app_nlp = FastAPI()

class NlpRequest(BaseModel):
    text: str

def get_message_tokens(model, role, content):
    content = f"{role}\n{content}\n</s>"
    content = content.encode("utf-8")
    message_tokens = model.tokenize(content, special=True)
    return message_tokens


def get_system_tokens(model):
    system_message = {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
    return get_message_tokens(model, **system_message)


def interact(
    request_text,
    model_path="mistralQ2_K.gguf",
    n_ctx=2000,
    top_k=30,
    top_p=0.9,
    temperature=0.2,
    repeat_penalty=1.1
):
    model = Llama(
        model_path=model_path,
        n_ctx=n_ctx,
        n_parts=1,
    )

    system_tokens = get_system_tokens(model)
    tokens = system_tokens
    model.eval(tokens)

    user_message = "Сделай краткое содержание этого текста, расскажи про что там говорится: " + request_text

    output = ""
    message_tokens = get_message_tokens(model=model, role="user", content=user_message)
    role_tokens = model.tokenize("bot\n".encode("utf-8"), special=True)
    tokens += message_tokens + role_tokens
    # full_prompt = model.detokenize(tokens)
    generator = model.generate(
        tokens,
        top_k=top_k,
        top_p=top_p,
        temp=temperature,
        repeat_penalty=repeat_penalty
    )
    for token in generator:
        token_str = model.detokenize([token]).decode("utf-8", errors="ignore")
        tokens.append(token)
        if token == model.token_eos():
            break
        print(token_str, end="", flush=True)
        output += token_str
    return(output)

@app_nlp.post("/nlp")
async def nlp(request: NlpRequest):
    try:
        output = interact(request.text)
        return output
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app_nlp, host="localhost", port=9001)
