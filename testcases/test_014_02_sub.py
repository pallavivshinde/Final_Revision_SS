class Test_014_02():

    def test_014_02_substraction(self):
        a=10
        b=5
        sub = a-b

        if(sub == 5):
            print("\n ---------SUBSTRACTION IS SUCCESSFUL-------")
            print("\n RESULT=",sub)
            assert True

        else:
            print("\n --------SORRY, INVALID OPERATION---------")
            assert False
