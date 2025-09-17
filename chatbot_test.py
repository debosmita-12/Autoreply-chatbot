import openai

# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
openai.api_key = "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"

command = ''' [21:00, 14/7/2025] Shashwat: Are aise mat karo yaar chat leak ho jayega 😂
[21:00, 14/7/2025] Shashwat: Python project?
[21:01, 14/7/2025] Debosmita: haan
[21:07, 14/7/2025] Shashwat: Bolo hogi kya leak ?
[21:07, 14/7/2025] Shashwat: Nice
[21:12, 14/7/2025] Debosmita: nhi'''

# Fix: use openai.ChatCompletion directly (not client.chat)
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Debosmita who speaks English, Hindi and Bengali. She is a coder and is from India. You analyse the chat and respond like Debosmita."},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)