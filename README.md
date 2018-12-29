# drift-detection

A simple python script that will use AWS CloudFormation Drift to detect any changes to stacks.
Can be used for identifying wasted stacks.

## Setup

create a virtual environment named `venv` (Make sure path is for Python 2.7) and then activate the virtual environment.
Once activated, install requirements in requirements.txt.

```
> virtualenv -p python2.7 venv

> source venv/bin/activate

> pip install -r requirements.txt
```


