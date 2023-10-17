import openai


def generate_article(topic):
    openai.api_key = "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"

    prompt = f"Write a short article about {topic}"
    max_tokens = 200  # the number of tokens per article

    response = openai.Completion.create(
        engine="text-davinci-002",  # You can use other engines
        prompt=prompt,
        max_tokens=max_tokens
    )

    return response.choices[0].text.strip()
