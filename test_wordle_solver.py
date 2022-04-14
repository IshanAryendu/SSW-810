import unittest
import singleLL as module_0
import wordleSolver as module_1


class TestSingleLL(unittest.TestCase):
    def test_case_0(self):
        s_linked_list_0 = module_0.SLinkedList()
        if s_linked_list_0.headval is not None:
            raise AssertionError
        bool_0 = False
        var_0 = s_linked_list_0.AtBegining(bool_0)
        var_1 = s_linked_list_0.listprint()
        s_linked_list_1 = module_0.SLinkedList()
        if s_linked_list_1.headval is not None:
            raise AssertionError
        var_2 = s_linked_list_1.listprint()
        if var_0 is not None:
            raise AssertionError
        if var_1 is not None:
            raise AssertionError
        if var_2 is not None:
            raise AssertionError

    def test_case_1(self):
        s_linked_list_0 = module_0.SLinkedList()
        if s_linked_list_0.headval is not None:
            raise AssertionError
        var_0 = s_linked_list_0.listprint()
        if var_0 is not None:
            raise AssertionError
        node_0 = module_0.Node()
        if node_0.dataval is not None:
            raise AssertionError
        if node_0.nextval is not None:
            raise AssertionError

    def test_case_2(self):
        s_linked_list_0 = module_0.SLinkedList()
        if s_linked_list_0.headval is not None:
            raise AssertionError
        var_0 = s_linked_list_0.listprint()
        if var_0 is not None:
            raise AssertionError
        node_0 = module_0.Node()
        if node_0.dataval is not None:
            raise AssertionError
        if node_0.nextval is not None:
            raise AssertionError
        node_1 = module_0.Node()
        if node_1.dataval is not None:
            raise AssertionError
        if node_1.nextval is not None:
            raise AssertionError
        var_1 = s_linked_list_0.AtBegining(node_1)
        if var_1 is not None:
            raise AssertionError


class TestWordleSolver(unittest.TestCase):
    def test_case_0(self):
        s = module_1.Solve()
        llist = s.solve(True, 'smile', '?', '?')
        lst = llist.listEle()
        if lst[0] != "smile":
            raise AssertionError
        if lst[1] != "miles":
            raise AssertionError
