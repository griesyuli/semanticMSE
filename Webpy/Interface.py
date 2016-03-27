import web
from web import form

import os
import fnmatch

import unicodedata
from nltk.corpus import stopwords

def get_hop1(SE,query):
    #-------------- FIND MATCH DOC ----------------------------------
    #searching for documents name in a directory based queries entered
    fileNameHop1 = []
    set_datadir_hop1 = "./data/OntoWiki/Hirarki/"+SE
    for fnhop1 in os.listdir(set_datadir_hop1):
        if fnmatch.fnmatch(fnhop1,("*%s_%s_subquery_hop1*" % (SE,query))):
            fileNameHop1.append(fnhop1)
            docNameHop1 = fnhop1
            #return fileNameHop1
        
    #-------------- STORE DATA IN DOC ----------------
    hop1_data = []
    hop1_null = []
    
    for i in range(len(fileNameHop1)):
        fileNameHop1[i] = set_datadir_hop1 + "/" + fileNameHop1[i]
    for a in fileNameHop1:
        with open(a) as f:
            for t in f:
                try:
                    temp = t.split(' :*: ')
                    temp = temp[1]
                    temp = temp.split(' ;*; ')
                    temp = temp [0]
                    #print temp
                    temp = temp.split(' , ')
                    #print 'temp in hop 1'+temp
                    #hop1_data = temp
                    for t in temp:
                        ts = unicode(t,errors='ignore')
                        hop1_data.append(unicodedata.normalize('NFKD', ts).encode('ascii', 'ignore'))
                        #hop_data.append(t.decode(encoding='UTF-8',errors='strict'))

                except:
                    break

    if hop1_data[0] == '':
        return hop1_null
    else:
        return hop1_data

#----------------------------------------------------------------------------------------------------
def get_another_hop(hop,SE,query):
    #-------------- FIND MATCH DOC ----------------------------------
    #searching for documents name in a directory based queries entered
    fileNameHop = []
    set_datadir_hop = "./data/OntoWiki/Hirarki/"+SE
    for fnhop in os.listdir(set_datadir_hop):
        if fnmatch.fnmatch(fnhop,("*%s_%s_subquery_%s*" % (SE,query,hop))):
            fileNameHop.append(fnhop)
            docNameHop = fnhop
            print fileNameHop
        
    #-------------- STORE DATA IN DOC ----------------
    hop_data = []
    
    for i in range(len(fileNameHop)):
        fileNameHop[i] = set_datadir_hop + "/" + fileNameHop[i]
    for a in fileNameHop:
        with open(a) as f:
            for t in f:
                try:
                    temp = t.split(' ;*; ')
                    temp = temp [0]
                    #print 'temp in another hop'+temp
                    temp = temp.split(' , ')
                    #print temp
                    for t in temp:
                        ts = unicode(t,errors='ignore')
                        hop_data.append(unicodedata.normalize('NFKD', ts).encode('ascii', 'ignore'))
                        #hop_data.append(t.decode(encoding='UTF-8',errors='strict'))
                except:
                    break
    #print hop_data
    return hop_data

#----- mengambil Degree, Closeness, dan Pagerank masing-masing hop 1 untuk QE dari direktori tersimpan -----
def get_stat_ontoWiki(SE,query,hop1,stat):
    
    kata_temp = []
    kata = []

    if hop1 == '':
        return kata
    
    else:
        set_datadir = "./data/OntoWiki/Stat/"+SE
        fileName = query+'_'+SE+'_'+hop1+'_'+stat

        fh = open(set_datadir+"/"+fileName.lower()+".txt")

        for line in fh:
            kalimat = line
            kalimat = kalimat.split('\n')
            kalimat = kalimat[0]
            kata_temp.append(kalimat)
                
        fh.close()

        for t in kata_temp[:]:
            no = kata_temp.index(t)+1
            temp = t.split(str(no)+";(")
            temp = temp[1]
    ##        temp = temp.split(", ")
    ##        temp = temp[0]
            temp = temp.replace("'","")
            temp = temp.replace('"','')
            temp = temp.replace("(","")
            temp = temp.replace(")","")
            temp = unicode(temp,errors='ignore')
            kata.append((unicodedata.normalize('NFKD', temp).encode('ascii', 'ignore')))
            #print baris_1

        return kata[:]

#----- mengambil Degree, Closeness, dan Pagerank pemenang hop 1 untuk QE dari direktori tersimpan -----
def get_stat_ontoWiki_winHop1(SE,query,hop1,stat):
    
    kata_temp = []
    kata = []

    set_datadir = "./data/OntoWiki/Stat/"+SE
    fileName = query+'_'+SE+'_'+hop1+'_'+stat

    fh = open(set_datadir+"/"+fileName.lower()+".txt")

    for line in fh:
        kalimat = line
        kalimat = kalimat.split('\n')
        kalimat = kalimat[0]
        kata_temp.append(kalimat)
            
    fh.close()

    for t in kata_temp[:]:
        no = kata_temp.index(t)+1
        temp = t.split(str(no)+";(")
        temp = temp[1]
        temp = temp.split(", ")
        temp = temp[0]
        temp = temp.replace("'","")
        temp = temp.replace('"','')
        temp = temp.replace("(","")
        temp = temp.replace(")","")
        temp = unicode(temp,errors='ignore')
        kata.append((unicodedata.normalize('NFKD', temp).encode('ascii', 'ignore')))
        #kata.append(temp.decode(encoding='UTF-8',errors='strict'))
        #print baris_1

    #print kata
    return kata[:100]

#----- mengambil irisan Degree, Closeness, dan Pagerank pemenang hop 1 untuk QE dari direktori tersimpan -----
def get_stat_ontoWiki_intersection(SE,query,stat):
    
    kata_temp = []
    kata = []

    set_datadir = "./data/OntoWiki/Intersection/"+SE
    fileName = query+'_'+SE+'_'+stat

    fh = open(set_datadir+"/Intersection_"+fileName.lower()+".txt")

    for line in fh:
        kalimat = line
        kalimat = kalimat.split('\n')
        kalimat = kalimat[0]
        kata_temp.append(kalimat)
            
    fh.close()

    for t in kata_temp[:]:
        no = kata_temp.index(t)+1
        temp = t.split(str(no)+" ;*; ")
        temp = temp[1]
        temp = temp.split(" ;*; ")
        temp = temp[0]
        temp = unicode(temp,errors='ignore')
        kata.append((unicodedata.normalize('NFKD', temp).encode('ascii', 'ignore')))
        #kata.append(temp.decode(encoding='UTF-8',errors='strict'))
        #print baris_1

    #print kata
    return kata[:]

#----- mengambil irisan final Degree, Closeness, dan Pagerank pemenang hop 1 untuk QE dari direktori tersimpan -----
def get_stat_ontoWiki_candidateQE(SE,query):
    
    kata_temp = []
    kata = []

    set_datadir = "./data/OntoWiki/candidate QE/"+SE
    fileName = query+'_'+SE

    fh = open(set_datadir+"/candidateQE_"+fileName.lower()+".txt")

    for line in fh:
        kalimat = line
        kalimat = kalimat.split('\n')
        kalimat = kalimat[0]
        kata_temp.append(kalimat)
            
    fh.close()

    for t in kata_temp[:]:
        no = kata_temp.index(t)+1
        temp = t.split(str(no)+" ;*; ")
        temp = temp[1]
        temp = temp.split(" ;*; ")
        temp = temp[0]
        temp = unicode(temp,errors='ignore')
        kata.append((unicodedata.normalize('NFKD', temp).encode('ascii', 'ignore')))
        #kata.append(temp.decode(encoding='UTF-8',errors='strict'))
        #print baris_1

    #print kata
    return kata[:]

#----- mengambil irisan final per kata untuk QE dari direktori tersimpan -----
def get_stat_ontoWiki_candidateQE_perKata(SE,query):
    
    kata_temp = []
    kata = []

    set_datadir = "./data/OntoWiki/all QE per kata/"+SE
    fileName = query+'_'+SE

    fh = open(set_datadir+"/allQE_"+fileName.lower()+".txt")

    for line in fh:
        kalimat = line
        kalimat = kalimat.split('\n')
        kalimat = kalimat[0]
        kata_temp.append(kalimat)
            
    fh.close()

    for t in kata_temp[:]:
        no = kata_temp.index(t)+1
        temp = t.split(str(no)+" ;*; ")
        temp = temp[1]
        temp = unicode(temp,errors='ignore')
        kata.append((unicodedata.normalize('NFKD', temp).encode('ascii', 'ignore')))
        #kata.append(temp.decode(encoding='UTF-8',errors='strict'))
        #print baris_1

    #print kata
    return kata[:]

#----- mengambil Query Rewriting untuk Wordnet, WikiSynonyms, Moby Thesaurus -----
def get_QR_sinonim(sinonim_engine,k,query):
    
    kata_temp = []
    kata = []

    set_datadir = "./data/QR/"
    fileName = 'query_'+sinonim_engine+'_'+k

    fh = open(set_datadir+"/"+fileName+".txt")

    for line in fh:
        kalimat = line
        kalimat = kalimat.split('\n')
        kalimat = kalimat[0]
        kata_temp.append(kalimat)
            
    fh.close()

    #print kata_temp
    #print query

    for t in kata_temp:
        if fnmatch.fnmatch(t,("*%s*" % (query))):
            kata.append(t)

    #print kata
    return kata

#----- mengambil Sinonim tiap query untuk Wordnet, WikiSynonyms, Moby Thesaurus -----
def get_sinonim_query(sinonim_engine,queryN):
    sino = []

    if queryN == '':
        return sino

    else:
        set_datadir = "./data/QR/Sinonim/Hasil Sinonim/"+sinonim_engine
        fileName = 'Sinonim_'+sinonim_engine+'_'+queryN.lower()

        fh = open(set_datadir+"/"+fileName+".txt")

        for line in fh:
            kalimat = line
            kata = kalimat.split(' ;*; ')
                
            sino_temp = kata[1]
            sino_temp = sino_temp.split('\n')
            sino_name = sino_temp[0].replace('_',' ')
            sino_name = sino_name.replace(')','')
            sino_name = sino_name.replace('(','')
            sino.append(sino_name.lower())
            
        fh.close()
        return sino

#----- mengambil kata Sinonim tiap query untuk Wordnet, WikiSynonyms, Moby Thesaurus -----
def get_kata_sinonim_query(sinonim_engine,queryN):
    sino = []

    if queryN == '':
        return sino

    else:
        set_datadir = "./data/QR/Sinonim/Hasil Kata/"+sinonim_engine
        fileName = 'kataQuery_'+sinonim_engine+'_'+queryN.lower()

        fh = open(set_datadir+"/"+fileName+".txt")

        for line in fh:
            kalimat = line
            
            sino_temp = kalimat.split('\n')
            sino_name = sino_temp[0]
            sino.append(sino_name)
            
        fh.close()
        return sino

#----- mengambil Query Rewriting untuk Wordnet, WikiSynonyms, Moby Thesaurus -----
def get_QR_ontowiki(SE,k,query):
    
    kata_temp = []
    kata = ''

    set_datadir = "./data/QR/WMIR"
    fileName = 'query_'+k+'_'+SE

    fh = open(set_datadir+"/"+fileName+".txt")

    for line in fh:
        kalimat = line
        kalimat = kalimat.split('\n')
        kalimat = kalimat[0]
        kata_temp.append(kalimat)
            
    fh.close()

    #print kata_temp
    #print query

    for t in kata_temp:
        if fnmatch.fnmatch(t,("*%s*" % (query))):
            kata = t

    #print kata
    return kata

#----- mengambil pemenang hop 1 OntoWiki -----
def get_win_hop1(SE,query):
    
    win = ''

    set_datadir = "./data/OntoWiki/Winner Hop1/"+SE
    fileName = 'WinnerHop1_'+query.lower()+'_'+SE.lower()

    fh = open(set_datadir+"/"+fileName+".txt")

    for line in fh:
        kalimat = line
        temp = kalimat
        kata = unicode(temp,errors='ignore')
        win = unicodedata.normalize('NFKD', kata).encode('ascii', 'ignore')

            
    fh.close()

    return win

#------------------------------------------ Read data SE ---------------------------------
def get_dataDoc_perSE(QE,source,SE,query):
    
    SE_code = ''
    if SE == ('Google'):
        SE_code = 'SE1'
    elif SE == ('Bing'):
        SE_code = 'SE2'
    elif SE == ('Lycos'):
        SE_code = 'SE3'
    elif SE == ('Exalead'):
        SE_code = 'SE4'
    else:
        SE_code = 'SE5'
      
    SE_dataDoc = []
    SE_link = []
    SE_title = []
    SE_snippet = []
    
    set_datadir = "./data/Hasil SE/"+QE+"/"+source+"/"+SE
    fileName = "List_LinksAndSnippets_"+SE_code+"_200pg_"+query.lower()

    fh = open(set_datadir+"/"+fileName+".txt")

    for line in fh:
       kalimat = line
       kata = kalimat.split(' ;*; ')
       data_temp = []
       url_name = kata[1]
       title = kata[2]
       snippet = kata[3]
       
       data_temp.append(url_name)
       SE_link.append(url_name)
       
       data_temp.append(title.decode('ascii','ignore'))
       SE_title.append(title.decode('ascii','ignore'))
       
       data_temp.append(snippet.decode('ascii','ignore'))
       SE_snippet.append(snippet.decode('ascii','ignore'))
       
       SE_dataDoc.append(data_temp)

    fh.close()
   
    return SE_dataDoc,SE_link,SE_title,SE_snippet


#=================================================================================================            

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/src/(.*)', 'src',
    '/data/(.*)', 'data',
    '/images/favicon.ico', 'icon'
)


app = web.application(urls, globals())

#web.config.debug = True
# ===========
# Input form 
# ===========
myform = form.Form(
    form.Textbox("Query_1", type="text", placeholder="First Query"),
    form.Dropdown('Operator_1', ['',' OR ', ' AND '], type="text"),
    form.Textbox("Query_2", type="text", placeholder="Second Query"),
    form.Dropdown('Operator_2', ['',' OR ', ' AND '], type="text"),
    form.Textbox("Query_3", type="text", placeholder="Third Query"),
    form.Checkbox('search_engine1',value='SE1',id="se"),
    form.Checkbox('search_engine2',value='SE2',id="se"),
    form.Checkbox('search_engine3',value='SE3',id="se"),
    form.Checkbox('search_engine4',value='SE4',id="se"),
    form.Checkbox('search_engine5',value='SE5',id="se"),
    form.Dropdown('pages',[]),
    form.Dropdown('pages2',[]),
    form.Dropdown('SE_drop',[]),
    form.Radio('radio_QE',[('K2','2'),('K3','3')]),
    form.Radio('source',[('Wordnet','Wordnet'),('WikiSynonyms','Wiki Synonyms'),('MobyThesaurus','Moby Thesaurus'),('WMIR','Wikipedia Ontology')]))
# ===========
# Classes 
# ===========
class index:
    def GET(self):
        #return render.page_1("Hello Gries Yulianti, Welcome to web.py")

        my_form = myform()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        query1 = my_form.Query_1.render()
        operator1 = my_form.Operator_1.render()
        query2 = my_form.Query_2.render()
        operator2 = my_form.Operator_2.render()
        query3 = my_form.Query_3.render()
        searchEngine1 = my_form.search_engine1.render()
        searchEngine2 = my_form.search_engine2.render()
        searchEngine3 = my_form.search_engine3.render()
        searchEngine4 = my_form.search_engine4.render()
        searchEngine5 = my_form.search_engine5.render()
        radioQE = my_form.radio_QE.render()
        sources = my_form.source.render()
        formAction = web.input()
        page = my_form.pages.render()
        page2 = my_form.pages2.render()
        SEdrop = my_form.SE_drop.render()
        
        return render.page_1(query1,operator1,
                             query2,operator2,
                             query3,
                             searchEngine1,
                             searchEngine2,
                             searchEngine3,
                             searchEngine4,
                             searchEngine5,radioQE,sources)
        

    
    def POST(self):
        #return "post"
        
        my_form = myform()
        query1 = my_form.Query_1
        operator1 = my_form.Operator_1
        query2 = my_form.Query_2
        operator2 = my_form.Operator_2
        query3 = my_form.Query_3
        searchEngine1 = my_form.search_engine1
        searchEngine2 = my_form.search_engine2
        searchEngine3 = my_form.search_engine3
        searchEngine4 = my_form.search_engine4
        searchEngine5 = my_form.search_engine5
        radioQE = my_form.radio_QE
        sources = my_form.source
        formAction = web.input()
        #print formAction
        page = my_form.pages
        page2 = my_form.pages2
        SEdrop = my_form.SE_drop
        
        if not my_form.validates():
            return render.page_1(my_form)
            
        else:            
            print formAction
            
            #print win

            SE = []

            SE1 = my_form['search_engine1'].get_value()
            if SE1 == True:
                SE.append('SE1')
            SE3 = my_form['search_engine3'].get_value()
            if SE3 == True:
                SE.append('SE3')
            SE2 = my_form['search_engine2'].get_value()
            if SE2 == True:
                SE.append('SE2')
            SE5 = my_form['search_engine5'].get_value()
            if SE5 == True:
                SE.append('SE5')
            SE4 = my_form['search_engine4'].get_value()
            if SE4 == True:
                SE.append('SE4')

            
            #SE2 = web.input(my_form['search_engine1'])
            print SE
            query = ''
            if len(SE) != 3:
                print 'Select SE WRONG'
                message = "Select 3 of 5 search engine"
                return render.page_1_a(query1,operator1,
                             query2,operator2,
                             query3,
                             searchEngine1,
                             searchEngine2,
                             searchEngine3,
                             searchEngine4,
                             searchEngine5,
                             radioQE,sources,message)
                
            else:
                print 'Select SE TRUE'

            # --- Name SE combination ---
            SE_all = ["SE1", "SE3", "SE2", "SE5", "SE4"]

            SE_combination = []
            SE_choose1 = [SE_all[0],SE_all[1],SE_all[2]]
            SE_choose2 = [SE_all[0],SE_all[1],SE_all[3]]
            SE_choose3 = [SE_all[0],SE_all[1],SE_all[4]]
            SE_choose4 = [SE_all[0],SE_all[2],SE_all[3]]
            SE_choose5 = [SE_all[0],SE_all[2],SE_all[4]]
            SE_choose6 = [SE_all[0],SE_all[3],SE_all[4]]
            SE_choose7 = [SE_all[1],SE_all[2],SE_all[3]]
            SE_choose8 = [SE_all[1],SE_all[2],SE_all[4]]
            SE_choose9 = [SE_all[1],SE_all[3],SE_all[4]]
            SE_choose10 = [SE_all[2],SE_all[3],SE_all[4]]

            SE_combination.append(SE_choose1)
            SE_combination.append(SE_choose2)
            SE_combination.append(SE_choose3)
            SE_combination.append(SE_choose4)
            SE_combination.append(SE_choose5)
            SE_combination.append(SE_choose6)
            SE_combination.append(SE_choose7)
            SE_combination.append(SE_choose8)
            SE_combination.append(SE_choose9)
            SE_combination.append(SE_choose10)
    
            SE_com_name = ["SE_com_01","SE_com_02","SE_com_03","SE_com_04","SE_com_05",
                           "SE_com_06","SE_com_07","SE_com_08","SE_com_09","SE_com_10"]
   
            SE_com = ''
            if SE == SE_combination[0]:
                SE_com = SE_com_name[0]
                
            elif SE == SE_combination[1]:
                SE_com = SE_com_name[1]
                
            elif SE == SE_combination[2]:
                SE_com = SE_com_name[2]
                
            elif SE == SE_combination[3]:
                SE_com = SE_com_name[3]
                
            elif SE == SE_combination[4]:
                SE_com = SE_com_name[4]
                
            elif SE == SE_combination[5]:
                SE_com = SE_com_name[5]
                
            elif SE == SE_combination[6]:
                SE_com = SE_com_name[6]
                
            elif SE == SE_combination[7]:
                SE_com = SE_com_name[7]
                
            elif SE == SE_combination[8]:
                SE_com = SE_com_name[8]
                
            else:
                SE_com = SE_com_name[9]

            print SE_com
                
            # --- extracting form ---
            query = my_form['Query_1'].get_value()+my_form['Operator_1'].get_value()+my_form['Query_2'].get_value()+my_form['Operator_2'].get_value()+my_form['Query_3'].get_value()
            
            print query
            if query == '':
                print 'Query kosong'
                message = "Input Query"
                return render.page_1_a(query1,operator1,
                                       query2,operator2,
                                       query3,
                                       searchEngine1,
                                       searchEngine2,
                                       searchEngine3,
                                       searchEngine4,
                                       searchEngine5,
                                       radioQE,sources,message)
                

            QE = my_form['radio_QE'].get_value()
            print QE

            source = my_form['source'].get_value()
            print source
                        
            #-------------- FIND MATCH DOC ----------------------------------
            #searching for documents name in a directory based queries entered
            fileName = []
            set_datadir = "./data/Result/"+QE+"/"+source
            for fn in os.listdir(set_datadir):
                if fnmatch.fnmatch(fn,("*%s_%s_%s*" % (query,QE,SE_com))):
                    fileName.append(fn)
                    docName = fn
            print 'File Name'
            print fileName

            if len(fileName) == 0:
                print 'Data Not Found'
                message = "Data Not Found"
                return render.page_1_a(query1,operator1,
                                       query2,operator2,
                                       query3,
                                       searchEngine1,
                                       searchEngine2,
                                       searchEngine3,
                                       searchEngine4,
                                       searchEngine5,
                                       radioQE,sources,message)
           
            #-------------- Get data Query Rewriting ---------------
            print '\n==--- Query Rewriting ---=='

            SE_drop_args = []
            SEuse = []
            
            for SEs in SE:
                if SEs == 'SE1':
                    SE_drop_args.append('Google')
                elif SEs == 'SE2':
                    SE_drop_args.append('Bing')
                elif SEs == 'SE3':
                    SE_drop_args.append('Lycos')
                elif SEs == 'SE4':
                    SE_drop_args.append('Exalead')
                else:
                    SE_drop_args.append('Ask')

            #print SE_drop_args
            
            if source == 'WikiSynonyms':
                print 'wikisynonyms'
                data_qr = get_QR_sinonim(source,QE,query)
                
                SEuse.append('')
                print SEuse             
                SEdrop.args=[x for x in SE_drop_args]
                
            elif source == 'Wordnet':
                print 'wordnet'
                data_qr = get_QR_sinonim(source,QE,query)
                                
                SEuse.append('')
                print SEuse

                print SE_drop_args
                SEdrop.args=[x for x in SE_drop_args]
                
            elif source == 'MobyThesaurus':
                print 'MobyThesaurus'
                data_qr = get_QR_sinonim(source,QE,query)
                
                SEuse.append('')
                print SEuse             
                SEdrop.args=[x for x in SE_drop_args]
                
            else:
                print 'WMIR / OntoWiki'
                SEuse = SE_drop_args
                print SEuse             

                print SE_drop_args
                SEdrop.args=[x for x in SE_drop_args]
                
                data_qr = []
                data_qr_SE1 = get_QR_ontowiki(SE_drop_args[0],QE,query)
                data_qr.append(data_qr_SE1)

                data_qr_SE2 = get_QR_ontowiki(SE_drop_args[1],QE,query)
                data_qr.append(data_qr_SE2)

                data_qr_SE3 = get_QR_ontowiki(SE_drop_args[2],QE,query)
                data_qr.append(data_qr_SE3)
                print data_qr
                
                
            #-------------- STORE DATA IN DOC INTO TEMP FILE ----------------
            print '\n==--- Data DOC ---=='

            tempKeyword = []
            tempDocPerKw = []
            tempRank = []
            tempLink = []
            tempTitle = []
            tempSnippet = []
            tempDate = []
            outputKW = []
            outputSE = []
            

            for i in range(len(fileName)):
                fileName[i] = set_datadir + "/" + fileName[i]
            for a in fileName:
                with open(a) as f:
                    for t in f:
                        try:
                            temp = t.split(";*;")
                            tempRank.append(temp[0]) #rank doc
                            tempLink.append(temp[1]) #link doc
                            tempTitle.append(temp[2].decode('ascii','ignore')) #title doc
                            tempSnippet.append(temp[3].decode('ascii','ignore')) #snippet doc
                            line = ""
                        except:
                            break
            # Compress multiple array variables into a single variable
            DataDoc = zip(tempRank, tempLink, tempTitle, tempSnippet)

            ddList = []
            tempData = 0
            countDoc = 0
            
            outputSE = []
            
            print "total document : "+str(len(DataDoc))
            
            pageIndex = int((len(DataDoc)/10)+(len(DataDoc)%10>0))
            print 'Index Page = '+str(pageIndex)

            #print outputSE[0]

            page.args=[x+1 for x in range(pageIndex)]

            button_do = formAction.form_action
            print button_do


            if button_do == 'Search':
                nowPage = 1
                return render.page_2(query1,operator1,query2,
                                     operator2,query3,
                                     searchEngine1,searchEngine2,searchEngine3,
                                     searchEngine4,searchEngine5,
                                     radioQE,sources,data_qr,SEuse,
                                     tempLink[0:10],tempTitle[0:10],tempSnippet[0:10],
                                     page,nowPage,(len(DataDoc)),0)

            elif button_do == 'Go':
                print 'Next'
                print page.get_value()
                index = int(page.get_value())
                print type(index)
                nowPage=index

                start = (index-1)*10
                print start
                finish = start+10
                print finish
                return render.page_2(query1,operator1,
                                     query2,operator2,
                                     query3,
                                     searchEngine1,
                                     searchEngine2,
                                     searchEngine3,
                                     searchEngine4,
                                     searchEngine5,
                                     radioQE,sources,
                                     data_qr,SEuse,
                                     tempLink[start:finish],tempTitle[start:finish],
                                     tempSnippet[start:finish],page,nowPage,(len(DataDoc)),start)
 
            elif (button_do == 'Detail') & ((source == 'Wordnet') | (source == 'WikiSynonyms') | (source == 'MobyThesaurus')):
                
                print "Detail Sinonim"
                q1 = my_form['Query_1'].get_value()
                q2 = my_form['Query_2'].get_value()
                q3 = my_form['Query_3'].get_value()
                
                q1_sinonim = get_sinonim_query(source,q1)
                #print q1_sinonim
                q2_sinonim = get_sinonim_query(source,q2)
                #print q2_sinonim
                q3_sinonim = get_sinonim_query(source,q3)
                #print q3_sinonim

                q1_data_kata = get_kata_sinonim_query(source,q1)
                q2_data_kata = get_kata_sinonim_query(source,q2)
                q3_data_kata = get_kata_sinonim_query(source,q3)
                
                return render.page_detail_sinonim(query1,operator1,query2,
                                                  operator2,query3,
                                                  searchEngine1,searchEngine2,searchEngine3,
                                                  searchEngine4,searchEngine5,radioQE,sources,
                                                  q1,q1_sinonim,q2,q2_sinonim,q3,q3_sinonim,
                                                  q1_data_kata,q2_data_kata,q3_data_kata,
                                                  data_qr[0])

            elif (button_do == 'Next') & ((source == 'Wordnet') | (source == 'WikiSynonyms') | (source == 'MobyThesaurus')):
                print "\n+++ Document per SE +++"
                print "Dokumen Sinonim Next"

                nowPage2 = 1

                SEnow = SE_drop_args[0]
                print SEnow

                SE_dataDoc,SE_link,SE_title,SE_snippet = get_dataDoc_perSE(QE,source,SEnow,query)
                #print len(SE_dataDoc)

                print "total document : "+str(len(SE_dataDoc))
            
                pageIndex2 = int((len(SE_dataDoc))/10)+((len(SE_dataDoc))%10>0)
                print 'Index Page = '+str(pageIndex2)

                #print outputSE[0]

                page2.args=[x+1 for x in range(pageIndex2)]

                return render.page_dokumenSE_sinonim(query1,operator1,query2,
                                                     operator2,query3,
                                                     searchEngine1,searchEngine2,searchEngine3,
                                                     searchEngine4,searchEngine5,radioQE,sources,
                                                     SEdrop, data_qr[0],
                                                     SE_link[0:10],SE_title[0:10],SE_snippet[0:10],
                                                     page2,nowPage2,(len(SE_dataDoc)),0)

            elif (button_do == 'See') & ((source == 'Wordnet') | (source == 'WikiSynonyms') | (source == 'MobyThesaurus')):

                print "\n+++ Document per SE +++"
                print "Dokumen Sinonim Next See button click"

                nowPage2 = 1
                
                SEnow = SEdrop.get_value()
                print "SE NOW "+SEnow

                SE_dataDoc,SE_link,SE_title,SE_snippet = get_dataDoc_perSE(QE,source,SEnow,query)
                #print len(SE_dataDoc)

                print "total document : "+str(len(SE_dataDoc))
            
                pageIndex2 = int((len(SE_dataDoc))/10)+((len(SE_dataDoc))%10>0)
                print 'Index Page = '+str(pageIndex2)

                #print outputSE[0]

                page2.args=[x+1 for x in range(pageIndex2)]

                return render.page_dokumenSE_sinonim(query1,operator1,query2,
                                                     operator2,query3,
                                                     searchEngine1,searchEngine2,searchEngine3,
                                                     searchEngine4,searchEngine5,radioQE,sources,
                                                     SEdrop,data_qr[0],
                                                     SE_link[0:10],SE_title[0:10],SE_snippet[0:10],
                                                     page2,nowPage2,(len(SE_dataDoc)),0)
                
            elif (button_do == 'GO') & ((source == 'Wordnet') | (source == 'WikiSynonyms') | (source == 'MobyThesaurus')):

                print "\n+++ Document per SE next page+++"
                print "Dokumen Sinonim Next GO button click"

                print page2.get_value()
                index2 = int(page2.get_value())
                print type(index2)
                nowPage2 = index2

                start2 = (index2-1)*10
                print start2
                finish2 = start2+10
                print finish2

                SEnow = SEdrop.get_value()
                print SEnow

                SE_dataDoc,SE_link,SE_title,SE_snippet = get_dataDoc_perSE(QE,source,SEnow,query)
                #print len(SE_dataDoc)

                print "total document : "+str(len(SE_dataDoc))
            
                pageIndex2 = int((len(SE_dataDoc))/10)+((len(SE_dataDoc))%10>0)
                print 'Index Page = '+str(pageIndex2)

                page2.args=[x+1 for x in range(pageIndex2)]

                return render.page_dokumenSE_sinonim(query1,operator1,query2,
                                                     operator2,query3,
                                                     searchEngine1,searchEngine2,searchEngine3,
                                                     searchEngine4,searchEngine5,radioQE,sources,
                                                     SEdrop,data_qr[0],
                                                     SE_link[start2:finish2],SE_title[start2:finish2],
                                                     SE_snippet[start2:finish2],
                                                     page2,nowPage2,(len(SE_dataDoc)),start2)

            elif (button_do == 'Back') & ((source == 'Wordnet') | (source == 'WikiSynonyms') | (source == 'MobyThesaurus')):
                
                print "Detail Sinonim"
                q1 = my_form['Query_1'].get_value()
                q2 = my_form['Query_2'].get_value()
                q3 = my_form['Query_3'].get_value()
                
                q1_sinonim = get_sinonim_query(source,q1)
                #print q1_sinonim
                q2_sinonim = get_sinonim_query(source,q2)
                #print q2_sinonim
                q3_sinonim = get_sinonim_query(source,q3)
                #print q3_sinonim

                q1_data_kata = get_kata_sinonim_query(source,q1)
                q2_data_kata = get_kata_sinonim_query(source,q2)
                q3_data_kata = get_kata_sinonim_query(source,q3)
                
                return render.page_detail_sinonim(query1,operator1,query2,
                                                  operator2,query3,
                                                  searchEngine1,searchEngine2,searchEngine3,
                                                  searchEngine4,searchEngine5,radioQE,sources,
                                                  q1,q1_sinonim,q2,q2_sinonim,q3,q3_sinonim,
                                                  q1_data_kata,q2_data_kata,q3_data_kata,
                                                  data_qr[0])

#----------------------------------------- Onto Wiki --------------------------------------------
            elif (button_do == 'Detail') & ((source == 'WMIR')):
                print "Detail OntoWiki"
                #--- Get Data Hop 1, Hop 2, and Hop 1 ---
                hop1_data = get_hop1(SE_drop_args[0],query)
                print 'Data Hop1'
                print hop1_data

                hop2_data = get_another_hop('hop2',SE_drop_args[0],query)
                print 'Data Hop2'
                #print hop2_data

                hop3_data = get_another_hop('hop3',SE_drop_args[0],query)
                print 'Data Hop3'
                #print hop3_data

                #--- Get degree, closeness, and pagerank
                degree_all = []
                closeness_all = []
                pagerank_all = []

                for z in range(len(hop1_data)):
                    degree_temp = []
                    closeness_temp = []
                    pagerank_temp = []
                        
                    degree = get_stat_ontoWiki(SE_drop_args[0],query,hop1_data[z],'degree')
                    closeness = get_stat_ontoWiki(SE_drop_args[0],query,hop1_data[z],'closeness')
                    pagerank = get_stat_ontoWiki(SE_drop_args[0],query,hop1_data[z],'pagerank')

                    degree_temp.append(hop1_data[z])
                    degree_temp.append(degree)

                    degree_all.append(degree_temp)

                    closeness_temp.append(hop1_data[z])
                    closeness_temp.append(closeness)

                    closeness_all.append(closeness_temp)

                    pagerank_temp.append(hop1_data[z])
                    pagerank_temp.append(pagerank)

                    pagerank_all.append(pagerank_temp)

                print len(degree_all) #hop1                
                #print len(degree_all[0][1]) #hop1 degree1

                #--- Get Hop 1 win ---
                hop1_win = get_win_hop1(SE_drop_args[0],query)
                print hop1_win

                degree_win = get_stat_ontoWiki_winHop1(SE_drop_args[0],query,hop1_win,'degree')
                closeness_win = get_stat_ontoWiki_winHop1(SE_drop_args[0],query,hop1_win,'closeness')
                pagerank_win = get_stat_ontoWiki_winHop1(SE_drop_args[0],query,hop1_win,'pagerank')

                degree_intersection = get_stat_ontoWiki_intersection(SE_drop_args[0],query,'degree')
                closeness_intersection = get_stat_ontoWiki_intersection(SE_drop_args[0],query,'closeness')
                pagerank_intersection = get_stat_ontoWiki_intersection(SE_drop_args[0],query,'pagerank')

                intersection_final = get_stat_ontoWiki_candidateQE(SE_drop_args[0],query)
                intersection_final_perKata = get_stat_ontoWiki_candidateQE_perKata(SE_drop_args[0],query)

                qr_final = get_QR_ontowiki(SE_drop_args[0],QE,query)

                #--- Return to page html ---                
                return render.page_detail_ontoWiki(query1,operator1,query2,
                                                   operator2,query3,
                                                   searchEngine1,searchEngine2,searchEngine3,
                                                   searchEngine4,searchEngine5,radioQE,sources,SEdrop,
                                                   hop1_data,hop2_data,hop3_data,
                                                   degree_all,closeness_all,pagerank_all,
                                                   hop1_win,degree_win,closeness_win,pagerank_win,
                                                   degree_intersection,closeness_intersection,pagerank_intersection,
                                                   intersection_final,intersection_final_perKata,qr_final)
            
            elif (button_do == 'See') & ((source == 'WMIR')):
                print "Detail OntoWiki"
                SEgo = SEdrop.get_value()
                print SEgo
                
                #--- Get Data Hop 1, Hop 2, and Hop 1 ---
                hop1_data = get_hop1(SEgo,query)
                print 'Data Hop1'
                print hop1_data

                hop2_data = get_another_hop('hop2',SEgo,query)
                print 'Data Hop2'
                #print hop2_data

                hop3_data = get_another_hop('hop3',SEgo,query)
                print 'Data Hop3'
                #print hop3_data

                #--- Get degree, closeness, and pagerank
                degree_all = []
                closeness_all = []
                pagerank_all = []

                for z in range(len(hop1_data)):
                    degree_temp = []
                    closeness_temp = []
                    pagerank_temp = []
                        
                    degree = get_stat_ontoWiki(SEgo,query,hop1_data[z],'degree')
                    closeness = get_stat_ontoWiki(SEgo,query,hop1_data[z],'closeness')
                    pagerank = get_stat_ontoWiki(SEgo,query,hop1_data[z],'pagerank')

                    degree_temp.append(hop1_data[z])
                    degree_temp.append(degree)

                    degree_all.append(degree_temp)

                    closeness_temp.append(hop1_data[z])
                    closeness_temp.append(closeness)

                    closeness_all.append(closeness_temp)

                    pagerank_temp.append(hop1_data[z])
                    pagerank_temp.append(pagerank)

                    pagerank_all.append(pagerank_temp)

                print len(degree_all) #hop1                
                #print len(degree_all[0][1]) #hop1 degree1

                #--- Get Hop 1 win ---
                hop1_win = get_win_hop1(SEgo,query)
                print hop1_win

                degree_win = get_stat_ontoWiki_winHop1(SEgo,query,hop1_win,'degree')
                closeness_win = get_stat_ontoWiki_winHop1(SEgo,query,hop1_win,'closeness')
                pagerank_win = get_stat_ontoWiki_winHop1(SEgo,query,hop1_win,'pagerank')

                degree_intersection = get_stat_ontoWiki_intersection(SEgo,query,'degree')
                closeness_intersection = get_stat_ontoWiki_intersection(SEgo,query,'closeness')
                pagerank_intersection = get_stat_ontoWiki_intersection(SEgo,query,'pagerank')

                intersection_final = get_stat_ontoWiki_candidateQE(SEgo,query)
                intersection_final_perKata = get_stat_ontoWiki_candidateQE_perKata(SEgo,query)

                qr_final = get_QR_ontowiki(SEgo,QE,query)

                #--- Return to page html ---                
                return render.page_detail_ontoWiki(query1,operator1,query2,
                                                   operator2,query3,
                                                   searchEngine1,searchEngine2,searchEngine3,
                                                   searchEngine4,searchEngine5,radioQE,sources,SEdrop,
                                                   hop1_data,hop2_data,hop3_data,
                                                   degree_all,closeness_all,pagerank_all,
                                                   hop1_win,degree_win,closeness_win,pagerank_win,
                                                   degree_intersection,closeness_intersection,pagerank_intersection,
                                                   intersection_final,intersection_final_perKata,qr_final)

            elif (button_do == 'Next') & ((source == 'WMIR')):

                print "\n+++ Dokumen OntoWiki Next per SE +++"

                nowPage2 = 1

                SEnow = SEdrop.get_value()
                print SEnow

                SE_dataDoc,SE_link,SE_title,SE_snippet = get_dataDoc_perSE(QE,source,SEnow,query)
                #print len(SE_dataDoc)

                print "total document : "+str(len(SE_dataDoc))
            
                pageIndex2 = int((len(SE_dataDoc))/10)+((len(SE_dataDoc))%10>0)
                print 'Index Page = '+str(pageIndex2)

                #print outputSE[0]

                page2.args=[x+1 for x in range(pageIndex2)]

                qr_final = get_QR_ontowiki(SEnow,QE,query)

                return render.page_dokumenSE_ontoWiki(query1,operator1,query2,
                                                      operator2,query3,
                                                      searchEngine1,searchEngine2,searchEngine3,
                                                      searchEngine4,searchEngine5,radioQE,sources,
                                                      SEdrop,qr_final,
                                                      SE_link[0:10],SE_title[0:10],SE_snippet[0:10],
                                                      page2,nowPage2,(len(SE_dataDoc)),0)

            elif (button_do == 'see') & ((source == 'WMIR')):

                print "\n+++ Document per SE +++"
                print "Dokumen OntoWiki Next See button click"

                print "\n+++ Document per SE +++"
                print "Dokumen Sinonim Next See button click"

                nowPage2 = 1
                
                SEnow = SEdrop.get_value()
                print "SE NOW "+SEnow

                SE_dataDoc,SE_link,SE_title,SE_snippet = get_dataDoc_perSE(QE,source,SEnow,query)
                #print len(SE_dataDoc)

                print "total document : "+str(len(SE_dataDoc))
            
                pageIndex2 = int((len(SE_dataDoc))/10)+((len(SE_dataDoc))%10>0)
                print 'Index Page = '+str(pageIndex2)

                #print outputSE[0]

                page2.args=[x+1 for x in range(pageIndex2)]

                qr_final = get_QR_ontowiki(SEnow,QE,query)

                return render.page_dokumenSE_ontoWiki(query1,operator1,query2,
                                                      operator2,query3,
                                                      searchEngine1,searchEngine2,searchEngine3,
                                                      searchEngine4,searchEngine5,radioQE,sources,
                                                      SEdrop,qr_final,
                                                      SE_link[0:10],SE_title[0:10],SE_snippet[0:10],
                                                      page2,nowPage2,(len(SE_dataDoc)),0)

            
            elif (button_do == 'GO') & ((source == 'WMIR')):

                print "\n+++ Document per SE OntoWiki next page+++"
                print "Dokumen OntoWiki Next GO button click"

                print page2.get_value()
                index2 = int(page2.get_value())
                print type(index2)
                nowPage2 = index2

                start2 = (index2-1)*10
                print start2
                finish2 = start2+10
                print finish2

                SEnow = SEdrop.get_value()
                print SEnow

                SE_dataDoc,SE_link,SE_title,SE_snippet = get_dataDoc_perSE(QE,source,SEnow,query)
                #print len(SE_dataDoc)

                print "total document : "+str(len(SE_dataDoc))
            
                pageIndex2 = int((len(SE_dataDoc))/10)+((len(SE_dataDoc))%10>0)
                print 'Index Page = '+str(pageIndex2)

                page2.args=[x+1 for x in range(pageIndex2)]

                qr_final = get_QR_ontowiki(SEnow,QE,query)

                return render.page_dokumenSE_ontoWiki(query1,operator1,query2,
                                                      operator2,query3,
                                                      searchEngine1,searchEngine2,searchEngine3,
                                                      searchEngine4,searchEngine5,radioQE,sources,
                                                      SEdrop,qr_final,
                                                      SE_link[start2:finish2],SE_title[start2:finish2],
                                                      SE_snippet[start2:finish2],
                                                      page2,nowPage2,(len(SE_dataDoc)),start2)


            elif (button_do == 'Back') & ((source == 'WMIR')):
                
                print "Detail OntoWiki"
                SEgo = SEdrop.get_value()
                print SEgo
                
                #--- Get Data Hop 1, Hop 2, and Hop 1 ---
                hop1_data = get_hop1(SEgo,query)
                print 'Data Hop1'
                print hop1_data

                hop2_data = get_another_hop('hop2',SEgo,query)
                print 'Data Hop2'
                #print hop2_data

                hop3_data = get_another_hop('hop3',SEgo,query)
                print 'Data Hop3'
                #print hop3_data

                #--- Get degree, closeness, and pagerank
                degree_all = []
                closeness_all = []
                pagerank_all = []

                for z in range(len(hop1_data)):
                    degree_temp = []
                    closeness_temp = []
                    pagerank_temp = []
                        
                    degree = get_stat_ontoWiki(SEgo,query,hop1_data[z],'degree')
                    closeness = get_stat_ontoWiki(SEgo,query,hop1_data[z],'closeness')
                    pagerank = get_stat_ontoWiki(SEgo,query,hop1_data[z],'pagerank')

                    degree_temp.append(hop1_data[z])
                    degree_temp.append(degree)

                    degree_all.append(degree_temp)

                    closeness_temp.append(hop1_data[z])
                    closeness_temp.append(closeness)

                    closeness_all.append(closeness_temp)

                    pagerank_temp.append(hop1_data[z])
                    pagerank_temp.append(pagerank)

                    pagerank_all.append(pagerank_temp)

                print len(degree_all) #hop1                
                #print len(degree_all[0][1]) #hop1 degree1

                #--- Get Hop 1 win ---
                hop1_win = get_win_hop1(SEgo,query)
                print hop1_win

                degree_win = get_stat_ontoWiki_winHop1(SEgo,query,hop1_win,'degree')
                closeness_win = get_stat_ontoWiki_winHop1(SEgo,query,hop1_win,'closeness')
                pagerank_win = get_stat_ontoWiki_winHop1(SEgo,query,hop1_win,'pagerank')

                degree_intersection = get_stat_ontoWiki_intersection(SEgo,query,'degree')
                closeness_intersection = get_stat_ontoWiki_intersection(SEgo,query,'closeness')
                pagerank_intersection = get_stat_ontoWiki_intersection(SEgo,query,'pagerank')

                intersection_final = get_stat_ontoWiki_candidateQE(SEgo,query)
                intersection_final_perKata = get_stat_ontoWiki_candidateQE_perKata(SEgo,query)

                qr_final = get_QR_ontowiki(SEgo,QE,query)

                #--- Return to page html ---                
                return render.page_detail_ontoWiki(query1,operator1,query2,
                                                   operator2,query3,
                                                   searchEngine1,searchEngine2,searchEngine3,
                                                   searchEngine4,searchEngine5,radioQE,sources,SEdrop,
                                                   hop1_data,hop2_data,hop3_data,
                                                   degree_all,closeness_all,pagerank_all,
                                                   hop1_win,degree_win,closeness_win,pagerank_win,
                                                   degree_intersection,closeness_intersection,pagerank_intersection,
                                                   intersection_final,intersection_final_perKata,qr_final)

###---------- Show Query Rewriting Process ----------
##            print '\n==--- Query Rewriting Process ---=='
##            SE_drop_args = []
##            
##            for SEs in SE:
##                if SEs == 'SE1':
##                    SE_drop_args.append('Google')
##                elif SEs == 'SE2':
##                    SE_drop_args.append('Bing')
##                elif SEs == 'SE3':
##                    SE_drop_args.append('Lycos')
##                elif SEs == 'SE4':
##                    SE_drop_args.append('Exalead')
##                else:
##                    SE_drop_args.append('Ask')
##
##            print SE_drop_args
##
##            stop = stopwords.words('english')
##            query_drop = [i for i in query.lower().split() if i not in stop]
##            print query_drop
##            
##                
##            if source == 'WMIR':
##                print 'ontologi wikipedia'
##
##                SEdrop.args=[x for x in SE_drop_args]
##
##                if formAction != web.input(form_action='Go'):
##                
##                    hop1_data = get_hop1(SE_drop_args[0],query)
##                    print 'Data Hop1'
##                    print hop1_data
##
##                    hop2_data = get_another_hop('hop2',SE_drop_args[0],query)
##                    print 'Data Hop2'
##                    #print hop2_data
##
##                    hop3_data = get_another_hop('hop3',SE_drop_args[0],query)
##                    print 'Data Hop3'
##                    #print hop3_data
##
##                    degree_all = []
##                    closeness_all = []
##                    pagerank_all = []
##
##                    for z in range(len(hop1_data)):
##                        degree_temp = []
##                        closeness_temp = []
##                        pagerank_temp = []
##                        
##                        degree = get_stat_ontoWiki(SE_drop_args[0],query,hop1_data[z],'degree')
##                        closeness = get_stat_ontoWiki(SE_drop_args[0],query,hop1_data[z],'closeness')
##                        pagerank = get_stat_ontoWiki(SE_drop_args[0],query,hop1_data[z],'pagerank')
##
##                        degree_temp.append(hop1_data[z])
##                        degree_temp.append(degree)
##
##                        degree_all.append(degree_temp)
##
##                        closeness_temp.append(hop1_data[z])
##                        closeness_temp.append(closeness)
##
##                        closeness_all.append(closeness_temp)
##
##                        pagerank_temp.append(hop1_data[z])
##                        pagerank_temp.append(pagerank)
##
##                        pagerank_all.append(pagerank_temp)
##
##                    print len(degree_all) #hop1
##                    print len(degree_all[0][1]) #hop1 degree1
##                        
##
##                    return render.page_QR_ontoWiki(query1,operator1,query2,operator2,query3,
##                                                   searchEngine1,searchEngine2,searchEngine3,
##                                                   searchEngine4,searchEngine5,radioQE,sources,
##                                                   SEdrop,hop1_data,degree_all,closeness_all,pagerank_all)
##            
##                else:
##
##                    SEgo = SEdrop.get_value()
##                    
##                    hop1_data = get_hop1(SEgo,query)
##                    print 'Data Hop1'
##                    print hop1_data
##
##                    hop2_data = get_another_hop('hop2',SEgo,query)
##                    print 'Data Hop2'
##                    #print hop2_data
##
##                    hop3_data = get_another_hop('hop3',SEgo,query)
##                    print 'Data Hop3'
##                    #print hop3_data
##
##                    degree_all = []
##                    closeness_all = []
##                    pagerank_all = []
##
##                    for z in range(len(hop1_data)):
##                        degree_temp = []
##                        closeness_temp = []
##                        pagerank_temp = []
##                        
##                        degree = get_stat_ontoWiki(SEgo,query,hop1_data[z],'degree')
##                        closeness = get_stat_ontoWiki(SEgo,query,hop1_data[z],'closeness')
##                        pagerank = get_stat_ontoWiki(SEgo,query,hop1_data[z],'pagerank')
##
##                        degree_temp.append(hop1_data[z])
##                        degree_temp.append(degree)
##
##                        degree_all.append(degree_temp)
##
##                        closeness_temp.append(hop1_data[z])
##                        closeness_temp.append(closeness)
##
##                        closeness_all.append(closeness_temp)
##
##                        pagerank_temp.append(hop1_data[z])
##                        pagerank_temp.append(pagerank)
##
##                        pagerank_all.append(pagerank_temp)
##
##                    print len(degree_all) #hop1
##                    print len(degree_all[0][1]) #hop1 degree1
##                        
##
##                    return render.page_QR_ontoWiki(query1,operator1,query2,operator2,query3,
##                                                   searchEngine1,searchEngine2,searchEngine3,
##                                                   searchEngine4,searchEngine5,radioQE,sources,
##                                                   SEdrop,hop1_data,degree_all,closeness_all,pagerank_all)
##
##                
##            elif source == 'WikiSynonyms':
##                print 'wikisynonyms'
##            elif source == 'Wordnet':
##                print 'wordnet'
##            else:
##                print 'MobyThesaurus'


class src:
    def GET(self,name):
        ext = name.split(".")[-1] # Gather extension

        cType = {
            "css":"text/css",
            "js":"text/js"
            }

        if name in os.listdir('src'):  # Security
            web.header("Content-Type", cType[ext]) # Set the Header
            return open('src/%s'%name,"rb").read() # Notice 'rb' for reading images
        else:
            raise web.notfound()

# for page /data/...
class data:
    def GET(self,name):
        ext = name.split(".")[-1] # Gather extension

        cType = {
            "txt":"tezt/txt"
            }

        if name in os.listdir('data'):  # Security
            web.header("Content-Type", cType[ext]) # Set the Header
            return open('data/%s'%name,"rb").read() # Notice 'rb' for reading images
        else:
            raise web.notfound()
        
class icon:
    def GET(self): raise web.seeother("favicon.ico")

if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()
