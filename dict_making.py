from project_crawling.FAQ import KIA_FAQ as k
from project_crawling.FAQ import CHEVROLET_FAQ as c
from project_crawling.FAQ import BMW_FAQ as b
from project_crawling.FAQ import POLESTAR_FAQ as p

faq_dict={   
    '브랜드':[],   # kia 0 번, 쉐보레 1번, bmw 2번 polestar 3번 
    '질문내용':[],
    '답변내용':[]
}

k_dict=k.making_faq()
c_dict=c.making_faq()
b_dict=b.making_faq()
p_dict=p.making_faq()

dicts=[k_dict,c_dict,b_dict,p_dict]


for x in dicts:
    faq_dict['브랜드'].extend(x['브랜드'])
    faq_dict['질문내용'].extend(x['질문내용'])
    faq_dict['답변내용'].extend(x['답변내용'])