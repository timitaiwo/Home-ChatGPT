from flask import request, Blueprint, render_template

from urllib.parse import urlparse, parse_qs

from transformers import AutoModelForCausalLM, AutoTokenizer

ai_model : Blueprint = Blueprint('ai_model', __name__)

def setup_model():
    LM_MODEL_STR = "amd/AMD-OLMo-1B-SFT"
    model = AutoModelForCausalLM.from_pretrained(LM_MODEL_STR)
    tokenizer = AutoTokenizer.from_pretrained(LM_MODEL_STR)

    return model, tokenizer

def make_promt(prompt, model, tokenizer):

    bos = tokenizer.eos_token
    input_text = bos + f'<|user|>\n{prompt}\n<|assistant|>\n'

    inputs = tokenizer([input_text], return_tensors='pt', return_token_type_ids=False)
    outputs = model.generate(**inputs, max_new_tokens=1000, do_sample=True, top_k=50, top_p=0.95)
    output =  tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]

    print()

    print(input_text)
    print(output)

    print()

    return output


model, tokenizer = setup_model()
@ai_model.route('/')
def index():

    parsed_query = urlparse(request.url).query
    prompt = parse_qs(parsed_query)['prompt'][0].strip()
    print("\n", prompt)
    output = make_promt(prompt, model, tokenizer).split("<|assistant|>")[1]
    
    print("End of run the output is: ", output)

    return render_template('assistant_page.html', prompt=prompt, response=output)
