# One Word Story
This is a game where the a user and a bot make a story by taking turns to say one word at a time.

**Building the one-word story app.**
- Using Ngram conditional Probability distributions. Greedy vs. beam search.
- Investigating failings of Ngram method. Lack of distributed representations, no sense of
closeness unless exact examples have been seen before.
- RNNs and learning long-distance dependencies. LSTMs.
- Vocabulary size contraints for Ngram vs. LSTM
- LSTM language model code. Making predictions - greedy vs. beam search.
- Multiple layers and the effects on fluency.
- Creating the simple word game. LSTM makes predictions on entire past sequence (inputs from user and bot).
- Flask web application


**Separate/future work**

- Using pre-trained speech recognition model to incorporate voice-activation. Argmax over vocab words becomes input into OWS app.
- Text to speech using a pre-trained model.
