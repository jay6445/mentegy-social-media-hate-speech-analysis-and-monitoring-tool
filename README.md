# Social Media Hate Speech Analysis and Monitoring

The application will be a mainstream live monitoring tool showing predictions of growing hate trends for advanced strategic planning by authorities and emergency response teams. It will also provide policy makers information to promote or create additional policies to mitigate the spread of online hate-speech. The dashboard will provide location based comprehensive timeseries analysis of growth trends with insightful visualisation capabilities. The solution will be cloud based and will be offered as a Software as a Solution (SaaS). It will therefore be scalable so as to react to fluctuations of situations thus deploying necessary resources where essential. The Pricing model will be a subscription based payment model and have initial public funding. The Operation, Maintenance and technical and functional support will be administered by the company.

**Analytics Pipeline**

 ![image](https://user-images.githubusercontent.com/67317976/118524683-4e050180-b736-11eb-804f-6b4b36686831.png)

**Technology Stack**

**Programming Language: Python**
Python would be the primary language this application will be coded in. Python is chosen for the flexibility and availability of multiple libraries that can be leveraged based on our scope. Backend services will include scraping of twitter streams, cleaning, natural language processing and classification, predictive analytics. Frontend application will be programmed using a Python based responsive web application library called Django.

**Twitter Scraping Libraries: Twitter api**
Twitter api will act as a tool to access continuous twitter streams to perform further analysis. Academic access to the Twitter’s developer profile would ensure additional functionalities from the api. Parameters for scraping can include geo, places for obtaining tweets from particular locations. For example, twitter streams can be obtained from all the counties in Ireland separately
for a population wellbeing comparison. The streams will then be inputted to the data analysis pipeline.

**NLP and Sentiment Analysis Libraries: vaderSentiment**
VADER (Valence Aware Dictionary Sentiment Reasoner) is a lexicon and rule-based sentiment analysis that is specifically attuned to sentiments expressed in social media. vaderSentiment python library will be used to perform pre-processing and natural language processing to identify negations, contradictions as negations, emphasis using ALL CAPS, intensity boosters such as “very” and intensity dampeners such as “kind off” and so on. The algorithm will then score the individual words in the sentences as positive, negative or neutral and calculate the overall compound score of the sentence.

**Predictive Analytics Libraries: SciPy optimize curve fit**
Predictive Analytics will be used to predict the growth of scores in different areas. Scipy optimize curve fit will be used to eliminate the need for normalization and transformation of the distribution of scores. After a further study of association between parameters that can be used in the analytics, the model can then take inputs from the scores and other parameters stored in the database.

**Descriptive Analytics: Tableau Server**
The data frame of the predicted scores will be used as a live data source for the Tableau Dashboard to have interactive visualizations for health and well-being agencies.

**Responsive Web Application: Django**
The responsive web application will be developed using Django which fast, scalable and provides a collection of plugins for database connectivity, sessions and authorization. The Tableau dashboard from Tableau Server will be embedded inside.
