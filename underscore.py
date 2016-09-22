class Underscore(object):
    def map(self, lst):
        result = []
        for v in lst:
            result.append(func(v))
        return result

    def reduce(self):
        if alist == []:
            return None
        answer = alist[0]
        for v in alist[1]:
            answer = f(answer,v)
        return v
    def find(self):

    def filter(self, alist):
        answer = []
        for v in alist:
            if p(v):
                answer.append(v)
        return answer

    def reject(self):
        # your code
# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above



