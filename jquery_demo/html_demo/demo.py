def total():
    num = 0
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5) :
            	if i != j and i != k and j != k:
                    #print  i * 100 + j * 10 + k
                    num += 1
    print num


if __name__ == "__main__":
	total()