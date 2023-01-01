# Socialmedia_Bullying_classification
To classify the social media bullying based on the text they posted

# Model 
A cyberbully classification system is used to identify and classify cyberbullying activities such as Flaming, Harassment, Racism and Terrorism in Social Media is proposed . Each words or texts comes under specific categories.Using Machine Learning we can easily categorise the text .Based on that , Naives Bayes algorithm is used to classify the twitter comments into 5 categories . Natural Language processing is used to preprocess the twitter comments by removing URLs,mentions,hashtags,symbols,etc.Then the model is trained using Naive bayes for classifying the text.

# Datasets

Twitter dataset is used for Social media bullying classification

Texts are classified as mentioned below :
 
_1. Age_

_2. Ethnicity_

_3. Gender_

_4. Religion_

_5. Other cyber bullying_

_6. Not cyber bullying_

**Original Dataset**

![image](https://user-images.githubusercontent.com/86719672/210181799-ffa96a84-21df-4c13-831e-51da580cfd0c.png)


**Preprocessed Dataset**

![image](https://user-images.githubusercontent.com/86719672/210181808-22cbd2b1-5233-47d4-8e69-bd2b8fa6a6a8.png)


# Libraries 

Snowball Stemmer - stemming algorithm(reducing a word to its stem that affixes to suffixes and prefixes)

Stopwords - set of commonly used words in any language

LabelEncoder - encoding the levels of categorical features into numeric values

Demoji - Accurately find or remove emojis from a blob of text

String - To search whether a substring is present in the main string or not

TfidfVectorizer - Converts a collection of raw documents into a matrix of TF-IDF features

# Algorithm 

**NAIVE BAYES **algorithm is used 

**Confusion Matrix**

![image](https://user-images.githubusercontent.com/86719672/210181924-782fc15a-a104-4fef-9a52-fc4f6f0d2326.png)

**Accuracy** - _0.89_

# Prediction

sample_text=["@pradeep : A feminist is an advocacy of the political, economic, and social equality of the sexes expressed especially through organized activity on behalf of women's rights and interests"]

**Output**

![image](https://user-images.githubusercontent.com/86719672/210181959-4a010718-6510-4045-836c-69d454404295.png)




