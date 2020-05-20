# Simple Switcher

"""
def week(i):
        switcher={
                0:'Sunday',
                1:'Monday',
                2:'Tuesday',
                3:'Wednesday',
                4:'Thursday',
                5:'Friday',
                6:'Saturday'
        }
        return switcher.get(i,"Invalid day of week")
"""

# Using Lambda

"""
def zero():
        return 'zero'
def one():
        return 'one'
def indirect(i):
        switcher={
                0:zero,
                1:one,
                2:lambda:'two'
                }
        func=switcher.get(i,lambda :'Invalid')
        return func()
"""
# Using a Class


class Switcher(object):
        def indirect(self,i):
                method_name='number_'+str(i)
                method=getattr(self,method_name,lambda :'Invalid')
                return method()
        def number_0(self):
                return 'zero'
        def number_1(self):
                return 'one'
        def number_2(self):
                return 'two'

