import random
#Paramètres :

#- Mixité de genre des triplettes (2+2 dans les quadruplettes)
#- Brassage des triplettes (jusqu'en 2020)
#- Le/la gestionnaire dans une quadriplette.
#- Tou.te.s les MEEs de chaque colonne de SPé sont dispos ensemble sur au moins 2 gestions (pour ne pas que la même spé tombe 2 fois sur la même gestion).

# LES SPE
# MATHS     ANGLAIS HLP         
# Arts      ESP     SES         
# HGGSP     SVT     PC/NSI?     

# On définit la liste de MEEs
mees = {
        'Gestionnaire': ['F',[],0],
        'Enoch': ['M',['Fanny', 'Mika', 'Flora'],1], 
        'Xavier': ['M',['Julie', 'Flora', 'Adèle', 'Maude'],2], 
        'Davy': ['M',['Maude', 'Maria', 'Nath', 'Fanny', 'Pauline'],3], 
        'Mika': ['M',['Flora','Fanny', 'Enoch', 'Benjamin', 'Xavier'],2], 
        'Clémentine': ['F',['Nath', 'Benjamin', 'Valentin', 'Maria'],0], 
        'Flora': ['F',['Xavier', 'Adèle', 'Julie', 'Fanny', 'Mika', 'Enoch'],1], 
        'Benjamin': ['M',['Nath', 'Clémentine', 'Mika', 'Maria'],3], 
        'Julie': ['F',['Adèle', 'Xavier', 'Flora', 'Valentin', 'Renaud'],3], 
        'Nath': ['F',['Benjamin', 'Davy', 'Clémentine', 'Maude', 'Renaud','Maria'],1], 
        'Fanny': ['F',['Davy', 'Pauline', 'Mika', 'Enoch', 'Flora','Benjamin'],2], 
        'Pauline': ['F',['Davy', 'Fanny','Maria'],2], 
        'Maria': ['F',['Maude', 'Davy', 'Pauline'],0], 
        'Maude': ['F',['Maria', 'Davy', 'Nath', 'Renaud', 'Xavier'],1], 
        'Valentin': ['M',['Julie', 'Clémentine','Maria','Nath', 'Renaud','Julie'],0], 
        'Marie': ['F',[],3], 
        'Renaud': ['M',['Adèle', 'Nath', 'Maude', 'Julie', 'Valentin'],1]
        }
mees_list = list(mees.keys())



def triplettes(mees_list):
    """Fonction pour établir les triplettes au hazard"""
    random.shuffle(mees_list)
    result = []
    result.append(frozenset(mees_list[:3]))
    result.append(frozenset(mees_list[3:6]))
    result.append(frozenset(mees_list[6:9]))
    result.append(frozenset(mees_list[9:13]))
    result.append(frozenset(mees_list[13:]))
    return set(result)


def genre_gb(triplettes):
    i=0
    spe=[]
    for triplette in triplettes:
        genre=[]
        spe.append([])
        for mee in triplette:
            genre.append(mees[mee][0])
            for mee_gb in mees[mee][1]:
                if mee_gb in triplette :
                    return False  
            spe[i].append(mees[mee][2])
        spe[i]=set(spe[i])
        spe[i].discard(0)    
        if len(set(genre)) == 1 or len(spe[i]) > 2:
            return False
        if len(genre)==4:
            if genre.count('M')!=2:
                return False
        i+=1
    for i in range(1,4):
        count=0
        for my_set in spe:
            if i in my_set:
                count += 1
        if count < 3:
            return False
    count=[0,0,0]
    for s in spe:
        for j in range(1,4):
            if j not in s:
                count[j-1]+=1
    for i in count:
        if i<2:
            return False
    return True


def adele(triplettes):
    """Fonction pour ontrôler que Adèle soit dans une quadriplette""" 
    for triplette in triplettes:
        if 'Gestionnaire' in triplette and len(triplette)==4:
            return True
    return False


results=[]

while True:
    #2 - Eviter triplettes non mixtes
    #3 - Eviter qu'un MEE soit dans le même groupe que l'an passé
    test=triplettes(mees_list)
    if adele(test) and genre_gb(test) and test not in results:
        results.append(test)
        trips=[]
        for trip in test:
            trips.append(set(trip))
        print(trips)




