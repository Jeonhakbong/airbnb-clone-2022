from django.core.management.base import BaseCommand


class Command(BaseCommand):

    """Customed Test Command"""

    help = "Customed Test Command."

    def add_arguments(self, parser):
        parser.add_argument("--times", help="How many time print it?")

    def handle(self, *args, **options):
        # print(args, options) # check *args and **options

        times = int(options.get("times"))
        for i in range(0, times):
            # print("hello")
            self.stdout.write(self.style.SUCCESS("Hello"))
