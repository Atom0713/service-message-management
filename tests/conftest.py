from typing import Iterator

import botocore
import moto.core
import pytest
from moto import mock_dynamodb as moto_mock_dynamodb
from src.datastore import delete_table
from src.service import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def mock_aws_response() -> Iterator[None]:
    class MockedAwsResponse(botocore.awsrequest.AWSResponse):
        raw_headers = {}  # type: ignore

        def read(self):  # type: ignore
            return self.text.encode()

    botocore_old_aws_response = botocore.awsrequest.AWSResponse
    moto_old_aws_response = botocore.awsrequest.AWSResponse

    botocore.awsrequest.AWSResponse = MockedAwsResponse  # type: ignore
    moto.core.botocore_stubber.AWSResponse = MockedAwsResponse

    yield

    botocore.awsrequest.AWSResponse = botocore_old_aws_response
    moto.core.botocore_stubber.AWSResponse = moto_old_aws_response


@pytest.fixture()
def mock_dynamodb(mock_aws_response):
    with moto_mock_dynamodb():
        ## seed

        yield

        delete_table()
