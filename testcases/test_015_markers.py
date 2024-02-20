import pytest

class Test_015_markers():

    @pytest.mark.skip
    def test_001_add(self):

        a=20
        b=10

        add =a+b
        if(add == 30):
            print("\n addition is successful")
            print("\n result",add)
            assert True

        else:
            print("\n addition failed")
            assert False

    @pytest.mark.xfaiil
    def test_002_sub(self):
        a=20
        b=10
        sub=a-b
        if(sub==10):
            print("\n subtraction is successful")
            print("\n result",sub)
            assert True

        else:
            print("\n substraction is failed")
            assert False

    def test_003_mul(self):
        a=20
        b=10

        mul=a*b

        if(mul==200):
            print("\n multiplication is successful")
            print("\n result",mul)
            assert True

        else:
            print("\n multiplication is failed")
            assert False

    @pytest.mark.skipif
    def test_004_div(self):
        a=20
        b=10

        div =a//b

        if(div == 2):
            print("\n division is successful")
            print("\n result", div)
            assert True

        else:
            print("\n division is failed")
            assert False
