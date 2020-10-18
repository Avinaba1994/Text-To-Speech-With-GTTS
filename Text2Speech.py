#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PyPDF2
from gtts import gTTS


# In[2]:


pdfFile= open("H:\sample_PDF.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(pdfFile)


# In[4]:


mytext= " "

for pagenum in range(pdfReader.numPages):
    page=pdfReader.getPage(pagenum)
    mytext += page.extractText()


# In[5]:


print(mytext)


# In[6]:


pdfFile.close()


# In[ ]:


output =gTTS(text= mytext, lang = "en")
output.save("speech.mp3")

