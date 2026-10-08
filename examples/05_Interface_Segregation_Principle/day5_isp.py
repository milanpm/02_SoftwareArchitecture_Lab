"""
===============================================================================
File: day5_isp.py
Project: 02_SoftwareArchitecture_Lab
Day: 5
Topic: Interface Segregation Principle (ISP)
Description:
    Separate connection checking and image sending interfaces.
    Learning example only; no actual DICOM communication.
Learning Objectives:
    Use only the interfaces required by each client.
    Match the required method with the object's available methods.
Author: Alex
Date: 2026-10-08
===============================================================================
"""

from abc import ABC, abstractmethod


class ConnectionChecker(ABC):
    @abstractmethod
    def echo(self) -> str:
        pass


class ImageSender(ABC):
    @abstractmethod
    def store(self, filename: str) -> str:
        pass


class EchoClient(ConnectionChecker):
    def echo(self) -> str:
        return "Connection checked"


class StoreOnlyClient(ImageSender):
    def store(self, filename: str) -> str:
        return f"Image sent: {filename}"


class SendClient(ConnectionChecker, ImageSender):
    def echo(self) -> str:
        return "Connection checked"

    def store(self, filename: str) -> str:
        return f"Image sent: {filename}"


def check_connection(checker: ConnectionChecker) -> None:
    print(checker.echo())


def send_image(sender: ImageSender, filename: str) -> None:
    print(sender.store(filename))


def main() -> None:
    print("[1] Connection only")
    check_connection(EchoClient())

    print("\n[2] Image sending only")
    send_image(StoreOnlyClient(), "sample.dcm")

    print("\n[3] Connection and image sending")
    client = SendClient()
    check_connection(client)
    send_image(client, "test.dcm")


if __name__ == "__main__":
    main()
