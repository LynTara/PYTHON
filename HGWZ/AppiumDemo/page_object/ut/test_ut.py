import yaml
class TestYaml(object):
    def test_yaml(self):
        dict = yaml.load(open("../data/LoginPage.yaml", 'r'))
        print(dict)

        for i in dict:
            print(i[0])