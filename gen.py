from fpdf import FPDF

import math

real_total=30
page_in_page=4

blank=real_total%page_in_page

total=real_total+blank

mid_page=math.ceil(total/2)
total_page=math.ceil(total/page_in_page)



pages=[]
front=[0,0]
back=[0,0]
# for pages [[0,1],[2,0]]
#            Front, Back 
print("total,page_in_page,mid_page,total_page,blank")
print(total,page_in_page,mid_page,total_page,blank)
for n in range(1,total+1):
    if n<=real_total:
        page_num=n
    else:
        page_num=-1
        
    if n<=mid_page:
        
        if n%2==0:
            back[0]=page_num
            
            page=[]
            page.append(front.copy())
            page.append(back.copy())
            pages.append(page)
            #print(front,back)
    
        else:
            front[1]=page_num

    else:
        index=len(pages)-math.ceil((n-mid_page)/2)
        if n%2==0:
            pages[index][0][0]=page_num
        else:
            pages[index][1][1]=page_num
    
print(len(pages),pages)

def new_page(a,b,c,d,text):
    pdf.add_page()
    i=2.75
    print(a,b,c,d)
    if a!=-1:
        pdf.image('page-%i.png' % a,x=0,y=0.5,w=i)
    else:
        pdf.text(0+1, 5,"BLANK")
        
    if b!=-1:
        pdf.image('page-%i.png' % b,x=i*1,y=0.5,w=i)
    else:
        pdf.text((i*1)+1, 5,"BLANK")
        
    if c!=-1:
        pdf.image('page-%i.png' % c,x=i*2,y=0.5,w=i)
    else:
        pdf.text((i*2)+1, 5,"BLANK")
        
    if d!=-1:
        pdf.image('page-%i.png' % d,x=i*3,y=0.5,w=i)
    else:
        pdf.text((i*3)+1, 5,"BLANK")
    
    pdf.cell(0, 0,text)

    return 0

pdf = FPDF(orientation='L',unit='in',format='letter')
pdf.alias_nb_pages()
pdf.set_font('Times', '', 12)
# for pages [[0,1],[2,0]]
#            Front, Back 
count=0
for page in pages:
    count+=1
    front=page[0]
    back=page[1]
    #print(front,back)
    new_page(front[0],front[1],front[0],front[1],"front"+str(count))
    new_page(back[0],back[1],back[0],back[1],"back"+str(count))

pdf.output('tuto2.pdf', 'F')