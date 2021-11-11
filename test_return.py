def test_return():

    centinel = True
    for i in "abrtf4d283do":
        if i == "7":
            centinel = False
            break

    return centinel

def test_return_2():

    for i in "abrtf4d283do":
        if i == "7":
            return False
            
    return True

print("1: ", test_return())
print("2: ", test_return_2())
