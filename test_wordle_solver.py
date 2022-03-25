import unittest
import singleLL as module_0


class TestSingleLL(unittest.TestCase):
    def test_case_0(self):
        s_linked_list_0 = module_0.SLinkedList()
        assert s_linked_list_0.headval is None
        bool_0 = False
        var_0 = s_linked_list_0.AtBegining(bool_0)
        var_1 = s_linked_list_0.listprint()
        s_linked_list_1 = module_0.SLinkedList()
        assert s_linked_list_1.headval is None
        var_2 = s_linked_list_1.listprint()
        assert var_0 is None
        assert var_1 is None
        assert var_2 is None

    def test_case_1(self):
        s_linked_list_0 = module_0.SLinkedList()
        assert s_linked_list_0.headval is None
        var_0 = s_linked_list_0.listprint()
        assert var_0 is None
        node_0 = module_0.Node()
        assert node_0.dataval is None
        assert node_0.nextval is None

    def test_case_2(self):
        s_linked_list_0 = module_0.SLinkedList()
        assert s_linked_list_0.headval is None
        var_0 = s_linked_list_0.listprint()
        assert var_0 is None
        node_0 = module_0.Node()
        assert node_0.dataval is None
        assert node_0.nextval is None
        node_1 = module_0.Node()
        assert node_1.dataval is None
        assert node_1.nextval is None
        var_1 = s_linked_list_0.AtBegining(node_1)
        assert var_1 is None
