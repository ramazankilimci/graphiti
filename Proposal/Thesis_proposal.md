## Absract

Extracting a semantic meaning from texts or documents is a popular research area. Most of the successful academic works have used machine learning techniques. These techniques have worked quite well for long texts or documents. However, with the advent of social media apps, short texts play a different role in today's world. Extracting a topic from these short texts can open a new path to understanding people. We will mainly focus on Twitter data for these short texts.
 
And the well-known techniques for longer texts do not work for shorter texts. Our goal is to use Deep Learning in combination with Graph Neural Networks (GNNs) and data structuring to extract topics from shorter texts. This is because we believe that data is the key to any Deep Learning research. Therefore, defining a new data type for tweets will help us achieve better results for our model under development and also for the existing models. With this new data structure and model, we believe that this topic extraction can help us to build profiles of people for marketing, prevent fraud or false information or extract valuable information.


## Introduction

In this research, our goal is to extract topics from tweets (microblogs). This topic modeling is not a new area of work. The analysis of texts using NLP methods has been a well-known research area for many years. In the past, the goal was to analyze long texts or documents. Because we did not know a microblog or a short text before. These analyzes for long texts were done with techniques like Latent Dirichlet Allocation (LDA). LDA uses BoW (Bag of Words) technique which is based on distance between the words. However, these do not work well for short texts. To solve this problem, researchers have proposed new methods using Deep Learning and knowledge graphs. In the following sections, we will talk about the steps we will work on.

First, we extract tweets using the Twitter API based on a given field. Then, we will construct entities from the individual tweets. However, tweets have very specific properties. These properties will help us understand the tweets better. Properties include hashtags, emoticons, mentions, retweets, and replies. Each of these properties can be used to add context to the tweet. Therefore, we believe that proposing a new way of representing tweets will provide better results compared to previous studies.

In second step, we will extract the entities from the tweets. We hope that the entity extraction will be improved by the new way of tweet representation. This entity extraction will be done using Wikidata. We would like to develop a flexible model to extract these entities. This will allow us to test our model at two, three, or more levels, depending on computational power.

In the third step, a graph neural network is presented based on the extracted topics. Graph Neural Networks are different from other neural networks such as feed-forward, RNN or CNN. They help us to represent specific relationships between data points. Therefore, they are the most advanced models for any research area.

Finally, we feed the test data into the GNN and compare the results with previous work and our previous models. We believe that the GNN will provide more accurate results with data representation. However, we also tend to take a new approach with the GNN architecture. Therefore, we hope that the accuracy will be much higher.

## Methodology

The research phase has started with the acquisition of basic knowledge about GNNs (Graph Neural Networks). This was an important step because our model relies heavily on GNNs. Moreover, the mathematical basics were very important to understand how neural networks work. To gain this ability, I worked on the fast Fourier transform and Gaussian models.

Another important turning point was understanding Twitter data. The Twitter API v2 and its results were carefully inspected to construct the entities. With the new way of defining the tweets, we expect better results compared to previous models.

Python code will help us preprocess tweets using the Twitter API v2. Data collection will include popular topics such as politics or sports as well as less popular topics to understand how our model works under different conditions.


| Tasks                        | 2022-Q1 | 2022-Q2 | 2022-Q3 | 2022-Q4 | 2023-Q1 |
|------------------------------|---------|---------|---------|---------|---------|
| Literature Search            |    X    |    X    |         |         |         |
| Model development            |         |    X    |    X    |         |         |
| Model tests                  |         |    X    |    X    |         |         |
| Thesis writing               |         |         |    X    |    X    |    X    |
| Publish an article           |         |         |    X    |    X    |    X    |
| Mdeole and thesis correction |         |         |         |    X    |    X    |