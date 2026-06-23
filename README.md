# tap-tigerbeetle

A [Singer](https://www.singer.io/) tap that extracts data from [TigerBeetle](https://docs.tigerbeetle.com/). It is built with [hotglue-singer-sdk](https://github.com/hotgluexyz/HotglueSingerSDK) and uses the [TigerBeetle Python client](https://docs.tigerbeetle.com/clients/python) to communicate directly with a TigerBeetle cluster.

## Overview

This repository contains a partially implemented Singer tap for TigerBeetle. Your assignment is to complete the implementation, verify it against a local TigerBeetle instance, and submit your results.

### What's already done

- Project scaffolding (pyproject.toml, tap class, base stream class).
- A basic `AccountsStream` that queries accounts via `client.query_accounts`.
- VS Code debugger launch configurations in `.vscode/launch.json`.
- A TigerBeetle client lifecycle managed in `client.py` (`request_records`).

### What you need to do

1. **Create test data** — spin up a local TigerBeetle instance, create accounts and transfers so the tap has data to extract.
2. **Add missing schema fields** to the `AccountsStream` — the current schema only includes a subset of the `Account` fields. Add the rest by looking at TigerBeetle documentation and assigning the correct types.
3. **Implement pagination** for the `AccountsStream` — the `get_next_page_token` method in `client.py` currently returns `None` (no pagination).

You can check examples of similar behavior in our [public tap repositories](https://github.com/hotgluexyz/tap-exact/blob/main/tap_exact/streams.py#L625)

## Requirements

- Python **3.10+**
- A local [TigerBeetle](https://docs.tigerbeetle.com/) instance, you can set it up by following their docs.

## Setup

Install all the dependencies in a virtual environment using pyproject.toml

## Running with the VS Code debugger

The project includes two VS Code debug configurations in `.vscode/launch.json`:

1. **`tap-tigerbeetle discover`** — runs `--discover` to output the stream catalog. You can check the example in the existing .secrets folder.
2. **`tap-tigerbeetle get`** — runs a full sync using the config, state, and catalog from the `.secrets/` folder.

To run a sync with the debugger:

1. Open VS Code / Cursor in the project root.
2. Go to **Run and Debug** (Ctrl+Shift+D / Cmd+Shift+D).
3. Select **`tap-tigerbeetle get`** from the dropdown.
4. Press **F5** to start.
5. Set breakpoints in `streams.py` or `client.py` to step through the sync.

Note: the debug configuration sets `"justMyCode": false`, so you can also step into the SDK internals if needed.

## Expected deliverables

Copy or fork this repository into a private repository under your own GitHub account. Make your changes there, then open a pull request in your repository and add the email addresses provided in the email as collaborators so we can review your submission.

### 1. Working code

- `AccountsStream` with all schema fields both in catalog.json and in the outout data.txt.
- Pagination implemented in `get_next_page_token` / `prepare_request`.

### 2. Output file — `data.txt`

Run the VS Code debugger (the `tap-tigerbeetle get` config writes to `.secrets/data.txt`).

### 3. TigerBeetle verification

Provide **either** a copy-paste of querying the same data directly through TigerBeetle's CLI REPL, showing that the records in your `data.txt` output match what TigerBeetle returns. For example:

```bash
tigerbeetle repl --cluster=0 --addresses=3000
```

```
lookup_accounts 1 2
```

Paste the terminal output into a file (e.g. `tigerbeetle-verification.txt`) in the `.secrets/` folder.

## Key files

| File                         | Purpose                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------ |
| `tap_tigerbeetle/tap.py`     | Tap class — register streams here                                              |
| `tap_tigerbeetle/client.py`  | Base stream class — TigerBeetle client lifecycle, pagination, response parsing |
| `tap_tigerbeetle/streams.py` | Stream definitions — `AccountsStream` (and your new `AccountTransfersStream`)  |
| `.vscode/launch.json`        | VS Code / Cursor debugger configurations                                       |
| `.secrets/config.json`       | Tap configuration                                                              |
| `.secrets/state.json`        | Sync state (bookmarks)                                                         |

## License

MIT — see `LICENSE` and `pyproject.toml`.

## Implementation Notes

### Test Data

Created 3 accounts and 3 transfers in a local TigerBeetle instance:

- Account 1 - Account 2: amount 1000
- Account 2 - Account 3: amount 500
- Account 3 - Account 1: amount 200

Verification output is available in `.secrets/tigerbeetle-verification.txt`.

### Schema Changes

Added the following missing fields to `AccountsStream` in `streams.py`:

- `user_data_128` (integer)
- `user_data_64` (integer)
- `user_data_32` (integer)
- `ledger` (integer)
- `code` (integer)
- `flags` (integer)
- `timestamp` (string — stored as string to preserve nanosecond precision)

### Pagination

Implemented cursor-based pagination in `client.py` using TigerBeetle's `timestamp_min` field:

- `get_next_page_token` returns the timestamp of the last record in each page
- `prepare_request` uses `timestamp_min = last_timestamp + 1` to fetch the next page
- When TigerBeetle returns an empty response, pagination stops

### Windows Setup Notes

The original `launch.json` used Mac/Linux paths. Updated `python` path to:
`.venv/Scripts/python.exe` for Windows compatibility.

## How to Run (Windows)

### Prerequisites

- Python 3.10 (required — the hotglue-singer-sdk is not compatible with Python 3.11+)
- TigerBeetle binary for Windows

### Setup

```bash
py -3.10 -m venv .venv
.venv\Scripts\Activate.ps1
pip install git+https://github.com/hotgluexyz/HotglueSingerSDK.git
pip install -e .
```

### Running the tap

```bash
# Generate catalog
python tap_tigerbeetle/tap.py --config .secrets/config.json --discover | Out-File -FilePath .secrets/catalog.json -Encoding utf8

# Run sync
python tap_tigerbeetle/tap.py --config .secrets/config.json --catalog .secrets/catalog.json --state .secrets/state.json | Out-File -FilePath .secrets/data.txt -Encoding utf8
```
