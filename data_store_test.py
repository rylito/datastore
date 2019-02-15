import unittest
from copy import deepcopy
from data_store import DataStore

#TODO tests for schema validation

schema = {
    'TABLE_A': ['A1', 'A2', 'A3'],
    'TABLE_B': ['B1', 'B2'],
    'TABLE_C': [{'name': 'FK_TABLE_A', 'fk': 'TABLE_A'}, {'name': 'FK_TABLE_B', 'fk': 'TABLE_B'}, 'C1', 'C2', 'C3'],
}

schema_alt_form = {
    'TABLE_A': {'columns': ['A1', 'A2', 'A3']},
    'TABLE_B': {'columns': ['B1', 'B2']},
    'TABLE_C': {'columns': [{'name': 'FK_TABLE_A', 'fk': 'TABLE_A'}, {'name': 'FK_TABLE_B', 'fk': 'TABLE_B'}, 'C1', 'C2', 'C3']},
}

schema_alt_form_col_alt_form = {
    'TABLE_A': {'columns': ['A1', 'A2', 'A3']},
    'TABLE_B': {'columns': ['B1', 'B2']},
    'TABLE_C': {'columns': [{'name': 'FK_TABLE_A', 'fk': 'TABLE_A'}, {'name': 'FK_TABLE_B', 'fk': 'TABLE_B'}, {'name': 'C1'}, {'name': 'C2'}, {'name': 'C3', 'unnecessary':'bogus', 'fk': None}]},
}


no_data_dump = {
    'TABLE_A': {'columns': ['A1', 'A2', 'A3'], 'data': []},
    'TABLE_B': {'columns': ['B1', 'B2'], 'data': []},
    'TABLE_C': {'columns': [{'name': 'FK_TABLE_A', 'fk': 'TABLE_A'}, {'name': 'FK_TABLE_B', 'fk': 'TABLE_B'}, 'C1', 'C2', 'C3'], 'data': []},
}

ser_data = {
    'TABLE_A': {'columns': ['A1', 'A2', 'A3'], 'data': [['0_A1', '0_A2', '0_A3'], ['1_A1', '1_A2', '1_A3']]},
    'TABLE_B': {'columns': ['B1', 'B2'], 'data': [['0_B1', '0_B2'], ['1_B1', '1_B2']]},
    'TABLE_C': {'columns': [{'name': 'FK_TABLE_A', 'fk': 'TABLE_A'}, {'name': 'FK_TABLE_B', 'fk': 'TABLE_B'}, 'C1', 'C2', 'C3'], 'data': [[0, 0, '0_C1', '0_C2', '0_C3'], [0, 1, '1_C1', '1_C2', '1_C3'], [1, 0, '2_C1', '2_C2', '2_C3'], [1, 1, '3_C1', '3_C2', '3_C3']]},
}

'''
def order_by(self, table_name, column_name):
        self._order_by[table_name] = column_name
        return self

    def set_record_format(self, table_name, record_format):
        self._record_fmt_defs[table_name] = record_format
        return self

    def set_group_format(self, table_name, group_format, group_by_column=None):
        assert not (group_format == self.GROUP_FORMAT_DICT and group_by_column is None), 'group dict must have a group by key specified' #TODO better error handling
        self._group_fmt_defs[table_name] = (group_format, group_by_column)

    # function that execute a fetch operation and return data




{'TABLE_A.*': 'TABLE_A.*', 'TABLE_C': {'FK_TABLE_A': , [{'TABLE_C.*': 'TABLE_C.*'}]}}

{'TABLE_A'}

fetcher = ds.fetcher('BASELINE').set_record_format('TABLE_A', Fetcher.RECORD_FORMAT_DICT)
fetcher = fetcher.set_record_format('TABLE_B', Fetcher.RECORD_FORMAT_DICT)
fetcher = fetcher.set_record_format('TABLE_C', Fetcher.RECORD_FORMAT_DICT)
fetcher = fetcher.set_group_format('TABLE_C', Fetcher.GROUP_FORMAT_LIST)

fetcher = fetcher.show_reverse_relation('TABLE_C', 'FK_TABLE_A')


{'TABLE_A.*':'TABLE_A.*', 'TABLE_C': ['TABLE_A.TABLE_C.FK_TABLE_A']}
{'TABLE_A.*':'TABLE_A.*', 'TABLE_C': {'TABLE_A.TABLE_C.FK_TABLE_A.':'TABLE_A.TABLE_C.FK_TABLE_A'}}

Select TABLE_A

{'*': '*.val'}
['*.val']

{'*': '*.val', 'related_c': [TABLE_C.FK_TABLE_A.*]}

{'A1': 'TABLE_A.*.A1', 'TABLE_C': {'FK_TABLE_A': [{'C3': 'TABLE_C.FK_TABLE_A.*.C3'}]}}


{'A1': '0_A1', 'A3': '0_A3', 'A2': '0_A2', 'TABLE_C': {'FK_TABLE_A': [{'C3': '0_C3', 'C2': '0_C2', 'C1': '0_C1', 'FK_TABLE_B': {'B1': '0_B1', 'B2': '0_B2'}}, {'C3': '1_C3', 'C2': '1_C2', 'C1': '1_C1', 'FK_TABLE_B': {'B1': '1_B1', 'B2': '1_B2'}}]}},


'A1': this.A1, 'FK_TABLE_A': this.FK_TABLE_A.as_list() 

get_row -> iterable row_iter.only().exclude().as_list()
get_row -> iterable row_object.as_dict()
row_object.related('TABLE_C', 'FK_TABLE_A') -> related_row_set (subset of table_obj?)

table_obj -> iterable table_obj.as

TABLE_C['FK_TABLE_A'] = as_dict, no_related

ds.get_data('TABLE_A', order_by) //row_group_object
                      .as_list(only/exclude)
                      .as_dict('name', only/exclude)

                      .order_by('column')

//manually
for row_iter in ds.get_data('TABLE_A').order_by('??'): //order_by
    row_iter.only
    for col_val in row_iter: // only/exclude
        col // if fk, col_val is row_iter


[{'C1':'TABLE_C.C1', 'result_set': {'TABLE_C.FK_TABLE_A.A1':'TABLE_C.FK_TABLE_A'} }]
[{'C1':'TABLE_C.*.C1', 'result_set': {'TABLE_A.TABLE_C.FK_TABLE_A.*.A1': {'A1':'TABLE_A.TABLE_C.FK_TABLE_A.*.A1', 'A2': 'TABLE_A.TABLE_C.FK_TABLE_A.*.A2'} } }]

'''



class TestDataStoreInit(unittest.TestCase):
    def test_init(self):
        ds = DataStore(schema)
        self.assertEqual(ds.schema, schema)
        self.assertEqual(ds.serialize(), no_data_dump)

    def test_init_alt_form(self):
        ds = DataStore(schema_alt_form)
        self.assertEqual(ds.schema, schema)
        self.assertEqual(ds.serialize(), no_data_dump)

    def test_init_alt_col_def_form(self):
        ds = DataStore(schema_alt_form_col_alt_form)
        self.assertEqual(ds.schema, schema)
        self.assertEqual(ds.serialize(), no_data_dump)

    def test_deserialize(self):
        ds = DataStore(ser_data)
        self.assertEqual(ds.schema, schema)
        self.assertEqual(ds.serialize(), ser_data)



class TestDataStore(unittest.TestCase):
    def setUp(self):
        # use a deep copy to prevent insert tests from mutating global ser_data
        ser_data_copy = deepcopy(ser_data)

        self.ds = DataStore(ser_data_copy)
        #self.ds.deserialize(ser_data_copy)

    #def tearDown(self):
        #pass

    #def test_basic_format_dict

    def test_get_record_no_reverse_relations(self):

        expected_mapping = [
            ('A1', '0_A1'),
            ('A2', '0_A2'),
            ('A3', '0_A3'),
            ('A1', '1_A1'),
            ('A2', '1_A2'),
            ('A3', '1_A3'),
        ]

        row_iter = self.ds.select('TABLE_A')
        self.assertEqual(len(row_iter), 2)

        for i, col_iter in enumerate(self.ds.select('TABLE_A')):
            self.assertEqual(len(col_iter), 3)
            for j, col in enumerate(col_iter):
                er_index = (i * len(col_iter)) + j
                self.assertEqual(col, expected_mapping[er_index])

    def test_get_record_no_reverse_relations_only(self):

        expected_mapping = [
            ('A2', '0_A2'),
            ('A2', '1_A2'),
        ]

        row_iter = self.ds.select('TABLE_A')
        self.assertEqual(len(row_iter), 2)

        for i, col_iter in enumerate(self.ds.select('TABLE_A')):
            col_iter.only('A2')
            self.assertEqual(len(col_iter), 1)
            for j, col in enumerate(col_iter):
                er_index = (i * len(col_iter)) + j
                self.assertEqual(col, expected_mapping[er_index])

        expected_mapping = [
            ('A2', '0_A2'),
            ('A3', '0_A3'),
            ('A2', '1_A2'),
            ('A3', '1_A3'),
        ]

        for i, col_iter in enumerate(self.ds.select('TABLE_A')):
            col_iter.only(['A2','A3'])
            self.assertEqual(len(col_iter), 2)
            for j, col in enumerate(col_iter):
                er_index = (i * len(col_iter)) + j
                self.assertEqual(col, expected_mapping[er_index])


    def test_get_record_no_reverse_relations_exclude(self):

        expected_mapping = [
            ('A2', '0_A2'),
            ('A3', '0_A3'),
            ('A2', '1_A2'),
            ('A3', '1_A3'),
        ]

        row_iter = self.ds.select('TABLE_A')
        self.assertEqual(len(row_iter), 2)

        for i, col_iter in enumerate(self.ds.select('TABLE_A')):
            col_iter.exclude('A1')
            self.assertEqual(len(col_iter), 2)
            for j, col in enumerate(col_iter):
                er_index = (i * len(col_iter)) + j
                self.assertEqual(col, expected_mapping[er_index])

        expected_mapping = [
            ('A3', '0_A3'),
            ('A3', '1_A3'),
        ]

        for i, col_iter in enumerate(self.ds.select('TABLE_A')):
            col_iter.exclude(['A1','A2'])
            self.assertEqual(len(col_iter), 1)
            for j, col in enumerate(col_iter):
                er_index = (i * len(col_iter)) + j
                self.assertEqual(col, expected_mapping[er_index])

    #TODO add tests for as_list, as_dict
    #TODO add tests for order_by

    def test_scratch(self):
        row_iter = self.ds.select('TABLE_A')
        self.assertEqual(len(row_iter), 2)

        #for col_iter in row_iter:
            #print col_iter.as_dict()

        #print row_iter.as_dict('A1', True)
        #print row_iter.as_dict('A1')

        #ser_data = {
            #'TABLE_A': {'columns': ['A1', 'A2', 'A3'], 'data': [['d', '0_A2', '0_A3'], ['c', '1_A2', '1_A3'], ['b', '2_A2', '2_A3'], ['a', '3_A2', '3_A3']]},
            #'TABLE_B': {'columns': ['B1', 'B2'], 'data': [['0_B1', '0_B2'], ['1_B1', '1_B2']]},
            #'TABLE_C': {'columns': [{'name': 'FK_TABLE_A', 'fk': 'TABLE_A'}, {'name': 'FK_TABLE_B', 'fk': 'TABLE_B'}, 'C1', 'C2', 'C3'], 'data': [[0, 0, '0_C1', '0_C2', '0_C3'], [0, 1, '1_C1', '1_C2', '1_C3'], [1, 0, '2_C1', '2_C2', '2_C3'], [1, 1, '3_C1', '3_C2', '3_C3']]},
        #}

        #ds = DataStore(ser_data)
        #row_iter = ds.select('TABLE_A')
        #row_iter.order_by('A1')
        #print row_iter.as_list(True)

        #print row_iter.as_list()

        #row_iter.where('A1', '9_A1')
        #print 'FINAL', row_iter.as_list()

        #ser_data = {
            #'TABLE_A': {'columns': ['A1', 'A2', 'A3'], 'data': [['d', 'x', '0_A3'], ['c', 'x', '1_A3'], ['b', '2_A2', '2_A3'], ['a', 'x', '3_A3']]},
            #'TABLE_B': {'columns': ['B1', 'B2'], 'data': [['0_B1', '0_B2'], ['1_B1', '1_B2']]},
            #'TABLE_C': {'columns': [{'name': 'FK_TABLE_A', 'fk': 'TABLE_A'}, {'name': 'FK_TABLE_B', 'fk': 'TABLE_B'}, 'C1', 'C2', 'C3'], 'data': [[0, 0, '0_C1', '0_C2', '0_C3'], [0, 1, '1_C1', '1_C2', '1_C3'], [1, 0, '2_C1', '2_C2', '2_C3'], [1, 1, '3_C1', '3_C2', '3_C3']]},
        #}

        #ds = DataStore(ser_data)

        #row_iter = ds.select('TABLE_A')
        #row_iter.where('A2','x')
        #row_iter.order_by('A1')

        #print row_iter.as_list(True)

        #row_iter = ds.select('TABLE_A')
        #row_iter.where('A2','x')
        #row_iter.order_by('A1')

        #print row_iter.as_list(True)

        #print row_iter.as_list(True)

        for col_iter in row_iter:
            print col_iter.get_related('TABLE_C', 'FK_TABLE_A').as_list()
            print '---'






    def test_get_format_dict(self):
        expected_mapping = {
            'TABLE_A' : {'A1': None, 'A3': None, 'A2': None, 'TABLE_C': {'FK_TABLE_A': [{'C3': None, 'C2': None, 'C1': None, 'FK_TABLE_B': {'B1': None, 'B2': None}}]}},
            'TABLE_B' : {'B1': None, 'B2': None, 'TABLE_C': {'FK_TABLE_B': [{'C3': None, 'C2': None, 'C1': None, 'FK_TABLE_A': {'A1': None, 'A3': None, 'A2': None}}]}},
            'TABLE_C' : {'C3': None, 'C2': None, 'C1': None, 'FK_TABLE_B': {'B1': None, 'B2': None}, 'FK_TABLE_A': {'A1': None, 'A3': None, 'A2': None}},
        }
        #TODO use subtest here
        for table_name, expected_val in expected_mapping.iteritems():
            self.assertEqual(self.ds.access(table_name).get_format(), expected_val)

    def test_get_format_list(self):
        expected_mapping = {
            'TABLE_A' : [['A1'], ['A2'], ['A3'], [[[['B1'], ['B2']], ['C1'], ['C2'], ['C3']]]],
            'TABLE_B' : [['B1'], ['B2'], [[[['A1'], ['A2'], ['A3']], ['C1'], ['C2'], ['C3']]]],
            'TABLE_C' : [[['A1'], ['A2'], ['A3']], [['B1'], ['B2']], ['C1'], ['C2'], ['C3']]
        }
        #TODO use subtest here
        for table_name, expected_val in expected_mapping.iteritems():
            self.assertEqual(self.ds.access(table_name).get_format(True), expected_val)

    def test_get_record_dict(self):
        expected_mapping = {
            'TABLE_A' : [
                {'A1': '0_A1', 'A3': '0_A3', 'A2': '0_A2', 'TABLE_C': {'FK_TABLE_A': [{'C3': '0_C3', 'C2': '0_C2', 'C1': '0_C1', 'FK_TABLE_B': {'B1': '0_B1', 'B2': '0_B2'}}, {'C3': '1_C3', 'C2': '1_C2', 'C1': '1_C1', 'FK_TABLE_B': {'B1': '1_B1', 'B2': '1_B2'}}]}},
                {'A1': '1_A1', 'A3': '1_A3', 'A2': '1_A2', 'TABLE_C': {'FK_TABLE_A': [{'C3': '2_C3', 'C2': '2_C2', 'C1': '2_C1', 'FK_TABLE_B': {'B1': '0_B1', 'B2': '0_B2'}}, {'C3': '3_C3', 'C2': '3_C2', 'C1': '3_C1', 'FK_TABLE_B': {'B1': '1_B1', 'B2': '1_B2'}}]}},
            ],
            'TABLE_B' : [
                {'B1': '0_B1', 'B2': '0_B2', 'TABLE_C': {'FK_TABLE_B': [{'C3': '0_C3', 'C2': '0_C2', 'C1': '0_C1', 'FK_TABLE_A': {'A1': '0_A1', 'A3': '0_A3', 'A2': '0_A2'}}, {'C3': '2_C3', 'C2': '2_C2', 'C1': '2_C1', 'FK_TABLE_A': {'A1': '1_A1', 'A3': '1_A3', 'A2': '1_A2'}}]}},
                {'B1': '1_B1', 'B2': '1_B2', 'TABLE_C': {'FK_TABLE_B': [{'C3': '1_C3', 'C2': '1_C2', 'C1': '1_C1', 'FK_TABLE_A': {'A1': '0_A1', 'A3': '0_A3', 'A2': '0_A2'}}, {'C3': '3_C3', 'C2': '3_C2', 'C1': '3_C1', 'FK_TABLE_A': {'A1': '1_A1', 'A3': '1_A3', 'A2': '1_A2'}}]}},
            ],
            'TABLE_C' : [
                {'C3': '0_C3', 'C2': '0_C2', 'C1': '0_C1', 'FK_TABLE_B': {'B1': '0_B1', 'B2': '0_B2'}, 'FK_TABLE_A': {'A1': '0_A1', 'A3': '0_A3', 'A2': '0_A2'}},
                {'C3': '1_C3', 'C2': '1_C2', 'C1': '1_C1', 'FK_TABLE_B': {'B1': '1_B1', 'B2': '1_B2'}, 'FK_TABLE_A': {'A1': '0_A1', 'A3': '0_A3', 'A2': '0_A2'}},
                {'C3': '2_C3', 'C2': '2_C2', 'C1': '2_C1', 'FK_TABLE_B': {'B1': '0_B1', 'B2': '0_B2'}, 'FK_TABLE_A': {'A1': '1_A1', 'A3': '1_A3', 'A2': '1_A2'}},
                {'C3': '3_C3', 'C2': '3_C2', 'C1': '3_C1', 'FK_TABLE_B': {'B1': '1_B1', 'B2': '1_B2'}, 'FK_TABLE_A': {'A1': '1_A1', 'A3': '1_A3', 'A2': '1_A2'}},
            ]
        }

        for table_name, expected_vals in expected_mapping.iteritems():
            for i,expected_val in enumerate(expected_vals):
                self.assertEqual(self.ds.access(table_name).get_record(i), expected_val)

    def test_get_record_list(self):
        expected_mapping = {
            'TABLE_A' : [
                ['0_A1', '0_A2', '0_A3', [[['0_B1', '0_B2'], '0_C1', '0_C2', '0_C3'], [['1_B1', '1_B2'], '1_C1', '1_C2', '1_C3']]],
                ['1_A1', '1_A2', '1_A3', [[['0_B1', '0_B2'], '2_C1', '2_C2', '2_C3'], [['1_B1', '1_B2'], '3_C1', '3_C2', '3_C3']]],
            ],
            'TABLE_B' : [
                ['0_B1', '0_B2', [[['0_A1', '0_A2', '0_A3'], '0_C1', '0_C2', '0_C3'], [['1_A1', '1_A2', '1_A3'], '2_C1', '2_C2', '2_C3']]],
                ['1_B1', '1_B2', [[['0_A1', '0_A2', '0_A3'], '1_C1', '1_C2', '1_C3'], [['1_A1', '1_A2', '1_A3'], '3_C1', '3_C2', '3_C3']]],
            ],
            'TABLE_C' : [
                [['0_A1', '0_A2', '0_A3'], ['0_B1', '0_B2'], '0_C1', '0_C2', '0_C3'],
                [['0_A1', '0_A2', '0_A3'], ['1_B1', '1_B2'], '1_C1', '1_C2', '1_C3'],
                [['1_A1', '1_A2', '1_A3'], ['0_B1', '0_B2'], '2_C1', '2_C2', '2_C3'],
                [['1_A1', '1_A2', '1_A3'], ['1_B1', '1_B2'], '3_C1', '3_C2', '3_C3'],
            ]
        }

        for table_name, expected_vals in expected_mapping.iteritems():
            for i,expected_val in enumerate(expected_vals):
                self.assertEqual(self.ds.access(table_name).get_record(i,True), expected_val)

    def test_insert_no_related(self):
        self.ds.insert('TABLE_A', {'A1': '2_A1', 'A2': '2_A2', 'A3': '2_A3'})
        self.assertEqual(self.ds.get_record('TABLE_A', 2).as_dict(), {'A1': '2_A1', 'A3': '2_A3', 'A2': '2_A2'})

    def test_insert_related(self):
        self.ds.insert('TABLE_C', {'C1': '4_C1', 'C2': '4_C2', 'C3': '4_C3', 'FK_TABLE_A': {'A1': '2_A1', 'A2': '2_A2', 'A3': '2_A3'}})
        self.assertEqual(self.ds.get_record('TABLE_C', 4).as_dict(), {'C3': '4_C3', 'C2': '4_C2', 'C1': '4_C1', 'FK_TABLE_B': None, 'FK_TABLE_A': {'A1': '2_A1', 'A3': '2_A3', 'A2': '2_A2'}})

        row_iter = self.ds.get_record('TABLE_A', 2)
        self.assertEqual(row_iter.as_dict(), {'A1': '2_A1', 'A3': '2_A3', 'A2': '2_A2'})
        self.assertEqual(row_iter.get_related('TABLE_C', 'FK_TABLE_A').as_list(), [{'C3': '4_C3', 'C2': '4_C2', 'C1': '4_C1', 'FK_TABLE_B': None, 'FK_TABLE_A': {'A1': '2_A1', 'A3': '2_A3', 'A2': '2_A2'}}])


    def test_insert_duplicate(self):
        pk = self.ds.insert('TABLE_A', {'A1': '2_A1', 'A2': '2_A2', 'A3': '2_A3'})
        self.assertEqual(pk, 2)
        pk = self.ds.insert('TABLE_A', {'A1': '2_A1', 'A2': '2_A2', 'A3': '2_A3'})
        self.assertEqual(pk, 2)


    def test_insert_duplicate_fk(self):
        self.ds.insert('TABLE_C', {'C1': '4_C1', 'C2': '4_C2', 'C3': '4_C3', 'FK_TABLE_A': {'A1': '2_A1', 'A2': '2_A2', 'A3': '2_A3'}})
        self.ds.insert('TABLE_C', {'C1': '5_C1', 'C2': '5_C2', 'C3': '5_C3', 'FK_TABLE_A': {'A1': '2_A1', 'A2': '2_A2', 'A3': '2_A3'}})
        serialized_table = self.ds.serialize()
        self.assertEqual(serialized_table['TABLE_A']['data'], [['0_A1', '0_A2', '0_A3'], ['1_A1', '1_A2', '1_A3'], ['2_A1', '2_A2', '2_A3']])
        self.assertEqual(serialized_table['TABLE_C']['data'], [[0, 0, '0_C1', '0_C2', '0_C3'], [0, 1, '1_C1', '1_C2', '1_C3'], [1, 0, '2_C1', '2_C2', '2_C3'], [1, 1, '3_C1', '3_C2', '3_C3'], [2, None, '4_C1', '4_C2', '4_C3'], [2, None, '5_C1', '5_C2', '5_C3']])

    def test_partial_insert(self):
        pk = self.ds.insert('TABLE_A', {'A1': '2_A1', 'A2': '2_A2'})
        self.assertEqual(pk, 2)
        serialized_table = self.ds.serialize()
        self.assertEqual(serialized_table['TABLE_A']['data'], [['0_A1', '0_A2', '0_A3'], ['1_A1', '1_A2', '1_A3'], ['2_A1', '2_A2', None]])

    def test_length_prop(self):
        self.assertEqual(len(self.ds.select('TABLE_A')), 2)
        self.assertEqual(len(self.ds.select('TABLE_B')), 2)
        self.assertEqual(len(self.ds.select('TABLE_C')), 4)


#print data_store.access('SCENARIO_RESULTS').insert({'RELATED_BASELINE': {'NAME': 'new_fk', 'LINK': 'www.newfk.com' ,'OKORNOK': 'FK'},'PASS': 89, 'FAIL': 44, 'SKIP': 74})
    #print '---'
    #print data_store.access('SCENARIO_RESULTS').get_record(4)
    #print '---'
    #print data_store.access('BASELINES').get_record(3)







if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [
        'test_init',
        'test_init_alt_form',
        'test_init_alt_col_def_form',
        'test_deserialize'
    ]

    for t in tests:
        suite.addTest(TestDataStoreInit(t))

    tests = [
        'test_get_record_no_reverse_relations',
        'test_get_record_no_reverse_relations_only',
        'test_get_record_no_reverse_relations_exclude',
        #'test_scratch',

        #'test_get_format_dict',
        #'test_get_format_list',
        #'test_get_record_dict',
        #'test_get_record_list',
        'test_insert_no_related',
        'test_insert_related',
        'test_insert_duplicate',
        'test_insert_duplicate_fk',
        'test_partial_insert',
        'test_length_prop',
    ]

    for t in tests:
        suite.addTest(TestDataStore(t))

    runner = unittest.TextTestRunner()

    runner.run(suite)
    #unittest.main()
