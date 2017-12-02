Simple Trello helper
===

`config.json`
---

Copy `config.json.example` to `config.json` and fill:

- `key` - API KEY from https://trello.com/app-key
- `token` - token from https://trello.com/1/authorize?expiration=never&name=SinglePurposeToken&key=PASTE_KEY_HERE

`duplicate_card.py`
---

Duplicates card by id

Example:

```
pipenv run python duplicate_card.py --board BOARD_ID --list LIST_NAME -s SOURCE_CARD_ID
```

- `BOARD_ID` - board ID (eg. from url right after `https://trello.com/b/`)
- `LIST_NAME` - name of list, can be substring
- `SOURCE_CARD_ID` - id of card to copy (id can be obtained from exporting cards)