import module


class Test_Data:

    def test_num(self):
        assert module.detect_num()

    def test_NaN(self):
        assert module.detect_NaN()
