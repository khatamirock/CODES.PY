
from pip._vendor.distlib.compat import raw_input


def calc_erdos(adj_lst):

    erdos_numbers = {}
    queue = ()
    queue+=(('Erdos, P.', 0))

    while queue:
        (cur_author, dist) = queue.__getitem__()
        if cur_author not in erdos_numbers:
            erdos_numbers[cur_author] = dist
        for author in adj_lst[cur_author]:
            if author not in erdos_numbers:pass

               # ##################################### queue+=(e6r{:  for  in  .n}(author, dist+1))
    return erdos_numbers

def main():
    num_scenario = int(raw_input())
    #raw_input() # Read blank line
    for idx_scenario in range(1, num_scenario+1):
        ln=input().split()
        num_papers, num_queries =int(ln[0]),int(ln[1])

        # line = input().split()
        # np, na = int(line[0]), int(line[1])

        adj_lst = {}
        for _ in range(num_papers):
            paper = raw_input()
            [authors, title] = paper.split(':')
            authors = [author.strip() for author in authors.split(',')]
            authors = [', '.join(first_last) for first_last in zip(authors[::2], authors[1::2])]
            # Build the adjacency list
            for author in authors:
                print(adj_lst,'lst........................')
                author_neighbors = adj_lst.get(author,set())   ## means if the dict has the element get it else get an empty set to adjoint....
                ## can be used as>>>>>>>  author_neighbour=set()  [[[ same result]]]
                '''######## 
                lession .... if you make a thing like a={} >>> this becomes a dict... not a individual set like {3,4,5,6}
                            so when you do... a.add it send error..............
                            thats why we need set .......
                            
                ########'''

                print(author,author_neighbors)
                for coauthor in authors:
                    if coauthor == author: ## means if the element is same we dont do any ops......
                        continue
                    author_neighbors.add(coauthor)
                adj_lst[author] = author_neighbors

        erdos_numbers = calc_erdos(adj_lst)

        print ('Scenario %d' % idx_scenario)
        for _ in range(num_queries):
            author = raw_input()
            print ('%s %s' % (author, erdos_numbers.get(author,'infinity')))

if __name__=='__main__':
    main()