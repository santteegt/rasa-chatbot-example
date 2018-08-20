# Chatbot example using Rasa

Basic chatbot example using the OpenSource [Rasa Stack](http://www.rasa.com/) (Rasa NLU and Rasa Core). Rasa is written in Python allows developers to expand chatbots and voice assistants beyond answering simple questions by enabling state-of-the-art machine learning models your bots can hold contextual conversations with users.

This repository is based on the official Rasa [quicktart](http://www.rasa.com/docs/core/quickstart/) guide, while also introduces the use of Ngrok to perform local tests of your chatbot interaction with Facebook messenger.

## Installation requirements

* Python 3.6
* pip
* conda
* Ngrok ([Website](https://ngrok.com/))
* Rasa Core and Rasa NLU. Follow official installation [instructions](http://www.rasa.com/docs/core/installation/). Altenatively you can just run the following on a terminal.
```bash
~ $ conda create --name rasa --file environment.yml
~ $ source activate rasa
(rasa) $ pip install -r requirements.txt
~ $
```

## Chatbot setup & deployment

Follow the instructions below to train and test the chatbot. Requires configuration files to setup your bot are:

* **Rasa Core**

- **stories.md**: Rasa Core works by learning from example conversations. A story starts with `##` followed by a name (optional). Lines that start with `*` are messages sent by the user. Although you don’t write the actual message, but rather the intent (and the entities) that represent what the user means. Lines that start with - are actions taken by your bot. In general an action can do anything, including calling an API and interacting with the outside world. Find more info about the format [here](http://www.rasa.com/docs/core/stories/).

- **domain.yml**: The domain defines the universe your bot lives in (see [Domain format](http://www.rasa.com/docs/core/domains/)):

| Conf      | Description                                        |
|-----------|----------------------------------------------------|
| actions   | things your bot can do and say                     |
| templates | template strings for the things your bot can say   |
| intents   | things you expect users to say                     |
| entities  | pieces of info you want to extract from messages   |
| slots     | information to keep track of during a conversation |

* **Rasa NLU**

- **nlu.md**: define the user messages the bot should be able to handle. It is suggested to define at least five examples of utterances.
- **nlu_config.yml**: NLU parameters configuration

### 1. Train your model

```bash
(rasa) $ python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue
```

### 2. Train your NLU agent

```bash
(rasa) $ python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose
```

### 3. Test your chatbot locally

```bash
(rasa) $ python -m rasa_core.run -d models/dialogue -u models/current/nlu
```

### 4. Connect to Facebook Messenger (Optional)

1. First of all, you need to set up a Facebook app and a page. To create the app go to: [https://developers.facebook.com/](https://developers.facebook.com/) and click on “Add a new app”.
1. Go to the Basic Settings of the app and copy the ${APP_SECRET} value.
1. Go onto the dashboard for the app and under Products, click Add Product and add Messenger. 
1. Under the settings for Messenger, scroll down to Token Generation and click on the link to create a new page for your app.
1. Copy the generated `${ACCESS_TOKEN}`.
1. On a separate terminal, start a ngrok tunnel with this command:
```bash
~ $ ngrok http 5002
```
1. Copy the public `${URL}` from the ngrok [dashboard](http://localhost:4040)
1. Go onto the dashboard for the app and under Products, click Add Product and add Webhooks.
1. Under Webhooks settings, select `Page` and then click on `Subscribe to this object`
1. Set the Callback URL & `${VERIFY_TOKEN}` properties to `${URL}/webhook` and `my-rasa-bot` respectively.
1. Configure the [fb_credentials.yml](fb_credentials.yml) file with properties `${VERIFY_TOKEN}`, `${APP_SECRET}` AND `${ACCESS_TOKEN}` you collected.
1. Deploy your chatbot locally by running the following command:
```bash
(rasa) $ python -m rasa_core.run -d models/dialogue -u models/current/nlu --port 5002 --connector facebook --credentials fb_credentials.yml
```
1. Now you can test your chatbot by sending messages to your Page through FB Messenger.

# License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE.txt)