from groq import Groq

from src.utilities import add_conversation, create_splits


class ConvoSummarizer:
    system_message = 'You are a conversation summarizer. For the given part of the conversation, summarize it. Focus on the main themes, key points and topics.'
    system_combined = 'As a person who keeps aggregates important information together, for the list of given summaries, make a unified summary.'

    def __init__(self, client: Groq, model: str = "llama-3.3-70b-versatile", batch_size=None):
        self.model = model
        self.batch_size = batch_size
        self.client = client

    def create_summaries(self, splits: list) -> list:
        """
        For each split containing text, make a summarization.

        Parameters:
        -----------
        splits: list of strings

        """
        summaries = []
        for index, split in enumerate(splits):
            conv = add_conversation(''.join(split))
            response = self.client.chat.completions.create(messages=conv, model=self.model)
            summary = response.choices[0].message.content
            summaries.append(summary)

            if index % 4 == 0:
                print(f'summarized {index + 1} out of {len(splits)}')
        return summaries

    def combine_summaries(self, summaries: list) -> str:
        """Combine list of summaries together.

        Parameters
        ----------
        summaries: list of summaries.

        """
        summary_str = ' '.join(summaries)  # combine all text from the list into a single string.
        print(f'total number of lines from the individual summary from the list is: {len(summary_str.split('\n'))}')
        summ_conv = add_conversation(summary_str, combined=True)
        response = self.client.chat.completions.create(messages=summ_conv, model=self.model)
        unified_summy = response.choices[0].message.content
        print(f'total number of lines in the final summary is: {len(unified_summy.split('\n'))}')

        return unified_summy

    def summarize_conversation(self, text: str) -> str:
        """Summarize the given conversation.

        Parameters
        ----------
        text: str

        """
        if self.batch_size:
            splits = create_splits(text, self.batch_size)
        splits = create_splits(text)
        summaries = self.create_summaries(splits)
        summary = self.combine_summaries(summaries)

        return summary
