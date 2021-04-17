import openai
from chronological import read_prompt, cleaned_completion, main
from .constants import *
from .search_results_utils import *

async def classify_erl_erk(input_data):
    print("Here")
    prompt_extract_erk_info = prompt
    prompt_extract_erk_info += input_data
    prompt_extract_erk_info += extracted_ids
    completion_extract_erk_info = await cleaned_completion(prompt_extract_erk_info, max_tokens=200, engine="davinci", temperature=0.5, top_p=1, frequency_penalty=0.2, stop=["\n\n"])

    return completion_extract_erk_info

async def semantic_search_erl_erk(input_data):
    response = await openai.Engine("davinci").search(
        search_model="davinci",
        query=input_data,
        documents=[
            "Endrechnungskennzeichen and Endlieferkennzeichen",
            "Endrechnungskennzeichen",
            "Endlieferkennzeichen"
            ]
    )

    search_results = create_search_results(response)
    if rel_diff_is_too_small(search_results):
        return classify_erl_erk(input_data)

    return search_results[0].type

async def logic(input_data):
    result = await classify_erl_erk(input_data)
    print(result)


# input_data = text_prompt
# main(logic(text_prompt))
