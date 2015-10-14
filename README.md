# weibo_text_mining
Apply Natural Language Processing techniques on weibo content analysis

###What is Weibo?
According to Wikipedia, Sina Weibo is a Chinese microblogging (weibo) webiste.
Every day, about 100 million messages are posted on Sina Weibo.

###What is our topic?
"Man's brutal beating of female driver divides Chinese public after different car videos emerge"
http://www.scmp.com/news/china/society/article/1787577/mans-brutal-beating-female-driver-divides-chinese-public-after?page=all

###Our Data
Through Weibo API and some web scripping techniques, we were able to get about 7000 tweets from May 3rd to June 3rd 2015 on Weibo.com, including usernames, ids, publish dates, and counts of repost, like,content, and etc.

###Method
Supervised Learning - Randomly selected 1/10 tweets from the database and analyze the attitude of the content. (1 -> The woman deserved the beating; 2-> The man lost his mind. - Read the tweets, decided the attitude of the content, and skipped the ones with murky attitude. (Eg: "I think both A and B were wrong, but I can't decide who was at more fault.")

###Data Clean
Got rid of the reposted content in Python using functions such as strip, split, and partition.

###Text Mining
Built and compared results from two models we built to text our data (Decision Tree and Native Bayes)
Result: NB had higher accuracy than DT in our case. (0.78 / 0.84) No. of Train data : Test data: 1:20
Splitted the tweets into two datasets based on the publish date and tested again. (Before and after the release of the second video)
Accuracy: 0.83 before the 2nd Video resleased; 0.65 afterwards.


###Model Application
Applied the model on 5000 untrained tweets, and let the machine predict the attitude of the content.
Result: Before the second video was released: only 3% of people on Weibo think that the female driver deserved the beating. However, the number quickly increased to 61.6% after the second video was released, which showed that the female driver's drving dangerously on the high way in front the male driver's car.
