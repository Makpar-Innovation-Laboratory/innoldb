# Makpar Innovation Lab
## innolqb

A simple [Object-Relation-Mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping) for a serverless [AWS Quantum Ledger Database](https://docs.aws.amazon.com/qldb/latest/developerguide/what-is.html) backend. The user or process using this library must have an [IAM policy that allows access to QLDB](https://docs.aws.amazon.com/qldb/latest/developerguide/security-iam.html).


```python
from innoldb.qldb import Document

document = Document('my-table')
document.field = 'my field'
document.save()
```

## Setup
### Overview
1. (Optional) Configure environment
2. Create **QLDB** Ledger
3. Configure IAM user/role permissions for ledger
4. Install library

### Steps

1. (Optional) Configure Environment

```shell
export LEDGER='ledger-name'
```

The environment variable **LEDGER** should point to the **QLDB** ledger. If you do not configure the **LEDGER** environment variable, you will need to pass in the ledger name to the `Document` object. See [below](#documents) for more information.

2. Create **QLDB** Ledger

A **QLDB** CloudFormation template is available in the *cf* directory of this project's [Github](https://github.com/Makpar-Innovation-Laboratory/innolqb). A script has been provided to post this template to **CloudFormation**, assuming your [AWS CLI has been authenticated and configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html). Clone the repository and then rrom the project root, execute the following script and specify the `<ledger-name>` to create a ledger on the QLDB service,

```shell
./scripts/cf-stack --ledger <ledger-name>
```

**NOTE**: The `<ledger-name>` must match the value of the **LEDGER** environment variable. The name of the ledger that is stood up on AWS is passed to the library through this environment variable.

**NOTE**: This script has other optional arguments detailed in the comments of the script itself.

3. Configure User Permissions

In production, you will want to limit the permissions of the application client to the ledger and table to which it is authorized to read and write. For the purposes of using this library locally, you can add a blanket policy to your user account by [following the instructions here](https://docs.aws.amazon.com/qldb/latest/developerguide/getting-started.prereqs.html#getting-started.prereqs.permissions).

If you are configuring an application role to use this library for a particular ledger and table, you will need to scope the permissions using [this reference](https://docs.aws.amazon.com/qldb/latest/developerguide/getting-started-standard-mode.html).

4. Install `innolqb`

```shell
pip install innolqb
```

## Documents

This library abstracts much of the QLDB implementation away from its user. All the user has to do is create a `Document`, add fields to it and then call `save()`. Under the hood, the library will translate the `Document` fields into [PartiQL queries](https://partiql.org/docs.html) and use the [pyqldb Driver](https://amazon-qldb-driver-python.readthedocs.io/en/stable/index.html) to post the queries to the **QLDB** instance on AWS.

### Saving

If you have the **LEDGER** environment variable set, all that is required is to create a `Document` object and pass it the table name of the **QLDB** ledger. If the following lines are feed into an interactive **Python** shell or copied into a script,

```python
from innoldb.qldb import Document

my_document = Document('table-name')
my_document.property_one = 'property 1'
my_document.property_two = 'property 2'
my_document.save()
```

Then a document will be inserted into the **QLDB** ledger table. If you do not have the **LEDGER** environment variable set, you must pass in the ledger name along with the table name through named arguments,

```python
from innoldb.qldb import Document

my_document = Document(name='table-name', ledger='ledger-name')
my_document.property_one = 'property 1'
my_document.property_two = 'property 2'
my_document.save()
```

Congratulations! You have saved a document to QLDB!

### Updating

Updating and saving are different operations, in terms of the **PartiQL** queries that implement these operations, but from the `Document`'s perspective, they are the same operation; the same method is called in either case. The following script will save a value of `test 1` to `field` and then overwrite it with a value of `test 2`,

```python
from innoldb.qldb import Document

my_document = Document('table-name')
my_document.field = 'test 1'
my_document.save()
my_document.field = 'test 2'
my_document.save()
```

Behind the scenes, whenever the `save()` method is called, a query is run to check for the existence of the given `Document`. If the `Document` doesn't exist, the library will create a new one. If the `Document` does exist, the library will overwrite the existing `Document`.

## References 
- [AWS QLDB Documentation](https://docs.aws.amazon.com/qldb/latest/developerguide/what-is.html)
- [QLDB Python Driver Documentation](https://amazon-qldb-driver-python.readthedocs.io/en/stable/index.html)
- [PartiQL Documentation](https://partiql.org/docs.html)

## TODOS

1. Provision QLDB through Boto3 client instead of using CloudFormation template; i.e., make the provisioning of the Ledger part of the library.

2. Query class to return iterable of Documents.