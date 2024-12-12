"""
prompts.py: This file will not be used in future versions of this package. Use LangSmith prompthub instead.
"""

from typing import List, Tuple
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.prompts import PromptTemplate
import re  # Import regex for filtering bad language

class Prompts:
    """
    A class to encapsulate prompt templates used in the application.

    Attributes
    ----------
    prompt : str
        A string template for QA prompts.
    """

    def __init__(self):
        """
        Initializes the Prompts class with predefined prompt templates.
        """
        self.bad_word_replacements = {
            "vacuous": "uninformed",
            "moronic": "unwise",
            "idiotic": "ill-considered",
            "ridiculous": "absurd",
            "brainlessly": "thoughtlessly",
            "foolish": "ill-advised",
            "stupid": "misguided",
            "nonsense": "unreasonable",
            "clueless": "uninformed",
            "absurdity": "incongruity",
        }


        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "Please only use the provided context to generate your responses.\n"
                    "Context information is below.\n"
                    "You are Siva, an Intelligent AI Assistant designed to provide quick and precise answers to queries. Your primary function is to extract relevant information from the document intelligently and summarize it when necessary. You aim for a response time of less than 5 seconds.\n"
                    """
                    Your responses should:
                        - Be sharp, intelligent, and precise, especially for short questions.
                        - Use natural and conversational language, incorporating interjections and expressions.
                        - Exhibit empathy and personalization to address the customer's issues effectively.
                        - Completely avoid inappropriate language; respond ethically and professionally. If a query contains offensive language, replace it with a more suitable alternative word while maintaining respect and professionalism.
                    """
                    "---------------------\n"
                    "{context}\n"
                    "---------------------\n"
                    "Do not use any external knowledge. Keep the language of your answers clear, polite, and respectful.\n"
                    "When greeted with hi hello or hey, your reply should be something like this: Hi, I am Siva, your Intelligent AI Assistant. How can I assist you today?\n"
                    "When asked about inappropriate topics or language, respond with: 'I prefer to maintain a respectful conversation. How can I assist you with your queries?'\n"
                    "If you are not aware of the context, respond with: 'I apologize for the inconvenience; I am still in my development phase.'\n"
                    "Structure your response as follows:\n"
                    "1. Acknowledge the query.\n"
                    "2. Provide the answer based on the provided context.\n"
                    "3. If the information is not available, provide the contact details of the support engineers.\n"
                    "Given the context information and not prior knowledge, answer {question}\n"
                    "---------------------\n"
                    "Thank you for reaching out! If you have any further questions, feel free to ask."
                ),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{question}"),
            ]
        )

    def replace_bad_language(self, text: str) -> str:
        """
        Replace bad language in the input text with better alternatives.

        Parameters
        ----------
        text : str
            The input text to filter.

        Returns
        -------
        str
            The filtered text with inappropriate language replaced.
        """
        for bad_word, alternative in self.bad_word_replacements.items():
            text = re.sub(r'\b' + re.escape(bad_word) + r'\b', alternative, text, flags=re.IGNORECASE)
        
        return text

    def get_filtered_prompt(self) -> str:
        """
        Get the prompt with filtered bad language.

        Returns
        -------
        str
            The prompt string with bad language replaced.
        """
        raw_prompt = self.prompt.messages[0][1]  # Get the raw prompt message
        return self.replace_bad_language(raw_prompt)

