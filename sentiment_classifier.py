import csv
import twitter_data as td

def strip_punctuation(word):
    for p_c in punctuation_chars:
        if(word.find(p_c) != -1):             
            word = word.replace(p_c, "")    
    return word

def get_pos(text):
    text = text.lower()
    cnt = 0
    for word in text.split(' '):
        word = strip_punctuation(word)
        if(word in positive_words):
            cnt += 1
    return cnt

def get_neg(text):
    text = text.lower()
    cnt = 0
    for word in text.split(' '):
        word = strip_punctuation(word)
        if(word in negative_words):
            cnt += 1
    return cnt


if __name__ == '__main__':

    td.get_tweets(query = "COVID-19", cnt = 50)

    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
        
    positive_words = []
    with open("files/positive_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                positive_words.append(lin.strip())

    negative_words = []
    with open("files/negative_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                negative_words.append(lin.strip())

    rowstring = ''
    lines = []
    with open("files/project_twitter_data.csv", encoding='utf-8') as twitter_data:        
        reader = csv.reader(twitter_data)    
        for row in reader:
            lines.append(row[0])    
        
    for index in range(1,len(lines)):        
        pos_score = get_pos(lines[index])
        neg_score = get_neg(lines[index])
        net_score = pos_score - neg_score
        rowstring += '{},{},{}'.format(pos_score, neg_score, net_score)        
        rowstring += '\n'    

    with open('files/resulting_data.csv', 'w') as csvfile:      
        csvfile.write('Positive Score, Negative Score, Net Score')  
        csvfile.write('\n')    
        csvfile.write(rowstring)
