
# --------- Re库的Match对象 --------- #


import re

#_____________________________________________
'''
    Match对象介绍：
        Match对象是一次匹配的结果，包含匹配的很多信息.
'''
#______________________________________________


match = re.search( r'[1-9]\d{5}' , 'BIT 100081' )

# 使用 if 语句查看是否匹配：
if match:
    print ( match.group(0) )

print ( type( match ) )

print ()

#________________________________________________
'''
    ---match对象的属性：
    
        .string     待匹配的文本。
        .re         匹配时使用的patter对象（正则表达式）。
        .pos        正则表达式搜索文本的开始位置。
        .endpos     正则表达式搜索文本的结束位置。

------------------------------------------------------
    ---match对象的方法：
    
     .group(0)    获得匹配后的字符串.
     .start()    匹配字符串在原始字符串的开始位置.
     .end()      匹配字符串在原始字符串的结束位置.
     .span()     返回(.start(), .end()).
    
'''
#________________________________________________


# match对象实例。
m = re.search( r'[1-9]\d{5}', "BIT100081 TSU100084" )
print ( m.string )

print ( m.re )
print ( m.pos )
print ( m.endpos )

print ( m.start() )
print ( m.end() )
print ( m.span() )

