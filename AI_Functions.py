#from openai import OpenAI
#client = OpenAI()


print("Hello World")

def call_llm(llm_model, messages, tools):
    response = client.chat.completions.create(
            model=llm_model, #gpt 4o is accurate in calling the exact number of calls based on request. gpt-3-turbo is not fully accurate. While the ideal way may be to call in loop. Since I am lazy, switched to gpt4o. Slightly higher cost.
            messages=messages,
            tools=tools,
            tool_choice="required",  # Forcing the use of tools
        )
    return response.choices[0].message