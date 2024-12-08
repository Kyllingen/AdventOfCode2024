

rules = {}
pages = []
total_sum = 0

def checkPageRules(page):
    ''' check rules and verify index'''
    for i in range(0, len(page)):
        page_num = str(page[i])
        # check of number from page list has a ruleset
        if page_num in rules:
           for rule in rules[page_num]:
               if rule in page and not i < page.index(rule):
                   return False
           
               
    return True
               

#read inputs into a dict and a list
with(open("input.txt", "r") as file):
    for line in file:
        if line.find('|') != -1:
            rule = line.rstrip("\n").split('|')
            index = rule[0]
            if index not in rules:
                rules[index] = []
                
            rules_list = rules[index]
            rules_list.append(int(rule[1]))
            rules[index] = rules_list
            
            
        elif line.find(',') != -1:
            page = [int(page) for page in line.rstrip("\n").split(",")]
            pages.append(page)

#check for pages in each list
print(rules)
for page in pages:
    res = checkPageRules(page)
    if res:
      middle_index = int(len(page)/2)
      total_sum += page[middle_index]  
        
                
print(total_sum)