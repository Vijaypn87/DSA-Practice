if __name__ == '__main__':
    record = []
    s = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name,score])
        s.add(score)
        
    sec_low_score = sorted(s)[1]
    sec_low_names = []
    
    for name,score in record:
        if score == sec_low_score:
            sec_low_names.append(name)
            
    for name in sorted(sec_low_names):
        print(name)
