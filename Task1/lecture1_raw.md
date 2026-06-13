# CS25 Lecture 1: llm01 - 原始转录文本

## 音频信息

- 来源：Stanford CS25 Transformers United V6
- 时长：1小时41分钟53秒
- 模型：small
- 总片段数：789

## 完整文本（带时间戳）

[00:00:00] Cool. Hello everyone and welcome to CME 295, Transformers and large language models.

[00:00:13] So my name is Afshin and I will be teaching this class with Sherwin who's in the back.

[00:00:19] And before I start, I'm just going to introduce ourselves. So we're twin brothers and we actually

[00:00:28] had kind of a similar background. So we both went to a school in France called

[00:00:33] Saint-Paul-Paris and then we each went our way. So on my end I went to MIT and then Sherwin went

[00:00:40] to Stanford to do the CME Masters program. And after that, I guess our industry background is

[00:00:49] very similar as well. So I first went to Uber and then Sherwin came to Uber as well and then

[00:00:55] Sherwin left to Google and I went to Google. And then very recently I joined Netflix and Sherwin

[00:01:01] joined Netflix as well and we've been working on large language models. So yeah, I guess we have

[00:01:08] like technical backgrounds and mostly oriented towards LLMs. Okay, so why are we doing this class?

[00:01:17] So since 2020, Sherwin and I have been specializing in NLP and we've been giving this class

[00:01:24] in the format of a workshop that was done in a yearly basis. So in 2021, 2022, 2023, 2024,

[00:01:33] child GPD came in 2022 and suddenly there was a lot of interest for LLMs. And so it's actually

[00:01:41] last spring that we started to offer this class as a Stanford course that is now called CME295.

[00:01:51] And this is the second instance. So what can you expect from this class? So first of all,

[00:02:01] LLMs are basically everywhere now. And I guess our goal here is twofold. So the first one is

[00:02:10] to learn about the underlying mechanism that makes all this work. And we're going to see the

[00:02:16] transformer, which is the foundational architecture that makes all this work. And then the second

[00:02:23] thing is to know how these LLMs are trained and where they are applied. So in case you're still

[00:02:32] wondering if this class is good for you, I would say that this class is great for people who just

[00:02:39] in general have an interest in this field, either because you wanted to make it your

[00:02:46] career goal, if you want to be a research scientist or an ML scientist, or if you want to

[00:02:53] develop like a personal project that relies on LLMs to some extent, to just like knowing the

[00:02:59] caveats, I guess what works, what doesn't. Or just say if you're in a separate field

[00:03:05] and you just want to know how this whole AI, JNAI, LLMs thing works and how you can apply it to your

[00:03:12] domain. Okay, so now in terms of prerequisites, I would say that at a very minimum, you should have

[00:03:22] some foundations in ML, like basically know whether how a model is trained, what a neural network is,

[00:03:31] and also some basics in linear algebra, so basically how matrices are multiplied, for instance.

[00:03:39] But even if you have kind of a developing, I guess, competency in these fields, I guess it's fine,

[00:03:46] we still be here to help you out. I guess this is like the ideal set of prerequisites.

[00:03:52] Cool, so still on the logistics, so this class will be held every Friday from

[00:04:02] 3.30 to 5.20, and it will be held here.

[00:04:09] So this class is two units, and you have the choice to either take it as a letter or a credit, non-credits.

[00:04:18] So as you could tell from the setup, we're basically recording this class,

[00:04:23] and if you cannot, for some reason, attend this time, this slot, we'll make sure we're driven to

[00:04:31] make the recordings available either tonight, like every Friday night or on Saturday.

[00:04:38] So in terms of the grades, so what we're doing for this quarter is to have two exams,

[00:04:47] so one is the midterm, which will be happening during our fifth instance, which is October 24th.

[00:04:56] And then the second exam will be the final exam, which will be held in the week of December 8th,

[00:05:05] so the date is still TBD, so we'll let you know.

[00:05:10] Cool, so every time we have a lecture, we'll be posting the slides and the recordings on the website,

[00:05:21] and in case you're interested, we also have the syllabus in there, so you can know a little bit

[00:05:26] what are the topics that we'll be talking about, and the class textbook is the Super Study Guide,

[00:05:34] Transformer and LMS, so we have a copy here in case you want to take a look.

[00:05:39] So yeah, I guess a lot of the concepts that we have in this class will actually be in the book,

[00:05:44] so I guess it's a helpful way to follow this as well.

[00:05:50] And also we did some kind of very short condensed version of the school class that we called

[00:05:57] the VIP Cheat Sheets, so this one is available on GitHub in case you're interested, and yeah,

[00:06:04] also translated into a number of languages now.

[00:06:07] By the way, if your language is not there, let us know, and yeah, happy to work on that as well together.

[00:06:16] Okay, cool. I think it's the last things on the logistics part, so in terms of announcements,

[00:06:21] we'll be posting things on Canvas. In case you have any questions, you can of course reach out to us,

[00:06:27] but there is also a tab on Canvas that's called EDD, I'm sure you're familiar.

[00:06:34] So you just click on that, just post your question, and then Shervin and I will be responding.

[00:06:41] And yeah, I guess to reach out to us, you have this mailing list, or just like,

[00:06:46] you know, we're just two, so just fingers.

[00:06:51] Cool, so on the logistics, do we have any questions so far? And one thing I forgot to mention

[00:06:57] is that given that we're recording this class,

[00:07:00] I guess if you're asking a question, it may not be super clear for the viewer what your question was,

[00:07:08] so I'm going to make an effort to just repeat your question. It will sound weird, but yeah,

[00:07:13] try to not forget. But yeah, so yeah, any questions so far on the logistics?

[00:07:21] Yeah.

[00:07:23] So the question is whether they're like coding parts in the exams, so the answer is no.

[00:07:34] So the exams will purely focus on concepts that we see in class, and actually it's not meant to,

[00:07:40] you know, trap you. So I guess if you follow the class, if you know, you see the slides and like

[00:07:45] the concepts that we see should be fine. Yeah.

[00:07:53] Oh yeah, the question is if you're waitlisted, what do you do? I think, so by experience, you know,

[00:07:59] a lot of people will kind of finalize their schedule, some people will drop, some won't.

[00:08:04] In case you're still waitlisted, you know, come talk to us, but I'm pretty confident,

[00:08:08] you know, it's going to be okay because I think the waitlist right now is like six.

[00:08:12] So yeah, things should be fine. Cool. Yeah.

[00:08:17] They will be on the websites and we'll make sure to also post it in Canvas.

[00:08:23] Yeah. So the question was where the slides and they're on the websites. Cool. Yeah.

[00:08:39] So question is on the waiting of the exams. So yeah, there is no homework.

[00:08:44] So 50% is midterm, 50% is final and no grades, I mean, no wait are from that.

[00:08:52] And in particular, I mean, if this slide is conflicting with something,

[00:08:56] just keep in mind that we are recording this. So it's fine if you, if you cannot attend,

[00:09:02] let's say, yeah. Sorry.

[00:09:07] Oh, is the question that the final is about just a second half of the class?

[00:09:16] We've not, we have not written the exam yet, but I think this is something we're thinking of.

[00:09:21] So yeah, the final is probably going to be the second half, about the second half of the topics.

[00:09:29] Cool. Okay. Long story short, 50% midterm, 50% exam, final exam,

[00:09:36] and yeah, it's a fun class. Cool. So with that, I'm going to just slowly start the class.

[00:09:44] So another thing that I want to mention was every time we're talking about something,

[00:09:49] you will see that at the bottom of the slide, there will be a source. It's mostly for, so first

[00:09:54] to credits whatever we're voting, but also for you to kind of dig into those material a little

[00:10:02] bit more in case you're interested, because of course we have only like two hours per week

[00:10:07] and we're going to have nine or 10 weeks. So there's nowhere near the, you know, enough time for us

[00:10:13] to cover everything. And the second disclaimer is you will see that the field is full of

[00:10:21] abbreviations. So I myself was completely scared of them when I started, but hopefully by the end

[00:10:29] of the class, you will have a mental mapping of what these abbreviations mean, respect to what

[00:10:34] they correspond to. So yeah, so if you have that mental mapping towards the end of the class, then

[00:10:39] we'll know we did a good job. So with that, let's start. And I guess we will start at the very

[00:10:48] high level, because I would just assume that, I guess we're starting from scratch. And we're going

[00:10:57] to talk about NLP in general. So NLP is going to be our first abbreviation. So NLP stands for

[00:11:04] natural language processing. And it is a field that is around like manipulating texts, just

[00:11:12] computing things with text. And at a very high level, can basically classify NLP tasks into three

[00:11:20] buckets. So the first bucket is what we call classification. So we have an input text as an

[00:11:29] input. And then what we want is to predict something. So one example is you have a movie review, and

[00:11:38] you want to predict whether the sentiment is positive, negative or neutral. So that's one

[00:11:44] example. You can also have intent detection, just knowing what, for instance, the person

[00:11:51] wants to do. So let's suppose you say, I want to create an alarm for tomorrow. So the intent here

[00:11:56] is create an alarm. So also to detect the language. So for instance, if you write in French, you want

[00:12:03] to detect that text is in French. Topic modeling. The second category is what we call multi-classification.

[00:12:14] So we still have a text as input. But this time, we predict more than one thing.

[00:12:21] So you have a number of tasks in that bucket as well. So one that is very popular is called

[00:12:27] named entity recognition, aka NER. So what that task does is, given an input text,

[00:12:37] we want to basically label some specific words, like for instance, identifying whether something

[00:12:43] is a location or a time and so on. And then you have some other tasks as well that are a little

[00:12:51] bit more on the linguistic side. I think they're less trending now, but I guess 10 years ago,

[00:12:56] it was something that people would study a lot. So part of speech tagging, which is about just

[00:13:02] figuring out which word is a noun, a verb, etc. Or some parsing related tasks, so dependency

[00:13:10] or constituency parsing. And then the last bucket, which is very popular these days,

[00:13:18] is the generation bucket. So you have the text as inputs, and you also have text as outputs.

[00:13:28] And here the length can be variable, meaning you don't know what the length of your output text will

[00:13:34] be beforehand. So here you have several tasks. So for instance, you have machine translation,

[00:13:40] so for instance, something in English, and I wanted to let's say German question answering. So

[00:13:46] typically, you know, the chat GPT, Gemini that you're using, you know, the system. So you ask a

[00:13:51] question and you have a response. And then you have like other tasks as well, like summarization,

[00:13:58] you want to summarize an article, let's say, or just generate something. So something can be

[00:14:03] generate codes, generate a poem, can also be a lot of things. Cool. So now what we will do

[00:14:13] is go through these tasks one by one to just illustrate what people typically handle with.

[00:14:21] So we're going to start with the first bucket, which is the classification bucket.

[00:14:27] And here we're going to illustrate this with the sentiment extraction task.

[00:14:32] So let's suppose we have a sentence, this teddy bear is so cute, we want our model to predict,

[00:14:39] you know, this to be a positive sentiment. But typically what you would use is, you know,

[00:14:45] datasets that are around sentiment extraction datasets. So I mentioned movie reviews. So this is

[00:14:51] IMDB critics, but you also have reviews about products, Amazon reviews, or, you know, tweets.

[00:14:58] Now I guess it's called X. So X posts. And the way you would evaluate such outputs would be by

[00:15:07] typically using traditional classification metrics. So you have accuracy, which is, you know, how many

[00:15:16] what is the percentage of the observations that you correctly predicted.

[00:15:21] But you also have two key metrics, which I'm just going to remind, I'm not sure if everyone knows

[00:15:27] about them. So one is precision, which is out of all the positive predictions that you made,

[00:15:34] which ones were correct. And then the second one is recall. Out of all the true labels,

[00:15:43] how many of them did you correctly predict as being positive? And you have this metric called

[00:15:49] the F1 score, which basically takes the harmonic mean of precision and recall to just give you one

[00:15:55] number. So now you may wonder, you know, why do you need all these metrics? So the short answer

[00:16:02] is that sometimes you have tasks and datasets where your classes are very in balance. So for instance,

[00:16:11] you can have 99% of your dataset that is positive label, and then only 1% of the dataset, which is

[00:16:18] negative. And so here, if you take like a metric like accuracy, it can be very misleading. Because

[00:16:26] if you have a model that would predict everything as the majority class, then you would have a great

[00:16:33] classifier, but it's not the case. So that's why precision and recall really play a role.

[00:16:38] So that's what the first one. Okay, so now let's move to the second category of NLP tasks. So this

[00:16:48] one is the multi classification category. So you have an input text, and you predict multiple things.

[00:16:55] And we're illustrating this with the NER task, which as I mentioned, is about identifying the

[00:17:04] category of given words. And so here, for instance, we want to identify teddy bear as being an entity.

[00:17:13] I guess for that, you would use classification metrics, but not at the sentence level, but more

[00:17:21] either at the token level or at the entity type level. And by that, I mean, let's suppose you

[00:17:28] have a category, let's say location, and you want to know how well you're predicting words in that

[00:17:36] category. So you would typically aggregate these metrics as a function of that. Cool.

[00:17:47] Okay, let's go to the last category, which is, as I mentioned, the most popular one. So this one is

[00:17:53] text in, text out. So I'm illustrating this with the machine translation task, which is around

[00:18:02] translating a text from a source language to a target language. So here you have the example with

[00:18:08] English to French. So cute teddy bear is reading, nooghsant peluche mignon li. So for that, I guess

[00:18:16] it's harder to get data sets because here you need to have pairs of text. So you have a very popular

[00:18:25] data set that's called WMT, which stands for workshop on machine translation. And that one

[00:18:32] contains a bunch of paired sequences in different languages. So for instance, you have the English,

[00:18:39] French, English, German coming from the European Parliament data set, for instance.

[00:18:45] Okay, so to evaluate those, to evaluate the performance of your model, it's actually a lot more

[00:18:52] tricky because as you can imagine, you can have many different ways to translate something. I'm sure

[00:19:00] many of us in the room are bilingual, trial and trailing. So yeah, that's what is making this

[00:19:09] hard. So in the past, people have used several rule based metrics to do that. So one that you may

[00:19:19] have heard is blue. Blue stands for bilingual evaluation under study. And it is a measure of how

[00:19:30] well your translation stands with respect to a reference text. Same story for rouge, which is

[00:19:39] actually a suite of metrics, but captures that in a different way. And you will see that the

[00:19:47] machine learning community is funny because blue, I'm not sure if you know, French means blue, but

[00:19:52] rouge means red. So yes, they try to kind of add some fun in this. But the problem with these metrics

[00:20:02] is that you always need a reference text. So you basically need labels. And in practice,

[00:20:11] having labels is very cost expensive. It takes a lot of time, a lot of money to get labels.

[00:20:21] And we will see later in the class that with the progress that we have made in the LLM space,

[00:20:27] or that the community has made in the LLM space, we can actually forego of these reference based

[00:20:34] metrics and go towards a more reference free kind of metrics. And we will see that later on.

[00:20:43] And then the last metric that I will say that people sometimes use is called

[00:20:47] Proplexity. And Proplexity only looks at the probabilities that are out to buy the model.

[00:20:54] And it basically quantifies how surprised the model is by its output.

[00:21:02] So blue and rouge, the higher the better, the complexity, the lower the better.

[00:21:08] And I guess LLMs have been kind of a hot topic since 2022. But actually, the field goes way back,

[00:21:22] way before that year. So in the 80s, we'll see it in a second. But there's a class of models that

[00:21:31] were actually kind of third of, even in the 80s. And the 90s, we had LLMs that we'll see also in

[00:21:39] a second. But the problem was during that time, we didn't have the internet, we didn't have a lot of

[00:21:46] compute. And I guess this was one of the limiting factors which prevented these models from like

[00:21:53] the models from today from being trained. And then more recently, we've had several advances. So

[00:22:00] World2Vec was really one of the kind of pioneering work in just computing meaningful embeddings.

[00:22:10] And we'll see it in a second. And then of course, we had the Transformers, which were part of a

[00:22:16] paper that was published in 2017, which is basically at the foundation of the models that you see today.

[00:22:23] And then these models, they just were scaled up both by compute, but also in terms of the data

[00:22:32] that was used to train them. And that's how LLMs were dubbed. And I guess these are more like the

[00:22:39] 2020s. But yeah, I guess we'll see those. Cool. Any questions on, I guess, the high level?

[00:22:51] Cool. Everyone good? Cool. So I guess the first question that I want to ask ourselves is

[00:23:04] what we want to do is to have a model that handles text. But models, they understand numbers, they

[00:23:11] don't really understand text. So we need to somehow do something with that text to make it more

[00:23:19] quantifiable, something that a model can understand. So if you look at a sentence, for instance,

[00:23:26] a cute teddy bear is reading, you first need to ask yourself, how can you cut

[00:23:34] this sentence to pass it to a model? So this part is called tokenization. And what it entails is

[00:23:44] basically cutting the text with respect to some arbitrary unit of text.

[00:23:52] So there are several ways of doing this. I guess the first way is doing it completely arbitrarily.

[00:23:58] So here, for instance, you would have A that would be one unit of text,

[00:24:03] cute would be another unit of text, teddy bear would be another one and so on.

[00:24:09] And by the way, the unit of text is called a token, which is why the method is called tokenization.

[00:24:19] Another way would be to just separate by words.

[00:24:25] But I guess we would have always pros and cons. I guess one of the goals that we want to achieve

[00:24:33] is for us to then be able to represent these tokens in a meaningful way.

[00:24:40] So one con with doing this at the word level is you will end up with words that look similar,

[00:24:49] but that are actually considered as different tokens. And I guess the limitation here is you

[00:24:56] will need to compute embeddings for these similar yet different tokens and somehow make

[00:25:05] their embeddings similar. So I'll give you an example. So let's suppose I have the word bear

[00:25:12] and then you have another word plural form bears. So these two words, they are very similar. Just

[00:25:20] one is singular, the other one is plural. If we go ahead with the word level tokenization,

[00:25:27] then we will end up with just two different entities, which are basically just considered

[00:25:33] as different. Same with run and then runs, you know, variations of verbs. So for that reason,

[00:25:43] people have dug into a category of tokenizers that are called subword tokenizers,

[00:25:55] which is around leveraging roots of words in order to find where the common roots that we

[00:26:03] can find is in these words. For instance, for bear and bears, you would have the bear particle that

[00:26:09] would be kind of shared. And so I guess the pro is that you get to leverage the root of the words,

[00:26:18] but then the con here is that your sequence would be longer. And we will see why this is a con.

[00:26:28] I guess later on, I guess I can give you a preview. So the complexity of these models

[00:26:36] is also a function of the sequence length. So the more tokens you have to process,

[00:26:44] the more time it would take for your model to run, because it needs to basically process all these

[00:26:50] tokens. So that's one con. So pro is it leverages the root of words. Con is it just makes your

[00:27:01] sequences longer. Okay, you have a last category of ways of tokenizing things,

[00:27:09] which is just going at the character level, just like taking all characters. So here,

[00:27:16] I guess you and I, when you write a message, we typically have sometimes misspellings.

[00:27:24] And with the sub word way of tokenizing things, you may not be able to recognize the word that has

[00:27:34] been misspelled. And this is something that the character level tokenizer can, I guess,

[00:27:41] take into consideration. But here, the problem is you have a sequence length that's much, much

[00:27:47] longer, which will make your model, I guess, take much more time to process the sequence.

[00:27:54] So that's one con. And then the other con is, I guess, when you want to represent each of these

[00:28:01] tokens, I guess, it's very hard to know what a representation of a letter really means.

[00:28:08] Like, what does the representation of the letter you mean? Very hard.

[00:28:17] Cool. So I have just a quick recap. So word level is a super naive way, super simple way of,

[00:28:27] I guess, dividing your text into arbitrary units. But then the problem is, as we mentioned,

[00:28:34] we do not leverage the root of words. And I did not mention this, but there's a term.

[00:28:41] Whenever you cut something, and then at inference time, when you want to make a prediction,

[00:28:49] I guess one prerequisite that you have is that you need to have the token

[00:28:56] that you saw at training time. You need to have it in your training sets.

[00:29:02] And the problem is, let's suppose at inference time, you cut your text into words. And let's

[00:29:09] suppose you have not seen a word at training time, you will need to mark it as unknown.

[00:29:16] And so this thing is called OOV out of vocabulary.

[00:29:21] So luckily, the subword level tokenizer mitigates that problem. So you have

[00:29:28] like a lower risk of OOV, but still you can have. And as we mentioned in terms of the pro,

[00:29:36] you leverage the root of the words. And then character level is robust to our misspellings

[00:29:46] and our casing errors. But the problem is, it makes computations just much slower. And your

[00:29:53] sequences would be very, very long, which will also make your inference time much higher.

[00:30:01] That sounds good. I guess this is really the foundation of how to handle things with text.

[00:30:08] But yeah, it doesn't make sense overall. Cool. Okay. So now, okay, what we did is we took

[00:30:19] an input text. What we did is we cut it into parts that are basically tokens.

[00:30:26] So in order for our model to understand these tokens, we need to find a representation for

[00:30:33] each of them. So here we're going to take a look at this. So that's called word representation or

[00:30:39] more, I guess, more correct way it should be token representation. So we want to find a way to

[00:30:48] represent each of these tokens. So the simple and naive way to do this would be to just assign

[00:30:57] a one hot vector for each word or for each token. So for instance, let's suppose we have a vocabulary

[00:31:07] of three tokens, book, soft and teddy bears. We would have, let's say, soft, that is a 100 vector

[00:31:16] teddy bear that is, let's say, a 010 vector and book that is, let's say, a 001 vector.

[00:31:25] So this is called a one hot encoding OHE, we typically see. So cool. Yeah, this is a way

[00:31:35] to represent our tokens. But basically what people want to do is compare these tokens to

[00:31:43] basically see which ones are more similar to what other ones. So common similarity measure that

[00:31:52] people use is something called cosine similarity. I'm not sure if you have heard of it. So we can

[00:32:00] think of it as just seeing what angle these vectors make in the n dimensional space. And

[00:32:10] if, I guess they are pointing in the right, in the same direction, then maybe they're similar,

[00:32:15] maybe if they're orthogonal, maybe they're kind of independent. And if they're completely opposite,

[00:32:21] then maybe they're opposite. That's basically the mental model we want to go into. So the problem is

[00:32:30] if you represent your tokens in a one hot fashion, you will end up with all your vectors

[00:32:37] being orthogonal to one another. So that's the problem. So ideally what we want is for tokens

[00:32:47] that mean the same or similar to basically have a high similarity. And for tokens that are not

[00:32:57] similar, like on, like about different things to be more like orthogonal. So here I just,

[00:33:05] for illustrative purposes, teddy bears are soft. So you want teddy bear and soft to be,

[00:33:12] I guess, with a high similarity. And let's say teddy bear and book, which is kind of independent,

[00:33:17] you want them to be closer to zero. So that's what you want. That's what you have with one

[00:33:23] hot encoding. And that's what you want. Yeah. Sorry. Oh, I see. The question is why do you

[00:33:41] care about the norm? So I guess cosine similarity is actually normalized by norms. So it's that

[00:33:52] product. Oh, you mean why did I just put that product here instead of two?

[00:34:01] Oh, I see. And your question is why do we not care about the norm?

[00:34:06] Cool. I guess the viewers know the question. I guess these measures, they're all, you know,

[00:34:11] measures. There are all ways to try to capture these kind of similarity things.

[00:34:19] So I guess why do you not care about the norm? I guess it's how people have tried to kind of

[00:34:27] quantify that. I guess you will need to see how your vectors are trained and whether the norm

[00:34:35] would be indicative of something. I guess the best answer I can give you is, I guess this is a measure.

[00:34:42] This is not the perfect measure. Yeah. People may use also that product as a measure. But yeah,

[00:34:49] I don't have like a great answer for you. Cool. But as long as you capture, I guess, how these

[00:34:56] vectors, they're pointing, I guess typically what you care about is the angle between them.

[00:35:03] But yeah, typically you don't really take into consideration the norm.

[00:35:07] Cool. Any questions? Any other questions? Yep.

[00:35:21] Yep.

[00:35:27] Yep.

[00:35:29] Yep.

[00:35:38] It's a great question. So question is around size of vocabulary and how that would inform the

[00:35:44] choice respect to word, subword, and how that changes across languages. It's a great question.

[00:35:50] So I would say it really depends, first of all, on the tasks that you're trying to achieve. If your

[00:35:55] task is just about one language, you will just take that same language. You typically go with a

[00:36:01] subword tokenizer just because of the reasons that we mentioned here. So I guess subwords is

[00:36:09] a nice tradeoff between being able to identify words by their roots, like leveraging that,

[00:36:17] but also running less into the OOV risk. So in terms of the size, I know that people, they've,

[00:36:29] you know, like tried different things. I think typically for English, you would target something

[00:36:34] on the order of tens of thousands of vocabulary size. But you know, like nowadays, the models,

[00:36:43] they're a multilingual, they're also about codes. So you will see that the vocabulary size now is

[00:36:48] sometimes on the order of hundreds of thousands. Okay, so with respect to Chinese, so I guess you

[00:36:55] have this, you know, difference in characters that you're using. So for Latin, I guess it's the alphabet

[00:37:02] we're all accustomed to, but of course, for the other ones, you'd have something similar, but in,

[00:37:08] I guess, the target language character. So yeah, I would say order of magnitude, tens of thousands

[00:37:17] for one language, hundreds of thousands if it's like multilingual. Yeah, these are the order of

[00:37:23] magnitude that you want to target for. Cool, yeah. Great question. So a question is how do you get

[00:37:42] those embeddings? So it's actually the next slide. So we're going to talk about this.

[00:37:46] Great. So, okay, so now that we know that the one hot encoding is not a good way to represent tokens,

[00:38:00] what we want to do is to learn those embeddings from the data. So I mentioned that there was this,

[00:38:09] you know, paper that came out in the 2010s, so I think it was 2013, that was called word to

[00:38:14] vex. And the reason why it was so popular is because they showed a very intuitive and interpretable

[00:38:24] way of seeing these embeddings, because they were saying something like, okay, king is the queen,

[00:38:30] what this is to that, like Paris is to France, what Berlin is to Germany. So there was basically a way

[00:38:35] to make sense of the embeddings. So now the question is how did they do that?

[00:38:41] So they had two ways of computing these embeddings. So one way was called continuous bag of words,

[00:38:50] the other one was called skipgram, but they all rely on the same idea, which is let's just leverage

[00:38:59] text that we have and then try to predict something that is part of the text based on,

[00:39:07] let's say, the context. So for instance, continuous bag of words, the goal is you take into consideration

[00:39:16] the words that are around a given target words, and your goal is to predict that target words.

[00:39:25] And skipgram is kind of the opposite, you go from a target word and you want to predict

[00:39:32] the words that are around it. So I guess this task is commonly called a proxy task,

[00:39:39] because at the end of the day, in this exercise, what we care about is not necessarily to predict

[00:39:47] the next word or at least not yet. Our goal is to learn a representation of these words that are

[00:39:54] meaningful. And so here, the idea is, if you have a model that somehow knows how to predict,

[00:40:04] let's say, the next word, then it means that your model has some understanding of how language works,

[00:40:15] which is basically what you want. You basically want an embedding that is reflective of,

[00:40:22] I guess, what language is, which is king and queen or similar, Paris and France,

[00:40:30] like this is the capital. You want to have these associations embedded in the representation.

[00:40:39] And let's go through a very simple example of what that looks like.

[00:40:45] So here, in our example, let's suppose that our proxy task is about predicting the next word.

[00:40:55] So here, what we take is a very vanilla neural network model, which basically receives a vector

[00:41:06] of size V, has some multiplication and a bias term to get like hidden states. And then another set

[00:41:18] of multiplications to get our final vector. So here, it's basically a very simple neural network.

[00:41:28] So the input is of size V. The hidden layer is of size D, which is typically much smaller than

[00:41:36] the vocabulary. So vocabulary is typically like tens of thousands or hundreds of thousands. So D is

[00:41:40] typically hundreds, like 768, for instance, is one example of dimension. So it's much, much smaller.

[00:41:52] So what we're trying to do is to learn the word representation through this proxy task.

[00:41:59] And what we're going to do is try to consider the words as inputs and predict the next word.

[00:42:12] So let's go with the first word of the sequence. So by the way, I use token and words interchangeably.

[00:42:21] So let's suppose we have the word A, and we want to predict the next word, which is the word Q.

[00:42:29] So what we do is we take the word A, we take the one hot encoding representation,

[00:42:40] and we pass it through the network. So here, if you're familiar with neural networks,

[00:42:45] so here you have, I guess, a multiplication between, I guess, a matrix and this vector.

[00:42:51] So you have a hidden state representation, which is a vector of size D. So here, let's suppose it's

[00:42:59] 0.2 and 0.9. So D equal 2. And then you have, I guess, another pass here. And then you get,

[00:43:08] after your softmax, a set of probabilities, which are around seeing what is the next word.

[00:43:17] So in this example, we have a vocabulary of size six. So the first word is predicted with probability

[00:43:27] 0.2, second word 0.4, and then the other words are all 0.1 in this example.

[00:43:36] So let's suppose that we want to somehow be able to maximize our prediction to be the second word

[00:43:45] of the vocabulary, which is the 0.4. So we basically compare the prediction with, I guess,

[00:43:55] 0100, which is the representation of the second word of the vocabulary.

[00:44:01] And then we do the backprop, we update the weights. I'm not sure if everyone is familiar with that

[00:44:08] part, but the idea here is once you obtain a prediction, you compute the loss, so typically

[00:44:16] cross entropy, which will determine how far off you are from the true answer. And based on that

[00:44:26] difference, you're going to update the weights in order to make your prediction closer to the truth.

[00:44:34] So that's what you do. And then you repeat that process and suppose you take the word cute,

[00:44:42] which as we said is the second word in the vocabulary. So the one hot

[00:44:47] encoding representation is 0100. So you go through that network, you have a hidden state,

[00:44:58] like the vector is 0.8 and 0.4, you do that again. And what you want to do is to predict

[00:45:03] the next token. And here's teddy bear. And so you see now your model in this example

[00:45:11] is predicting the next word to be kind of like uniform, but you want to somehow

[00:45:16] maximize the probability for teddy bear. So you go back doing this again and again for all the words.

[00:45:23] And at the end of the day, you obtain a model that learns how to predict the next words,

[00:45:32] which is basically the proxy task. And what you're going to do is to take the representation

[00:45:38] that the model learns, which is the green units. So what happens now is every time you have a word,

[00:45:47] you just represent that as one hot encoding representation. And you just multiply this

[00:45:56] with these weights and then you obtain the green representation. And that is your word representation.

[00:46:09] Does that make sense? Yeah.

[00:46:26] Yeah. Great question. Yes. Great question. So the question is about what does V correspond to

[00:46:38] and why there's only six? So yes, in this example, we only have six possible words,

[00:46:44] which is basically the vocabulary size, just like very kind of a two example, because in

[00:46:49] practice, there's many more. So I guess that's one of the challenges with language. So you can

[00:46:57] technically have many variations of words, which is why if you take a word level way to divide your

[00:47:05] text into tokens, you can end up with the vocabulary that's like very big because you need to account

[00:47:11] for all the variations of given words. And the other thing that I want to point out is

[00:47:20] let's suppose you have a vocabulary size of six, and it's the six words that you saw at training

[00:47:24] time. But what happens is if at inference time, you have a word that you have not seen at training

[00:47:30] time. And so the answer for that is typically what people do is they reserve a spot for what they

[00:47:39] call an unknown token or out of vocabulary token, which basically can think of it as a bucket for

[00:47:50] everything that we were not able to identify. So if let's suppose that inference time, you have

[00:47:58] a token that you were not able to identify, they will all take that representation, which is the

[00:48:03] unknown token representation. And it's by the way something that I guess the word level tokenizer

[00:48:13] has kind of trouble to do because you will have a much bigger chance of having out of vocabulary

[00:48:19] tokens. Subword level will have a lower chance. And then character level, I guess you don't have

[00:48:26] that problem. Does that answer your question? Yeah. Great question. So first question is

[00:48:55] when do you know when you're done? So the thing with the proxy task is when you train your model,

[00:49:02] I guess your true objective is to not really learn, I mean in this case, to learn how to predict the

[00:49:07] next word. Your objective is to have meaningful representations. But what you can do is to somehow

[00:49:14] track the loss function for the proxy test that you're pursuing, but then also taking into consideration

[00:49:21] that this is not necessarily your end goal. So I guess one very reasonable way of going about doing

[00:49:29] this is just to wait until your model converges. So here what you do is you track the loss as a

[00:49:36] function of, so there's this term epoch, just how many times your model sees the training set.

[00:49:42] And so you compare these different curves. And when this converges, this is typically like a

[00:49:48] good time to stop the training process and just see if that makes sense. Depends on your downstream

[00:49:55] task, of course. But that's one. Okay, so your second question, sorry, can you repeat the second

[00:50:01] question? Yeah. Yeah. Oh, great question. So the question is how do you know when the generation

[00:50:22] stops? I guess like otherwise it will stop, it will never stop. So yeah, exactly. So you have

[00:50:27] some spatial tokens. Typically you have end of sequence, end of sequence. So typically when you

[00:50:33] have the end of sequence token generated, then it's when it stops. All right. So second question was

[00:50:43] what informs the size of the hidden layer? I would say it's a trade off. Because you want

[00:50:53] the embedding to be rich enough that it can be informative for your downstream task. So for

[00:50:59] instance, if you want to somehow get an embedding of let's say your sentence, and if you want to,

[00:51:05] let's say, do a very, very specialist task, super, you know, like with a lot of different outcomes,

[00:51:11] maybe you want a vector that recaptures that. So maybe you want a bigger vector. But if you

[00:51:17] have like a very simple task, maybe a smaller vector, it makes sense. So I guess the size of your

[00:51:24] hidden dimension also impacts the complexity of whatever you're running after. Because of course,

[00:51:32] if you have longer vectors, you'll have more computations. So your inference would be probably

[00:51:37] more expensive, et cetera. So I guess there's a lot of factors. So just to recap, one is how

[00:51:44] complicated your downstream task is. Second one is how sensitive are you with like latency, cost,

[00:51:51] all these things. So it's really a trade off. But out there, you would typically see embeddings of

[00:51:57] who have hundreds or thousands. Of course, you know, these models, they've been growing. So

[00:52:05] number may change. But that's the order of magnitude that you're looking at.

[00:52:08] Right. This is indeed empirical. Yeah. I guess you can also rely on what others found

[00:52:17] and just go from that. Yeah, but 768 and yeah, like these numbers are things that people typically

[00:52:23] did. Yeah. Cool. Yeah.

[00:52:30] Yeah.

[00:52:47] Yeah. The question is how can you distinguish words that are spelled the same, but in different

[00:52:54] contexts. So you're way ahead of me. So this is basically the basics. And we're going to tackle

[00:53:01] methods that can tackle these problems of just contextualizing the word in the sentence.

[00:53:08] So yeah. So we'll see that in a bit. Cool. Not on time. So I'll try to get moving.

[00:53:21] So, okay. So now what we did was see how we could learn representations of tokens.

[00:53:31] But I guess you may also want to get representations of sentences or pieces of text.

[00:53:41] So one very naive way to do that with what we saw before is to take something like the average

[00:53:49] of words, let's say, the word representations. But the problem is you lose a lot of meaning,

[00:53:55] you lose the order, you lose, and I guess here, I think you pointed out very well,

[00:54:02] the representations that you learn are token specific regardless of where they're at.

[00:54:09] So that's why we have a class of models that aim at capturing the sequential nature of how

[00:54:18] text appears. So we're going to talk about RNNs, which stands for recurrent neural network.

[00:54:26] So what RNNs do is instead of processing words one at a time, what they do is they keep a hidden

[00:54:37] representation of the sentence so far, and they consider tokens one at a time.

[00:54:45] So as I mentioned before, this technique was actually you introduced like a fair amount of time

[00:54:52] ago, so in the 80s. And what this model does is it takes into consideration the order at which

[00:55:01] words appeared or tokens appeared. And so in this example, you start the, I guess, processing at

[00:55:11] the very beginning of the sentence, you have some dummy hidden states that is called A, typically

[00:55:18] noted A or H, it's called a hidden state activation or even sometimes a context vector.

[00:55:26] And you have some kind of a module that takes into account the hidden state so far,

[00:55:34] and the word at time step T. So here, time step one. So here, what it does is it takes in

[00:55:45] the meaning of the sentence so far and takes into consideration the words that is happening now.

[00:55:52] And it produces an output vector that here can be used to try to predict the next word. So for

[00:55:59] instance, here, we have this hidden state and this representation of the words that then you

[00:56:07] have some matrix multiplications in this blue box, and you have an output vector that you try to

[00:56:16] train on predicting the next words. And then you keep on doing that by

[00:56:25] keeping this hidden state, keeping track of this hidden state. And so you repeat the process.

[00:56:34] And I guess the way you would interpret this hidden state is it's a representation of the

[00:56:44] sequence process so far. So the good thing with RNNs is now the word order matters.

[00:56:56] And you're also able to encode the sentence in a more natural way.

[00:57:04] So let's see roughly how it works. So we have the same favorite example, so cute teddy bear is

[00:57:11] reading. So you would have the token A, you find the one that includes vector, you pass it through

[00:57:19] your network, you compute the hidden states, you try to predict cute. But then you keep track of the

[00:57:27] hidden states. And then you input that into another module. And then you also consider the next words.

[00:57:37] So you consider not only the word itself, but also the hidden states of the sentence so far,

[00:57:43] and you try to predict the next word again, and again and again.

[00:57:51] So this is RNN. So RNNs were used for a bunch of tasks, and just like mapping that

[00:58:01] to the categories that we saw before. For classification purposes, you can basically

[00:58:08] use the hidden states of the last word in your sentence. For instance, if you want to predict

[00:58:16] review, like the sentiment of a review, you would take basically the last vector here and try to

[00:58:23] project it into the space of the predictions or the labels that you want to predict on. So for

[00:58:28] instance, if you want positive or negative, we basically project that vector into that space.

[00:58:33] You can do that here. For multi-classification, so you would basically have the representation

[00:58:39] of the token of interest, and you would project that. Or for generation, you would basically

[00:58:47] process the whole source text and then have kind of a context vector, a.k.a. activation vector,

[00:58:58] hidden states at the end of your processing, which will then be used to decode the output

[00:59:06] prediction. This is how you would use an RNN for each of these tasks. So the reason why

[00:59:17] you have not really heard of RNNs these days is because they had some pros with a lot of cons.

[00:59:26] So one of the cons is that the meaning of the sentence is basically solely encapsulated into

[00:59:34] this hidden state. So you have this problem of long range dependencies, which basically

[00:59:45] like impacts your ability to quote unquote remember what the model saw in the past,

[00:59:53] which is why you have another class of models that try to build on RNNs. So this one is called

[00:59:59] LSTMs, long short-term memory. And the goal of that extension is to have a way to somehow

[01:00:11] keep track of the things that are quote unquote important to remember on top of the hidden

[01:00:19] state that we talked about. So here you have A of t, which is your activation,

[01:00:26] like basically the sequence so far encoded in there. And then you have another

[01:00:32] quantity that you track that is called the cell states. It's going to be noted c here.

[01:00:39] So this architecture aims at improving that piece, but I guess it was not perfect either.

[01:00:49] But yeah, so that was like the main issue of RNN-based methods, which is that they have this

[01:00:59] issue of kind of forgetting what was in the past. So you will see in the literature that this

[01:01:04] phenomenon is called vanishing gradients. And the reason why it's called that way, so I know we're

[01:01:11] kind of running out of time, but I'm going to just explain that part. So in order for you

[01:01:18] to predict, let's say, the last words, you're basically dependent on every hidden state that came before that.

[01:01:30] So far so good. And so whenever you want to update the weights of your model to match

[01:01:39] the prediction here with the actual prediction, when you do the back propagation,

[01:01:45] you somehow need to take into account that the loss, the value here is basically not only a matter

[01:01:55] of this computation, but also this computation or this computation that basically happened in a

[01:02:00] sequential matter. So you have this kind of, this phenomenon of trying to, I guess, back propagate

[01:02:12] through time. But the problem is in practice, when you kind of write that down, so it's a very ugly

[01:02:18] formula, but when you write that down, it ends up being a product of a bunch of quantities

[01:02:28] that can, so if it's greater than one, then it's exploding. If it's less than one, it's vanishing,

[01:02:34] because if you multiply a lot of things that are less than one, it just goes to zero. So I guess

[01:02:39] if you have something that you're trying to update that goes to zero, you basically have

[01:02:44] trouble just like doing your updates. So that's a high level intuition. This is not the focus of

[01:02:50] this class, which is why I'm not going into the detail of these ugly formulas, but I hope you

[01:02:55] get the idea that for remembering things from the past, it's not doing a great job because of this

[01:03:03] sequential, I guess, characteristic. Does that make sense? Okay, I hope the next thing will make

[01:03:15] it more sense, but before that, I'll just recap what we saw. So our goal is to represent text.

[01:03:24] So we first started with representing words or tokens, which was what we tried to do with

[01:03:30] word 2-vec. And we saw that it was a good way to leverage proxy tasks to learn this representation,

[01:03:39] but we had a bunch of limitations. And one of them that you mentioned was that this was not

[01:03:46] aware of the context, and also the word ordered didn't count. And so you have this other class

[01:03:53] of methods that is able to take into consideration the words, but then they have some trouble keeping

[01:04:03] track of things when the sequence gets very long. And you have this problem of vanishing gradients

[01:04:10] or long range dependencies. So whenever you see this term, it's basically referring to that.

[01:04:16] And also another thing that I have not mentioned, but the computations are very slow.

[01:04:22] So when you want to train these models at training time, in order to predict this word,

[01:04:29] you basically need to compute all the seed and state before. So when your sequence gets very long,

[01:04:37] it just takes a very long time.

[01:04:41] So for all of these reasons, for, I guess, what reasons? So for the fact that

[01:04:56] the model has trouble remembering things from the past, people have tried having more direct

[01:05:05] connections between something and the thing from the past. And this is the idea behind

[01:05:12] attention. So what attention does is it tries to have a direct link between what we're trying to

[01:05:22] predict and something from the past. So in this example, let's suppose I'm trying to translate

[01:05:31] an English sentence into a French one. So here, I guess the input sentence is given,

[01:05:37] I'm computing the hidden states, I'm processing words one at a time, this is my traditional

[01:05:42] RNN. So AQ Teddy Bear is reading, so here I have a hidden state that I'm then decoding.

[01:05:50] And you can imagine that when wanting to generate the next word of my translation,

[01:05:58] it would be great if I knew what word I'm trying to predict. Or in other words,

[01:06:07] it would be great if I could take a peek at a certain area of the input text. So the idea

[01:06:16] behind attention is to have a direct link between what you're trying to predict and things before.

[01:06:24] This is the idea behind attention. And so it was introduced in 2014. And yeah,

[01:06:31] again, this is trying to kind of solve for these long range dependencies issues.

[01:06:43] And so, yeah, this example, we want to do that. And this concept is going to actually be key

[01:06:50] for this class. Because we're going to see that the attention mechanism is the thing that is going

[01:06:57] to make everything, I mean, most of the things work. And this is actually the main principle

[01:07:05] that the transformer paper relies on. So the transformer, which is the core architecture

[01:07:12] that we will see in this class, has been introduced, like was introduced in 2017,

[01:07:18] in this paper named attention is all you need. So even from the title, you can see that, you know,

[01:07:25] the authors wanted to just rely on that on that part. So what the authors tried to do was to move

[01:07:32] away from these sequential way of processing the text. And instead let the model just have

[01:07:42] direct connections with all parts of the text at once. So that is called self attention.

[01:07:52] So they tried that on translation tasks. And they just realized that, you know,

[01:07:57] it was giving great results. So back to the example that we're still using acute teddy bear is reading.

[01:08:05] Here, what we would say is that in order to compute the representation of the token teddy bear,

[01:08:15] we're going to look at all the other tokens in the sequence at once.

[01:08:24] And directly with direct links. So I guess back to your question. Here we would have a

[01:08:30] representation of teddy bear that would be unique to the context that it is part of.

[01:08:36] So back to your question about river bank and robbing a bank, like here the bank would have

[01:08:43] different representations. So this is the idea. I guess does the idea roughly make sense?

[01:08:52] And again, this is called the self attention mechanism.

[01:08:59] But how am I doing on time? Okay. Cool. So this is the idea. So now I'm going to just

[01:09:10] introduce another set of ideas, which is more terminology, but it's going to be very important.

[01:09:16] So when you want to express something in terms of something else, we use the words key, sorry,

[01:09:26] query key and value QK and V. So in this example, our goal is to figure out

[01:09:37] what other tokens is the query teddy bear more similar to. So here the question is,

[01:09:44] okay, you have a query and you want to see what other tokens are most similar.

[01:09:52] And so what you're going to do is to look at all the other tokens, which are basically composed of

[01:10:01] keys and values. So we're going to compare the query to the key to quantify how similar

[01:10:09] your query is to the given key and take the corresponding value.

[01:10:16] So we'll see that in this example. So let's suppose you want to express teddy bear in terms of

[01:10:20] everything else. What you're going to do is you're going to take the query teddy bear and you're going

[01:10:26] to compare that query with all the other keys to see which elements is more similar and then wait

[01:10:36] to more similar ones and take their associated value. So that's a very high level idea of

[01:10:46] is how these things are. Of course, we're going to see exactly how they work, but that's the general idea.

[01:10:55] Okay, cool. And speaking of query and key and value, we will also see that one benefit of

[01:11:02] expressing things this way is that we can express doing this self-attention computation across the

[01:11:11] whole sequence in a matrix format. And GPUs love matrices. So it's really like made for the hardware

[01:11:22] that we have. And I guess what I mentioned here can be expressed in a form of softmax

[01:11:30] of the query and the key. It's basically a way to get some kinds of weights of which values will

[01:11:39] be more important. So for instance, if a value is more important, you have bigger weights and

[01:11:43] another one less important, you have a smaller weight and you basically multiply that by the value.

[01:11:51] So don't worry, we'll have a detailed example after. So if it still feels very, you know,

[01:11:58] high level fuzzy, don't worry, we'll have a detailed walkthrough. And yes, so this is how it works.

[01:12:08] Okay, cool. Any questions on how self, what self-attention is? Yeah.

[01:12:28] Great question. So the question is, what is value? What is key? I guess how do you get those? What

[01:12:45] do they mean? So first of all, I just want to say that these quantities, they're learned.

[01:12:51] So you are not fixing them. But from an interpretation standpoint, you can interpret

[01:12:56] that the key is there for you to figure out which one is most similar to the query. And the value is

[01:13:05] the actual value that is associated with that with that element. So here, you will have something like

[01:13:14] you want to express this in terms of all the values. So the weights in your weighted average

[01:13:20] will be basically the dot product between basically between the query and the key.

[01:13:26] And the value will be the actual vector that we use. But again, these things are learned and

[01:13:33] there's something I've not mentioned, but you mentioned it correctly. So we're going to actually do

[01:13:37] projections to obtain these quantities. And these projections are actually learned by the model.

[01:13:43] That's good. Okay, cool. So with that, we have 15 minutes to talk about the architecture.

[01:14:02] Okay, so

[01:14:05] at a very high level, in order to make the self-attention mechanism happen,

[01:14:12] the authors propose an architecture that is composed of two parts, an encoder, which is on

[01:14:19] the left side, and a decoder, which is on the right side. So the application that they have

[01:14:27] is translation. So what we'll go through the encoder is the input text in your source language.

[01:14:37] And what is going to go through the decoder is the target language that you're predicting.

[01:14:43] So the high level idea is you're going to compute meaningful embeddings from your input text

[01:14:53] by passing them through the encoder. And you want that self-attention mechanism to apply,

[01:15:00] meaning you want to compute representations of each token as a function of others.

[01:15:07] And you do that by using a layer called the attention layer. So multi-head,

[01:15:14] attention layer, but multi-head is just doing this computation in different ways to just allow

[01:15:20] the model to learn different representations or different projections. But the idea here is

[01:15:27] you're going to input your input text, and all the tokens in your input text

[01:15:37] are going to attend to one another. So for instance, a cute teddy bear is reading,

[01:15:42] you're going to compute the representation of all the tokens in this text, basically as a

[01:15:50] function of others. And you're going to do that with the encoder. So here with the multi-head

[01:15:55] attention, and then you have a feedforward layer, which is just to kind of let the model learn

[01:16:03] another kind of projection. And what you're going to obtain at the end of your encoding process is

[01:16:13] rich representations of the tokens from the input sentence.

[01:16:17] So far so good. But now your goal is to actually translate the input sentence. So what you're going

[01:16:27] to do is to start your translation with, let's suppose, the beginning of sentence token,

[01:16:35] it's your first token. And what you're going to do is use all the representations from your input

[01:16:44] sentence in order to figure out what to predict next. So this, what I just said, is the cross

[01:16:55] attention layer, which is the one that is the second store. This one, which basically,

[01:17:03] you know, you see, I'm not sure if you see the arrows, but there are two arrows coming from the

[01:17:07] encoder, one arrow coming from the decoder. Can anyone tell me what the error from the decoder

[01:17:14] represents? Is it query, key, or value?

[01:17:22] Yes, there is one over three, thirty, three percent chance. Who wants to try? Is the key? Okay.

[01:17:32] Hmm. Query. Okay. So the way to think about it is you're trying to ask yourself,

[01:17:42] what are the words from the input that matter? Right. So basically, you want to know, given

[01:17:51] your query, what are the elements from the input that matter? So here, this arrow is indeed the

[01:17:59] query, because this is the thing that you want to figure out. And the keys and values are actually

[01:18:06] coming from the encoder, which are basically coming from the input sequence. And then you have

[01:18:15] another attention layer, which is this one. And that one is trying to figure out what other

[01:18:24] tokens of the output sentence that you're decoding is going to be useful to predict the next token.

[01:18:32] So let's suppose you, you know, start decoding and you say,

[01:18:37] en nous sans pollution, which is in French, to predict the next word, you want to basically

[01:18:42] figure out where the tokens translated so far, they are going to be useful to predict the next

[01:18:50] word. So this is what this attention layer is about. And it's called masked, because it only looks

[01:18:59] at the tokens translated so far. It does not look at tokens that were not translated, because,

[01:19:07] of course, they were not translated. So there's no way, like on the right side of the, of the token

[01:19:11] that you're trying to predict. Cool. So at a very high level, you have this attention layer,

[01:19:21] which is present in the encoder, which is present in the decoder, but it has several, I guess,

[01:19:27] use cases. So the attention layer here aims at computing embeddings from the input sentence

[01:19:39] as a function of themselves. And then the ones from the decoder, so the first one, the masked

[01:19:45] self attention layer aims at expressing something as a function of everything that has been decoded

[01:19:54] so far. And the second one, the cross attention layer tries to express things as a function of

[01:20:01] what has been seen in the inputs. So here, given that you are having direct links to different

[01:20:12] tokens, you don't have this sense of order, right? Because in the RNN, you were basically expressing

[01:20:21] things, you know, one at a time. So you had some sense of the word order, but here you don't have

[01:20:27] it because it's like a direct link, which is why you have position encodings,

[01:20:34] which are there to inform on the position of the word in the sequence. So we're not going

[01:20:41] to dig into that today, but I just want to call that out. So at a very high level, and we're going

[01:20:48] to see this in the detailed example, what we do is in order to translate a sentence from

[01:20:55] source language to target language, we're first going to tokenize the text, so you know,

[01:21:01] dividing into arbitrary units, we're going to learn an embedding for these tokens.

[01:21:07] So this is what the input embedding is about. Then we're going to add some encoding with respect

[01:21:12] to the position. We're not going to talk about it today, but just go to notes. And then we go to

[01:21:19] the encoder. So the encoder tries to figure out how to express things as a function of other things

[01:21:29] from the inputs. So it does that in the multi-head attention layer. And then it goes to a feed for

[01:21:36] all neural network, which is just a way to just project the vectors to just like have some more

[01:21:44] degrees of freedom to learn things. And then once you have these representations from the inputs,

[01:21:51] you're then going to start your translation. So you start with the BOS token. And what you're

[01:21:59] trying to do is figuring out what the next word is. So you're going to see, okay, what are the

[01:22:05] words that were translated so far that are useful for a translation? So this is what the masked

[01:22:11] multi-head attention layer does. And then you have another attention layer, which is about

[01:22:18] expressing things as a function of what was in the inputs, which is the cross attention

[01:22:26] layer over there. And then you have a feed for all neural network to again give some more degrees of

[01:22:31] freedom. And at the end of the day, you have a vector that you then go through softmax.

[01:22:39] And it just is a way for you to guess what is the next words. So you have a vector of size,

[01:22:48] vocabulary size. And you're going to use these values to determine what is your next word.

[01:22:59] Easy, right? Any questions on this?

[01:23:04] Yeah.

[01:23:09] All right. That's a great question. The question is, what does head mean?

[01:23:15] So I guess I went too fast. I kind of ignored that part. But when you do the attention,

[01:23:21] self-attention computation, you basically make queries interact with keys and then take the

[01:23:30] corresponding value. But nothing prevents you from doing that several times.

[01:23:35] So the term head is given to the projection matrices that you use to obtain the query key and value.

[01:23:44] And when you have several heads, what you're doing is you're allowing your model to learn

[01:23:50] different projections. So it's basically an additional degree of freedom for your model to

[01:23:57] learn different associations between your vectors. So it's a great question.

[01:24:03] So typically, it will be noted lowercase h, number of heads. And this is what this corresponds to.

[01:24:13] Does that answer your question? Cool. Very cool.

[01:24:24] Okay. We have a lot to discuss. But here I had a slide actually for this. So this is the

[01:24:31] multi-head that you are mentioning. So we're basically running the self-attention

[01:24:35] computation several times in parallel, again, with different projection matrices that

[01:24:40] the model learns. So in case you have a computer vision background, it is similar to

[01:24:48] having multiple filters in your convolution. So it's very similar idea. But I guess it's different here.

[01:25:01] So the question is, are the projections different? So we're not typically not constraining things.

[01:25:13] We're just letting the model learn. But in practice, it just tends to learn different ways of saying

[01:25:19] the same thing. So yeah, typically, there is no constraint. Of course, you have papers that dig

[01:25:25] into how about if you change this, but typically, you don't have any constraint.

[01:25:34] Cool. Great. I will just mention one trick, another trick that transformer

[01:25:44] authors use. So it's called label smoothing. Who has heard of label smoothing?

[01:25:51] Okay. So one new thing here is in NLP, when you want to predict what comes next,

[01:26:03] there's speaking more than one way. Like when you say what a great day, what a great lecture,

[01:26:11] what a great book, what a great... There's always multiple choices. Like there's more than one way

[01:26:17] of filling that gap. So label smoothing is a technique that tries to intuitively address that.

[01:26:25] And what it does is instead of saying, predict this word 100%, there's no other words.

[01:26:33] What it does is it says, okay, predict this word, but there's a chance it's not this word.

[01:26:40] And in practice, what it does is it takes the one hot encoding and instead of saying it's

[01:26:45] 100, that you need to predict, it says it's actually one minus epsilon and then epsilon over

[01:26:53] the minus one, I guess, is you're trying to predict. So in practice, it's a method that

[01:27:06] tends to make your model be more unsure. Like it would be less sure about this prediction because

[01:27:11] you always tell it, okay, try to predict this, but actually it's possible it's not the correct value.

[01:27:19] But in practice, the authors see that it tends to improve metrics like blue, which is a kind of

[01:27:27] proxy metric for translation tasks. So yeah, I think this method is like pretty general for NLP.

[01:27:34] So yeah, it's a good one to know. And with that, I think there's about 20-ish minutes left. So

[01:27:43] Sherwin is going to walk you through an end-to-end example. And with that, you...

[01:27:50] Yeah.

[01:27:57] The loo... Oh, you? So I guess here you can think of this as something, I guess some quantity. It's

[01:28:06] not defined. So some quantity. And yeah, the delta is like the one hot, if you want.

[01:28:15] Yeah. Something like this. Yeah, it can also be a constant. Yeah. Yeah.

[01:28:32] So question is, is there a relation with exploring exploits? It's an interesting one.

[01:28:39] So why would softmask give it for free, by the way?

[01:28:48] Right. But I guess it was still... So I guess at the end of the day, what you're trying to do

[01:28:56] is to compare your prediction with respect to the label. So I guess the question here is,

[01:29:01] do you want to compare with 1, 0, 0, 0? Or do you want to compare with something that is not 1,

[01:29:08] 0, 0? So I guess to softmask does not allow you to do that.

[01:29:14] Exactly. Yes. So I'm not sure if this was super clear, but this is actually the label. So

[01:29:18] what we're trying to predict is not 1, 0, 0, but we change the label in a way that makes the model

[01:29:26] I guess predict something as less sure, I guess. Cool. Thanks. And with that, yeah, Sherwin.

[01:29:34] Okay. Great. Thank you, I've seen. And yes, so we saw basically how the transformer worked.

[01:29:39] And now we're going to piece it all together with one specific example.

[01:29:46] Okay. Great. So let's take our favorite example again. So acute teddy bear is reading, and then

[01:29:52] we'll go all together through each step. So first we start with tokenization.

[01:30:00] So as we said, we can use any arbitrary decomposition to decompose this into tokens.

[01:30:08] And then as someone mentioned, you need to have some way to indicate the start and the end of a

[01:30:15] sequence. So typically this is done with the BOS and EOS tokens. So you add them.

[01:30:24] Okay. So now let's focus on the composition of each token representation.

[01:30:28] So you have its embedding that is learned. And then as I've mentioned, in order to have an idea of

[01:30:35] what is the position of the words or the token, I should say, as part of the sequence, you have

[01:30:40] some added information that is in the form of a position embedding. And here the original paper

[01:30:47] uses the convention of some signs and cosines that it adds additively to the representation.

[01:30:55] So it's like an element-wise addition. Okay. Great. So now you have the position aware

[01:31:02] embedding for your token. And you repeat that for each of your tokens. Okay. So now you can see

[01:31:11] all of these embeddings in the format of a matrix, which is of size D model, which is the

[01:31:17] size of your embeddings. And then the other dimension is the length of the sequence.

[01:31:22] So typically N. So that makes sense so far. Any questions on the inputs? Okay. Great.

[01:31:36] So now we will send this representation through the encoder. Okay. So as I've said,

[01:31:43] you have this concept of self-attention. And the way you perform self-attention is that you take

[01:31:49] this input and project it on three spaces. So you project it to the space WQ, you get queries.

[01:32:00] You project the same embeddings into space WK, you get keys. And you do the same for values,

[01:32:07] you get your values. And then WQ, WK, and WV are learned by the model. They're basically projection

[01:32:15] matrices. So far so good. Okay. So now with all of that in mind, you can apply the formula that

[01:32:26] Afshin mentioned, that is the self-attention formula, which is softmax of QK transpose over

[01:32:32] square root of DK times V, which gives you another matrix out of all of this.

[01:32:39] So that's the first step. Now let's pause for a second and look at how this computation is done

[01:32:47] in practice and what every step means. So let's look at Q. When you compute Q,

[01:32:56] that basically you project your embeddings into that space. What do you obtain? You obtain a

[01:33:01] matrix where each row represents a given query. When you say K transpose, it's basically the

[01:33:10] same kind of matrix, but transposed where each column represents the key representation of each

[01:33:17] token. Now let's mix them together with the matrix multiplication. So when you multiply each of them,

[01:33:28] you see that each row represents the projection of the query over each key.

[01:33:36] Such that when you take the matrix multiplication and get the softmax of all of this, you get a

[01:33:45] probability distribution of the projection of the query over keys for each query. Each line will have

[01:33:52] this. I don't know if anyone asked the question regarding why do we scale by square root of

[01:34:01] DK. So it could be DK as well because matrix multiplication, like the dot product here,

[01:34:08] enforces the fact that DK equals DK. And basically what you see is that these dot products,

[01:34:16] as the dimension of key and queries grows, it will tend to grow as well. So you want to normalize

[01:34:22] these dot products. And this is why you divide by square root of the dimension of keys.

[01:34:30] Okay, great. And then now you have your softmax of all of this. And then you multiply it with the

[01:34:36] matrix V. And this is what I've seen explained as having the query projected on the space of keys

[01:34:47] and then multiply it by the corresponding value. So the value is the representation of the corresponding

[01:34:53] key that we project on. So you end up with the weight sum of values for each query.

[01:35:03] Okay, great. Does that make sense so far?

[01:35:07] Okay, awesome. And someone asked, you know, what is the multi-head stuff? So you are right. It's

[01:35:18] not just single one, one time that it's done is actually done each time. And what you obtain is

[01:35:25] like all of that is done in parallel. And at the end, you obtain each such matrices. And you

[01:35:33] concatenate them with respect to the columns. And at the end of this, you have another projection

[01:35:40] matrix that you call WO that will project all of these back to the original dimension of embeddings.

[01:35:49] So it's a way for a network to basically have a dimension invariance way to bless you, to go from

[01:35:57] like the original dimension back to the original one.

[01:36:03] Any questions? Yep.

[01:36:15] So the question is regarding age, is it possible to get the same result each time? And if you

[01:36:21] concatenate the same thing, you know, will it be helpful? Did I get the question right?

[01:36:27] So what makes it different? So it's the magic of gradient descent. So the network has an objective

[01:36:33] function at the end, it has degrees of freedom. Its incentive is to build the representation that

[01:36:39] will be helpful to learn the next word. So it doesn't have an incentive to copy the same thing or do

[01:36:45] the same mechanism. And this is why in practice, you see the model converge towards building

[01:36:51] different representations that it can then concatenate and then project into something useful.

[01:36:57] So what makes it such that you don't have the same thing? Nothing. Like you don't have any

[01:37:02] constraints. But the nature of the learning that you let the model have makes it do so in practice.

[01:37:14] Any other questions?

[01:37:15] Yeah. And that is a great question. I mean, it's like typically gradient descent does wonders.

[01:37:25] Okay. Great. So now that we have gone through the self-attention layer, you have another component

[01:37:33] that is the FFM. And I think there was a question just here regarding how to choose the dimension of

[01:37:39] the hidden layer with respect to the input and outputs. So when I've seen mentioned word to vex,

[01:37:44] typically you have a smaller dimension than the input and outputs. But here, actually, the hidden

[01:37:50] layer is of a bigger dimension than input and outputs. And the rationale for that is that you

[01:37:57] want to have enough degrees of freedom for the model to learn useful representations. So it's a

[01:38:03] way to complexify the features that you learn. And just into. Okay. Great. And you don't have just

[01:38:13] one encoder module. You have actually N of them, big N in the original paper. And at the end of all

[01:38:20] of this, you have an encoded context to where set of embeddings. And then each of these set of

[01:38:29] encoded embeddings will be those that will be fed to the N decoders. So you have like a stacked

[01:38:37] like succession of N encoders, you have a stacked succession of N decoders. And the last

[01:38:44] representation of the encoder is what we feed to the cross attention of each decoder.

[01:38:54] So yeah, we're going to see that more in detail. So how do we even start the decoding process?

[01:39:01] So you start with the BOS token, basically saying to the model, you know, hey, we need to predict

[01:39:06] the next word, you know, let's start. So what happens to the BOS token at the very beginning?

[01:39:14] So you feed it to the decoder and then similarly as before for the encoder, you have a self attention

[01:39:19] layer. And as I've mentioned, the self attention layer is causal. So the attention will be done

[01:39:29] on the same token and the tokens that precede it. So on this first BOS token, you don't see a difference

[01:39:36] because it will just attend to itself. But when you have other tokens that you want to decode,

[01:39:42] you will have this difference in where you attend with respect to the encoder.

[01:39:48] Okay, great goes through the self attention layer. And then you have what I mentioned to be

[01:39:54] the cross attention that takes as keys and values these encoded embeddings as inputs.

[01:40:04] And then the queries are those of the that come out of the self attention layer.

[01:40:12] Okay, great. And then once you do this cross attention, you have just like in the encoder,

[01:40:18] an FFN components that's a main store representation richer. Was there a question there?

[01:40:24] No. And then at the very end, so you do that all of that end times. And at the very end of the

[01:40:33] decoding process, you have a linear projection and a softmax layer to turn the prediction of the

[01:40:40] next word into a probability distribution over the vocabulary. Okay, great. So we saw how to do

[01:40:47] that for the next word here. And basically, you do that again and again. So you have found your

[01:40:55] next token. And then which is like one whole one hot, basically, including of what you want.

[01:41:03] And then you take that embedding and then put it back in the decoder and continue this process.

[01:41:10] And when do you stop?

[01:41:11] So question for you all. When you hit the EOS token. Yeah. Yeah, exactly.

[01:41:23] Okay, great. And with this process, it's basically how the authors of this original

[01:41:30] like landmark paper did machine translation. So this is typically the use case that was presented.

[01:41:38] Any questions?

[01:41:41] Okay, awesome. And with that, thank you for your attention.

