# Fake News Classification with a Flask Front End
----
#### by Ben Inoyatov

### Introduction
---
- Fake news has become a buzzword in the days of the Digital Revolution. With the power of the internet, *anyone* can have their voice heard. While this idea has led to the exponential growth of real, trustworthy data it has also led to the rise of 'fake' data. Take for example 70News - a fake news website hosted on WordPress. After the 2016 election, they claimed Donald Trump won the popular vote. The story became so popular that it was one of the top results when googling "final election results." [Source](https://www.cbsnews.com/news/googles-top-search-result-for-final-election-numbers-leads-to-fake-news-site/) 

- It is more important now than ever before that we maintain a ground-truth of what the internet can be. This project focuses on analyzing twenty thousand+ articles [Kaggle Source](https://www.kaggle.com/c/fake-news/overview) that were deemed 'fake' or not. In addition to tuning a model, there is also a front end Flask application where a user can enter a URL link to an article and the application will output whether it deems the article fake. 
- Libraries used: ```pandas | numpy | matplotlib | scikitlearn | NLTK | Flask```

Notebooks to refer to:
- For EDA and csv compilation refer to: ```eda_and_cleaning.ipynb```
- For the model process along with visualizations refer to: ```NLP_modeling.ipynb```

#### Model Process
---
- The best model was a passive aggressive classifier that had a 97% accuracy.
- Accuracy was used to achieve the best overall performance of the model due to the even class balance that the data came with. 
- 
![model_confusion_matrix](https://user-images.githubusercontent.com/44031998/98063901-1203f200-1e1f-11eb-916f-f44b447174b2.png)

#### Word count bar graphs 
- Fake news and Real news have similiar word usage however some differences are shown e.g., true news' most used word was 'said' which implies that those news outlets use direct quotes of the people they report about. In constrast fake news cannot rely on direct quotes often times and instead paraphrase or use other inflammatory words to distract the reader. 
![word_count_bar_graphs](https://user-images.githubusercontent.com/44031998/98063728-b3d70f00-1e1e-11eb-8235-44ffce4a5180.png)



- Real news wordcloud

![real_wordcloud](https://user-images.githubusercontent.com/44031998/98063782-d23d0a80-1e1e-11eb-9859-5436b2a1113f.png)

- Fake news wordcloud

![fake_wordcloud](https://user-images.githubusercontent.com/44031998/98063821-ebde5200-1e1e-11eb-87f3-e732f8938747.png)



## Links 
---
[Kaggle Source](https://www.kaggle.com/c/fake-news/overview)

[Google Slides](https://docs.google.com/presentation/d/1J8PWzQ1aH5EcLo3egiD1mbHyhR61dhtSv_kgYRAXsVE/edit?usp=sharing)
