# Create your own ChatGPT

# Introduction
- ChatGPT (Chat Generative Pre-trained Transformer) is an AI-powered chatbot created by [OpenAI](https://openai.com/) that enables users to have highly sophisticated, human-like conversations. The language model is capable of answering questions and assist in various tasks, including writing emails, essays, and code. Due to its dialogue design, ChatGPT is capable of answering follow-up questions, acknowledging errors, questioning incorrect assumptions, and declining inappropriate requests.

- The ChatGPT model was fine-tuned from a model in the GPT-3.5 series, which completed its training in early 2022. The ChatGPT as well as the related GPT-3.5 models were trained on a high-performance Azure AI supercomputing infrastructure.

- While ChatGPT possesses many strengths, being a generalized model, it may not always be the most effective solution for narrower, more specialized topics with limited training data available. Moreover, the dialog interface has not yet been made available by OpenAI for businesses to integrate.

[OpenAI Python Library Repo](https://github.com/openai/openai-python)

[OpenAI Python Library Website](https://platform.openai.com/docs/libraries)


# GPT-3
- In 2020, the Generative Pre-trained Transformer 3 (GPT-3) was introduced as an autoregressive language model capable to generate high-quality text that resembles human writing. The GPT-3 is the third generation of the GPT language models made available by OpenAI.

- By providing an initial prompt as input, GPT-3 has the ability to produce a continuation of the text that follows the style and structure of the input prompt. The model is capable of performing a range of tasks, including but not limited to, text classification, question answering, text generation, text summarization, named-entity recognition, and language translation.


# ChatGPT Methods

- We trained this model using Reinforcement Learning from Human Feedback (RLHF), using the same methods as [InstructGPT](https://openai.com/blog/instruction-following/), but with slight differences in the data collection setup. We trained an initial model using supervised fine-tuning: human AI trainers provided conversations in which they played both sides—the user and an AI assistant. We gave the trainers access to model-written suggestions to help them compose their responses. We mixed this new dialogue dataset with the InstructGPT dataset, which we transformed into a dialogue format.

- To create a reward model for reinforcement learning, we needed to collect comparison data, which consisted of two or more model responses ranked by quality. To collect this data, we took conversations that AI trainers had with the chatbot. We randomly selected a model-written message, sampled several alternative completions, and had AI trainers rank them. Using these reward models, we can fine-tune the model using [Proximal Policy Optimization](https://openai.com/blog/openai-baselines-ppo/). We performed several iterations of this process.

- ChatGPT is fine-tuned from a model in the GPT-3.5 series, which finished training in early 2022. You can learn more about the 3.5 series [here](https://beta.openai.com/docs/model-index-for-researchers). ChatGPT and GPT 3.5 were trained on an Azure AI supercomputing infrastructure.


# ChatGPT Limitations
- ChatGPT sometimes writes plausible-sounding but incorrect or nonsensical answers. Fixing this issue is challenging, as: during RL training, there’s currently no source of truth; training the model to be more cautious causes it to decline questions that it can answer correctly; and supervised training misleads the model because the ideal answer [depends on what the model knows](https://www.alignmentforum.org/posts/BgoKdAzogxmgkuuAt/behavior-cloning-is-miscalibrated), rather than what the human demonstrator knows.

- ChatGPT is sensitive to tweaks to the input phrasing or attempting the same prompt multiple times. For example, given one phrasing of a question, the model can claim to not know the answer, but given a slight rephrase, can answer correctly.

- The model is often excessively verbose and overuses certain phrases, such as restating that it’s a language model trained by OpenAI. These issues arise from biases in the training data (trainers prefer longer answers that look more comprehensive) and well-known over-optimization issues.

- Ideally, the model would ask clarifying questions when the user provided an ambiguous query. Instead, our current models usually guess what the user intended.

- While we’ve made efforts to make the model refuse inappropriate requests, it will sometimes respond to harmful instructions or exhibit biased behavior. We’re using the [Moderation API](https://openai.com/blog/new-and-improved-content-moderation-tooling/) to warn or block certain types of unsafe content, but we expect it to have some false negatives and positives for now. We’re eager to collect user feedback to aid our ongoing work to improve this system.

# Model index
- Our models are used for both research purposes and developer use cases in production. Researchers often learn about our models from papers that we have published, but there is often not a perfect match between what is available in the OpenAI API and what is published in a paper.

- The purpose of this page is to help clarify:

  - Some of the differences in the ways that our models are trained, which impacts the comparisons that can be made between models, and various evaluation results.
  - The differences between various model series, such as GPT 3.5 and InstructGPT.
  - Which if any of the models available in the API today match with a model in a paper. In some cases, there might not be a match.

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
