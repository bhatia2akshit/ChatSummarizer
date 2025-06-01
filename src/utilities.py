# static methods
system_message='You are a conversation summarizer. For the given part of the conversation, summarize it. Focus on the main themes, key points and topics.'
system_combined = 'As a person who keeps aggregates important information together, for the list of given summaries, make a unified summary.'

def add_conversation(content: str, combined: bool = False) -> list:
    """This creates the conversation dictionary.

    Parameters
    ----------
    content: string message. if list of messages, combine them with a space and join function.
    combined: boolean flag that when is true, means different summaries needs to be combined.

    Returns
    -------
    returns a list object, containing dictionaries with key being the role and value being the content.
    """

    list_convo = []
    if combined:
        list_convo.append({"role": 'system', 'content': system_combined})
    else:
        list_convo.append({"role": 'system', 'content': system_message})

    list_convo.append({"role": "user", "content": content})

    return list_convo


# make splits of 300
def create_splits(text: str, size=200) -> list:
    """Creates splits such that each contains the given size."""
    splits = []
    texts = text.split("\n")
    print('length of lines in the given conversation is: ', len(texts))

    for ind, i in enumerate(range(0, len(texts), size)):
        if i + size >= len(texts):
            splits.append(texts[i:i + len(texts)])
            continue

        splits.append(texts[i:i + size])

    return splits