"""Stream type classes for tap-tigerbeetle."""

from __future__ import annotations

from typing import Any

import requests
from hotglue_singer_sdk import typing as th  # JSON Schema typing helpers

from tap_tigerbeetle.client import TigerbeetleStream
import tigerbeetle as tb


class AccountsStream(TigerbeetleStream):
    """Stream for ``accounts``."""

    name = "accounts"
    path = "/"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        # TODO: Add the rest of the properties / fields from the API response (types, nested objects, etc.).
        th.Property(
            "id",
            th.StringType,
        ),
        th.Property(
            "debits_pending",
            th.IntegerType,
        ),
        th.Property(
            "credits_pending",
            th.IntegerType,
        ),
        th.Property(
            "debits_posted",
            th.IntegerType,
        ),
        th.Property(
            "credits_posted",
            th.IntegerType,
        ),
    ).to_dict()

    def prepare_request(
        self, context: dict | None, next_page_token: Any | None
    ) -> requests.PreparedRequest:
        params: dict = self.get_url_params(context, next_page_token)

        query_filter = tb.QueryFilter(
            timestamp_min=0,
            timestamp_max=0,
            limit=1,
            flags=0,
            user_data_128=0,
            user_data_64=0,
            user_data_32=0,
            code=0,
            ledger=0,
        )
        return query_filter

    def _request(
        self, prepared_request: requests.PreparedRequest, context: dict | None, client: tb.ClientSync | None = None
    ) -> requests.Response:
        response = client.query_accounts(prepared_request)
        return response


#TODO: Add a child stream for accounts transfers