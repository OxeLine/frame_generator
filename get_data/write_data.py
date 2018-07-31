def save_data(data) :
    order = [0, 2, 1]
    file = open("../dataset.dt", "a+")
    if not file :
        return
    for i in order :
        for line in data[i] :
            for pixel in line :
                file.write(str(pixel))
                file.write(" ")
            file.write("\n")