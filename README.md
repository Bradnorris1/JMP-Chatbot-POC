# JMP-Chatbot-POC

Python chatbot proof-of-concept designed as an intern project by Brad Norris for the summer of 2023 at JMP.

You will need to download 'punkt' nltk model, as well as the following libraries:
nltk, torch, tensorflow, flask, numpy, json

To train the bot, simply run the "train.py" file.
To change the number of training cycles, modify the "num_epochs" variable in the "train.py" file.

To modify training data, simply change any information inside the "intents.json" file.
**"tag"** - categorical, for organizational purposes.
**"patterns"** - the training data itself, make sure this is unique and clean for each case.
**"responses"** - The response to be sent by the bot, you can include multiple responses and one will be chosen at random.

Once the bot has been locally trained, initiate the bot by running the file "FlaskChat.py". You will need to visit the link that outputs in the console in order to chat with the bot.
