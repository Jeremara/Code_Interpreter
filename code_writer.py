import openai
import time
from openai.error import RateLimitError

# Set your OpenAI API key
openai.api_key = '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'

def generate_code_with_retry(prompt, max_retries=3, backoff_factor=2):
    retries = 0
    while retries < max_retries:
        try:
            response = openai.Completion.create(
                engine="gpt-3.5-turbo",
                prompt=prompt,
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7,
            )
            return response.choices[0].text.strip()
        except RateLimitError as e:
            retries += 1
            if retries >= max_retries:
                raise e
            wait_time = backoff_factor ** retries
            print(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
