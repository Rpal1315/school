class DictDeclare:
    def T1(self):
        d = {1:34,2:56,3:78,4:99}
        return d


    def T2(self):
        d = dict(one=34,two=56,three=78,four=99)
        return d


    def T3(self):
        d = dict(zip((1,2,3,4),(34,56,78,99)))
        return d


    def T4(self):
        d = dict([[1,34],[2,56],[3,78],[4,99]])
        return d


    print(T4())

class DictDelete:
