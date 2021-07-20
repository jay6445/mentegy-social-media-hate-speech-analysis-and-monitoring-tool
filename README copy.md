# Social Media Hate Speech Analysis and Monitoring

Mentegy is a live hate speech monitoring application that scrapes data from social media (Twitter), performs sentiment analyses (predictive analytics) on it using supervised learning models and shows the insights on a dashboard (descriptive analytics) for the authorities to make informed decisions.  The following flowchart depicts the technologies that give life to Mentegy.
 
Data Source: Twitter API v2 endpoint is used to obtain precise, complete and unbiased data from the public conversation. Twitter Academic Research access to the API ensures live stream as well as historical access to the public tweet data with a monthly cap of 10 million tweets.  Rules are used to filter the live stream to obtain the tweets niche to Mentegy’s use case. The rules include a corpus of keywords generated based on the influential xenophobic and racist hate speeches in the past. To focus on the hate speech in the target area, attributes like the geo-tag and point radius are added to the rules.  Python is used as a primary programming language to access the API, add the necessary rules and pre-process the data hence obtained.

Sentiment Analysis: Mentegy uses VADER (Valence Aware Dictionary and sEntiment Reasoner) as a lexicon and rule-based sentiment analysis model. VADER is specifically trained using the sentiments expressed on the social media and is therefore befit for the research.  The model takes in the text for the tweet as an explanatory variable and its sentiment score is the target variable. The valence scores of each word in the text is calculated which categorizes it into positive, negative and neutral. The model has been trained previously to identify contradictions as negations, utf-8 encoded emojis, emoticons, intensity boosting and dampening words, usage of punctuations like exclamation to increase sentiment intensity and the usage of word-shape like ALL CAPS words. The scores calculated for each word as a result is then summed, tuned as per the rules and normalized such that they are between -1 and 1 which then would be the compound score for the tweet text.
VADER has been tested for accuracy using a test dataset that has 100 racist and xenophobic tweets manually marked positive and negative. The polarity of the tweets are then calculated by inputting it into the model and the prediction obtained are compared with the previously marked results using a confusion matrix as seen below.
 
The confusion matrix shows the higher false positives at 29 but lower false negatives at 9 which means that the model has higher probability of marking a non-hate tweet as hate than marking a hate-tweet as non-hate which is favourable as the latter is a more serious error in this use case. The overall accuracy of the model is 61.62% having a 95% confidence interval of 51.3% and 71.22%.
The rule based tweet scraping and sentiment analysis forming the core of the application is coded in Python and is running on an EC2 t3.micro instance on the Amazon Web Services public cloud.
Database: 
Mentegy uses an RDS instance with MySQL Community database engine on the Amazon Web Service cloud for storing the tweet data and the sentiment scores. RDS provides regular automated backups and instantaneous restore thereby increasing the fault tolerance of the application. The ‘pymysql’ library in Python provides the functions to connect to the database host and insert the data using standard SQL syntax. The sentiment scores are calculated for the live twitter stream and are inserted along with the tweet metadata as they come in, into the database.
Application:
Mentegy uses the Django framework of Python as the backend of the web application that consumes the data and performs descriptive analytics concerning to the end user. Django provides inbuilt features that provide session handling and authentication that can be leveraged to secure the access to the application hosted publicly. Presence of Object Relational Mapping (ORM) ensures that the deployment of the application is faster and error free as the database schema is automatically created based on the models explicitly created in the code. The data is fetched from the database by Django and Chart JS library is used to create an interactive dashboard displaying different metrics like the present hate speech status in an area and the comparative analysis of the hate scores during the past week. Following are some screenshots from the application.
































Hosting: The public ipv4 address of the EC2 instance and the port Mentegy is running on is mapped to the domain name in the Route 53 Service of the AWS. Mentegy can be accessed on http://mentegy.org

#Stages of development:

The whole Journey of Mentegy started from February to July. All the different stages of development, the innovation and failures will be discussed in this section. 
During February, the initial focus was towards the idea of each group members. Understanding each other ideas gave all the group members a platform to discuss the further steps. Then, the individual idea summaries and simultaneously working towards the workflows gave the group members more understanding regarding the other components. Later in February, technologies and executive summary was the priority to be looked towards, which can help all the group members to be bounded on certain areas. 
After the feasibility study, the initial priority was analysing libraries and Twitter scrapping which best suits our service and has enough potential in terms of accuracy. vaderSentiment analyzer has been used for the sentiment analysis which gives positive, negative, neutral and the compound score. Furthermore, after sentiment analysis different algorithms were being tested to know the efficiency and accuracy of the prediction model. 
During the later stages, as the live Twitter streams were being extracted, there was a need for shifting all the services to the cloud platform to keep the application code running 24x7. Hence, all the Mentegy’s components were shifted to the AWS cloud. Continuing further progress, all the tweets data were being displayed on the live visual representation of the dashboard. The Dashboard shows the compound score based on days, minutes, and seconds. The granularity has been focused and hence, tweets score based on seconds are also being displayed on the dashboard. To understand a certain impact or changes in the Twitter, daily tweets data give more insights. 
Finally, a domain name was purchased and mapped to the EC2 IP address and port number the application was running on such that it could be accessed publicly.

