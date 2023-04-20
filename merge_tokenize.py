import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import csv

lemmatizer = WordNetLemmatizer()

diseases=os.listdir("AI_diary_entries")

entries_ADHD=os.listdir("AI_diary_entries\ADHD")
entries_Anxiety=os.listdir("AI_diary_entries\Anxiety")
entries_Autism=os.listdir("AI_diary_entries\Autism")
entries_Bipolar_disorder=os.listdir("AI_diary_entries\Bipolar_disorder")
entries_Depression=os.listdir("AI_diary_entries\Depression")
entries_Schizophrenia=os.listdir("AI_diary_entries\Schizophrenia")
entries_PTSD=os.listdir("AI_diary_entries\PTSD")
entries_aam_aadmi=os.listdir("AI_diary_entries\\aam_aadmi")

stop_words=list(stopwords.words("english"))
stop_words.append("\\n")

f=open("tokenized_data.csv","w+",newline="\n")
csv_writer=csv.writer(f)
csv_writer.writerow(["label","text"])

for i in entries_ADHD:
    s=""
    with open("AI_diary_entries\\ADHD\\"+str(i),"r",encoding="UTF-8") as f2:
        temp=f2.readlines()
        for j in temp:
            s+=j
    s=word_tokenize(s)
    l=[]
    for i in s:
        i=i.lower()
        if i.isalpha() and i not in stop_words:
            l.append(lemmatizer.lemmatize(i))
    csv_writer.writerow(["ADHD",l])

for i in entries_Anxiety:
    s=""
    with open("AI_diary_entries\\Anxiety\\"+str(i),"r",encoding="UTF-8") as f2:
        temp=f2.readlines()
        for j in temp:
            s+=j
    s=word_tokenize(s)
    l=[]
    for i in s:
        i=i.lower()
        if i.isalpha() and i not in stop_words:
            l.append(lemmatizer.lemmatize(i))
    csv_writer.writerow(["Anxiety",l])

for i in entries_aam_aadmi:
    s=""
    with open("AI_diary_entries\\aam_aadmi\\"+str(i),"r",encoding="UTF-8") as f2:
        temp=f2.readlines()
        for j in temp:
            s+=j
    s=word_tokenize(s)
    l=[]
    for i in s:
        i=i.lower()
        if i.isalpha() and i not in stop_words:
            l.append(lemmatizer.lemmatize(i))
    csv_writer.writerow(["aam_aadmi",l])

for i in entries_Autism:
    s=""
    with open("AI_diary_entries\\Autism\\"+str(i),"r",encoding="UTF-8") as f2:
        temp=f2.readlines()
        for j in temp:
            s+=j
    s=word_tokenize(s)
    l=[]
    for i in s:
        i=i.lower()
        if i.isalpha() and i not in stop_words:
            l.append(lemmatizer.lemmatize(i))
    csv_writer.writerow(["Autism",l])


for i in entries_Bipolar_disorder:
    s=""
    with open("AI_diary_entries\\Bipolar_disorder\\"+str(i),"r",encoding="UTF-8") as f2:
        temp=f2.readlines()
        for j in temp:
            s+=j
    s=word_tokenize(s)
    l=[]
    for i in s:
        i=i.lower()
        if i.isalpha() and i not in stop_words:
            l.append(lemmatizer.lemmatize(i))
    csv_writer.writerow(["Bipolar_disorder",l])


for i in entries_Depression:
    s=""
    with open("AI_diary_entries\\Depression\\"+str(i),"r",encoding="UTF-8") as f2:
        temp=f2.readlines()
        for j in temp:
            s+=j
    s=word_tokenize(s)
    l=[]
    for i in s:
        i=i.lower()
        if i.isalpha() and i not in stop_words:
            l.append(lemmatizer.lemmatize(i))
    csv_writer.writerow(["Depression",l])


for i in entries_PTSD:
    s=""
    with open("AI_diary_entries\\PTSD\\"+str(i),"r",encoding="UTF-8") as f2:
        temp=f2.readlines()
        for j in temp:
            s+=j
    s=word_tokenize(s)
    l=[]
    for i in s:
        i=i.lower()
        if i.isalpha() and i not in stop_words:
            l.append(lemmatizer.lemmatize(i))
    csv_writer.writerow(["PTSD",l])

for i in entries_Schizophrenia:
    s=""
    with open("AI_diary_entries\\Schizophrenia\\"+str(i),"r",encoding="UTF-8") as f2:
        temp=f2.readlines()
        for j in temp:
            s+=j
    s=word_tokenize(s)
    l=[]
    for i in s:
        i=i.lower()
        if i.isalpha() and i not in stop_words:
            l.append(lemmatizer.lemmatize(i))
    csv_writer.writerow(["Schizophrenia",l])