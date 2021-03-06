from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

##############################################
# snippet of code that helps downloading the language 
# corpora in my desktop



#####################Feel free to erase#########################
# import nltk
# import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# nltk.download()


##############################################
app = Flask(__name__)

english_bot = ChatBot("Chatterbot",storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3')
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english.conversations")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
