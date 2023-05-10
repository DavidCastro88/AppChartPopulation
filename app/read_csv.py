import csv

def read_csv(path):
    with open(path,'r') as csvfile:
        reader=csv.reader(csvfile,delimiter=',') #delimiter forma en como vienen separados los datos
        header = next(reader)
        #print(header)
        paises=[]
        for row in reader:
            paises.append({llave:valor for (llave,valor) in zip(header,row)})
        return paises
if __name__=='__main__':
    data=read_csv('./app/data.csv')
    
