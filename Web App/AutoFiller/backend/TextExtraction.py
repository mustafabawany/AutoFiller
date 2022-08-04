""" Importing Packages """

import itertools
import re
import pytesseract
import os
import spacy
from spacy.matcher import Matcher
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

""" Class Implementation """

class TextExtraction:
    
    def __init__(self):
        """ Setting Regular Expression for Email And Contact Number """
        self.PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
        self.EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')

    def ExtractText(self , img) : 
        """ Extract Text From Image Using Pytesseract OCR """
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(img, config=custom_config)
        return text

    def removing_extra(self, text):
        """ Remove Extra Sentences From Top Of The Image For Better Results """
        new_sentence = ""
        result = ""
        token_sentence = sent_tokenize(text)
        if "applying for" in token_sentence[0].lower() or "applied for" in token_sentence[0].lower() or "post applied" in token_sentence[0].lower():
            sentences = token_sentence[0].split("\n")
            for sent in sentences:
                if "applying for" in sent.lower() or "applied for" in sent.lower():
                    continue
                else:
                    new_sentence = new_sentence + sent + "\n"
            i = 0
            for sentence in token_sentence:
                if i == 0:
                    result = result + new_sentence + "\n"
                else:
                    result = result + sentence  + "\n"
                i += 1
            return result 
        else:
            return text
    
    def extract_name(self , text):
        """ Extracting Name From Text """
        nlp = spacy.load('en_core_web_sm')

        matcher = Matcher(nlp.vocab)

        # Words that are to be avoided while extracting name
        ignore_words = ["curriculum" , "vitae" , "vita" , "post" , "applied" , "for" , "address" , "resume" , "engineering" , "engineer",
                    "mechanical" , "address" , "mobile" , "contact" , "phone" , "temporary" , "street" , "resume", "computer" ,
                    "software" , "personal" , "information" , "name" , "date" , "box" , "work" , "professional", "near" ,
                    "objective" , "general" , "skills" , "skill" , "officer" , "administration" , "administrator" , "career", "position",
                    "technology" , "it", "qualification" , "academic", "experience", "department" , "email" , "e-mail"]

        new_content = self.removing_extra(text)
        
        nlp_text = nlp(new_content)
        
        punctuations = '''!()-[]{};:'"\,<>/?@#$%^&*_~'''

        pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
        
        matcher.add('NAME', [pattern])
        
        matches = matcher(nlp_text)

        for match_id, start, end in matches:
            span = nlp_text[start:end]
            foundwords = span.text.lower().split()
            found = 0
            for word in foundwords:
                if word in ignore_words:
                    found = 1
                    break

            # If found name has unusual Characters or punctuations discard.
            if not(found):
                token_words = word_tokenize(span.text)
                flag = 0
                for word in token_words:
                    if word in punctuations:
                        flag = 1 
                    break
                if flag == 0:
                    return span.text
        return ""
    
    def extract_phone_number(self , resume_text):
        """ Extracting Contact Number From Text """
        phone = re.findall(self.PHONE_REG, resume_text)
        if phone:
            number = ''.join(phone[0])
            if resume_text.find(number) >= 0 and len(number) < 16:
                number = number.replace("-" , "")
                number = number.replace("(" , "")
                number = number.replace(")" , "")
                number = number.replace(" " , "")
                return number
        return None

    def extract_emails(self, resume_text):
        """ Extracting Email ID From Text """
        return re.findall(self.EMAIL_REG, resume_text)

    def process_emails(self , emailID):
        """ Correcting Spelling Mistakes of Gmail """
        # Identifying the string slicing for gmail
        if type(emailID) == list:
            emailNum = 0
            for eml in emailID:
                for i in range(len(eml)):
                    if eml[i] == '@':
                        index1 = i
                        break
                for j in range(index1 , len(eml)):
                    if eml[j] == '.':
                        index2 = j
                        break
                if eml[index1 + 1:index2] == 'qmail' or eml[index1 + 1:index2] == 'gqmail':
                    part1 = eml[0:index1 + 1]
                    part2 = eml[index1 + 1 : index2]
                    part3 = eml[index2:len(eml)]
                    eml = part1 + 'gmail' + part3
                    emailID[emailNum] = eml
                    emailNum =  emailNum + 1
        else:
            for i in range(len(emailID)):
                if emailID[i] == '@':
                    index1 = i
                    break
            for j in range(index1 , len(emailID)):
                if emailID[j] == '.':
                    index2 = j
                    break
            part1 = emailID[0:index1 + 1]
            part2 = emailID[index1 + 1 : index2]
            part3 = emailID[index2:len(emailID)]
            emailID = part1 + 'gmail' + part3
        return emailID