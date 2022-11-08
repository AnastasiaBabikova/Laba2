import json
from numpy import array
from pandas.core.common import flatten
from collections import OrderedDict


def Questions(data):
    q=[]
    
    dict1 = []
    dict2 = []
    all_dict = {}
    for item in data:
        #q = item.get('question')#Список вопросов
        
        q.append(item.get('question'))
        q = (list(array(q).flat))
        q = (list(flatten(q)))
        qq=list(OrderedDict.fromkeys(q))#удалить дубликаты вопросов
    print(qq)
    print('-----------------------')


    for question in qq:
        
        if (question == 'Какая погода?'):
            answer = int(input(question + ' (числовое значение): '))
            
           
        else:
            answer = input(question + ' (да/нет): ')
        
        dict1.append({
            'question':question,
           'answer':answer})
        
    print("СЛОВАРЬ",dict1)
    print("-----------------------")
    
    Answer(data,dict1)

    
          
#i - База
def Answer(data,dict1):
    count = []#сколько вопросов в списке
    new_dict = {}
    for it in data:
        k = it.get('question')
        count.append(len(k))
    #print(count)

        
    for i in data:
        k = i.get('question')
        k_1 = i.get('answer')
         
        lenght = len(k)
        if (lenght == 2):
            index = 0
            for x,item in enumerate(dict1):
                p = item.get('question')
                p_1 = item.get('answer')
               
                if(k[index]==p and k_1[index]==p_1):
                   index = index + 1 
                   ind = dict1[x+1]
                   p = ind.get('question')
                   p_1 = ind.get('answer')
                   
                   if(k[index] == p and k_1[index]==p_1):
                        print(i.get('result'))
                        print(i.get('style'))
                        print(i.get('place'))
                        break
                

        if (lenght == 3):
            
            index = 0
            
            for x,item in enumerate(dict1):
                p = item.get('question')
                p_1 = item.get('answer')
                
                if((str(k[index]))==str(p) and str(p_1)>= str(k_1[index])):
                    index = index +1
                    ind = dict1[x+1]
                    p = ind.get('question')
                    p_1 = ind.get('answer')
                    
                    if(k[index]==p and k_1[index]==p_1):
                        index = index + 1 
                        ind = dict1[x+2]
                        p = ind.get('question')
                        p_1 = ind.get('answer')
                   
                        if(k[index] == p and k_1[index]==p_1):
                            print(i.get('result'))
                            print(i.get('style'))
                            print(i.get('place'))
                            break

                    break 
     

def Main():
    with open('base.json', 'r', encoding='utf-8') as fh: #открываем файл на чтение
        data = json.load(fh) #загружаем из файла данные в словарь data
        
        
    print("База знаний", data)

    Questions(data)
    #print(" Dict" , dict1)
    

Main()
