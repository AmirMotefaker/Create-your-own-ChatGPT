# Create your own CatGPT

# Introduction
- ChatGPT (Chat Generative Pre-trained Transformer) is an AI-powered chatbot created by [OpenAI](https://openai.com/) that enables users to have highly sophisticated, human-like conversations. The language model is capable of answering questions and assisting in various tasks, including writing emails, essays, and code. Due to its dialogue design, ChatGPT is capable of answering follow-up questions, acknowledging errors, questioning incorrect assumptions, and declining inappropriate requests.

- The ChatGPT model was fine-tuned from a model in the GPT-3.5 series, which completed its training in early 2022. The ChatGPT, as well as the related GPT-3.5 models, were trained on a high-performance Azure AI supercomputing infrastructure.

- While ChatGPT possesses many strengths, being a generalized model, it may not always be the most effective solution for narrower, more specialized topics with limited training data available. Moreover, the dialog interface has not yet been made available by OpenAI for businesses to integrate.

[OpenAI Python Library Repo](https://github.com/openai/openai-python)

[OpenAI Python Library Website](https://platform.openai.com/docs/libraries)


# GPT-3
- In 2020, the Generative Pre-trained Transformer 3 (GPT-3) was introduced as an autoregressive language model capable of generating high-quality text that resembles human writing. The GPT-3 is the third generation of the GPT language models made available by OpenAI.

- By providing an initial prompt as input, GPT-3 has the ability to produce a continuation of the text that follows the style and structure of the input prompt. The model is capable of performing a range of tasks, including but not limited to text classification, question answering, text generation, text summarization, named-entity recognition, and language translation.


# ChatGPT Methods

- We trained this model using Reinforcement Learning from Human Feedback (RLHF), using the same methods as [InstructGPT](https://openai.com/blog/instruction-following/), but with slight differences in the data collection setup. We trained an initial model using supervised fine-tuning: human AI trainers provided conversations in which they played both sides—the user and an AI assistant. We gave the trainers access to model-written suggestions to help them compose their responses. We mixed this new dialogue dataset with the InstructGPT dataset, which we transformed into a dialogue format.

- To create a reward model for reinforcement learning, we needed to collect comparison data, which consisted of two or more model responses ranked by quality. To collect this data, we took conversations that AI trainers had with the chatbot. We randomly selected a model-written message, sampled several alternative completions, and had AI trainers rank them. Using these reward models, we can fine-tune the model using [Proximal Policy Optimization](https://openai.com/blog/openai-baselines-ppo/). We performed several iterations of this process.

- ChatGPT is fine-tuned from a model in the GPT-3.5 series, which finished training in early 2022. You can learn more about the 3.5 series [here](https://beta.openai.com/docs/model-index-for-researchers). ChatGPT and GPT 3.5 were trained on an Azure AI supercomputing infrastructure.


# ChatGPT Limitations
- ChatGPT sometimes writes plausible-sounding but incorrect or nonsensical answers. Fixing this issue is challenging, as: during RL training, there’s currently no source of truth; training the model to be more cautious causes it to decline questions that it can answer correctly; and supervised training misleads the model because the ideal answer [depends on what the model knows](https://www.alignmentforum.org/posts/BgoKdAzogxmgkuuAt/behavior-cloning-is-miscalibrated), rather than what the human demonstrator knows.

- ChatGPT is sensitive to tweaks to the input phrasing or attempting the same prompt multiple times. For example, given one phrasing of a question, the model can claim to not know the answer, but given a slight rephrase, it can answer correctly.

- The model is often excessively verbose and overuses certain phrases, such as restating that it’s a language model trained by OpenAI. These issues arise from biases in the training data (trainers prefer longer answers that look more comprehensive) and well-known over-optimization issues.

- Ideally, the model would ask clarifying questions when the user provided an ambiguous query. Instead, our current models usually guess what the user intended.

- While we’ve made efforts to make the model refuse inappropriate requests, it will sometimes respond to harmful instructions or exhibit biased behavior. We’re using the [Moderation API](https://openai.com/blog/new-and-improved-content-moderation-tooling/) to warn or block certain types of unsafe content, but we expect it to have some false negatives and positives for now. We’re eager to collect user feedback to aid our ongoing work to improve this system.

# Model index
- Our models are used for both research purposes and developer use cases in production. Researchers often learn about our models from papers that we have published, but there is often not a perfect match between what is available in the OpenAI API and what is published in a paper.

- The purpose of this page is to help clarify:

  - Some of the differences in the ways that our models are trained, which impact the comparisons that can be made between models, and various evaluation results.
  - The differences between various model series, such as GPT 3.5 and InstructGPT.
  - Which if any of the models available in the API today match a model in a paper? In some cases, there might not be a match.

# Models referred to as "GPT 3.5"
- GPT-3.5 series is a series of models that was trained on a blend of text and code from before Q4 2021. The following models are in the GPT-3.5 series:

  - code-davinci-002 is a base model, so good for pure code-completion tasks
  - text-davinci-002 is an InstructGPT model based on code-davinci-002
  - text-davinci-003 is an improvement on text-davinci-002


# TRAINING METHOD	MODELS
  - SFT
    - Supervised fine-tuning on human demonstrations	davinci-instruct-beta1

  - FeedME
    - Supervised fine-tuning on human-written demonstrations and on model samples rated 7/7 by human labelers on an overall quality score	text-davinci-001, text-davinci-002, text-curie-001, text-babbage-001

  - PPO
    - Reinforcement learning with reward models trained from comparisons by humans	text-davinci-003

#### The SFT and PPO models are trained similarly to the ones from the [InstructGPT paper](https://arxiv.org/abs/2203.02155). FeedME (short for "feedback made easy") models are trained by distilling the best completions from all of our models. Our models generally used the best available datasets at the time of training, and so different engines using the same training methodology might be trained on different data.


### [Model index for researchers](https://platform.openai.com/docs/model-index-for-researchers)


### [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)

- Making language models bigger does not inherently make them better at following a user's intent. For example, large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user. In other words, these models are not aligned with their users. In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback. Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model behavior, which we use to fine-tune GPT-3 using supervised learning. We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback. We call the resulting models InstructGPT. In human evaluations on our prompt distribution, outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters. Moreover, InstructGPT models show improvements in truthfulness and reductions in toxic output generation while having minimal performance regressions on public NLP datasets. Even though InstructGPT still makes simple mistakes, our results show that fine-tuning with human feedback is a promising direction for aligning language models with human intent.


# Advantages and Disadvantages of ChatGPT

#### Advantages:
1. Imitates Human Conversation
    - The core feature of ChatGPT centers on providing human-like conversation based on user-placed queries or commands. It is generally similar to virtual assistant technologies and software applications such as Siri from Apple and Alexa from Amazon. However, considering its capabilities, it mimics real-life conversation because it is based on more advanced supervised learning and reinforcement learning using large language models.
    

2. Built Based on GPT-3 Model
    - GPT-3 or Generative Pre-trained Transformer 3 is an autoregressive language and language prediction model developed by OpenAI. It is the largest non-sparse language model and has been considered one of the most important AI systems ever produced. The quality of texts it generates makes it difficult to ascertain whether or not it is written by a human.
    

3. Expansive Applications and Benefits
    - The chatbot is versatile. It can write outputs similar to commercial AI copywriters. Experiments have shown that it can even compose music and produce works of fiction such as short stories. It can help content creators or technical writers produce an outline. The chatbot can also summarize, digest, and explain large bodies of text. Another interesting application of ChatGPT is that it can also write and debug computer programs.
    

4. Open For Further Fine-Tuning
    - Another advantage of ChatGPT is that its responses and overall performance can be fine-tuned. It banks on existing large language models while also having room for further improvements through active training using supervised learning and reinforcement learning. A user can upvote or downvote a particular response while also providing additional feedback.
    

#### Disadvantages:
1. Inaccuracies and Ambiguities
    - One of the biggest criticisms and limitations of ChatGPT is that it sometimes tends to produce texts that sound plausible or convincing but are incorrect or nonsensical under the surface. This phenomenon is called “hallucination,” and it is common in language models. Furthermore, when it comes to obtaining information, it does not provide references or citations. Using this chatbot alone for research purposes and electronic trailing is not ideal.
    

2. Limited Knowledge of Recent Events
    - The version launched in November 2022 can only provide information about events occurring in 2021 and earlier. It will soon provide more recent events as it continues to feed on data based on human-generated texts. Nevertheless, considering this drawback, users should keep in mind that it has limited knowledge of facts because it uses datasets that are not updated.
    

3. Ethical Issues and Concerns
    - Another disadvantage of ChatGPT is that it has been subjected to scrutiny. Several educational institutions have banned its use. Researchers and creatives have worried about copyright infringement because their outputs are based on human-generated texts. It also raises the question of whether it is ethical to use it as a substitute for services that require human interactions, such as customer service representation and even therapeutic counseling.
    

4. Other Possible Legal Implications
    - GPT was built with data from the Common Crawl dataset which contains copyrighted materials from publishing companies and individual authors, and researchers. Experts have also warned that AI-based applications can be used for cybercriminal activities. ChatGPT and other derivatives face legal uncertainties and possible compliance costs.


# ChatGPT Heralds an Intellectual Revolution

- Generative artificial intelligence presents a philosophical and practical challenge on a scale not experienced since the start of the Enlightenment.

- The new technology is known as generative artificial intelligence; GPT stands for Generative Pre-Trained Transformer. ChatGPT, developed at the OpenAI research laboratory, is now able to converse with humans. As its capacities become broader, they will redefine human knowledge, accelerate changes in the fabric of our reality, and reorganize politics and society.

- Generative AI will similarly open revolutionary avenues for human reason and new horizons for consolidated knowledge. But there are categorical differences. Enlightenment knowledge was achieved progressively, step by step, with each step testable and teachable. AI-enabled systems start at the other end. They can store and distill a huge amount of existing information, in ChatGPT’s case, much of the textual material on the internet and a large number of books—billions of items. Holding that volume of information and distilling it is beyond human capacity.

- AI’s capacities are not static but expand exponentially as technology advances. Recently, the complexity of AI models has been doubling every few months. Therefore, generative AI systems have capabilities that remain undisclosed even to their inventors. With each new AI system, they are building new capacities without understanding their origin or destination. As a result, our future now holds an entirely novel element of mystery, risk, and surprise.

- The ability of large language models to generate humanlike text was an almost accidental discovery. These models are trained to be able to predict the next word in a sentence, which is useful in tasks such as autocompletion for sending text messages or searching the web. But it turns out that the models also have the unexpected ability to create highly articulate paragraphs, articles, and in time, perhaps books.

- ChatGPT’s answers, statements, and observations appear without an explanation of where they came from and without an identifiable author. On its face, ChatGPT has no discernible motive or bias. Its outputs are complex, but its work is astonishingly rapid: In a matter of seconds, it can produce answers that coherently explain a high-level topic. They are not simply copied from the text in the computer’s memory. They are generated anew by a process that humans are unable to replicate. It is able to incorporate hypotheticals and non-obvious psychological inferences. It can prioritize among billions of data points to select the single set of 200 words that is most relevant (or will appear most relevant to a human reader). In its own words, it makes probabilistic judgments about future outcomes, blending information from discrete domains into an integrated answer. It appears to accept contrary views, presenting them as simultaneously compatible. It imitates other writing without copying it. Even though the model is incapable of understanding in the human sense, its outputs reflect an underlying essence of human language.

- The biggest of these models are expensive to train—north of $1 billion per model. Once trained, thousands of computers work 24 hours a day to operate them. Operating a pretrained model is cheap compared with the training itself, and it requires only capital, rather than capital and computing skill. Still, paying for exclusive use of a large language model remains outside the bounds of most enterprises. These models’ developers are likely to sell subscriptions, so that a single model will serve the needs of many thousands of individuals and businesses. As a result, the number of very large language models in the next decade may be relatively constrained. Design and control of these models will be highly concentrated, even as their power to amplify human efforts and thought becomes much more diffuse.

- The lack of citations in ChatGPT’s answers makes it difficult to discern truth from misinformation. We know already that malicious actors are injecting reams of manufactured “facts,” and increasingly convincing deepfake images and videos, into the internet—that is to say, into ChatGPT’s present and future learning set. Because ChatGPT is designed to answer questions, it sometimes makes up facts to provide a seemingly coherent answer. That phenomenon is known among AI researchers as “hallucination” or “stochastic parroting,” in which an AI strings together phrases that look real to a human reader but have no basis in fact. What triggers these errors and how to control them remain to be discovered.

### You can refer to this [link](https://www.wsj.com/articles/chatgpt-heralds-an-intellectual-revolution-enlightenment-artificial-intelligence-homo-technicus-technology-cognition-morality-philosophy-774331c6) to read this interesting and rich article in full from WSJ.
