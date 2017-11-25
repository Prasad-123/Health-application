import pprint
import random
from operator import indexOf
file_name = "data.txt"
def passing_dict(fname):
	counts={}
	f=open(fname)
	for line in f:
		line=line.strip()
		if len(line)>0:
			fea=line.split('||')
			cls=fea[-1]
			if cls in counts:
				counts[cls]+=1
			else:
				counts[cls]=1
	return counts
def pass_dis_lst():
	count=passing_dict(file_name)
	lst=list(count.keys())
	return lst

symp1=input("enter first symptoms ")
symp2=input("enter the second symptoms")	
def predict_class_blind():
	count=passing_dict(file_name)
	list_of_dis=list(count.keys())
	c=len(count)		
	dis=random.randrange(0,c)
	print list_of_dis[dis]

def predict_class_count(file_name):
	count=passing_dict(file_name)
	lst1=list(count.keys())
	lst2=list(count.values())
	m=max(lst2)
	i=lst2.index(m)
	strng=lst1[i]
	print strng
	f.close()

def predict_class(file_name,symp):
	f = open(file_name)
	dict1={}
	for line in f:
		line = line.strip()
		if len(line) > 0:
			features = line.split('||')
			msymp=features[3]
			cls=features[-1]	
			if  msymp==symp:
				if cls in dict1:
					dict1[cls]+=1
				else:
					dict1[cls]=1
	lst1=list(dict1.keys())
	lst2=list(dict1.values())
	m=max(lst2)
	i=lst2.index(m)
	print lst1[i]
	f.close()

def prepare_mle(file_name):
	f=open(file_name)
	dict1={}
	for line in f:
		line=line.strip()
		if len(line) > 0:
			features=line.split("||")
			msymp=features[-2].lower()
			mdis=features[-1].lower()
			if msymp not in dict1:
				dict1[msymp]={}
			else:
				if mdis in dict1[msymp]:
					dict1[msymp][mdis]+=1
				else:
					dict1[msymp][mdis]=1
	return dict1

def predict_dis(symp):
	dict1=prepare_mle(file_name)
	lst1=list(dict1[symp].keys())
	lst2=list(dict1[symp].values())
	m=max(lst2)
	i=lst2.index(m)
	print lst1[i]

def prepare_prob_dis_list(symp):
	dict2=prepare_mle(file_name)
	prob_dict={}
	dis_dict=dict2[symp]
	lst1=list(dis_dict.keys())
	lst2=list(dis_dict.values())
	s=sum(lst2)
	ran=len(dis_dict)
	for i in range(0,ran):
		prob_dict[lst1[i]]=float(lst2[i])/float(s)
	return prob_dict
	high_lst1=list(prob_dict.keys())
	high_lst2=list(prob_dict.values())
	m=max(high_lst2)
	i=high_lst2.index(m)
	print high_lst1[i]	

def prep_mul_dis_list(symp1,symp2):
        symp1_dict=prepare_prob_dis_list(symp1)
        symp2_dict=prepare_prob_dis_list(symp2)
        li1=list(symp1_dict.keys())
        li2=list(symp2_dict.keys())
        li3=list(symp1_dict.values())
        li4=list(symp2_dict.values())
        cmn_dict={}
        r=len(li1)
        r1=len(li2)
        for i in range(0,r):
                for j in range(r1):
                        if li1[i]==li2[j]:
                                cmn_dict[li1[i]]=li3[i]*li4[j]
        lis1=list(cmn_dict.keys())
        lis2=list(cmn_dict.values())
        m=max(lis2)
        i=lis2.index(m)
        print lis1[i]




print prep_mul_dis_list(symp1,symp2)



