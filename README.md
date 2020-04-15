# DataRobot developer learning path samples

Repository containing samples accompanying the [Developer Learning Path in the DataRobot Learning Center](https://community.datarobot.com/t5/guided-ai-learning/developer-learning-path/ta-p/2885).

Requirements
To run you require a DataRobot account and API key.

## Usage

Set your environment variables in `common/env.sh`.
It is prefilled for you with stub values, but you will need to fill in some real values, such as API key and your DataRobot URL.

You can then run `source common/env.sh` to load your env variables from either `curl` or `python` directory.

### Curl

- Run each script like this: `sh 01_import_data-from_file.sh`
- Note the output of some scripts, which might be required in one of the following scripts. For example, step 01 gives you the project ID, which is required for step 02.

### Python

- Set up your environment: `python3 -m venv .venv && . .venv/bin/activate && pip install datarobot`
- Run each script like this: `python 01_import_data.py`
- Note the output of some scripts, which might be required in one of the following scripts. For example, step 01 gives you the project ID, which is required for step 02.
- To run the end to end process of creating the project, and make predictions, run `python end_to_end.py`

## Repository Contents

Scripts in various languages, and accompanying files
- `curl` - Curl (bash) scripts
- `python` - Python scripts
- `common` - Environment variables and datasets used in examples

## Development and Contributing

If you'd like to report an issue or bug, suggest improvements, or contribute code to this project, please refer to [CONTRIBUTING.md](CONTRIBUTING.md).

# Code of Conduct

This project has adopted the Contributor Covenant for its Code of Conduct. 
See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) to read it in full.

# License

Licensed under the Apache License 2.0. 
See [LICENSE](LICENSE) to read it in full.


