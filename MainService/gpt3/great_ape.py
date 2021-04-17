from chronological import read_prompt, cleaned_completion, main
from .constants import *

async def classify_erl_erk(input_data):
    print("Here")
    prompt_extract_erk_info = prompt
    prompt_extract_erk_info += input_data
    prompt_extract_erk_info += extracted_ids
    completion_extract_erk_info = await cleaned_completion(prompt_extract_erk_info, max_tokens=200, engine="davinci", temperature=0.5, top_p=1, frequency_penalty=0.2, stop=["\n\n"])

    return completion_extract_erk_info



async def logic(input_data):
    result = await classify_erl_erk(input_data)
    print(result)

    
# input_data = text_prompt
# main(logic(text_prompt))