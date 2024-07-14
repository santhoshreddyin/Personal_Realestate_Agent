from openai import OpenAI
client = OpenAI()

def call_llm(llm_model, messages, tools,temperature):
    if tools:
        response = client.chat.completions.create(
            model=llm_model,
            messages=messages,
            tools=tools,
            tool_choice="required", 
            temperature=temperature,
        )
    else:
        response = client.chat.completions.create(
        model=llm_model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message