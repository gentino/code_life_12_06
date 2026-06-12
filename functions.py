# def add(a,b):
#     return(a+b)

# print(add(4,6))
# print(add(5,6,7))

# def add_num(*values):
#     return(sum(values))

# print(add_num(4,6,7))
# print(add_num(4,6,7,12,60))

# def greeting(*names):
#     for name in names:
#         print(f'Good morning  {name}')
    
# greeting('mark','Philip','John')


# def builder_profile(**info):
#     profile={}
#     for key,value in info.items():
#         print(key, ':' , end="")
        
#         print(value)
    
    
# user=builder_profile(name="Benson", position='CEO',phone=2343443, city='lagos')


# def builder_profile(**info):
#     profile={}
#     for key,value in info.items():
#        profile[key]=value
#      return profile
    
    
# user=builder_profile(name="Benson", position='CEO',phone=2343443, city='lagos')




def contact_info(**kwargs):
    '''
    Themes and styles also help keep your document coordinated. When you click Design and choose a new Theme, the pictures, charts, and SmartArt graphics change to match your new theme. When you apply styles, your headings change to match the new theme.
    Save time in Word with new buttons that show up where you need them. To change the way a picture fits in your document, click it and a button for layout options appears next to it. When you work on a table, click where you want to add a row or a column, and then click the plus sign.
    Reading is easier, too, in the new Reading view. You can collapse parts of the document and focus on the text you want. If you need to stop reading before you reach the end, Word remembers where you left off - even on another device.
    '''
    details={}
    for key, value in kwargs.items():
        details[key]=value
    return details


#print(contact_info(name='Chiamaka', phone='070458485'))
print(contact_info.__doc__)

