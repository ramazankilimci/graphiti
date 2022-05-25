## Absract

Topic extraction from long texts or documents have been a popular research area. Machine learning models were state-of-the-art models which provides the topic extraction from longer texts. Testing these models on shorter texts did not work well. It is because shorter texts have different contexts.
With the advent of social media apps, short texts have become more important. Extracting a topic from these short texts can open a new path. 
 
Our aim is to use Deep Learning in combination with Graph Neural Networks (GNNs) and data structuring to extract topics from shorter texts. This is because we believe that data is the key to any Deep Learning research. Therefore, defining a new data type for short texts will help us achieve better results for a machine learning model. With this new data structure and model, this topic extraction can help us profiling for marketing, preventing fraud or false information or extracting valuable information.



## Introduction

In this research, our goal is to extract topics from tweets (microblogs). This topic modeling and the analysis of texts using NLP methods has been a well-known research area for many years. In the past, the aim was to analyze long texts or documents. Because there is no a microblog or a short text before social media. Studies for long texts have been achieved with methods known as Latent Dirichlet Allocation (LDA). LDA uses BoW (Bag of Words) practice which is based on distance between the words. However, these studies do not work well for short texts. To figure out this specific problem, researchers have proposed new methods based on Deep Learning and knowledge graphs. In the following sections, we will mention about the steps in our study.

Primarily, tweet extraction will be done with the help of Twitter API. Subsequently, entity construction can be achieved from the extracted individual tweets. Yet, in reality, tweets have many exclusive properties in which may include hashtags, emoticons, mentions, retweets, and replies. Each of these exclusive properties can be utilized to add more context to the tweet. Therefore, proposing a new way of representing tweets can provide preferable outcomes compared to previous studies.

Secondarily, the entity extraction is composed by using from the tweets. Our expectance is that the entity extraction will be improved by the new way of tweet representation. This entity extraction is achieved using Wikidata by developing a flexible model to extract these entities. This enables us to test our model at two, three, or more levels, depending on computational power.

In the next step of our study, a graph neural network is presented based on the extracted topics. Graph Neural Networks differentiates from other neural networks which are known as feed-forward, RNN or CNN. They enable to represent particular relationships between data points. Hereby, it can be said that they are one of the most advanced models for any research area.

Lastly, the test data is fed into the GNN and is compared the outcomes with previous work and our previous models. We believe that the GNN can provide more accurate results with new data representation. Yet, we also tend to take a new approach with the GNN architecture. Therefore, our expectance is that the greater accuracy can be achieved.

## Problem Definition & Motivation
Short texts are more important in today’s world. Most importantly with the invent of social media, they became crucial. However, extracting an information without a human interpretation is not that easy. Not only text, even an emoji, a picture or an internet link can strengthen the meaning of a short text. Studies have been done around longer texts do not give expected outcomes when compared to the shorter texts. Therefore new researches gathered shorter texts have been emerged. These researches consubstantiates deep learning models, generally graph neural networks, and knowledge graphs which can be dynamic or static according to specific scenarios. In this research,  one of our objectives is to form the input data by including the contents of short texts, meaning emojis, hashtags etc. By forming the short text withing this context, our expectance is to gain preferable results even with the models which have been tested with former input data. More importantly, accuracy rates will advance as the model will be improved.


## Methodology

The research phase has started with the acquisition of basic knowledge about GNNs (Graph Neural Networks). This was an important step because our model relies heavily on GNNs. Moreover, the mathematical basics were very important to understand how neural networks work. To gain this ability, I worked on the fast Fourier transform and Gaussian models.

Another important turning point was understanding Twitter data. The Twitter API v2 and its results were carefully inspected to construct the entities. With the new way of defining the tweets, we expect better results compared to previous models.

Python code will help us preprocess tweets using the Twitter API v2. Data collection will include popular topics such as politics or sports as well as less popular topics to understand how our model works under different conditions.


## Timeline

| Tasks                        | 2022-Q1 | 2022-Q2 | 2022-Q3 | 2022-Q4 | 2023-Q1 |
|------------------------------|---------|---------|---------|---------|---------|
| Literature Search            |    X    |    X    |         |         |         |
| Model development            |         |    X    |    X    |         |         |
| Model tests                  |         |    X    |    X    |         |         |
| Thesis writing               |         |         |    X    |    X    |    X    |
| Publish an article           |         |         |    X    |    X    |    X    |
| Mdeole and thesis correction |         |         |         |    X    |    X    |