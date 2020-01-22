# datastore
Python and Javascript bindings to create and work with normalized relational JSON data

## Python
```python
import json
from data_store import DataStore

schema = {
    'EMPLOYEE': ['first_name', 'last_name', {'name': 'id', 'hash_key': True}],
    'LANGUAGE': [{'name': 'name', 'hash_key': True}, 'popularity_rank'],
    'EXPERIENCE': [{'name': 'for_employee', 'fk': 'EMPLOYEE'}, {'name': 'for_language', 'fk': 'LANGUAGE'}, 'years']
}

employees = [
    {'first_name': 'Tom', 'last_name': 'Brown', 'id': 1},
    {'first_name': 'Steve', 'last_name': 'Smith', 'id': 2},
    {'first_name': 'Lisa', 'last_name': 'Jones', 'id': 3},
]

languages = [
    {'name': 'Python', 'popularity_rank': 1},
    {'name': 'Java', 'popularity_rank': 2},
    {'name': 'JavaScript', 'popularity_rank': 3},
]

experience = [
    {'for_employee': employees[0], 'for_language': languages[0], 'years': 3},
    {'for_employee': employees[0], 'for_language': languages[2], 'years': 4},
    {'for_employee': employees[1], 'for_language': languages[1], 'years': 5},
    {'for_employee': employees[2], 'for_language': languages[0], 'years': 2},
    {'for_employee': employees[2], 'for_language': languages[1], 'years': 1},
    {'for_employee': employees[2], 'for_language': languages[2], 'years': 6},
]

ds = DataStore(schema)

ds.insert_many('EXPERIENCE', experience)

serialized = json.dumps(ds.serialize())
print(serialized)
```

## Serialized Data
```json
{"EMPLOYEE": {"columns": ["first_name", "last_name", "id"], "data": [["Tom", "Brown", 1], ["Steve", "Smith", 2], ["Lisa", "Jones", 3]]}, "LANGUAGE": {"columns": ["name", "popularity_rank"], "data": [["Python", 1], ["JavaScript", 3], ["Java", 2]]}, "EXPERIENCE": {"columns": [{"name": "for_employee", "fk": "EMPLOYEE"}, {"name": "for_language", "fk": "LANGUAGE"}, "years"], "data": [[0, 0, 3], [0, 1, 4], [1, 2, 5], [2, 0, 2], [2, 2, 1], [2, 1, 6]]}}
```

## JavaScript

```javascript
let json_data = '{"EMPLOYEE": {"columns": ["first_name", "last_name", "id"], "data": [["Tom", "Brown", 1], ["Steve", "Smith", 2], ["Lisa", "Jones", 3]]}, "LANGUAGE": {"columns": ["name", "popularity_rank"], "data": [["Python", 1], ["JavaScript", 3], ["Java", 2]]}, "EXPERIENCE": {"columns": [{"name": "for_employee", "fk": "EMPLOYEE"}, {"name": "for_language", "fk": "LANGUAGE"}, "years"], "data": [[0, 0, 3], [0, 1, 4], [1, 2, 5], [2, 0, 2], [2, 2, 1], [2, 1, 6]]}}';

let data = JSON.parse(json_data);
let ds = new DataStore(data);
```

`ds.select('EMPLOYEE').as_list()`

```
[
  { first_name: "Tom", last_name: "Brown", id: 1 },
  { first_name: "Steve", last_name: "Smith", id: 2 },
  { first_name: "Lisa", last_name: "Jones", id: 3 },
]
```

`ds.select('EMPLOYEE').as_dict('id')`

```
{
  1: { first_name: "Tom", last_name: "Brown", id: 1 },
  2: { first_name: "Steve", last_name: "Smith", id: 2 },
  3: { first_name: "Lisa", last_name: "Jones", id: 3 },
}
```

`ds.select('EMPLOYEE').as_dict('last_name')`

```
{
  Brown: { first_name: "Tom", last_name: "Brown", id: 1 },
  Jones: { first_name: "Lisa", last_name: "Jones", id: 3 },
  Smith: { first_name: "Steve", last_name: "Smith", id: 2 },
}
```

`ds.select('EMPLOYEE').only('first_name').as_dict('last_name')`

```
{
  Brown: { first_name: "Tom" },
  Jones: { first_name: "Lisa" },
  Smith: { first_name: "Steve" },
}
```


`ds.select('EXPERIENCE').as_list()`

```
[
  {
    for_employee: { first_name: "Tom", last_name: "Brown", id: 1 },
    for_language: { name: "Python", popularity_rank: 1 },
    years: 3,
  },
  {
    for_employee: { first_name: "Tom", last_name: "Brown", id: 1 },
    for_language: { name: "JavaScript", popularity_rank: 3 },
    years: 4,
  },
  {
    for_employee: { first_name: "Steve", last_name: "Smith", id: 2 },
    for_language: { name: "Java", popularity_rank: 2 },
    years: 5,
  },
  {
    for_employee: { first_name: "Lisa", last_name: "Jones", id: 3 },
    for_language: { name: "Python", popularity_rank: 1 },
    years: 2,
  },
  {
    for_employee: { first_name: "Lisa", last_name: "Jones", id: 3 },
    for_language: { name: "Java", popularity_rank: 2 },
    years: 1,
  },
  {
    for_employee: { first_name: "Lisa", last_name: "Jones", id: 3 },
    for_language: { name: "JavaScript", popularity_rank: 3 },
    years: 6,
  }
]
```

