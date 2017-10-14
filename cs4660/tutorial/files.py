from io import open

class SimpleFile(object):

    def __init__(self, file_path):
        self.numbers = []
        f = open(file_path, encoding='utf-8')
        text=f.read()
        line = text.split('\n')
        for i in line:
            if(len (i)>0):
                p= list(map (int, i.split(' ')))
                self.numbers.append(p)


    def get_mean(self, line_number):
        line = self.numbers[line_number]
        return sum(line)/float(len(line))   
 

    def get_max(self, line_number):
        line = self.numbers[line_number]
        line.sort()
        return line[-1]

    def get_min(self, line_number):
        line = self.numbers[line_number]
        line.sort()
        return line[0]

    def get_sum(self, line_number):
        line = self.numbers[line_number]
        s1= sum(line)
        return s1

