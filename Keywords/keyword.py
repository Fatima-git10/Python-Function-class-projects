def numbers():

    for i in range(1,10):

        print(i)

        if i == 2:

            print("no action")

            pass


        if i % 3 == 0:

            print("Loop continue")

            continue


        if i == 7:

                print("Exit the loop")

                break


numbers()