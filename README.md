# Telegram_bot
A simple example of a telegram chatbot with a neural network as a the engine.

### Overview
This is a simple first attempt of an telegram chatbot with a 2 layer CNN network running at its core. It is trained on simple words of affection and its sentiments(tags). It is then trained to return a variety of prefix responses based on the sentiment(tags). The trained data can be found in src\intents.json

### Prerequisite
You need to generate a token for your own telegram bot. You can do this by talking to BotFather telegram's bot and creating a new bot!
### To Run
To run it , please input your telegram token inside the resoruces\config.cfg file and then run main.py.

You can include or change/add/edit src\intents.json and then run src\training.py to train the model on your own set of words with tags.

The telegram_bot.py is a skeleton of the bot.

#### Training
Model training is done with the src\intents.json as the input data and src\training.py 
Not much data cleaning is done for the training stage. Simply running src\training.py would create a .h5 model in the resources folder.

NOTE: I plan to create a more robust data ingestion pipeline that can be used for training data and test data.
#### Inference 
The data preprocess for prediction,model instantiation and inference is done in src\chatbot.py.

NOTE: I have future plans to clean this up and creat a model class that handles this and training together under one model class


### FUTURE PLANS
1. Plan to do logging of conversations with users based on the day and username.
    - Outputs a txt file
2. Create a proper training data ingestion pipeline 
    - Takes in a txt file and converts it to a json format. User might have to fill up/group bag of words into tags
    - Find an automated solution for this.
3. Experiement with more complex models as the engine
    - Create a new model ingestion pattern that can simply plug and play different models.