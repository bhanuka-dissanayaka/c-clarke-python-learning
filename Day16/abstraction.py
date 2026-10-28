from abc import ABC , abstractmethod  # abstract base class

class Notifier(ABC):  # This is an abstract class

    @abstractmethod  # decorator
    def send(self, message):
        pass

class SMSNotifier(Notifier):
    def send(self,message: str) -> None :
        print(f"Sending message - {message}")

class EmailNotifier(Notifier):
    def send(self,message: str) -> None:
        if message != "":
            print(f"Sending message {message}")
        else:
            print("Message is empty")
