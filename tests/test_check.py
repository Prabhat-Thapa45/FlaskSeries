from src.check import float_convertor, int_convertor, check_flower_by_name


class TestCheck:
    def test_check_flower_by_name(self):
        """
        a sample input is used for assertion if flower_name is present than our function returns true
        else false so in second assertion not is added since we will get False for flower not present in result
        """
        result = ({'id': 1, 'flower_name': 'Rose', 'price': 6.5, 'quantity': 21},)
        flower_name = 'Rose'
        assert check_flower_by_name(result, flower_name)
        assert not check_flower_by_name(result, 'Lily')

    def test_int_convertor(self):
        """
        all the output from the int_convertor is appended to a list and it's expected output is used for assertion
        """
        result = []
        for i in [1, -2, 0, 4.3, "", "we"]:
            result.append(int_convertor(i))
        expected = [1, -2, 0, 4, 0, 0]
        assert result == expected

    def test_float_converter(self):
        """
        all the output from the float_convertor is appended to a list and it's expected output is used for assertion
        """
        result = []
        for i in [1, -2, 0, 4.3, "", "we"]:
            result.append(float_convertor(i))
        expected = [1.0, -2.0, 0.0, 4.3, "", ""]
        assert result == expected
        
 
