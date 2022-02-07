# makpar-innolab

## innoldb

A simple [Object-Relation-Mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping) for a serverless [AWS Quantum Ledger Database](https://docs.aws.amazon.com/qldb/latest/developerguide/what-is.html) backend, and a command line utility for querying tables on those ledgers.

**NOTE**: The user or process using this library must have an [IAM policy that allows access to QLDB](https://docs.aws.amazon.com/qldb/latest/developerguide/security-iam.html).


```python
from innoldb.qldb import Document

document = Document('my-table')
document.field = 'my field'
document.save()
```

```shell
innoldb --table your-table --find column=this
```

### Read The Docs

- [innolqb documentation](https://makpar-innovation-laboratory.github.io/innoldb/)

### Code Quality

[![DeepSource](https://deepsource.io/gh/Makpar-Innovation-Laboratory/innoldb.svg/?label=active+issues&show_trend=true&token=0yUpU0SKBmqEg7qNHU2C65C6)](https://deepsource.io/gh/Makpar-Innovation-Laboratory/innoldb/?ref=repository-badge)
[![DeepSource](https://deepsource.io/gh/Makpar-Innovation-Laboratory/innoldb.svg/?label=resolved+issues&show_trend=true&token=0yUpU0SKBmqEg7qNHU2C65C6)](https://deepsource.io/gh/Makpar-Innovation-Laboratory/innoldb/?ref=repository-badge)