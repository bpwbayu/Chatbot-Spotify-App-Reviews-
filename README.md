# 🤖 Chatbot Spotify App Reviews
This project analyzes Spotify user reviews to predict customer sentiment using machine learning. The goal is to understand user satisfaction, provide insights for improving services, and allow interactive testing of predictions through a web interface using Streamlit.

---
## 📁Dataset
Source: Kaggle - Spotify App Reviews
- The dataset contains user reviews along with their ratings and thumbs-up counts, making it suitable for building sentiment classification models and evaluating overall user satisfaction with Spotify.
---
## ⚙ Tools 
- Python (Pandas, NumPy, Scikit-Learn, Re, Joblib,  Matplotlib, Seaborn, NLTK, Streamlit )
- Jupyter Notebook/VS Code
---
## 🎯 Purpose of Analysis
- Analyse Spotify user reviews to understand user sentiment.
- Build a machine learning model for sentiment analysis.
- Deploy an interactive demo using Streamlit.
- Extract actionable insights to improve the user experience.
---
## 🔎 Steps 
### !. Data Loading, Data Cleaning, and Exploratory Data Analysis (EDA)
- Reading datasets using Pandas
- Checking and handling missing values
- Analyzing distribution review length distribution, rating distribution, distribution total thumbs up, and number of reviews by date/time  
### 2. Feature Engineering
- Performing text preprocessing, including cleaning and lemmatization
- Generating sentiment score features and converting them into sentiment labels
- Applying one-hot encoding for additional categorical features
### 4. Modeling
  Model used:
- Multinomial Naive Bayes
- Logistic Regression
- Random Forest Classifier
- LinearSVC
- KNN
### 5. Evaluation
- Accuracy Score
- Classification Report (Precision, Recall, F1-support)
- Confusion Matrix
---
## 📊 Visualization
- Sentiment Distribution, The sentiment distribution shows a balanced dataset between positive and negative reviews, each appearing with relatively similar frequency.
- Text Length Distribution,  The text length distribution indicates that most reviews are short to medium in length, while a small number of reviews extend far longer, with some exceeding 10,000 characters.
- Rating Distribution, The rating distribution reveals that 5-star ratings are the most common, suggesting a generally positive user experience.
- Thumbs Up Distribution, The thumbs up distribution shows that most reviews receive little to no engagement, while only a few reviews accumulate significantly high thumbsup counts.
- WordCloud Visualization, The word clouds highlight frequently used terms in positive and negative reviews, allowing a quick understanding of common user expressions and themes.
---
## 🧠Insight
- The majority of Spotify user reviews express positive sentiment, indicating a high level of user satisfaction with the service.
- The LinearSVC model demonstrated the best performance with an accuracy of 89%, making it the most suitable choice for deployment.
- The application of text preprocessing and TF-IDF significantly improved the model’s accuracy compared to a simpler baseline approach.
---
## 🚀 How to Run
- Ensure all required packages are installed:
  
  ```pip install pandas numpy scikit-learn re joblib matplotlib seaborn nltk streamlit```
- Run the notebook in Jupyter or VS Code:
  
  ```jupyter notebook Project_ChatbotCustomerSupport.ipynb```
- Run the Streamlit:
  
  ```streamlit run app.py```
