# configuration setup.
from pathlib import Path
from groq import Groq
from conversation_summarizeer import ConvoSummarizer


key = "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"
client = Groq(api_key=key)

text_file = Path("/Users/akshitbhatia/Downloads/_chat 6.txt")
conv_text = text_file.open('r').read()

summarizer = ConvoSummarizer(client)
summary = summarizer.summarize_conversation(conv_text)

Path("/Users/akshitbhatia/Downloads/summary.txt").write_text(summary)