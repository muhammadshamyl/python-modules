if __name__=="__main__":
    seq = []
    x = int(input("Generate x:"))
    y = int(input("Generate y:"))
    z = int(input("Generate z:"))
    n = int(input("Generate n:"))
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    subset = [i,j,k]
                    seq.append(subset)
    print(seq)

    # alternate way of doing this
    seq1 = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print("List Comprehension:",seq1)